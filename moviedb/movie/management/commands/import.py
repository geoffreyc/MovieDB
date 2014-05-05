from django.core.management.base import BaseCommand, CommandError
from moviedb.settings import *
import datetime
import csv
from moviedb.movie.models import *

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        html = ''
        old2new = {}
        movieactors = {}
        moviecats = {}

        with open(BASE_DIR+'/movieDB/movie/asset/movies.csv', mode='rb') as csvfile:
            self.stdout.write("Importing Movies...")
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
            self.stdout.write("Importing Actors...")
            spamreader = csv.reader(csvfile)
            currentid = 0
            currActor = None
            actorcount = 0
            for row in spamreader:
                old_id = int(row[0])
                if int(row[1]) != currentid:
                    currentid = int(row[1])
                    currActor = MovieActor()
                    currActor.name = row[2]
                    currActor.save()
                    actorcount += 1
                if (actorcount % 500) == 0:
                    self.stdout.write("\t-Imported "+str(actorcount)+" Actors...")
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
            self.stdout.write("Importing categories...")
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
            self.stdout.write("Importing Stock...")
            spamreader = csv.reader(csvfile)
            stocklist = []
            for row in spamreader:
                stock = MovieStock()
                if int(row[3]) == 1:
                    stock.original = True
                else:
                    stock.original = False
                stock.quantity = int(row[4])
                stock.location = row[5]
                stock.movie_id = old2new[int(row[1])].id
                stock.moviestocktype_id = int(row[2])
                stocklist.append(stock)
            MovieStock.objects.bulk_create(stocklist)