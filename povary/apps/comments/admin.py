# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.gis.utils import GeoIP

from django_countries.fields import Country

from comments.models import Comment, CommentAnswer


class CommentAdmin(admin.ModelAdmin):
    list_display = (
    'body_safe', 'authority', 'published', 'content_type', 'created',
    'ip_address', 'location', 'created',
    'comment_link', 'image'
    )
    list_filter = ('author', 'is_anonymous',
                   'published', 'content_type')
    search_fields = ('title', 'body')
    list_display_links = ('body_safe', )

    def body_safe(self, instance):
        return mark_safe(instance.body)

    body_safe.allow_tags = True
    body_safe.short_description = "Сообщение"

    def location(self, instance):
        city = GeoIP().city(instance.ip_addr or "")
        if city:
            flag_url = Country(city['country_code']).flag
            city_name = city['city']
            location = """
			<img src="%s"/> %s
			""" % (flag_url, city_name)
            return mark_safe(location)
        return "Не определено"

    location.allow_tags = True
    location.short_description = "Местонахождение по IP"

    def comment_link(self, obj):
        link = "<a href='%s'>Смотреть на сайте</a>" % (obj.get_absolute_url())
        return link

    comment_link.short_description = "Ссылка на комментарий"
    comment_link.allow_tags = True

    def ip_address(self, obj):
        if not obj.ip_addr:
            return "Не определено"
        whois_url = "http://whois.domaintools.com/%s" % obj.ip_addr
        link = "<a href='%s'>%s</a>" % (whois_url, obj.ip_addr)
        return link

    ip_address.short_description = "IP адресс"
    ip_address.allow_tags = True

    def authority(self, obj):
        if not obj.author:
            return "Аноним"
        else:
            return obj.author.username

    authority.short_description = "Автор"


class CommentAnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_safe', 'author', 'is_anonymous',
                    'published', 'created', 'ip_addr', 'location')
    list_filter = ('author', 'is_anonymous',
                   'published')
    search_fields = ('title', 'body')
    list_display_links = ('title', 'body_safe')

    def body_safe(self, instance):
        return mark_safe(instance.body)

    body_safe.allow_tags = True
    body_safe.short_description = "Сообщение"

    def location(self, instance):
        city = GeoIP().city(instance.ip_addr or "")
        if city:
            flag_url = Country(city['country_code']).flag
            city_name = city['city']
            location = """
			<img src="%s"/> %s
			""" % (flag_url, city_name)
            return mark_safe(location)
        return "Не определено"

    location.allow_tags = True
    location.short_description = "Местонахождение по IP"


admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentAnswer, CommentAnswerAdmin)
