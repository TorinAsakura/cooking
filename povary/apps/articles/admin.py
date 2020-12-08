# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic

from sorl.thumbnail.admin.compat import AdminImageMixin
from sorl.thumbnail import get_thumbnail

from articles.models import Article, ArticleCategory
from articles.forms import ArticleAdminForm
from tags.models import Tag, TaggedItem

from markitup.widgets import AdminMarkItUpWidget


class TaggedItemInline(generic.GenericStackedInline):
    model = TaggedItem
    max_num = 1


class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
    "title", "thumbnail", "tag_list", "verified", "category", "pub_date",
    "published",
    "created", "updated")

    list_filter = ("published", "verified", "author", "category")
    form = ArticleAdminForm
    search_fields = ("title",)


    def thumbnail(self, obj):
        if obj.image:
            im = get_thumbnail(obj.image, '100x100', crop='center', quality=80)
            img_location = """<img src="/media/%s" />""" % im.name
            return img_location
        return u''

    thumbnail.short_description = "Превью"
    thumbnail.allow_tags = True


    def tag_list(self, instance):
        tag_list = ', '.join([tag.title for tag in instance.tags])
        return tag_list or "Ничего"

    tag_list.short_description = "Тэги"

    def direct_link(self, instance):
        link = "<a href='%s'>Смотреть на сайте</a>" % (
        instance.get_absolute_url())
        return link

    direct_link.short_description = "Ссылка на сайт"
    direct_link.allow_tags = True


    # Markitup
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'body':
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(ArticleAdmin, self).formfield_for_dbfield(db_field,
                                                               **kwargs)


class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
    "title", "author", "published", "created", "updated", "tag_list",
    "direct_link", "visits_num")
    inlines = (TaggedItemInline,)
    list_filter = ("published", "author")

    def tag_list(self, instance):
        tag_list = ', '.join([tag.title for tag in instance.tags])
        return tag_list or "Ничего"

    tag_list.short_description = "Тэги"

    def direct_link(self, instance):
        link = "<a href='%s'>Смотреть на сайте</a>" % (
        instance.get_absolute_url())
        return link

    direct_link.short_description = "Ссылка на сайт"
    direct_link.allow_tags = True


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
