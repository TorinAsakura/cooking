# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from uuslug import uuslug as slugify


class Tag(models.Model):
	title = models.CharField("Тэг", max_length=255, unique=True)
	slug = models.SlugField("URL", unique=True)
	published = models.BooleanField("Опубликовано", default=True)
	created = models.DateTimeField("Время создания", auto_now_add=True)
	updated = models.DateTimeField("Время последнего обновления", auto_now=True)
	visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)

	def save(self, *args, **kwargs):
		if not self.slug:
			slug_from = self.title[:30]
			self.slug = slugify(slug_from, instance=self)
		super(Tag, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	def inc_visits(self):
		self.visits_num += 1
		self.save()

	class Meta:
		verbose_name = "Тэг"
		verbose_name_plural = "Тэги"


class TaggedItem(models.Model):
	tags = models.ManyToManyField(Tag, verbose_name="Тэги")
	object_id = models.PositiveIntegerField()
	content_type = models.ForeignKey(ContentType)
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	created = models.DateTimeField("Время создания", auto_now_add=True)
	updated = models.DateTimeField("Время последнего обновления", auto_now=True)

	def __unicode__(self):
		tag_list = ', '.join([tag.title for tag in self.tags.all()])
		return tag_list

	class Meta:
		verbose_name = "Тэгированный обьект"
		verbose_name_plural = "Тэгированные обьекты"
