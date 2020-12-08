# -*- coding: utf-8 -*-
from django.contrib import admin

from categories.models import Category, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "visits_num")


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, CategoryAdmin)