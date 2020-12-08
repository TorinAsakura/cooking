# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    depends_on = (
        ("profiles", "0001_initial"),
        ("ingredients", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('recipes_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('recipes', ['Category'])

        # Adding model 'SubCategory'
        db.create_table('recipes_subcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('recipes', ['SubCategory'])

        # Adding M2M table for field category on 'SubCategory'
        db.create_table('recipes_subcategory_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subcategory', models.ForeignKey(orm['recipes.subcategory'], null=False)),
            ('category', models.ForeignKey(orm['recipes.category'], null=False))
        ))
        db.create_unique('recipes_subcategory_category', ['subcategory_id', 'category_id'])

        # Adding model 'VitaminTitle'
        db.create_table('recipes_vitamintitle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('recipes', ['VitaminTitle'])

        # Adding model 'Vitamin'
        db.create_table('recipes_vitamin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.VitaminTitle'])),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('measure', self.gf('django.db.models.fields.CharField')(default='gramm', max_length=255)),
        ))
        db.send_create_signal('recipes', ['Vitamin'])

        # Adding model 'MineralTitle'
        db.create_table('recipes_mineraltitle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('recipes', ['MineralTitle'])

        # Adding model 'Mineral'
        db.create_table('recipes_mineral', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.MineralTitle'])),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('measure', self.gf('django.db.models.fields.CharField')(default='gramm', max_length=255)),
        ))
        db.send_create_signal('recipes', ['Mineral'])

        # Adding model 'Ingredient'
        db.create_table('recipes_ingredient', (
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
        db.send_create_signal('recipes', ['Ingredient'])

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

        # Adding model 'Cuisine'
        db.create_table('recipes_cuisine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('recipes', ['Cuisine'])

        # Adding model 'Holiday'
        db.create_table('recipes_holiday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('recipes', ['Holiday'])

        # Adding model 'Recipe'
        db.create_table('recipes_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('main_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_photorecipe', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cuisine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Cuisine'], null=True, blank=True)),
            ('complexity', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('eating_time', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('taste', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('age_limit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('diet', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('satiety', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('holiday', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Holiday'], null=True, blank=True)),
            ('prepare_time', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('caloric_value', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('portion_num', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 5, 11, 0, 0))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('recipes', ['Recipe'])

        # Adding M2M table for field ingredients on 'Recipe'
        db.create_table('recipes_recipe_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False)),
            ('ingredient', models.ForeignKey(orm['recipes.ingredient'], null=False))
        ))
        db.create_unique('recipes_recipe_ingredients', ['recipe_id', 'ingredient_id'])

        # Adding M2M table for field category on 'Recipe'
        db.create_table('recipes_recipe_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False)),
            ('category', models.ForeignKey(orm['recipes.category'], null=False))
        ))
        db.create_unique('recipes_recipe_category', ['recipe_id', 'category_id'])

        # Adding M2M table for field sub_category on 'Recipe'
        db.create_table('recipes_recipe_sub_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False)),
            ('subcategory', models.ForeignKey(orm['recipes.subcategory'], null=False))
        ))
        db.create_unique('recipes_recipe_sub_category', ['recipe_id', 'subcategory_id'])

        # Adding model 'RecipesBox'
        db.create_table('recipes_recipesbox', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='own_recipesboxes', to=orm['profiles.Profile'])),
        ))
        db.send_create_signal('recipes', ['RecipesBox'])

        # Adding M2M table for field recipe_list on 'RecipesBox'
        db.create_table('recipes_recipesbox_recipe_list', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipesbox', models.ForeignKey(orm['recipes.recipesbox'], null=False)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False))
        ))
        db.create_unique('recipes_recipesbox_recipe_list', ['recipesbox_id', 'recipe_id'])

        # Adding M2M table for field followers on 'RecipesBox'
        db.create_table('recipes_recipesbox_followers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipesbox', models.ForeignKey(orm['recipes.recipesbox'], null=False)),
            ('profile', models.ForeignKey(orm['profiles.profile'], null=False))
        ))
        db.create_unique('recipes_recipesbox_followers', ['recipesbox_id', 'profile_id'])

    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('recipes_category')

        # Deleting model 'SubCategory'
        db.delete_table('recipes_subcategory')

        # Removing M2M table for field category on 'SubCategory'
        db.delete_table('recipes_subcategory_category')

        # Deleting model 'VitaminTitle'
        db.delete_table('recipes_vitamintitle')

        # Deleting model 'Vitamin'
        db.delete_table('recipes_vitamin')

        # Deleting model 'MineralTitle'
        db.delete_table('recipes_mineraltitle')

        # Deleting model 'Mineral'
        db.delete_table('recipes_mineral')

        # Deleting model 'Ingredient'
        db.delete_table('recipes_ingredient')

        # Removing M2M table for field vitamins on 'Ingredient'
        db.delete_table('recipes_ingredient_vitamins')

        # Removing M2M table for field minerals on 'Ingredient'
        db.delete_table('recipes_ingredient_minerals')

        # Deleting model 'Cuisine'
        db.delete_table('recipes_cuisine')

        # Deleting model 'Holiday'
        db.delete_table('recipes_holiday')

        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table('recipes_recipe_ingredients')

        # Removing M2M table for field category on 'Recipe'
        db.delete_table('recipes_recipe_category')

        # Removing M2M table for field sub_category on 'Recipe'
        db.delete_table('recipes_recipe_sub_category')

        # Deleting model 'RecipesBox'
        db.delete_table('recipes_recipesbox')

        # Removing M2M table for field recipe_list on 'RecipesBox'
        db.delete_table('recipes_recipesbox_recipe_list')

        # Removing M2M table for field followers on 'RecipesBox'
        db.delete_table('recipes_recipesbox_followers')

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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
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
    }

    complete_apps = ['recipes']