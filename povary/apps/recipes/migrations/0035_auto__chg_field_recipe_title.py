# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recipe.title'
        db.alter_column('recipes_recipe', 'title', self.gf('django.db.models.fields.CharField')(max_length=120))
    def backwards(self, orm):

        # Changing field 'Recipe.title'
        db.alter_column('recipes_recipe', 'title', self.gf('django.db.models.fields.CharField')(max_length=244))
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
        'categories.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'categories.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['categories.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        'profiles.award': {
            'Meta': {'object_name': 'Award'},
            'icon': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'added_recipes_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'awards': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['profiles.Award']", 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'books': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cake_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cookery_in_life': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fb_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['gallery.Gallery']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'original_avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'registration_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'vk_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'recipes.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.holiday': {
            'Meta': {'object_name': 'Holiday'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'icon': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'addit_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_group': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ingredient_info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingredients.USAIngredient']"}),
            'measure': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ingredients'", 'to': "orm['recipes.Recipe']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'recipes.ingredientgroup': {
            'Meta': {'object_name': 'IngredientGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.ingredientinfo': {
            'Meta': {'object_name': 'IngredientInfo'},
            'allergen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'calory': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'carbs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'carbs_measure': ('django.db.models.fields.CharField', [], {'default': "'mgramm'", 'max_length': '255'}),
            'fat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fat_measure': ('django.db.models.fields.CharField', [], {'default': "'mgramm'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'protein': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'protein_measure': ('django.db.models.fields.CharField', [], {'default': "'mgramm'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.mineral': {
            'Meta': {'object_name': 'Mineral'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.IngredientInfo']"}),
            'measure': ('django.db.models.fields.CharField', [], {'default': "'gramm'", 'max_length': '255'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.MineralTitle']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'recipes.mineraltitle': {
            'Meta': {'object_name': 'MineralTitle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.prepmethod': {
            'Meta': {'object_name': 'PrepMethod'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'age_limit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caloric_value': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['categories.Category']", 'null': 'True', 'blank': 'True'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'complexity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'eating_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'holiday': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Holiday']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['gallery.Gallery']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'is_photorecipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'portion_num': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'preparation_method': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'recipes'", 'null': 'True', 'to': "orm['recipes.PrepMethod']"}),
            'prepare_time_from': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prepare_time_to': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 23, 0, 0)'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Season']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sub_category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['categories.SubCategory']", 'null': 'True', 'blank': 'True'}),
            'taste': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'recipes.recipedescstep': {
            'Meta': {'ordering': "('recipe',)", 'unique_together': "(('recipe', 'step_num'),)", 'object_name': 'RecipeDescStep'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': "orm['recipes.Recipe']"}),
            'step_num': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'recipes.recipesbox': {
            'Meta': {'object_name': 'RecipesBox'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'own_recipesboxes'", 'to': "orm['profiles.Profile']"}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recipesboxes'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['profiles.Profile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'recipe_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipes.Recipe']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'recipes.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.vitamin': {
            'Meta': {'object_name': 'Vitamin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.IngredientInfo']"}),
            'measure': ('django.db.models.fields.CharField', [], {'default': "'gramm'", 'max_length': '255'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.VitaminTitle']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'recipes.vitamintitle': {
            'Meta': {'object_name': 'VitaminTitle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['recipes']