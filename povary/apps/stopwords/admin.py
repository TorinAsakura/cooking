# -*- coding: utf-8 -*-
from django.contrib import admin
from stopwords.models import StopWord


class StopWordAdmin(admin.ModelAdmin):
	list_display_links = ("id", )
	list_display = ("id", "stopword", "replaceword", "active")
	list_editable = ("stopword", "replaceword", "active")


admin.site.register(StopWord, StopWordAdmin)