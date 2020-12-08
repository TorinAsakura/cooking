# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Category.description'
        db.alter_column('categories_category', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Category.image'
        db.alter_column('categories_category', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255, null=True))

        # Changing field 'SubCategory.description'
        db.alter_column('categories_subcategory', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SubCategory.image'
        db.alter_column('categories_subcategory', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Category.description'
        raise RuntimeError("Cannot reverse this migration. 'Category.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Category.image'
        raise RuntimeError("Cannot reverse this migration. 'Category.image' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SubCategory.description'
        raise RuntimeError("Cannot reverse this migration. 'SubCategory.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SubCategory.image'
        raise RuntimeError("Cannot reverse this migration. 'SubCategory.image' and its values cannot be restored.")

    models = {
        'categories.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'categories.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['categories.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['categories']