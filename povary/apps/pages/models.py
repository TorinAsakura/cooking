# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Page(models.Model):
	title = models.CharField("Заголовок", max_length=255)
	slug = models.SlugField("URL", unique=True)
	body = models.TextField("Текст страницы")
	published = models.BooleanField("Опубликовано", default=True)
	created = models.DateTimeField("Создано", auto_now_add=True)
	updated = models.DateTimeField("Обновлено", auto_now=True)


	def get_absolute_url(self):
		return reverse("page_details", args=(self.slug, ))


	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Страница"
		verbose_name_plural = "Страницы"
