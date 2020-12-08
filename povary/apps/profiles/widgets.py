# -*- coding: utf-8 -*-
from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class AvatarWidget(forms.widgets.Input):
	def render(self, name, value, attrs=None):
		data = {"name": name, "value": value}
		return render_to_string("widgets/avatar_widget.html", data)

