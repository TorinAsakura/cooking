# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class TrackingType(models.Model):
	title = models.CharField(max_length=255, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title


class Tracking(models.Model):
	tracking_type = models.ForeignKey(TrackingType)
	message = models.TextField(blank=True, null=True)
	content_type = models.ForeignKey(ContentType, blank=True, null=True)
	object_id = models.PositiveIntegerField(blank=True, null=True)
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Tracking'
		verbose_name_plural = 'Trackings'
		ordering = ('-created', 'content_type')

	def __unicode__(self):
		# return self.content_object.__unicode__()
		return self.content_object


class Visits(models.Model):
	user_agent = models.CharField("Браузер", max_length=255, blank=True, null=True)
	visits_num = models.PositiveIntegerField("Количество посещений", default=0)
	ip_addr = models.CharField("IP", max_length=255, blank=True, null=True)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	created = models.DateTimeField("Время посещения", auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
