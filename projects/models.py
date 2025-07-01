from django.db import models
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim


def banner_image_path(instance, filename) -> str:
    return f"project_{instance.id}/media/{filename}"


class Project(models.Model):
    STATUS_CHOICES = {
        "F": "Future",
        "A": "Actual",
        "P": "Past",
    }
    title = models.CharField(max_length=200)
    banner_image = models.FileField(upload_to=banner_image_path, blank=True)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)
    square = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    land_area = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    equipment = models.TextField(null=True, blank=True)
    expose = models.FileField(upload_to="expose/", blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="F")

    latitude = models.FloatField(null=True, blank=True, editable=False)
    longitude = models.FloatField(null=True, blank=True, editable=False)

    def __str__(self) -> str:
        return str(self.address)

    def get_self_id(self):
        return self.pk

    def get_coordinates(self) -> tuple[float, float]:
        try:
            geolocator = Nominatim(user_agent="erstehaus")
            location = geolocator.geocode(self.address)
            if location:
                return (location.latitude, location.longitude)
        except GeocoderTimedOut:
            pass
        return (52.5200, 13.4049)

    def save(self, *args, **kwargs):
        if self.address:
            lat, lon = self.get_coordinates()
            self.latitude = lat
            self.longitude = lon

        super().save(*args, **kwargs)


def media_file_path(instance, filename) -> str:
    return f"project_{instance.project.id}/media/{filename}"


class MediaFile(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_media", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to=media_file_path, blank=True)


class VideoFile(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_video", on_delete=models.CASCADE
    )
    video = models.FileField(upload_to=media_file_path, blank=True)


def plan_file_path(instance, filename) -> str:
    return f"project_{instance.project.id}/floor_plan/{filename}"


class FloorPlan(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_floor_plan", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to=plan_file_path, blank=True)
