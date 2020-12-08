# -*- coding: utf-8 -*-
from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from gallery.models import Gallery, GalleryImage


class GalleryImageInline(admin.TabularInline):
	model = GalleryImage


class GalleryAdmin(admin.ModelAdmin):
	inlines = (GalleryImageInline, )
	list_display = ("title", "visits_num")


class GalleryImageAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ("image", "visits_num")


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)