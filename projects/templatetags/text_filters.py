from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def from_char_cut(string, char):
    """Removes all characters in string from given char"""
    return string.split(char)[0]
