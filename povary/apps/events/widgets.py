# -*- coding: utf-8 -*-
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from regions.models import Country, City


class CountryWidget(TextInput):
	def render(self, name, value, attrs=None):
		value_id = value
		filled_value = Country.objects.get(id=int(value)).title if value else ""
		final_attrs = ""
		if attrs:
			for name, value in attrs.items():
				final_attrs += "%s='%s' " % (name, value)
		print final_attrs, value_id, filled_value
		return mark_safe(
			render_to_string(
				['events/country_widget.html', ],
				{
					"attrs": final_attrs,
					"value_name": filled_value,
					"value_id": value_id
				}
			)
		)


class CityWidget(TextInput):
	def render(self, name, value, attrs=None):
		value_id = value
		filled_value = City.objects.get(id=int(value)).title if value else ""
		final_attrs = ""
		if attrs:
			for name, value in attrs.items():
				final_attrs += "%s='%s' " % (name, value)
		print final_attrs, value_id, filled_value
		return mark_safe(
			render_to_string(
				['events/city_widget.html', ],
				{
					"attrs": final_attrs,
					"value_name": filled_value,
					"value_id": value_id
				}
			)
		)