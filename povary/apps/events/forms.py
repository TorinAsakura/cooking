# -*- coding: utf-8 -*-
from django import forms

from regions.models import City, Country

from events.models import Event
from events.widgets import CountryWidget, CityWidget


class EventForm(forms.ModelForm):
    country = forms.CharField(
        widget=CountryWidget,
        label='Страна')
    city = forms.CharField(widget=CityWidget,
                           label='Город')

    def clean_country(self):

        print self.cleaned_data

        country = self.cleaned_data['country']
        if not country:
            raise forms.ValidationError("Обязательное поле")
        return Country.objects.get(id=country)

    def clean_city(self):
        city = self.cleaned_data['city']
        country = self.cleaned_data['country']
        if not city:
            raise forms.ValidationError("Обязательное поле")
        if not country:
            raise forms.ValidationError("Сначала заполните страну")
        return City.objects.get(id=city, country=country)

    class Meta:
        model = Event
