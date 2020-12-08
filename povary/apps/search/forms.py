# -*- coding: utf-8 -*-
from django import forms


from haystack.forms import FacetedSearchForm
from haystack.query import RelatedSearchQuerySet, SearchQuerySet

from recipes.models import Recipe, RecipeDescStep
from cakegallery.models import CakeGallery, CakeCategory
from master_class.models import CategoryMC, MasterClass
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class RecipeSearchForm(FacetedSearchForm):
	q = forms.CharField(required=False, label="Поиск по названию")

	def search(self, *args, **kwargs):
		if self.is_valid():
			query = self.cleaned_data.get('q', None)
		else:
			query = None
		if query:
			sqs = self.searchqueryset.auto_query(query)
		else:
			sqs = self.searchqueryset

		if self.load_all:
			sqs = sqs.load_all()
		#todo - переделать поиск
		sqs = sqs.models(Recipe)

		allowed_fields = ("cuisine", "complexity", "eating_time", "taste", "age_limit",
			"diet", "holiday", "caloric_value", "category",
			"sub_category", "preparation_method"
		)
		filters = tuple(set(self.data.keys()).intersection(allowed_fields))
		for facet_key in filters:
			facet_value = self.data[facet_key]
			if facet_value:
				sqs = sqs.narrow(u"%s:%s" % (facet_key, facet_value))
		return sqs

class CakeGallerySearchForm(FacetedSearchForm):
	q = forms.CharField(required=False, label="Поиск по названию")
	cat = forms.CharField(required=False, label="Категория")
	afilter = forms.CharField(required=False, label="Фильтр")	

	def search(self, *args, **kwargs):
		if self.is_valid():
			query = self.cleaned_data.get('q', None)
			category = self.cleaned_data.get('cat', None)			
			afilter = self.cleaned_data.get('afilter', None)
		else:
			query = None
			category = None			
			afilter = None
		if query:
			sqs = self.searchqueryset.auto_query(query)
		else:
			sqs = self.searchqueryset	
		if self.load_all:
			sqs = sqs.load_all()
		#todo - переделать поиск		
		sqs = sqs.models(CakeGallery)		
		if category:
			category = CakeCategory.objects.get(slug=category)
			sqs = sqs.filter(category=category)			
		allowed_fields = ("author", "category"
		)
		filters = tuple(set(self.data.keys()).intersection(allowed_fields))
		for facet_key in filters:
			facet_value = self.data[facet_key]
			if facet_value:
				sqs = sqs.narrow(u"%s:%s" % (facet_key, facet_value))	
		if afilter=='top':
			sqs = sqs.order_by("-votes")
		elif afilter=='comm':
			sqs = sqs.order_by("-comments")
		else:
			sqs = sqs.order_by("-updated") 				
		return sqs		

class MCSearchForm(FacetedSearchForm):
	q = forms.CharField(required=False, label="Поиск по названию")
	cat = forms.CharField(required=False, label="Категория")
	ing = forms.CharField(required=False, label="Ингредиент")	
	afilter = forms.CharField(required=False, label="Фильтр")	

	def search(self, *args, **kwargs):
		if self.is_valid():
			query = self.cleaned_data.get('q', None)
			category = self.cleaned_data.get('cat', None)
			ingredient = self.cleaned_data.get('ing', None)
			afilter = self.cleaned_data.get('afilter', None)
		else:
			query = None
			category = None
			ingredient = None
			afilter = None
		if query:
			sqs = self.searchqueryset.auto_query(query)
		else:
			sqs = self.searchqueryset	
		if self.load_all:
			sqs = sqs.load_all()
		#todo - переделать поиск		
		sqs = sqs.models(MasterClass)		
		if category:
			category = CategoryMC.objects.get(slug=category)
			sqs = sqs.filter(category=category)			
		if ingredient:
			sqs = sqs.filter(ingredients=ingredient)
		
		allowed_fields = ("description", "author", "category", "ingredients"
		)
		filters = tuple(set(self.data.keys()).intersection(allowed_fields))
		for facet_key in filters:
			facet_value = self.data[facet_key]
			if facet_value:
				sqs = sqs.narrow(u"%s:%s" % (facet_key, facet_value))	
		if afilter=='top':
			sqs = sqs.order_by("-votes")
		elif afilter=='comm':
			sqs = sqs.order_by("-comments")
		else:
			sqs = sqs.order_by("-created") 	
		return sqs			

class FacetSearchForm(forms.ModelForm):
	class Meta:
		model = Recipe
		fields = ("cuisine", "complexity", "eating_time", "taste", "age_limit",
			"diet", "holiday", "preparation_method", "caloric_value"
		)


