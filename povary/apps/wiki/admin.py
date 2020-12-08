# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.template.defaultfilters import date as date_format
from django.conf import settings

from wiki.models import WikiPage, WikiPageVersion, WikiCategory, \
	WikiSubCategory, WikiSubSubCategory, WikiDiscussion


class WikiPageVersionInline(admin.StackedInline):
	model = WikiPageVersion
	extra = 0


class DiscussionInline(admin.StackedInline):
	model = WikiDiscussion
	extra = 0


class WikiPageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ("title", "author", "category", "subcategory",
		"subsubcategory", "published", "verified", "created", "updated",
		"last_revision"
	)
	inlines = (WikiPageVersionInline, )
	raw_id_fields = ('redactors', )

	def last_revision(self, obj):
		revision_list = obj.revisions.all().order_by('-changed')
		if not revision_list:
			return "Нет версий"
		date = revision_list[0].changed
		from django.forms.util import to_current_timezone
		return date_format(to_current_timezone(date), settings.DATETIME_FORMAT)
	last_revision.short_description = "Последняя версия"
	last_revision.allow_tags = True


class WikiPageVersionAdmin(admin.ModelAdmin):
	list_display = ("page", "page_id", "revision", "changed", "author", "ip_addr", "status")
	ordering = ("page__id", )
	inlines = (DiscussionInline, )

	def page_id(self, obj):
		return obj.page.id
	page_id.short_description = "ID страницы"



class WikiCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}


class WikiSubCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}


class WikiSubSubCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}


admin.site.register(WikiPage, WikiPageAdmin)
admin.site.register(WikiPageVersion, WikiPageVersionAdmin)
admin.site.register(WikiCategory, WikiCategoryAdmin)
admin.site.register(WikiSubCategory, WikiSubCategoryAdmin)
admin.site.register(WikiSubSubCategory, WikiSubSubCategoryAdmin)
