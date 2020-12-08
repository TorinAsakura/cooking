# -*- coding: utf-8 -*-
from django import template
from django.contrib.contenttypes.models import ContentType

from ranking.models import Vote

register = template.Library()

@register.filter
def get_votes(item):
	item_contenttype = ContentType.objects.get_for_model(item.__class__)
	vote_list = Vote.objects.filter(
		content_type=item_contenttype, object_id=item.id
	)
	return vote_list

@register.filter
def user_ranked(item, user):
	if user.is_anonymous():
		return False
	item_contenttype = ContentType.objects.get_for_model(item.__class__)
	return len(Vote.objects.filter(content_type=item_contenttype, object_id=item.id, user=user)) > 0
