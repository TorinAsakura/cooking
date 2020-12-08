# -*- coding: utf-8 -*-
import os
import Image

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User

from filebrowser.fields import FileBrowseField
from filebrowser.base import FileObject
from uuslug import uuslug as slugify
from sorl.thumbnail import ImageField


class Gallery(models.Model):
	title = models.CharField("Имя", max_length=255)
	visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)

	def __unicode__(self):
		return self.title


	def inc_visits(self):
		self.visits_num += 1
		self.save()


	class Meta:
		verbose_name = "Галерея изображений к рецептам"
		verbose_name_plural = "Галереии изображений к рецептам"


def get_upload_path(instance, filename):
	from utils import timestampbased_filename
	gallery_slug = slugify(instance.gallery.title)
	user_slug = slugify(instance.author.username) if instance.author else "anonymous"
	path = os.path.join(
		'gallery',
		gallery_slug,
		user_slug,
		timestampbased_filename(filename))
	return path


class GalleryImage(models.Model):
	image = ImageField("Изображение", upload_to=get_upload_path, max_length=255)
	title = models.CharField("Подпись", max_length=255, blank=True, null=True)
	author = models.ForeignKey(User, verbose_name="Автор", blank=True, null=True)
	gallery = models.ForeignKey(Gallery, verbose_name="Галерея изображений", related_name="images")
	visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)

	def __unicode__(self):
		return self.title if self.title else self.image.name


	def inc_visits(self):
		self.visits_num += 1
		self.save()


	class Meta:
		verbose_name = "Изображение"
		verbose_name_plural = "Изображения"


@receiver(post_save, sender=GalleryImage)
def watermark(sender, instance, created, **kwargs):
	from utils import add_watermark
	marked_img = add_watermark(instance.image)
	if not marked_img:
		return
	instance.image = marked_img
	instance.save()
