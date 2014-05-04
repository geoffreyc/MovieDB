# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'movie_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('api_id', self.gf('django.db.models.fields.BigIntegerField')(default=None, null=True)),
            ('imdb_id', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('release_year', self.gf('django.db.models.fields.DateField')(null=True)),
            ('synopsy', self.gf('django.db.models.fields.TextField')(null=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('poster', self.gf('django.db.models.fields.TextField')(null=True)),
            ('additional_content', self.gf('django.db.models.fields.TextField')(null=True)),
            ('movie_internal_order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('trailer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.MovieTrailer'], null=True)),
        ))
        db.send_create_signal(u'movie', ['Movie'])

        # Adding M2M table for field categories on 'Movie'
        m2m_table_name = db.shorten_name(u'movie_movie_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movie.movie'], null=False)),
            ('moviecategory', models.ForeignKey(orm[u'movie.moviecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'moviecategory_id'])

        # Adding M2M table for field actors on 'Movie'
        m2m_table_name = db.shorten_name(u'movie_movie_actors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movie.movie'], null=False)),
            ('movieactor', models.ForeignKey(orm[u'movie.movieactor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'movieactor_id'])

        # Adding model 'MovieOld'
        db.create_table(u'movie_movieold', (
            ('movie', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['movie.Movie'], unique=True, primary_key=True)),
            ('old_id', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'movie', ['MovieOld'])

        # Adding model 'MovieActor'
        db.create_table(u'movie_movieactor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'movie', ['MovieActor'])

        # Adding model 'MovieCategory'
        db.create_table(u'movie_moviecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'movie', ['MovieCategory'])

        # Adding model 'MovieTrailer'
        db.create_table(u'movie_movietrailer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'movie', ['MovieTrailer'])

        # Adding model 'MovieStockType'
        db.create_table(u'movie_moviestocktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=510)),
        ))
        db.send_create_signal(u'movie', ['MovieStockType'])

        # Adding model 'MovieStock'
        db.create_table(u'movie_moviestock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('moviestocktype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.MovieStockType'])),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
            ('original', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('quantity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'movie', ['MovieStock'])

        # Adding model 'MovieRented'
        db.create_table(u'movie_movierented', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('moviestock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.MovieStock'])),
            ('renter', self.gf('django.db.models.fields.TextField')()),
            ('renterEmail', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'movie', ['MovieRented'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'movie_movie')

        # Removing M2M table for field categories on 'Movie'
        db.delete_table(db.shorten_name(u'movie_movie_categories'))

        # Removing M2M table for field actors on 'Movie'
        db.delete_table(db.shorten_name(u'movie_movie_actors'))

        # Deleting model 'MovieOld'
        db.delete_table(u'movie_movieold')

        # Deleting model 'MovieActor'
        db.delete_table(u'movie_movieactor')

        # Deleting model 'MovieCategory'
        db.delete_table(u'movie_moviecategory')

        # Deleting model 'MovieTrailer'
        db.delete_table(u'movie_movietrailer')

        # Deleting model 'MovieStockType'
        db.delete_table(u'movie_moviestocktype')

        # Deleting model 'MovieStock'
        db.delete_table(u'movie_moviestock')

        # Deleting model 'MovieRented'
        db.delete_table(u'movie_movierented')


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
            'title': ('django.db.models.fields.TextField', [], {}),
            'trailer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.MovieTrailer']", 'null': 'True'})
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
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['movie']