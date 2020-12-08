# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubscriptionArchiv'
        db.create_table('subscriptions_subscriptionarchiv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_send', self.gf('django.db.models.fields.DateTimeField')()),
            ('subscription', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('subscriptions', ['SubscriptionArchiv'])


    def backwards(self, orm):
        # Deleting model 'SubscriptionArchiv'
        db.delete_table('subscriptions_subscriptionarchiv')


    models = {
        'subscriptions.subscriptionarchiv': {
            'Meta': {'object_name': 'SubscriptionArchiv'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_send': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'subscription': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['subscriptions']