from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    rooms = models.IntegerField(null=True)
    square = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    land_area = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    description = models.TextField(null=True)
    details = models.TextField(null=True)
    equipment = models.TextField(null=True)

    def __str__(self) -> models.CharField:
        return self.address


class MediaFile(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_media", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="project_media/", blank=True)


class FloorPlan(models.Model):
    project = models.ForeignKey(
        Project, related_name="project_floor_plan", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="project_floor_plan/", blank=True)
