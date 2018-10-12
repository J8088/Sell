from django import template

register = template.Library()


@register.filter
def upper(value):
    """Converts a string into all upper"""
    return value.upper()