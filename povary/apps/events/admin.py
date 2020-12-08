# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic

from events.models import Event, EventCategory
from events.forms import EventForm


class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('title', 'category', 'start_date', 'end_date', 'published', 'direct_link', "visits_num")
	form = EventForm
        
	def direct_link(self, obj):
		if obj.published:
			link = "<a href='%s'>Смотреть на сайте</a>" % (obj.get_absolute_url())
			return link
		else:
			return "NP"
	direct_link.short_description = "Ссылка на сайт"
	direct_link.allow_tags = True


class EventCategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'published', 'created', 'updated', 'direct_link', "visits_num")
	prepopulated_fields = {"slug": ("title",)}

	def direct_link(self, obj):
		if obj.published:
			link = "<a href='%s'>Смотреть на сайте</a>" % (obj.get_absolute_url())
			return link
		else:
			return "NP"
	direct_link.short_description = "Ссылка на сайт"
	direct_link.allow_tags = True


admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
