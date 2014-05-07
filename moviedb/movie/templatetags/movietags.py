from django import template
from moviedb.movie.models import *

register = template.Library()


def moviehastocktype(value, arg):
    """
    @type value: Movie
    """
    retval = value.hasStockType(arg)
    if retval:
        return "has"+arg
    else:
        return "hasno"+arg


register.filter('moviehastocktype', moviehastocktype)