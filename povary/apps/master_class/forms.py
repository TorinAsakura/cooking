# -*- coding: utf-8 -*-
from django import forms
from django.contrib.contenttypes.models import ContentType

from master_class.models import MasterClass, MCStep, CategoryMC, SubCategoryMC

from tags.models import Tag, TaggedItem
from tags.widgets import TagSelect
from autoslug import AutoSlugField

from autoslug.settings import slugify as default_slugify
from ingredients.models import USAIngredient
from recipes.forms import IngredientSelect
from models import Ingredient

from file_resubmit.admin import AdminResubmitImageWidget, AdminResubmitFileWidget


class IngredientForm(forms.ModelForm):
	ingredient_info = forms.ModelChoiceField(
		queryset=USAIngredient.objects.all(), label="Список ингредиентов",
		widget=IngredientSelect({"style": "width: 150px;"})
	)
	
	def save(self, mc, commit=True):
		ingredient = super(IngredientForm, self).save(commit=False)
		if self.cleaned_data:
			ingredient.master_class = mc
			ingredient.ingredient_group = self.cleaned_data.get("ingredient_group")
			ingredient.save()			
		return ingredient

	class Meta:
		model = Ingredient
		exclude = ('master_class', )


class MasterClassForm(forms.ModelForm):
	tags = forms.CharField(
		widget=TagSelect,
		required=False,
	)
	
	def __init__(self, *args, **kwargs):
		
		instance = kwargs.get('instance')
		if hasattr(instance, 'pk'):				
			tags = ', '.join([tag.title for tag in instance.get_tags()])
			self.declared_fields['tags'].initial = tags
		super(MasterClassForm, self).__init__(*args, **kwargs)
	
	def save(self, commit=True):			
		instance = super(MasterClassForm, self).save(commit)	
		instance.save()	
		tags = self.cleaned_data['tags'].strip(',')
		tag_list = tags.split(',')
		content_type = ContentType.objects.get_for_model(MasterClass)
		tagged_item, created = TaggedItem.objects.get_or_create(
			object_id=instance.id, content_type=content_type
		)
		tagged_item.tags.clear()
		for title in tag_list:
			if title:
				title = title.strip(u'\xd7')
				tag, created = Tag.objects.get_or_create(title=title)
				tagged_item.tags.add(tag)
			else:
				continue			
		return MasterClass.objects.get(id=instance.id)

	class Meta:
		model = MasterClass

	class Media:
		css = {
			"tagit": (
				"tags/css/reset.css",
				"tags/css/master.css",
				"tags/css/tagit.ui-zendesk.css",
				"tags/css/jquery.tagit.css",
				)
		}
		js = (
			'js/jquery-1.7.2.min.js',
			'js/jquery-ui-1.8.20.custom.min.js',
			'tags/js/tag-it.js',
			'tags/js/tags.js'
		)


class CakeMCStepForm(forms.ModelForm):
	def save(self, mc, commit=True):
		step = super(CakeMCStepForm, self).save(commit=False)
		if self.cleaned_data:
			step.master_class = mc
			step.save()
		return step

	class Meta:
		model = MCStep
		exclude = ('master_class', 'step_num')
		widgets = {'image': AdminResubmitImageWidget}


class CakeMCFormStep1(forms.ModelForm):	
	cats = forms.CharField(widget=forms.Select, required=True)
	subcat = forms.CharField(widget=forms.Select, required=True)
	mc_tags = forms.CharField(required=False)
	
	def clean_prepare_time_to(self):
		data = self.cleaned_data
		timefrom = data.get('prepare_time_from')
		timeto = data.get('prepare_time_to')
		if timefrom > timeto:
			raise forms.ValidationError("Время приготовления указано неверно")
		return timeto	

	def clean_cats(self):
		data = self.cleaned_data
		cat_slug = data.get('cats')			
		try:
			category = CategoryMC.objects.get(slug=cat_slug)			
			data.update({'category': category})
		except:
			pass
		return cat_slug	

	def clean_subcat(self):	
		data = self.cleaned_data
		subcat_slug = data.get('subcat')	
		try:
			subcategory = SubCategoryMC.objects.get(slug=subcat_slug)			
			data.update({'subcategory':subcategory})			
		except:
			pass
		return subcat_slug	

	def return_slug(self, title):
		new_slug = default_slugify(title).replace('-', '_')
		count = MasterClass.objects.filter(slug__startswith=new_slug).count()
		if count == 0:
			return new_slug
		else:
			return '%s-%d' % (new_slug, count)

	def save(self, author, commit=True):
		mc = super(CakeMCFormStep1, self).save(commit=False)
		mc.author = author
		mc.slug = self.return_slug(mc.title)
		mc.category = self.cleaned_data["category"]			
		mc.subcategory = self.cleaned_data["subcategory"]
		mc.is_cake = True
		mc.save()			
		mc_tags_data = self.cleaned_data["mc_tags"]
		tag_list = mc_tags_data.split(',')
		content_type = ContentType.objects.get_for_model(MasterClass)
		tagged_item, created = TaggedItem.objects.get_or_create(
			object_id=mc.id, content_type=content_type
		)
		tagged_item.tags.clear()
		for title in tag_list:
			if title:
				title = title.strip(u'\xd7')
				tag, created = Tag.objects.get_or_create(title=title)
				tagged_item.tags.add(tag)
			else:
				continue
		return mc

	class Meta:
		model = MasterClass
		fields = ("image", "prepare_time_from", "prepare_time_to", "category", "subcategory", "title", "description")
		widgets = {'image': AdminResubmitImageWidget}

	class Media:
		js = ()


class CakeMCFormStep2(forms.ModelForm):	
	groups = forms.CharField(required=False)		

	class Meta:	
		model = MasterClass			
		fields = ()


class CakeMCFormStep3(forms.ModelForm):		

	class Meta:
		model = MasterClass
		fields = ()
		widgets = {'image': AdminResubmitImageWidget}
