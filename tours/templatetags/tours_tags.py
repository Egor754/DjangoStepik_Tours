from django import template
from tours.models import Depart

register = template.Library()


@register.simple_tag()
def get_departur():
    return Depart.objects.all()
