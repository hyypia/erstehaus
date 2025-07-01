from django.contrib import admin

from .models import AboutUsMediaContent, HomePageContent, MainTitleMediaContent


class MainTitleMediaContentInline(admin.TabularInline):
    model = MainTitleMediaContent
    extra = 1
    fields = ["file"]


class AboutUsMediaContentInline(admin.TabularInline):
    model = AboutUsMediaContent
    extra = 1
    fields = ["file"]


class HomePageContentAdmin(admin.ModelAdmin):
    inlines = [MainTitleMediaContentInline, AboutUsMediaContentInline]

    def has_add_permission(self, request):
        if HomePageContent.objects.exists():
            return False
        return True


admin.site.register(HomePageContent, HomePageContentAdmin)
