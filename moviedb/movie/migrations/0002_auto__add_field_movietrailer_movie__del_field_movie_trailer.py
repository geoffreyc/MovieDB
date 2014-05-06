# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MovieTrailer.movie'
        db.add_column(u'movie_movietrailer', 'movie',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['movie.Movie']),
                      keep_default=False)

        # Deleting field 'Movie.trailer'
        db.delete_column(u'movie_movie', 'trailer_id')


    def backwards(self, orm):
        # Deleting field 'MovieTrailer.movie'
        db.delete_column(u'movie_movietrailer', 'movie_id')

        # Adding field 'Movie.trailer'
        db.add_column(u'movie_movie', 'trailer',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.MovieTrailer'], null=True),
                      keep_default=False)


    models = {
        u'movie.movie': {
            'Meta': {'object_name': 'Movie'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.MovieActor']", 'symmetrical': 'False'}),
            'additional_content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'api_id': ('django.db.models.fields.BigIntegerField', [], {'default': 'None', 'null': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.MovieCategory']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'movie_internal_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'poster': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'release_year': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'synopsy': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'movie.movieactor': {
            'Meta': {'object_name': 'MovieActor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'movie.moviecategory': {
            'Meta': {'object_name': 'MovieCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'movie.movieold': {
            'Meta': {'object_name': 'MovieOld'},
            'movie': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['movie.Movie']", 'unique': 'True', 'primary_key': 'True'}),
            'old_id': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'movie.movierented': {
            'Meta': {'object_name': 'MovieRented'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moviestock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.MovieStock']"}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'renter': ('django.db.models.fields.TextField', [], {}),
            'renterEmail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'})
        },
        u'movie.moviestock': {
            'Meta': {'object_name': 'MovieStock'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Movie']"}),
            'moviestocktype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.MovieStockType']"}),
            'original': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'quantity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'movie.moviestocktype': {
            'Meta': {'object_name': 'MovieStockType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '510'})
        },
        u'movie.movietrailer': {
            'Meta': {'object_name': 'MovieTrailer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Movie']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['movie']