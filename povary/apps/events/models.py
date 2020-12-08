# -*- coding: utf-8 -*-
import os

from django.db import models
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField

from regions.models import Country, City


class EventCategory(models.Model):
	title = models.CharField("Заголовок", max_length=255, blank=True, null=True)
	slug = models.SlugField("URL", unique=True)
	description = models.TextField("Описание")
	published = models.BooleanField("Опубликовано", default=True)
	created = models.DateTimeField("Время создания", auto_now_add=True)
	updated = models.DateTimeField("Время последнего обновления", auto_now=True)
	visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('eventcategory_details', args=[self.slug, ])


	def inc_visits(self):
		self.visits_num += 1
		self.save()


	class Meta:
		verbose_name = "Категория событий"
		verbose_name_plural = "Категории событий"

def event_uploadto(instance, filename):
	from utils import timestampbased_filename
	path = os.path.join(
		'events',
		instance.slug,
		timestampbased_filename(filename)
	)
	return path

class Event(models.Model):
	title = models.CharField("Заголовок", max_length=255)
	slug = models.SlugField("URL", unique=True)
	description = models.TextField("Описание", blank=True, null=True)
	image = ImageField("Изображение", upload_to=event_uploadto, blank=True, null=True)
	start_date = models.DateTimeField("Начало")
	end_date = models.DateTimeField("Окончание")
	country = models.ForeignKey(Country, blank=True, null=True,
		verbose_name="Страна", related_name='events'
	)
	city = models.ForeignKey(City, blank=True, null=True, verbose_name="Город",
		related_name='events'
	)
	category = models.ForeignKey(EventCategory, verbose_name="Категория", related_name="events")
	published = models.BooleanField("Опубликовано", default=True)
	created = models.DateTimeField("Время создания", auto_now_add=True)
	updated = models.DateTimeField("Время последнего обновления", auto_now=True)
	visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)
	is_cake = models.BooleanField("Событие тортоделов", default=False)
	is_cook = models.BooleanField("Событие поваров", default=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('event_details', args=[self.slug, ])


	def inc_visits(self):
		self.visits_num += 1
		self.save()


	class Meta:
		verbose_name = "Событие"
		verbose_name_plural = "События"
