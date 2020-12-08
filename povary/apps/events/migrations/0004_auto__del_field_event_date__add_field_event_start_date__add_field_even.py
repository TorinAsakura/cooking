# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.date'
        db.delete_column('events_event', 'date')

        # Adding field 'Event.start_date'
        db.add_column('events_event', 'start_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 19, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.end_date'
        db.add_column('events_event', 'end_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 19, 0, 0)),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'Event.date'
        db.add_column('events_event', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 19, 0, 0)),
                      keep_default=False)

        # Deleting field 'Event.start_date'
        db.delete_column('events_event', 'start_date')

        # Deleting field 'Event.end_date'
        db.delete_column('events_event', 'end_date')

    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['events.EventCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'events.eventcategory': {
            'Meta': {'object_name': 'EventCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['events']