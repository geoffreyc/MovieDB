# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MovieOld'
        db.create_table(u'movie_movieold', (
            ('movie', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['movie.Movie'], unique=True, primary_key=True)),
            ('old_id', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'movie', ['MovieOld'])


    def backwards(self, orm):
        # Deleting model 'MovieOld'
        db.delete_table(u'movie_movieold')


    models = {
        u'movie.movie': {
            'Meta': {'object_name': 'Movie'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.MovieActor']", 'symmetrical': 'False'}),
            'additional_content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'api_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.MovieCategory']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'movie_internal_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'poster': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'rating': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'release_year': ('django.db.models.fields.DateField', [], {}),
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
            'Movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Movie']"}),
            'MovieStockType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.MovieStockType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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