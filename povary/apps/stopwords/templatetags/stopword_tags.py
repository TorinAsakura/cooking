# -*- coding: utf-8 -*-
from django import template

from stopwords.utils import replace_stopwords


register = template.Library()


@register.filter
def r_stopwords(text):
	return replace_stopwords(text)

