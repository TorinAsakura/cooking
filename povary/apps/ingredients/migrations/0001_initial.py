# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'USAIngredient'
        db.create_table('ingredients_usaingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ndb_no', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('water', self.gf('django.db.models.fields.FloatField')()),
            ('energy', self.gf('django.db.models.fields.FloatField')()),
            ('protein', self.gf('django.db.models.fields.FloatField')()),
            ('lipid_total', self.gf('django.db.models.fields.FloatField')()),
            ('ash', self.gf('django.db.models.fields.FloatField')()),
            ('carbohydrt', self.gf('django.db.models.fields.FloatField')()),
            ('fiber_td', self.gf('django.db.models.fields.FloatField')()),
            ('sugar_total', self.gf('django.db.models.fields.FloatField')()),
            ('calcium', self.gf('django.db.models.fields.FloatField')()),
            ('iron', self.gf('django.db.models.fields.FloatField')()),
            ('magnesium', self.gf('django.db.models.fields.FloatField')()),
            ('phosphorus', self.gf('django.db.models.fields.FloatField')()),
            ('potassium', self.gf('django.db.models.fields.FloatField')()),
            ('sodium', self.gf('django.db.models.fields.FloatField')()),
            ('zinc', self.gf('django.db.models.fields.FloatField')()),
            ('copper', self.gf('django.db.models.fields.FloatField')()),
            ('manganese', self.gf('django.db.models.fields.FloatField')()),
            ('selenium', self.gf('django.db.models.fields.FloatField')()),
            ('vitamin_c', self.gf('django.db.models.fields.FloatField')()),
            ('thiamin', self.gf('django.db.models.fields.FloatField')()),
            ('riboflavin', self.gf('django.db.models.fields.FloatField')()),
            ('niacin', self.gf('django.db.models.fields.FloatField')()),
            ('panto_acid', self.gf('django.db.models.fields.FloatField')()),
            ('vitamin_b6', self.gf('django.db.models.fields.FloatField')()),
            ('folate_total', self.gf('django.db.models.fields.FloatField')()),
            ('food_folate', self.gf('django.db.models.fields.FloatField')()),
            ('folate_dfe', self.gf('django.db.models.fields.FloatField')()),
            ('choline_total', self.gf('django.db.models.fields.FloatField')()),
            ('vitamin_b12', self.gf('django.db.models.fields.FloatField')()),
            ('vitamin_a_ui', self.gf('django.db.models.fields.FloatField')()),
            ('vitamin_a_rae', self.gf('django.db.models.fields.FloatField')()),
            ('retinol', self.gf('django.db.models.fields.FloatField')()),
            ('alpha_carot', self.gf('django.db.models.fields.FloatField')()),
            ('beta_carot', self.gf('django.db.models.fields.FloatField')()),
            ('beta_crypt', self.gf('django.db.models.fields.FloatField')()),
            ('lycopene', self.gf('django.db.models.fields.FloatField')()),
            ('lut_zea', self.gf('django.db.models.fields.FloatField')()),
            ('vitamin_e', self.gf('django.db.models.fields.FloatField')()),
            ('vitamin_d', self.gf('django.db.models.fields.FloatField')()),
            ('vi_vit_d_ui', self.gf('django.db.models.fields.FloatField')()),
            ('vitamin_k', self.gf('django.db.models.fields.FloatField')()),
            ('fa_sat', self.gf('django.db.models.fields.FloatField')()),
            ('fa_mono', self.gf('django.db.models.fields.FloatField')()),
            ('fa_poly', self.gf('django.db.models.fields.FloatField')()),
            ('cholestrl', self.gf('django.db.models.fields.FloatField')()),
            ('gm_wt1', self.gf('django.db.models.fields.FloatField')()),
            ('gmwt_desc1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gmwt_2', self.gf('django.db.models.fields.FloatField')()),
            ('gmwt_desc2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('refuse_pct', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('ingredients', ['USAIngredient'])

    def backwards(self, orm):
        # Deleting model 'USAIngredient'
        db.delete_table('ingredients_usaingredient')

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
            'ndb_no': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'niacin': ('django.db.models.fields.FloatField', [], {}),
            'panto_acid': ('django.db.models.fields.FloatField', [], {}),
            'phosphorus': ('django.db.models.fields.FloatField', [], {}),
            'potassium': ('django.db.models.fields.FloatField', [], {}),
            'protein': ('django.db.models.fields.FloatField', [], {}),
            'refuse_pct': ('django.db.models.fields.FloatField', [], {}),
            'retinol': ('django.db.models.fields.FloatField', [], {}),
            'riboflavin': ('django.db.models.fields.FloatField', [], {}),
            'selenium': ('django.db.models.fields.FloatField', [], {}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sodium': ('django.db.models.fields.FloatField', [], {}),
            'sugar_total': ('django.db.models.fields.FloatField', [], {}),
            'thiamin': ('django.db.models.fields.FloatField', [], {}),
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
        }
    }

    complete_apps = ['ingredients']