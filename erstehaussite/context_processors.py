from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404

from home.models import HomePageContent
from projects.models import Project


def global_context(request):
    content = get_object_or_404(HomePageContent)
    email = content.email
    address = content.address
    actuals = get_list_or_404(Project, status="A")
    pasts = get_list_or_404(Project, status="P")
    futures = get_list_or_404(Project, status="F")

    return {
        "email": email,
        "address": address,
        "actuals": actuals,
        "pasts": pasts,
        "futures": futures,
        "google_analytics_id": settings.GOOGLE_ANALYTICS_ID,
    }
