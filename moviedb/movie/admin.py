from django.contrib import admin
from moviedb.movie.models import *
# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieStockType)
admin.site.register(MovieStock)
admin.site.register(MovieActor)
admin.site.register(MovieCategory)
admin.site.register(MovieTrailer)
admin.site.register(MovieRented)