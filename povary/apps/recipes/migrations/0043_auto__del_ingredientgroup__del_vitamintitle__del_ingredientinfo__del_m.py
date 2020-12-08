# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'IngredientGroup'
        db.delete_table(u'recipes_ingredientgroup')

        # Deleting model 'VitaminTitle'
        db.delete_table(u'recipes_vitamintitle')

        # Deleting model 'IngredientInfo'
        db.delete_table(u'recipes_ingredientinfo')

        # Deleting model 'MineralTitle'
        db.delete_table(u'recipes_mineraltitle')

        # Deleting model 'Vitamin'
        db.delete_table(u'recipes_vitamin')

        # Deleting model 'Mineral'
        db.delete_table(u'recipes_mineral')

        # Adding field 'Recipe.on_main'
        db.add_column(u'recipes_recipe', 'on_main',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'PrepMethod.icon'
        db.alter_column(u'recipes_prepmethod', 'icon', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Adding model 'IngredientGroup'
        db.create_table(u'recipes_ingredientgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('recipes', ['IngredientGroup'])

        # Adding model 'VitaminTitle'
        db.create_table(u'recipes_vitamintitle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('recipes', ['VitaminTitle'])

        # Adding model 'IngredientInfo'
        db.create_table(u'recipes_ingredientinfo', (
            ('fat_measure', self.gf('django.db.models.fields.CharField')(default='mgramm', max_length=255)),
            ('price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('carbs_measure', self.gf('django.db.models.fields.CharField')(default='mgramm', max_length=255)),
            ('fat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('allergen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('protein_measure', self.gf('django.db.models.fields.CharField')(default='mgramm', max_length=255)),
            ('protein', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carbs', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('calory', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('recipes', ['IngredientInfo'])

        # Adding model 'MineralTitle'
        db.create_table(u'recipes_mineraltitle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('recipes', ['MineralTitle'])

        # Adding model 'Vitamin'
        db.create_table(u'recipes_vitamin', (
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.VitaminTitle'])),
            ('ingredient_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.IngredientInfo'])),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('measure', self.gf('django.db.models.fields.CharField')(default='gramm', max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('recipes', ['Vitamin'])

        # Adding model 'Mineral'
        db.create_table(u'recipes_mineral', (
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.MineralTitle'])),
            ('ingredient_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.IngredientInfo'])),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('measure', self.gf('django.db.models.fields.CharField')(default='gramm', max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('recipes', ['Mineral'])

        # Deleting field 'Recipe.on_main'
        db.delete_column(u'recipes_recipe', 'on_main')


        # Changing field 'PrepMethod.icon'
        db.alter_column(u'recipes_prepmethod', 'icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

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
        u'categories.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'categories.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['categories.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'cities_light.city': {
            'Meta': {'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'cities_light.country': {
            'Meta': {'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'cities_light.region': {
            'Meta': {'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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
        u'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'added_recipes_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'books': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cake_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True', 'blank': 'True'}),
            'cook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cookery_in_life': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']", 'null': 'True', 'blank': 'True'}),
            'fb_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['gallery.Gallery']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'original_avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'registration_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'vk_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'recipes.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipes.holiday': {
            'Meta': {'object_name': 'Holiday'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'icon': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'addit_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_group': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ingredient_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ingredients.USAIngredient']"}),
            'measure': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ingredients'", 'to': u"orm['recipes.Recipe']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'recipes.prepmethod': {
            'Meta': {'object_name': 'PrepMethod'},
            'icon': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'add_watermark': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'age_limit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caloric_value': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['categories.Category']", 'null': 'True', 'blank': 'True'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'complexity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'eating_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'holiday': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Holiday']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'images': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['gallery.Gallery']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'is_photorecipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'on_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'portion_num': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'preparation_method': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'recipes'", 'null': 'True', 'to': u"orm['recipes.PrepMethod']"}),
            'prepare_time_from': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prepare_time_to': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 9, 2, 0, 0)'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Season']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sub_category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['categories.SubCategory']", 'null': 'True', 'blank': 'True'}),
            'taste': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'recipes.recipedescstep': {
            'Meta': {'ordering': "('recipe',)", 'unique_together': "(('recipe', 'step_num'),)", 'object_name': 'RecipeDescStep'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': u"orm['recipes.Recipe']"}),
            'step_num': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'recipes.recipesbox': {
            'Meta': {'object_name': 'RecipesBox'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'own_recipesboxes'", 'to': u"orm['profiles.Profile']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recipesboxes'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['profiles.Profile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'recipe_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipes.Recipe']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'recipes.season': {
            'Meta': {'object_name': 'Season'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['recipes']