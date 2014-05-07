from django.shortcuts import render
from django.http import HttpResponse
from moviedb.settings import *
import datetime
from moviedb.movie.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    movieperaage = 30
    movielist = Movie.objects.all().order_by(*["title", "movie_internal_order"])
    #movielist = movielist.filter(moviestocks__moviestocktype__code="DVD")
    movielist = __filtermovies(request, movielist)
    movielist = movielist.prefetch_related("moviestocks__moviestocktype")
    paginator = Paginator(movielist, movieperaage)
    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    contextdict = {'movies': movies, 'paginator': paginator, 'posterpath': POSTER_PATH}
    return render(request, 'movies/listing.html',contextdict)


def __filtermovies(request, movielist):
    support = request.GET.get('support')
    if support != None and support != "":
        movielist = movielist.filter(moviestocks__moviestocktype__code=support)
    return movielist