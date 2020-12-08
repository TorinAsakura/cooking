# -*- coding: utf-8 -*-
from django import template
from django.contrib.contenttypes.models import ContentType

from comments.models import Comment

register = template.Library()

@register.filter
def get_comments(item):
	item_contenttype = ContentType.objects.get_for_model(item.__class__)
	comments = Comment.objects.filter(
		content_type=item_contenttype, object_id=item.id
	).order_by("created").prefetch_related('answers')\
	.prefetch_related('author').select_related("author__profile")
	return comments
