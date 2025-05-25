from django.db import models


def banner_image_path(instance, filename) -> str:
    return f"project_{instance.id}/media/banner_{filename}"


class Project(models.Model):
    title = models.CharField(max_length=200)
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
    banner_image = models.FileField(upload_to=banner_image_path, blank=True)

    def __str__(self) -> str:
        return str(self.address)


def media_file_path(instance, filename) -> str:
    return f"project_{instance.project.id}/media/{filename}"


class MediaFile(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_media", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to=media_file_path, blank=True)


def plan_file_path(instance, filename) -> str:
    return f"project_{instance.project.id}/floor_plan/{filename}"


class FloorPlan(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_floor_plan", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to=plan_file_path, blank=True)
