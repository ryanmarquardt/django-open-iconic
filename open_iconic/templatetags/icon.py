#!/usr/bin/env python3

from django import template
from django.utils.safestring import SafeText
from django.utils.html import conditional_escape as cesc

register = template.Library()


@register.simple_tag
def icon(name=None, empty_text="", empty_icon=""):
    if name:
        return SafeText('<span class="oi oi-{}"></span>'.format(cesc(name)))
    elif empty_text:
        return cesc(empty_text)
    elif empty_icon:
        return SafeText('<span class="oi oi-{}"></span>'.format(cesc(empty_icon)))
    return SafeText('')
