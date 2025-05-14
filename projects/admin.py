from django.contrib import admin

from .models import Project, MediaFile, FloorPlan
from .forms import ProjectForm


class MediaFileInline(admin.TabularInline):
    model = MediaFile
    extra = 1
    fields = ["file"]


class FloorPlanInline(admin.TabularInline):
    model = FloorPlan
    extra = 1
    fields = ["file"]


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    inlines = [MediaFileInline, FloorPlanInline]


admin.site.register(Project, ProjectAdmin)
