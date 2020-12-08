# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic

from subscriptions.models import SubscriptionArchiv

class SubscriptionArchivAdmin(admin.ModelAdmin):

	class Media:
		js = (
			'/static/tiny_mce/tiny_mce.js',
			'/static/tiny_mce/articles_tinymce_config.js'
		)

admin.site.register(SubscriptionArchiv, SubscriptionArchivAdmin)
