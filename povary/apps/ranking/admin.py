# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic

from sorl.thumbnail.admin.compat import AdminImageMixin

from ranking.models import Vote
#from articles.forms import ArticleAdminForm
from tags.models import Tag, TaggedItem

'''
class TaggedItemInline(generic.GenericStackedInline):
	model = TaggedItem
	max_num = 1


class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ("title", "author", "verified", "category", "pub_date", "published",
		"created", "updated", "tag_list", "direct_link", "visits_num")
	list_filter = ("published", "verified", "author", "category")
	form = ArticleAdminForm
	search_fields = ("title", )

	def tag_list(self, instance):
		tag_list = ', '.join([tag.title for tag in instance.tags])
		return tag_list or "Ничего"
	tag_list.short_description = "Тэги"

	def direct_link(self, instance):
		link = "<a href='%s'>Смотреть на сайте</a>" %  (instance.get_absolute_url())
		return link
	direct_link.short_description = "Ссылка на сайт"
	direct_link.allow_tags = True

	class Media:
		js = (
			'/static/tiny_mce/tiny_mce.js',
			'/static/tiny_mce/articles_tinymce_config.js'
		)


class ArticleCategoryAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ("title", "author", "published", "created", "updated", "tag_list", "direct_link", "visits_num")
	inlines = (TaggedItemInline)
	list_filter = ("published", "author")

	def tag_list(self, instance):
		tag_list = ', '.join([tag.title for tag in instance.tags])
		return tag_list or "Ничего"
	tag_list.short_description = "Тэги"

	def direct_link(self, instance):
		link = "<a href='%s'>Смотреть на сайте</a>" %  (instance.get_absolute_url())
		return link
	direct_link.short_description = "Ссылка на сайт"
	direct_link.allow_tags = True

	class Media:
		js = (
			'/static/tiny_mce/tiny_mce.js',
			'/static/tiny_mce/articles_tinymce_config.js'
		)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
'''

class VoteAdmin(admin.ModelAdmin):
	list_display = ('user', 'content_type', 'created')
	list_filter = ('content_type', 'created')
	search_fields = ('user',)
	list_display_links = ('user', )

	def user(self, instance):
		return instance.author.username
	user.allow_tags = True
	user.short_description = "Пользователь"

admin.site.register(Vote, VoteAdmin)
