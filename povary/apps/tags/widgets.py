# -*- coding: utf-8 -*-
from django.forms.widgets import TextInput
from django.forms.util import flatatt
from django.utils.safestring import mark_safe


class TagSelect(TextInput):

    def render(self, name, value, attrs=None, choices=()):
        # import ipdb
        # ipdb.set_trace()
        value = value or ''
        output = u"""
	        <input type="text" name="tags" id="id_tags" value="%s">
	        <ul id="mytags"></ul>
        """ % (value)
        return mark_safe(output)
