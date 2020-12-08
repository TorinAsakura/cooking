# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StopWord'
        db.create_table('stopwords_stopword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stopword', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('replaceword', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('stopwords', ['StopWord'])

    def backwards(self, orm):
        # Deleting model 'StopWord'
        db.delete_table('stopwords_stopword')

    models = {
        'stopwords.stopword': {
            'Meta': {'object_name': 'StopWord'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'replaceword': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stopword': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['stopwords']