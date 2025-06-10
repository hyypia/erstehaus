from django.urls import path

from . import views

urlpatterns = [
    path("", views.news_index, name="news_index"),
    path("<str:slug>/", views.post_detail, name="post_detail"),
]
