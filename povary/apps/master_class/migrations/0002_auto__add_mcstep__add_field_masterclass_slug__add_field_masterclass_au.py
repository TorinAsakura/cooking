# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MCStep'
        db.create_table('master_class_mcstep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('step_num', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('master_class', self.gf('django.db.models.fields.related.ForeignKey')(related_name='masterclasses', to=orm['master_class.MasterClass'])),
        ))
        db.send_create_signal('master_class', ['MCStep'])

        # Adding field 'MasterClass.slug'
        db.add_column('master_class_masterclass', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', unique=True, max_length=50),
                      keep_default=False)

        # Adding field 'MasterClass.author'
        db.add_column('master_class_masterclass', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'MasterClass.published'
        db.add_column('master_class_masterclass', 'published',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'MasterClass.pub_date'
        db.add_column('master_class_masterclass', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 8, 2, 0, 0)),
                      keep_default=False)

        # Adding field 'MasterClass.created'
        db.add_column('master_class_masterclass', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 8, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'MasterClass.updated'
        db.add_column('master_class_masterclass', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 8, 2, 0, 0), blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'MCStep'
        db.delete_table('master_class_mcstep')

        # Deleting field 'MasterClass.slug'
        db.delete_column('master_class_masterclass', 'slug')

        # Deleting field 'MasterClass.author'
        db.delete_column('master_class_masterclass', 'author_id')

        # Deleting field 'MasterClass.published'
        db.delete_column('master_class_masterclass', 'published')

        # Deleting field 'MasterClass.pub_date'
        db.delete_column('master_class_masterclass', 'pub_date')

        # Deleting field 'MasterClass.created'
        db.delete_column('master_class_masterclass', 'created')

        # Deleting field 'MasterClass.updated'
        db.delete_column('master_class_masterclass', 'updated')

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
        'ingredients.usaingredient': {
            'Meta': {'object_name': 'USAIngredient'},
            'alpha_carot': ('django.db.models.fields.FloatField', [], {}),
            'ash': ('django.db.models.fields.FloatField', [], {}),
            'beta_carot': ('django.db.models.fields.FloatField', [], {}),
            'beta_crypt': ('django.db.models.fields.FloatField', [], {}),
            'calcium': ('django.db.models.fields.FloatField', [], {}),
            'carbohydrt': ('django.db.models.fields.FloatField', [], {}),
            'cholestrl': ('django.db.models.fields.FloatField', [], {}),
            'choline_total': ('django.db.models.fields.FloatField', [], {}),
            'copper': ('django.db.models.fields.FloatField', [], {}),
            'energy': ('django.db.models.fields.FloatField', [], {}),
            'fa_mono': ('django.db.models.fields.FloatField', [], {}),
            'fa_poly': ('django.db.models.fields.FloatField', [], {}),
            'fa_sat': ('django.db.models.fields.FloatField', [], {}),
            'fiber_td': ('django.db.models.fields.FloatField', [], {}),
            'folate_dfe': ('django.db.models.fields.FloatField', [], {}),
            'folate_total': ('django.db.models.fields.FloatField', [], {}),
            'folic_acid': ('django.db.models.fields.FloatField', [], {}),
            'food_folate': ('django.db.models.fields.FloatField', [], {}),
            'gm_wt1': ('django.db.models.fields.FloatField', [], {}),
            'gmwt_2': ('django.db.models.fields.FloatField', [], {}),
            'gmwt_desc1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gmwt_desc2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iron': ('django.db.models.fields.FloatField', [], {}),
            'lipid_total': ('django.db.models.fields.FloatField', [], {}),
            'lut_zea': ('django.db.models.fields.FloatField', [], {}),
            'lycopene': ('django.db.models.fields.FloatField', [], {}),
            'magnesium': ('django.db.models.fields.FloatField', [], {}),
            'manganese': ('django.db.models.fields.FloatField', [], {}),
            'name_rus': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ndb_no': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'niacin': ('django.db.models.fields.FloatField', [], {}),
            'panto_acid': ('django.db.models.fields.FloatField', [], {}),
            'phosphorus': ('django.db.models.fields.FloatField', [], {}),
            'potassium': ('django.db.models.fields.FloatField', [], {}),
            'protein': ('django.db.models.fields.FloatField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'refuse_pct': ('django.db.models.fields.FloatField', [], {}),
            'retinol': ('django.db.models.fields.FloatField', [], {}),
            'riboflavin': ('django.db.models.fields.FloatField', [], {}),
            'selenium': ('django.db.models.fields.FloatField', [], {}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sodium': ('django.db.models.fields.FloatField', [], {}),
            'sugar_total': ('django.db.models.fields.FloatField', [], {}),
            'thiamin': ('django.db.models.fields.FloatField', [], {}),
            'translated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updatable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'vi_vit_d_ui': ('django.db.models.fields.FloatField', [], {}),
            'vitamin_a_rae': ('django.db.models.fields.FloatField', [], {}),
            'vitamin_a_ui': ('django.db.models.fields.FloatField', [], {}),
            'vitamin_b12': ('django.db.models.fields.FloatField', [], {}),
            'vitamin_b6': ('django.db.models.fields.FloatField', [], {}),
            'vitamin_c': ('django.db.models.fields.FloatField', [], {}),
            'vitamin_d': ('django.db.models.fields.FloatField', [], {}),
            'vitamin_e': ('django.db.models.fields.FloatField', [], {}),
            'vitamin_k': ('django.db.models.fields.FloatField', [], {}),
            'water': ('django.db.models.fields.FloatField', [], {}),
            'zinc': ('django.db.models.fields.FloatField', [], {})
        },
        'master_class.categorymc': {
            'Meta': {'object_name': 'CategoryMC'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'master_class.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'addit_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_group': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ingredient_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usa_ingredients'", 'to': "orm['ingredients.USAIngredient']"}),
            'master_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ingredients'", 'to': "orm['master_class.MasterClass']"}),
            'measure': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'master_class.masterclass': {
            'Meta': {'object_name': 'MasterClass'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['master_class.CategoryMC']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'for_registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['master_class.SubCategoryMC']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'master_class.mcstep': {
            'Meta': {'object_name': 'MCStep'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'master_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'masterclasses'", 'to': "orm['master_class.MasterClass']"}),
            'step_num': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'master_class.mctool': {
            'Meta': {'object_name': 'MCTool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'master_class.subcategorymc': {
            'Meta': {'object_name': 'SubCategoryMC'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['master_class.CategoryMC']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['master_class']