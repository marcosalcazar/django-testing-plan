# -*- coding: utf-8 *-*
from django import template

register = template.Library()


@register.simple_tag
def user_display_name(user):
    if user.first_name or user.last_name:
        return u" ".join((user.first_name, user.last_name))
    else:
        return unicode(user)
