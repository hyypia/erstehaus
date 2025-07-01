from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

from news.models import Post
from projects.models import Project

from .form import ContactForm
from .models import HomePageContent


def home(request):
    page_content = get_object_or_404(HomePageContent)
    projects = get_list_or_404(Project)
    news = get_list_or_404(Post)

    main_title_slides = page_content.main_title_slides.all()
    about_us_slides = page_content.about_us_slides.all()

    def get_office_coordinates():
        try:
            geolocator = Nominatim(user_agent="erstehaus")
            location = geolocator.geocode(page_content.address)
            if location:
                return (location.latitude, location.longitude)
        except GeocoderTimedOut:
            pass
        return (52.5200, 13.4049)

    lat, lon = get_office_coordinates()

    # Contact Form
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"Neue Kontaktanfrage von {name}"
            full_message = (
                f"Name: {name}\n"
                f"Telefon: {phone}\n"
                f"E-Mail: {email}\n\n"
                f"Nachricht:\n{message}"
            )

            try:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ["igortereschuk92@gmail.com"],
                    fail_silently=False,
                )
                messages.success(
                    request, "Vielen Dank! Ihre Nachricht wurde erfolgreich gesendet."
                )
                return redirect("/#form")
            except BadHeaderError:
                messages.error(request, "Ungültiger Header gefunden.")
        else:
            messages.error(request, "Bitte korrigieren Sie die Fehler im Formular.")
    else:
        form = ContactForm()

    context = {
        "page_content": page_content,
        "main_title_slides": main_title_slides,
        "about_us_slides": about_us_slides,
        "projects": projects,
        "news": news,
        "google_maps_api_key": settings.GOOGLE_KEY,
        "latitude": lat,
        "longitude": lon,
        "form": form,
    }
    return render(request, "home.html", context=context)
