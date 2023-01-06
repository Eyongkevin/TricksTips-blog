from django import template
import readtime

register = template.Library()


@register.filter(name="read")
def read(post):
    return readtime.of_html(post)
