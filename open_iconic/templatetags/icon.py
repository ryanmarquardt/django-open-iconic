#!/usr/bin/env python3

from django import template

register = template.Library()

@register.simple_tag
def icon(name=None, empty_text="", empty_icon=""):
    if name:
        return '<span class="oi oi-{}"></span>'.format(name)
    elif empty_text:
        return empty_text
    elif empty_icon:
        return '<span class="oi oi-{}"></span>'.format(empty_icon)
    return ''
