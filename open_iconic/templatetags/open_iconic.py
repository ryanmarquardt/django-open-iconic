#!/usr/bin/env python3

from django import template
from django.utils.safestring import SafeText
from django.utils.html import format_html
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def icon(name=None, empty_text="", empty_icon=""):
    if name:
        return format_html('<span class="oi oi-{}"></span>', name)
    elif empty_icon:
        return format_html('<span class="oi oi-{}"></span>', empty_icon)
    elif empty_text:
        return empty_text
    return SafeText('')


@register.simple_tag
def open_iconic_head():
    return format_html("""
        <link rel="stylesheet" href="{}">
    """, static('open_iconic/font/css/open-iconic-bootstrap.css'))