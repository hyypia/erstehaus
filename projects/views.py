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
    }
    return render(request, "projects/project_detail.html", context=context)
