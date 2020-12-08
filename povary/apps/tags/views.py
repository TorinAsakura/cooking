# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType

from tags.models import Tag, TaggedItem


def search_tag(request):
	item_list = []
	if request.method == "GET":
		term = request.GET.get("term")
		if term:
			tag_list = Tag.objects.filter(title__istartswith=term)
		for tag in tag_list:
			item_list.append({
				"id": TaggedItem.objects.filter(tags=tag).count(),
				"label": tag.title,
				"value": tag.title
			})
	return HttpResponse(json.dumps(item_list), mimetype="application/json")


def tag_details(request, tag_slug, contenttype_id):
	tag = get_object_or_404(Tag, slug=tag_slug, published=True)
	contenttype = ContentType.objects.get(id=contenttype_id)
	taggeditem_list = TaggedItem.objects.filter(tags=tag, content_type=contenttype).values('object_id')
	model_class = contenttype.model_class()
	instance_list = model_class.objects.filter(
		id__in=map(lambda k: k['object_id'], taggeditem_list),
		published=True
	)
	tag.inc_visits()
	data = {
		"instance_list": instance_list
	}
	return render(request, "tags/tag_details.html", data)