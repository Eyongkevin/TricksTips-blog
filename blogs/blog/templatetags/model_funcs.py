import math
from django import template

register = template.Library()


@register.filter(name="get_absolute_url")
def get_absolute_url(post, tag):
    return post.get_absolute_url(tag)
