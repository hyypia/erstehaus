from django import forms
from django.utils.safestring import mark_safe

from .models import Project


# Add special sighns for price and squares fields
class SuffixTextInput(forms.TextInput):
    def __init__(self, suffix="", attrs=None):
        self.suffix = suffix
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        base = super().render(name, value, attrs, renderer)
        return mark_safe(
            f"<div style='display:flex; align-items:center;'>{base}<span style='margin-left:4px;'>{self.suffix}</span></div>"
        )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "price": SuffixTextInput(suffix="€"),
            "square": SuffixTextInput(suffix="m²"),
            "land_area": SuffixTextInput(suffix="m²"),
        }
