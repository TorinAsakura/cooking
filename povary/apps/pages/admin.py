# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.sites.models import Site

from pages.models import Page


class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ("title", "abs_url", "created", "updated")

	def abs_url(self, obj):
		site = Site.objects.get_current()
		url = "http://%s%s" % (site.domain, obj.get_absolute_url())
		return url
	abs_url.short_description = "Полный URL"

	class Media:
		js = (
			'/static/tiny_mce/tiny_mce.js',
			'/static/js/tiny_mce_config.js'
		)


admin.site.register(Page, PageAdmin)
