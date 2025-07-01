from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Project


def index(request):
    if request.path == "/aktuelle_projekte/":
        status = "A"
    elif request.path == "/abgeschlossene_projekte/":
        status = "P"
    elif request.path == "/zukuenftige_projekte/":
        status = "F"
    else:
        status = None

    if status:
        projects = get_list_or_404(Project, status=status)
    else:
        projects = get_list_or_404(Project)
    return render(request, "projects/projects.html", {"projects": projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    equipment = project.equipment.split("\n")
    media_files = project.project_media.all()
    videos = project.project_video.all()
    floor_plans = project.project_floor_plan.all()
    context = {
        "project": project,
        "media_files": media_files,
        "videos": videos,
        "plans": floor_plans,
        "equipment": equipment,
        "google_maps_api_key": settings.GOOGLE_KEY,
        "latitude": project.latitude,
        "longitude": project.longitude,
    }
    return render(request, "projects/project_detail.html", context=context)
