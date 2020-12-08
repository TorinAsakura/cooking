# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from sorl.thumbnail.admin import AdminImageMixin

from cakegallery.models import CakeCategory, CakeSubCategory, CakeImage, CakeGallery
from cakegallery.forms import CakeImageAdminForm
from comments.models import Comment
from file_resubmit.admin import AdminResubmitMixin

class CommentInline(generic.GenericStackedInline):
	model = Comment
	extra = 1

class CakeGalleryAdmin(AdminResubmitMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ('title', 'category', 'subcategory', 'author', 'images_num', 'created', 'updated')	

	def images_num(self, obj):
		return CakeImage.objects.filter(gallery=obj).count()
	images_num.short_description = "Кол. изображений"


class CakeCategoryAdmin(AdminResubmitMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ('title', 'published', 'subcategory_num', 'images_num')

	def subcategory_num(self, obj):
		return obj.subcategories.all().count()
	subcategory_num.short_description = "Кол. подкатегорий"

	def images_num(self, obj):
		return obj.images.all().count()
	images_num.short_description = "Кол. изображений"


class CakeSubCategoryAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ('title', 'published', 'images_num')

	def images_num(self, obj):
		return obj.images.all().count()
	images_num.short_description = "Кол. изображений"


class CakeImageAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	inlines = (CommentInline,)
	form = CakeImageAdminForm
	list_display = ('title', 'gallery', 'category', 'subcategory', 'published',
		'for_registered', 'visits_num', 'author', 'created', 'tags',
		'comments_num', 'ip_address', 'direct_link'
	)

	def tags(self, obj):
		return ','.join([tag.title for tag in obj.tags]) or "Нет"
	tags.short_description = "Тэги"

	def comments_num(self, obj):
		cakeimage_contenttype = ContentType.objects.get_for_model(CakeImage)
		comments = Comment.objects.filter(content_type=cakeimage_contenttype, object_id=obj.id)
		return comments.count()
	comments_num.short_description = "Кол. комментариев"

	def ip_address(self, obj):
		if not obj.ip_addr:
			return "Не определено"
		whois_url = "http://whois.domaintools.com/%s" % obj.ip_addr
		link = "<a href='%s'>%s</a>" % (whois_url, obj.ip_addr)
		return link
	ip_address.short_description = "IP адрес"
	ip_address.allow_tags = True

	def direct_link(self, obj):
		link = "<a href='%s'>Смотреть</a>" % (obj.get_absolute_url())
		return link
	direct_link.short_description = "Ссылка"
	direct_link.allow_tags = True
      


admin.site.register(CakeGallery, CakeGalleryAdmin)
admin.site.register(CakeCategory, CakeCategoryAdmin)
admin.site.register(CakeSubCategory, CakeSubCategoryAdmin)
admin.site.register(CakeImage, CakeImageAdmin)
