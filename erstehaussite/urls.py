from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Erstehaus Admin"
admin.site.site_title = "Erstehaus Admin Portal"
admin.site.index_title = "Welcome to the Erstehaus-Site Administration"

urlpatterns = [
    path("", include("home.urls")),
    path("news/", include("news.urls")),
    path("projekte/", include("projects.urls")),
    path("aktuelle_projekte/", include("projects.urls")),
    path("abgeschlossene_projekte/", include("projects.urls")),
    path("zukuenftige_projekte/", include("projects.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
