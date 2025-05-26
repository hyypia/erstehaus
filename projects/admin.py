from django.contrib import admin

from .forms import ProjectForm
from .models import FloorPlan, MediaFile, Project


class MediaFileInline(admin.TabularInline):
    model = MediaFile
    extra = 1
    fields = ["file"]


class FloorPlanInline(admin.TabularInline):
    model = FloorPlan
    extra = 1
    fields = ["file"]


class ProjectAdmin(admin.ModelAdmin):
    exclude = ("latitude", "longitude")
    form = ProjectForm
    inlines = [MediaFileInline, FloorPlanInline]


admin.site.register(Project, ProjectAdmin)
