from django.db import models


class HomePageContent(models.Model):
    company_description = models.TextField()
    about_us = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return "Homepage content"


class MainTitleMediaContent(models.Model):
    homepage = models.ForeignKey(
        HomePageContent, on_delete=models.CASCADE, related_name="main_title_slides"
    )
    file = models.FileField(upload_to="homepage_slides/main_title_slides", blank=True)

    def __str__(self):
        return f"Slide - {self.file.name}"


class AboutUsMediaContent(models.Model):
    homepage = models.ForeignKey(
        HomePageContent, on_delete=models.CASCADE, related_name="about_us_slides"
    )
    file = models.FileField(upload_to="homepage_slides/about_us_slides", blank=True)

    def __str__(self):
        return f"Slide - {self.file.name}"
