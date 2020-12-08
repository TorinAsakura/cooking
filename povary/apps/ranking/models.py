# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Vote(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	object_id = models.IntegerField()
	content_type = models.ForeignKey(ContentType)
	content_object = generic.GenericForeignKey()
