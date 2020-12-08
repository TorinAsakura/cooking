# -*- coding: utf-8 -*-
from django import template
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem

register = template.Library()

@register.filter
def contenttype_id(obj):
	contenttype = ContentType.objects.get_for_model(obj.__class__)
	return contenttype.id

@register.filter
def get_tags(obj):
	contenttype = ContentType.objects.get_for_model(obj.__class__)
	try:
		tagged_item = TaggedItem.objects.get(object_id=obj.id, content_type=contenttype)
	except TaggedItem.DoesNotExist:
		return []
	return tagged_item.tags.all()

