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
            if kwargs[key]is not None:
                uristr.append(key+"="+kwargs[key])
            kwargs.pop(key, None)
        else:
            uristr.append(key+"="+value)
    for key, value in kwargs.iteritems():
        if kwargs[key]is not None:
            uristr.append(key+"="+value)
    return "&".join(uristr)


def isfilteractive(getdict, **kwargs):
    isactive = ""
    for key, value in kwargs.iteritems():
        if key in getdict and getdict[key] == value:
            isactive = "active"
        elif key not in getdict and value is None:
            isactive = "active"
    return isactive


register.filter('moviehastocktype', moviehastocktype)
register.simple_tag(buildfilterurl, name="buildfilterurl")
register.simple_tag(isfilteractive, name="isfilteractive")