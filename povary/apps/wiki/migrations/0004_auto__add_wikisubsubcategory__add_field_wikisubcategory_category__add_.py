# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WikiSubSubCategory'
        db.create_table('wiki_wikisubsubcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subcategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wiki.WikiSubCategory'])),
        ))
        db.send_create_signal('wiki', ['WikiSubSubCategory'])

        # Adding field 'WikiSubCategory.category'
        db.add_column('wiki_wikisubcategory', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['wiki.WikiCategory']),
                      keep_default=False)

        # Adding field 'WikiPage.category'
        db.add_column('wiki_wikipage', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['wiki.WikiCategory']),
                      keep_default=False)

        # Adding field 'WikiPage.subcategory'
        db.add_column('wiki_wikipage', 'subcategory',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['wiki.WikiSubCategory']),
                      keep_default=False)

        # Adding field 'WikiPage.subsubcategory'
        db.add_column('wiki_wikipage', 'subsubcategory',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['wiki.WikiSubSubCategory']),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'WikiSubSubCategory'
        db.delete_table('wiki_wikisubsubcategory')

        # Deleting field 'WikiSubCategory.category'
        db.delete_column('wiki_wikisubcategory', 'category_id')

        # Deleting field 'WikiPage.category'
        db.delete_column('wiki_wikipage', 'category_id')

        # Deleting field 'WikiPage.subcategory'
        db.delete_column('wiki_wikipage', 'subcategory_id')

        # Deleting field 'WikiPage.subsubcategory'
        db.delete_column('wiki_wikipage', 'subsubcategory_id')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'wiki.wikicategory': {
            'Meta': {'object_name': 'WikiCategory'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'wiki.wikipage': {
            'Meta': {'object_name': 'WikiPage'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiki.WikiCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiki.WikiSubCategory']"}),
            'subsubcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiki.WikiSubSubCategory']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'warnings': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'wiki.wikipageversion': {
            'Meta': {'object_name': 'WikiPageVersion'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_body': ('django.db.models.fields.TextField', [], {}),
            'new_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'new_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'new_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'old_body': ('django.db.models.fields.TextField', [], {}),
            'old_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'old_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'old_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiki.WikiPage']"}),
            'revision': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'wiki.wikisubcategory': {
            'Meta': {'object_name': 'WikiSubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiki.WikiCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'wiki.wikisubsubcategory': {
            'Meta': {'object_name': 'WikiSubSubCategory'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wiki.WikiSubCategory']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['wiki']