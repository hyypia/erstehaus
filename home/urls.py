from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("impressum/", views.impresum, name="impressum"),
    path("datenschutz/", views.datenschutz, name="datenschutz"),
]
