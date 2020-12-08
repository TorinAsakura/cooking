# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType

from utils import ajax_required, get_avatar
from setman import settings as custom_settings

from statistics.tasks import track_event
from notifications.views import send_notice
from ranking.models import Vote

@ajax_required
@csrf_protect
def add_vote(request, contenttype_id, obj_id):
	if request.method=="POST":
		user = request.user
		if user.is_anonymous():
			data = json.dumps({
				"status": "error",
				"message": "user is anonymous"
			})
			return HttpResponse(data, mimetype="application/json")
		contenttype = ContentType.objects.get(id=contenttype_id)
		obj_model = contenttype.model_class()
		user_votes = Vote.objects.filter(content_type=contenttype_id, object_id=obj_id, user=user)
		vote_added = False
		if len(user_votes) == 0:			
			vote_added = True		
		try:
			obj = obj_model.objects.get(id=obj_id)
		except obj_model.DoesNotExist:
			data = json.dumps({
				"status": "error",
				"message": "Object doesn't exist"
			})
			return HttpResponse(data, mimetype="application/json")	
		
		if user.is_authenticated():
			if vote_added:
				vote = Vote(user=user,object_id=obj_id,content_type=contenttype)					
				vote.save()
			else:
				Vote.objects.filter(user=user,object_id=obj_id,content_type=contenttype).delete()
		site = Site.objects.get_current()
		if vote_added:
			send_notice(
				title=u"Новый голос",
				message=u"""Ваш "%s" был поддержан "%s". http://%s """ %
				(
					obj.title, user.username, site.domain
				),
				to_user=obj.author
			)
			tracking_data = {
				"object_id": vote.id,
				"model": Vote,
				"tracking_type": "vote"
			}
			track_event.delay(tracking_data)
		votes_num = Vote.objects.filter(object_id=obj_id,content_type=contenttype).count()
		data = json.dumps({
			"status": "ok",
			"message": "Vote accepted",
			"votes": votes_num,
		})
		return HttpResponse(data, mimetype="application/json")
	else:
		data = json.dumps({
			"status": "error",
			"message": "Only POST request"
		})
		return HttpResponse(data, mimetype="application/json")

