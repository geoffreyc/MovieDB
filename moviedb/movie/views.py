from django.shortcuts import render
from django.http import HttpResponse
from moviedb.settings import *
import datetime
from moviedb.movie.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    moviePerPage = 60
    movieList = Movie.objects.all()
    paginator = Paginator(movieList, 60)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render(request, 'layouts/master.html', {})