# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MasterClass.cook_time_min'
        db.add_column(u'master_class_masterclass', 'cook_time_min',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'MasterClass.cook_time_max'
        db.add_column(u'master_class_masterclass', 'cook_time_max',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MasterClass.cook_time_min'
        db.delete_column(u'master_class_masterclass', 'cook_time_min')

        # Deleting field 'MasterClass.cook_time_max'
        db.delete_column(u'master_class_masterclass', 'cook_time_max')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ingredients.usaingredient': {
            'Meta': {'object_name': 'USAIngredient'},
            'alpha_carot': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ash': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'beta_carot': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'beta_crypt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'calcium': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'carbohydrt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cholestrl': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'choline_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'copper': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'energy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fa_mono': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fa_poly': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fa_sat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fiber_td': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'folate_dfe': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'folate_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'folic_acid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'food_folate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gm_wt1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gmwt_2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gmwt_desc1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gmwt_desc2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iron': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lipid_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lut_zea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lycopene': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'magnesium': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'manganese': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name_rus': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ndb_no': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'niacin': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'panto_acid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'phosphorus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'potassium': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'protein': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'refuse_pct': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'retinol': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'riboflavin': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'selenium': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sodium': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sugar_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'thiamin': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'translated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updatable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'vi_vit_d_ui': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin_a_rae': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin_a_ui': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin_b12': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin_b6': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin_c': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin_d': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin_e': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin_k': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'zinc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'master_class.categorymc': {
            'Meta': {'object_name': 'CategoryMC'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'is_cake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'master_class.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'addit_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_group': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ingredient_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usa_ingredients'", 'to': u"orm['ingredients.USAIngredient']"}),
            'master_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ingredients'", 'to': u"orm['master_class.MasterClass']"}),
            'measure': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'master_class.masterclass': {
            'Meta': {'object_name': 'MasterClass'},
            'add_watermark': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['master_class.CategoryMC']", 'null': 'True', 'blank': 'True'}),
            'cook_time_max': ('django.db.models.fields.PositiveIntegerField', [], {'default': '200'}),
            'cook_time_min': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'for_registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ip_addr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_cake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'subcategory': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['master_class.SubCategoryMC']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'master_class.mcstep': {
            'Meta': {'object_name': 'MCStep'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'master_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'masterclasses'", 'to': u"orm['master_class.MasterClass']"}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'step_num': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'master_class.mctool': {
            'Meta': {'object_name': 'MCTool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'master_class.subcategorymc': {
            'Meta': {'object_name': 'SubCategoryMC'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['master_class.CategoryMC']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['master_class']