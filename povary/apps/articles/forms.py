# -*- coding: utf-8 -*-
from django import forms
from django.contrib.contenttypes.models import ContentType

from sorl.thumbnail.admin.current import AdminImageWidget

from tags.models import Tag, TaggedItem
from tags.widgets import TagSelect
from articles.models import Article


class ArticleAdminForm(forms.ModelForm):
	tags = forms.CharField(
		widget=TagSelect,
		required=False
	)

	def __init__(self, *args, **kwargs):
		instance = kwargs.get('instance')
		if hasattr(instance, 'pk'):
			tags = ', '.join([tag.title for tag in instance.tags])
			self.declared_fields['tags'].initial = tags
		super(ArticleAdminForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		tags = self.cleaned_data['tags'].strip(',')
		tag_list = tags.split(',')
		instance = super(ArticleAdminForm, self).save(commit)
		instance.save()
		content_type = ContentType.objects.get_for_model(Article)
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
		return Article.objects.get(id=instance.id)

	
	class Meta:
		model = Article
		widgets = {
            'image': AdminImageWidget
        }

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
