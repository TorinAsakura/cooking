# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'USAIngredient.fa_mono'
        db.alter_column('ingredients_usaingredient', 'fa_mono', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.copper'
        db.alter_column('ingredients_usaingredient', 'copper', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vitamin_a_rae'
        db.alter_column('ingredients_usaingredient', 'vitamin_a_rae', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.folate_total'
        db.alter_column('ingredients_usaingredient', 'folate_total', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.energy'
        db.alter_column('ingredients_usaingredient', 'energy', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.lipid_total'
        db.alter_column('ingredients_usaingredient', 'lipid_total', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vitamin_b12'
        db.alter_column('ingredients_usaingredient', 'vitamin_b12', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.alpha_carot'
        db.alter_column('ingredients_usaingredient', 'alpha_carot', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.carbohydrt'
        db.alter_column('ingredients_usaingredient', 'carbohydrt', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.fiber_td'
        db.alter_column('ingredients_usaingredient', 'fiber_td', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.zinc'
        db.alter_column('ingredients_usaingredient', 'zinc', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.protein'
        db.alter_column('ingredients_usaingredient', 'protein', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vitamin_b6'
        db.alter_column('ingredients_usaingredient', 'vitamin_b6', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.niacin'
        db.alter_column('ingredients_usaingredient', 'niacin', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vitamin_k'
        db.alter_column('ingredients_usaingredient', 'vitamin_k', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.sodium'
        db.alter_column('ingredients_usaingredient', 'sodium', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vitamin_c'
        db.alter_column('ingredients_usaingredient', 'vitamin_c', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.selenium'
        db.alter_column('ingredients_usaingredient', 'selenium', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.thiamin'
        db.alter_column('ingredients_usaingredient', 'thiamin', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vitamin_d'
        db.alter_column('ingredients_usaingredient', 'vitamin_d', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vitamin_e'
        db.alter_column('ingredients_usaingredient', 'vitamin_e', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.folic_acid'
        db.alter_column('ingredients_usaingredient', 'folic_acid', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.refuse_pct'
        db.alter_column('ingredients_usaingredient', 'refuse_pct', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.short_description'
        db.alter_column('ingredients_usaingredient', 'short_description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'USAIngredient.fa_poly'
        db.alter_column('ingredients_usaingredient', 'fa_poly', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vitamin_a_ui'
        db.alter_column('ingredients_usaingredient', 'vitamin_a_ui', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.panto_acid'
        db.alter_column('ingredients_usaingredient', 'panto_acid', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.vi_vit_d_ui'
        db.alter_column('ingredients_usaingredient', 'vi_vit_d_ui', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.beta_crypt'
        db.alter_column('ingredients_usaingredient', 'beta_crypt', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.gmwt_2'
        db.alter_column('ingredients_usaingredient', 'gmwt_2', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.potassium'
        db.alter_column('ingredients_usaingredient', 'potassium', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.cholestrl'
        db.alter_column('ingredients_usaingredient', 'cholestrl', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.water'
        db.alter_column('ingredients_usaingredient', 'water', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.lycopene'
        db.alter_column('ingredients_usaingredient', 'lycopene', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.fa_sat'
        db.alter_column('ingredients_usaingredient', 'fa_sat', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.gmwt_desc2'
        db.alter_column('ingredients_usaingredient', 'gmwt_desc2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'USAIngredient.gmwt_desc1'
        db.alter_column('ingredients_usaingredient', 'gmwt_desc1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'USAIngredient.sugar_total'
        db.alter_column('ingredients_usaingredient', 'sugar_total', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.ash'
        db.alter_column('ingredients_usaingredient', 'ash', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.lut_zea'
        db.alter_column('ingredients_usaingredient', 'lut_zea', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.beta_carot'
        db.alter_column('ingredients_usaingredient', 'beta_carot', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.phosphorus'
        db.alter_column('ingredients_usaingredient', 'phosphorus', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.retinol'
        db.alter_column('ingredients_usaingredient', 'retinol', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.choline_total'
        db.alter_column('ingredients_usaingredient', 'choline_total', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.gm_wt1'
        db.alter_column('ingredients_usaingredient', 'gm_wt1', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.manganese'
        db.alter_column('ingredients_usaingredient', 'manganese', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.calcium'
        db.alter_column('ingredients_usaingredient', 'calcium', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.riboflavin'
        db.alter_column('ingredients_usaingredient', 'riboflavin', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.magnesium'
        db.alter_column('ingredients_usaingredient', 'magnesium', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.iron'
        db.alter_column('ingredients_usaingredient', 'iron', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.food_folate'
        db.alter_column('ingredients_usaingredient', 'food_folate', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'USAIngredient.folate_dfe'
        db.alter_column('ingredients_usaingredient', 'folate_dfe', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'USAIngredient.fa_mono'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.fa_mono' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.copper'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.copper' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vitamin_a_rae'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vitamin_a_rae' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.folate_total'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.folate_total' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.energy'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.energy' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.lipid_total'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.lipid_total' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vitamin_b12'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vitamin_b12' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.alpha_carot'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.alpha_carot' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.carbohydrt'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.carbohydrt' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.fiber_td'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.fiber_td' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.zinc'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.zinc' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.protein'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.protein' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vitamin_b6'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vitamin_b6' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.niacin'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.niacin' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vitamin_k'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vitamin_k' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.sodium'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.sodium' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vitamin_c'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vitamin_c' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.selenium'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.selenium' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.thiamin'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.thiamin' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vitamin_d'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vitamin_d' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vitamin_e'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vitamin_e' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.folic_acid'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.folic_acid' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.refuse_pct'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.refuse_pct' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.short_description'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.short_description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.fa_poly'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.fa_poly' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vitamin_a_ui'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vitamin_a_ui' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.panto_acid'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.panto_acid' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.vi_vit_d_ui'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.vi_vit_d_ui' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.beta_crypt'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.beta_crypt' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.gmwt_2'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.gmwt_2' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.potassium'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.potassium' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.cholestrl'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.cholestrl' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.water'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.water' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.lycopene'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.lycopene' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.fa_sat'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.fa_sat' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.gmwt_desc2'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.gmwt_desc2' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.gmwt_desc1'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.gmwt_desc1' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.sugar_total'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.sugar_total' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.ash'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.ash' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.lut_zea'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.lut_zea' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.beta_carot'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.beta_carot' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.phosphorus'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.phosphorus' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.retinol'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.retinol' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.choline_total'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.choline_total' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.gm_wt1'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.gm_wt1' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.manganese'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.manganese' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.calcium'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.calcium' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.riboflavin'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.riboflavin' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.magnesium'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.magnesium' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.iron'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.iron' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.food_folate'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.food_folate' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'USAIngredient.folate_dfe'
        raise RuntimeError("Cannot reverse this migration. 'USAIngredient.folate_dfe' and its values cannot be restored.")

    models = {
        'ingredients.usaingredient': {
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        }
    }

    complete_apps = ['ingredients']