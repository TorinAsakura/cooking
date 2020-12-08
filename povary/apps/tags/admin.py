# -*- coding: utf-8 -*-
from django.contrib import admin

from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
	list_display_links = ('id', )
	list_display = ('id', 'title', 'published', 'created', 'updated', "visits_num")
	list_editable = ('title', 'published')

admin.site.register(Tag, TagAdmin)