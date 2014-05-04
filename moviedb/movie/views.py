from django.shortcuts import render
from django.http import HttpResponse
from moviedb.settings import *
import datetime
from moviedb.movie.models import *
import csv
from models import *
# Create your views here.


def import_old_movies(request):
    html = ''
    old2new = {}
    movieactors = {}
    moviecats = {}
    with open(BASE_DIR+'/movieDB/movie/asset/movies.csv', mode='rb') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader, None)
        for row in spamreader:
            movie = Movie()
            movie.title = row[1]
            try:
                movie.release_year = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S').date()
            except:
                movie.release_year = None
            movie.synopsy = row[3]
            movie.rating = float(row[6])
            movie.poster = row[8]
            movie.api_id = 0
            html += ', '.join(row)+'<br />'
            movie.save()
            movieold = MovieOld()
            movieold.old_id = int(row[0])
            movieold.movie = movie
            movieold.save()
            old2new[movieold.old_id] = movie
    with open(BASE_DIR+'/movieDB/movie/asset/movie_actor.csv', mode='rb') as csvfile:
        spamreader = csv.reader(csvfile)
        currentid = 0
        currActor = None
        for row in spamreader:
            old_id = int(row[0])
            if int(row[1]) != currentid:
                currentid = int(row[1])
                currActor = MovieActor()
                currActor.name = row[2]
                currActor.save()
            if old_id in old2new:
                if old_id not in movieactors:
                    movieactors[old_id] = []
                movieactors[old_id].append(currActor)
                #currmovie = old2new[old_id]
                #currmovie.actors.add(currActor)
                #currmovie.save()
        for key, value in movieactors.iteritems():
            if key in old2new:
                currmovie = old2new[key]
                currmovie.actors.add(*value)
    with open(BASE_DIR+'/movieDB/movie/asset/movie_categorie.csv', mode='rb') as csvfile:
        spamreader = csv.reader(csvfile)
        currentid = 0
        currCat = None
        for row in spamreader:
            old_id = int(row[0])
            if int(row[1]) != currentid:
                currentid = int(row[1])
                currCat = MovieCategory()
                currCat.name = row[3]
                currCat.save()
            if old_id in old2new:
                if old_id not in moviecats:
                    moviecats[old_id] = []
                moviecats[old_id].append(currCat)
                #currmovie = old2new[old_id]
                #currmovie.actors.add(currActor)
                #currmovie.save()
        for key, value in moviecats.iteritems():
            if key in old2new:
                currmovie = old2new[key]
                currmovie.categories.add(*value)
    with open(BASE_DIR+'/movieDB/movie/asset/movie_stocks.csv', mode='rb') as csvfile:
        spamreader = csv.reader(csvfile)
        stocklist = []
        for row in spamreader:
            stock = MovieStock()
            stock.original = bool(row(3))
            stock.quantity = int(row(4))
            stock.location = row(5)
            stock.movie_id = old2new[int(row(1))].id
            stocklist.add(stock)
        MovieStock.objects.bulk_create(stocklist)

    return HttpResponse(html)