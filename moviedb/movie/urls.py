from django.conf.urls import patterns, include, url

from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moviedb.views.home', name='home'),
    url(r'^import/$', 'moviedb.movie.views.import_old_movies', name='importold'),
)
