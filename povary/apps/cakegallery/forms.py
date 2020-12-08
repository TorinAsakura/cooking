# -*- coding: utf-8 -*-
import datetime

from autoslug.settings import slugify as default_slugify

from django import forms
from django.contrib.contenttypes.models import ContentType

from tags.models import Tag, TaggedItem
from tags.widgets import TagSelect
from cakegallery.models import CakeImage, CakeGallery, CakeCategory, CakeSubCategory
from file_resubmit.admin import AdminResubmitImageWidget, AdminResubmitFileWidget


class CakeImageAdminForm(forms.ModelForm):
	tags = forms.CharField(
		widget=TagSelect,
		required=False
	)

	def __init__(self, *args, **kwargs):
		instance = kwargs.get('instance')
		if hasattr(instance, 'pk'):
			tags = ', '.join([tag.title for tag in instance.tags])
			self.declared_fields['tags'].initial = tags
		super(CakeImageAdminForm, self).__init__(*args, **kwargs)

	def clean_author(self):
		return self.cleaned_data.get('author')

	def clean_category(self):
		return self.cleaned_data.get('category')

	def clean_subcategory(self):
		return self.cleaned_data.get('subcategory')

	def clean_gallery(self):
		data = self.cleaned_data
		gallery = data.get('gallery')
		if gallery:
			upd = {
				"category":gallery.category,
				"subcategory":gallery.subcategory,
				"author":gallery.author
			}
			data.update(upd)
		return gallery

	def save(self, commit=True):
		tags = self.cleaned_data['tags'].strip(',')
		tag_list = tags.split(',')
		instance = super(CakeImageAdminForm, self).save(commit)
		instance.save()
		content_type = ContentType.objects.get_for_model(CakeImage)
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
		return CakeImage.objects.get(id=instance.id)


	class Meta:
		model = CakeImage

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



class CakeImageForm(forms.ModelForm):

	cats = forms.CharField(widget=forms.Select,required=False)
	subcat = forms.CharField(widget=forms.Select,required=False)
	mc_tags = forms.CharField(required=False)

	def __init__(self, gallery, *args, **kwargs):
		super(CakeImageForm, self).__init__(*args, **kwargs)
		self.gallery = gallery
		if gallery:
			self.category = gallery.category
			self.subcategory = gallery.subcategory
			self.author = gallery.author

	def clean_cats(self):
		if self.gallery:
			return self.gallery.category
		data = self.cleaned_data
		cat_slug = data.get('cats')
		try:
			category = CakeCategory.objects.get(slug=cat_slug)
			data.update({'category':category})
		except:
			return None
		return category

	def clean_subcat(self):
		if self.gallery:
			return self.gallery.subcategory
		data = self.cleaned_data
		subcat_slug = data.get('subcat')
		try:
			subcategory = CakeSubCategory.objects.get(slug=subcat_slug)
			data.update({'subcategory':subcategory})
		except:
			return None
		return subcategory

	def return_slug(self, title):
		new_slug = default_slugify(title).replace('-', '_')
		count = CakeImage.objects.filter(slug__startswith=new_slug).count()
		if count == 0:
			return new_slug
		else:
			return '%s-%d' % (new_slug, count)

	def save(self, author, commit=True):
		cimage = super(CakeImageForm, self).save(commit=False)
		cimage.slug = self.return_slug(cimage.title)
		cimage.gallery = self.gallery
		if self.gallery:
			cimage.category = self.gallery.category
			cimage.subcategory = self.gallery.subcategory
		else:
			sc = self.cleaned_data["subcategory"]
			cimage.category = self.cleaned_data["category"]
			cimage.subcategory = self.cleaned_data["subcategory"]
			sc_gallery = None
			try:
				sc_gallery = CakeGallery.objects.get(slug=sc.slug)
			except:
				sc_gallery = CakeGallery()
				sc_gallery.category = cimage.category
				sc_gallery.subcategory = cimage.subcategory
				sc_gallery.title = sc_gallery.subcategory.title
				sc_gallery.slug = sc.slug
				sc_gallery.created = datetime.datetime.now()
				sc_gallery.save()
			sc_gallery.updated = datetime.datetime.now()
			cimage.gallery = sc_gallery
		cimage.author = author
		cimage.save()
		mc_tags_data = self.cleaned_data["mc_tags"]
		tag_list = mc_tags_data.split(',')
		content_type = ContentType.objects.get_for_model(CakeImage)
		tagged_item, created = TaggedItem.objects.get_or_create(
			object_id=cimage.id, content_type=content_type
		)
		tagged_item.tags.clear()
		for title in tag_list:
			if title:
				title = title.strip(u'\xd7')
				tag, created = Tag.objects.get_or_create(title=title)
				tagged_item.tags.add(tag)
			else:
				continue
		return cimage

	class Meta:
		model = CakeImage
		fields = (
			"image",   "category", "subcategory", "title","description"
		)
		widgets = {
            'image': AdminResubmitImageWidget,
        }

	class Media:
		js = (
			'/static/tiny_mce/tiny_mce.js',
			'/static/tiny_mce/articles_tinymce_config.js',
		)
