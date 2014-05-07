from django.shortcuts import render
from django.http import HttpResponse
from moviedb.settings import *
import datetime
from moviedb.movie.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    moviePerPage = 30
    movieList = Movie.objects.all().order_by(*["title", "movie_internal_order"]).filter().prefetch_related("moviestocks__moviestocktype")
    paginator = Paginator(movieList, moviePerPage)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    contextdict = {'movies': movies, 'paginator': paginator, 'posterpath': POSTER_PATH}
    return render(request, 'movies/listing.html',contextdict)