# -*- coding: utf-8 -*-
from django import template
from django.contrib.contenttypes.models import ContentType

from comments.models import Comment

register = template.Library()


@register.filter
def get_published_articles_count(category):
    return category.articles.filter(published=True, verified=True).count()
