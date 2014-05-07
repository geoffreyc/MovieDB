from django import template
from django.http import HttpResponse
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


def buildfilterurl(getdict, **kwargs):
    uristr = []
    for key, value in getdict.iteritems():
        if key in kwargs:
            uristr.append(key+"="+kwargs[key])
        else:
            uristr.append(key+"="+value)
    return "&".join(uristr)


register.filter('moviehastocktype', moviehastocktype)
register.simple_tag(buildfilterurl, name="buildfilterurl")