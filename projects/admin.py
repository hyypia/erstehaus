from django.contrib import admin

from .forms import ProjectForm
from .models import FloorPlan, MediaFile, Project, VideoFile


class MediaFileInline(admin.TabularInline):
    model = MediaFile
    extra = 1
    fields = ["file"]


class VideoFileInline(admin.TabularInline):
    model = VideoFile
    extra = 1
    fields = ["video"]


class FloorPlanInline(admin.TabularInline):
    model = FloorPlan
    extra = 1
    fields = ["file"]


class ProjectAdmin(admin.ModelAdmin):
    exclude = ("latitude", "longitude")
    form = ProjectForm
    inlines = [MediaFileInline, VideoFileInline, FloorPlanInline]


admin.site.register(Project, ProjectAdmin)
