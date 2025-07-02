from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aktuelle/", views.index, name="index"),
    path("abgeschlossene/", views.index, name="index"),
    path("zukuenftige/", views.index, name="index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
