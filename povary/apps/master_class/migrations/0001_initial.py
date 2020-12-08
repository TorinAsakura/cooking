# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategoryMC'
        db.create_table('master_class_categorymc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('master_class', ['CategoryMC'])

        # Adding model 'SubCategoryMC'
        db.create_table('master_class_subcategorymc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['master_class.CategoryMC'])),
        ))
        db.send_create_signal('master_class', ['SubCategoryMC'])

        # Adding model 'MCTool'
        db.create_table('master_class_mctool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('master_class', ['MCTool'])

        # Adding model 'MasterClass'
        db.create_table('master_class_masterclass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['master_class.CategoryMC'], null=True, blank=True)),
            ('subcategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['master_class.SubCategoryMC'], null=True, blank=True)),
            ('for_registered', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('master_class', ['MasterClass'])

        # Adding model 'Ingredient'
        db.create_table('master_class_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient_info', self.gf('django.db.models.fields.related.ForeignKey')(related_name='usa_ingredients', to=orm['ingredients.USAIngredient'])),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('measure', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ingredient_group', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('addit_info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('master_class', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ingredients', to=orm['master_class.MasterClass'])),
        ))
        db.send_create_signal('master_class', ['Ingredient'])

    def backwards(self, orm):
        # Deleting model 'CategoryMC'
        db.delete_table('master_class_categorymc')

        # Deleting model 'SubCategoryMC'
        db.delete_table('master_class_subcategorymc')

        # Deleting model 'MCTool'
        db.delete_table('master_class_mctool')

        # Deleting model 'MasterClass'
        db.delete_table('master_class_masterclass')

        # Deleting model 'Ingredient'
        db.delete_table('master_class_ingredient')

    models = {
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['master_class.CategoryMC']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'for_registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['master_class.SubCategoryMC']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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