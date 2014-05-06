from django.conf.urls import patterns, include, url

from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moviedb.views.home', name='home'),
    url(r'^', 'moviedb.movie.views.index', name='movieindex'),
    url(r'movie/add/', 'moviedb.movie.views.index', name='movieadd'),
)
