from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from .models import Project


def index(request):
    try:
        projects = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404("Projects does not exists")
    return render(request, "projects/projects.html", {"projects": projects})


def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404("Project not found")

    equipment = project.equipment.split("\n")

    media_files = project.project_media.all()
    floor_plans = project.project_floor_plan.all()
    context = {
        "project": project,
        "media_files": media_files,
        "plans": floor_plans,
        "equipment": equipment,
        "google_maps_api_key": settings.GOOGLE_KEY,
        "latitude": project.latitude or 48.1351,  # Default to Munich if no coordinates
        "longitude": project.longitude or 11.5820,
    }
    return render(request, "projects/project_detail.html", context=context)
