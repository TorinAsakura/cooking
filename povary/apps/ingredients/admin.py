# -*- coding: utf-8 -*-
from django.contrib import admin
from ingredients.models import USAIngredient


class USAIngredientAdmin(admin.ModelAdmin):
	list_display = ('ndb_no', 'short_description', 'name_rus', 'translated',
		'updatable', 'published')
	list_editable = ('short_description', 'name_rus', 'translated',
		'updatable', 'published')
	list_display_links = ('ndb_no', )
	list_filter = ('translated', 'published')
	search_fields = ("name_rus", "short_description")

admin.site.register(USAIngredient, USAIngredientAdmin)