# -*- coding: utf-8 -*-
from haystack import indexes

from recipes.models import Recipe, RecipeDescStep


class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, model_attr='title')
	title = indexes.CharField(model_attr='title')
	description = indexes.CharField(model_attr="description", null=True)
	cuisine = indexes.CharField(faceted=True, model_attr="cuisine", null=True)
	taste = indexes.CharField(faceted=True, model_attr="taste", null=True)
	age_limit = indexes.CharField(faceted=True, model_attr="age_limit", null=True)
	complexity = indexes.CharField(faceted=True, model_attr="complexity", null=True)
	eating_time = indexes.CharField(faceted=True, model_attr="eating_time", null=True)
	diet = indexes.CharField(faceted=True, model_attr="diet", null=True)
	holiday = indexes.CharField(faceted=True, model_attr="holiday", null=True)
	caloric_value = indexes.CharField(faceted=True, model_attr="caloric_value", null=True)
	season = indexes.CharField(faceted=True, model_attr="season", null=True)
	body = indexes.CharField(model_attr="body", null=True)
	step_descriptions = indexes.CharField(model_attr="step_descriptions", null=True)
	

	def get_model(self):
		return Recipe

	def index_queryset(self, using=None):
		return self.get_model().objects.all().select_related()


from master_class.models import MasterClass

class MCIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, model_attr='title')
	title = indexes.CharField(model_attr='title')
	description = indexes.CharField(model_attr="description", null=True)
	category = indexes.CharField(indexed=True, model_attr="category", null=True)	
	ingredients = indexes.MultiValueField(indexed=True, stored=True)	
	votes = indexes.IntegerField()
	comments = indexes.IntegerField()
	created = indexes.DateTimeField()

		
	def prepare_category(self, obj):        	
	    return obj.category		

	def prepare_ingredients(self, obj):        	
		if obj.get_ingredients():
	        	return [ing.ingredient_info.ndb_no for ing in obj.get_ingredients()]
		else:
			return []

	def prepare_votes(self, obj):        	
		return obj.num_votes	

	def prepare_comments(self, obj):        	
		return obj.get_comments_num()

	def prepare_created(self, obj):        	
		return obj.created		

	def get_model(self):
		return MasterClass

	def index_queryset(self, using=None):
		return self.get_model().objects.all()

from cakegallery.models import CakeGallery, CakeCategory

class CakeGalleryIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, model_attr='title')
	title = indexes.CharField(model_attr='title')	
	category = indexes.CharField(indexed=True, model_attr="category", null=True)
	votes = indexes.IntegerField()
	comments = indexes.IntegerField()
	updated = indexes.DateTimeField()	
		
	def prepare_category(self, obj):        	
	    return obj.category			

	def prepare_votes(self, obj):        	
		return obj.num_votes	

	def prepare_comments(self, obj):        	
		return obj.num_comments

	def prepare_updated(self, obj):        	
		return obj.updated	

	def get_model(self):
		return CakeGallery

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
