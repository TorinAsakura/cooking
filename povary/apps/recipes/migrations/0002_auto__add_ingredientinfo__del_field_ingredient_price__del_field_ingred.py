# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IngredientInfo'
        db.create_table('recipes_ingredientinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('calory', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('fat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('protein', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('carbs', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('allergen', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('recipes', ['IngredientInfo'])

        # Adding M2M table for field vitamins on 'IngredientInfo'
        db.create_table('recipes_ingredientinfo_vitamins', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ingredientinfo', models.ForeignKey(orm['recipes.ingredientinfo'], null=False)),
            ('vitamin', models.ForeignKey(orm['recipes.vitamin'], null=False))
        ))
        db.create_unique('recipes_ingredientinfo_vitamins', ['ingredientinfo_id', 'vitamin_id'])

        # Adding M2M table for field minerals on 'IngredientInfo'
        db.create_table('recipes_ingredientinfo_minerals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ingredientinfo', models.ForeignKey(orm['recipes.ingredientinfo'], null=False)),
            ('mineral', models.ForeignKey(orm['recipes.mineral'], null=False))
        ))
        db.create_unique('recipes_ingredientinfo_minerals', ['ingredientinfo_id', 'mineral_id'])

        # Deleting field 'Ingredient.price'
        db.delete_column('recipes_ingredient', 'price')

        # Deleting field 'Ingredient.fat'
        db.delete_column('recipes_ingredient', 'fat')

        # Deleting field 'Ingredient.allergen'
        db.delete_column('recipes_ingredient', 'allergen')

        # Deleting field 'Ingredient.protein'
        db.delete_column('recipes_ingredient', 'protein')

        # Deleting field 'Ingredient.carbs'
        db.delete_column('recipes_ingredient', 'carbs')

        # Deleting field 'Ingredient.title'
        db.delete_column('recipes_ingredient', 'title')

        # Deleting field 'Ingredient.image'
        db.delete_column('recipes_ingredient', 'image')

        # Deleting field 'Ingredient.calory'
        db.delete_column('recipes_ingredient', 'calory')

        # Adding field 'Ingredient.ingredient_info'
        db.add_column('recipes_ingredient', 'ingredient_info',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['recipes.IngredientInfo'], unique=True),
                      keep_default=False)

        # Adding field 'Ingredient.value'
        db.add_column('recipes_ingredient', 'value',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Ingredient.measure'
        db.add_column('recipes_ingredient', 'measure',
                      self.gf('django.db.models.fields.CharField')(default='num', max_length=255),
                      keep_default=False)

        # Removing M2M table for field vitamins on 'Ingredient'
        db.delete_table('recipes_ingredient_vitamins')

        # Removing M2M table for field minerals on 'Ingredient'
        db.delete_table('recipes_ingredient_minerals')

    def backwards(self, orm):
        # Deleting model 'IngredientInfo'
        db.delete_table('recipes_ingredientinfo')

        # Removing M2M table for field vitamins on 'IngredientInfo'
        db.delete_table('recipes_ingredientinfo_vitamins')

        # Removing M2M table for field minerals on 'IngredientInfo'
        db.delete_table('recipes_ingredientinfo_minerals')

        # Adding field 'Ingredient.price'
        db.add_column('recipes_ingredient', 'price',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ingredient.fat'
        db.add_column('recipes_ingredient', 'fat',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ingredient.allergen'
        db.add_column('recipes_ingredient', 'allergen',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Ingredient.protein'
        db.add_column('recipes_ingredient', 'protein',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ingredient.carbs'
        db.add_column('recipes_ingredient', 'carbs',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ingredient.title'
        db.add_column('recipes_ingredient', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Default title', max_length=255),
                      keep_default=False)

        # Adding field 'Ingredient.image'
        db.add_column('recipes_ingredient', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ingredient.calory'
        db.add_column('recipes_ingredient', 'calory',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Ingredient.ingredient_info'
        db.delete_column('recipes_ingredient', 'ingredient_info_id')

        # Deleting field 'Ingredient.value'
        db.delete_column('recipes_ingredient', 'value')

        # Deleting field 'Ingredient.measure'
        db.delete_column('recipes_ingredient', 'measure')

        # Adding M2M table for field vitamins on 'Ingredient'
        db.create_table('recipes_ingredient_vitamins', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ingredient', models.ForeignKey(orm['recipes.ingredient'], null=False)),
            ('vitamin', models.ForeignKey(orm['recipes.vitamin'], null=False))
        ))
        db.create_unique('recipes_ingredient_vitamins', ['ingredient_id', 'vitamin_id'])

        # Adding M2M table for field minerals on 'Ingredient'
        db.create_table('recipes_ingredient_minerals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ingredient', models.ForeignKey(orm['recipes.ingredient'], null=False)),
            ('mineral', models.ForeignKey(orm['recipes.mineral'], null=False))
        ))
        db.create_unique('recipes_ingredient_minerals', ['ingredient_id', 'mineral_id'])

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
        'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'books': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cake_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cookery_in_life': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fb_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'vk_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'recipes.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'seo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['seo.SEO']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['seo.SEO']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.holiday': {
            'Meta': {'object_name': 'Holiday'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_info': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['recipes.IngredientInfo']", 'unique': 'True'}),
            'measure': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'recipes.ingredientinfo': {
            'Meta': {'object_name': 'IngredientInfo'},
            'allergen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'calory': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'carbs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'minerals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['recipes.Mineral']", 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'protein': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vitamins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['recipes.Vitamin']", 'null': 'True', 'blank': 'True'})
        },
        'recipes.mineral': {
            'Meta': {'object_name': 'Mineral'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measure': ('django.db.models.fields.CharField', [], {'default': "'gramm'", 'max_length': '255'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.MineralTitle']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'recipes.mineraltitle': {
            'Meta': {'object_name': 'MineralTitle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'age_limit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caloric_value': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['recipes.Category']", 'null': 'True', 'blank': 'True'}),
            'complexity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'diet': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'eating_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'holiday': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Holiday']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['recipes.Ingredient']", 'null': 'True', 'blank': 'True'}),
            'is_photorecipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portion_num': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prepare_time': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 5, 11, 0, 0)'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'satiety': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'seo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['seo.SEO']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sub_category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['recipes.SubCategory']", 'null': 'True', 'blank': 'True'}),
            'taste': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'recipes.recipesbox': {
            'Meta': {'object_name': 'RecipesBox'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'own_recipesboxes'", 'to': "orm['profiles.Profile']"}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recipesboxes'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['profiles.Profile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipes.Recipe']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipes.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'seo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['seo.SEO']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.vitamin': {
            'Meta': {'object_name': 'Vitamin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measure': ('django.db.models.fields.CharField', [], {'default': "'gramm'", 'max_length': '255'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.VitaminTitle']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'recipes.vitamintitle': {
            'Meta': {'object_name': 'VitaminTitle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'seo.seo': {
            'Meta': {'object_name': 'SEO'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['recipes']