# -*- coding: utf-8 -*-
import datetime
import os

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

from uuslug import uuslug as slugify
from sorl.thumbnail import ImageField

from recipes.models import INGREDIENT_MEASURE_CHOICES
from ingredients.models import USAIngredient
from tags.models import TaggedItem
from ranking.models import Vote
from comments.models import Comment, CommentAnswer

def categorymc_upload(instance, filename):
	from utils import timestampbased_filename
	filename = timestampbased_filename(filename)
	path = os.path.join(
		"master_class",
		"category",
		slugify(instance.title),
		filename
	)
	return path


def subcategorymc_upload(instance, filename):
	from utils import timestampbased_filename
	path = os.path.join(
		"master_class",
		"subcategory",
		slugify(instance.title),
		timestampbased_filename(filename)
	)
	return path


class CategoryMC(models.Model):
	title = models.CharField("Название", max_length=255)
	slug = models.SlugField("URL", unique=True)
	image = ImageField("Фото", upload_to=categorymc_upload)
	description = models.TextField("Описание")
	published = models.BooleanField("Опубликовано", default=True)
	created = models.DateTimeField("Создано", auto_now_add=True)
	updated = models.DateTimeField("Обновлено", auto_now=True)
	visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)
	is_cake = models.BooleanField("Категория випечок?", default=False)

	def get_absolute_url(self):
		return reverse("mc_category_details", args=(self.slug, ))

	def __unicode__(self):
		return self.title

	def inc_visits(self):
		self.visits_num += 1
		self.save()

	class Meta:
		verbose_name = "Раздел"
		verbose_name_plural = "Разделы"


class SubCategoryMC(models.Model):
	title = models.CharField("Название", max_length=255)
	slug = models.SlugField("URL", unique=True)
	image = ImageField("Фото", upload_to=subcategorymc_upload)
	description = models.TextField("Описание")
	category = models.ForeignKey(CategoryMC, verbose_name="Раздел")
	published = models.BooleanField("Опубликовано", default=True)
	created = models.DateTimeField("Создано", auto_now_add=True)
	updated = models.DateTimeField("Обновлено", auto_now=True)
	visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)

	def get_absolute_url(self):
		return reverse("mc_subcategory_details", args=(self.slug, ))

	def __unicode__(self):
		return self.title

	def inc_visits(self):
		self.visits_num += 1
		self.save()

	class Meta:
		verbose_name = "Подраздел"
		verbose_name_plural = "Подразделы"


class MCTool(models.Model):
	title = models.CharField("Название", max_length=255)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Инструмент"
		verbose_name_plural = "Инструменты"


def mc_upload_path(instance, filename):
	from utils import timestampbased_filename
	timestamp_filename = timestampbased_filename(filename)
	path = os.path.join(
		"master_class",
		"main_images",
		"user_%s" % instance.author.id,
		slugify(instance.title),
		timestamp_filename
	)
	return path

from autoslug import AutoSlugField


class MasterClass(models.Model):
	title = models.CharField("Заголовок", max_length=255)
	slug = models.SlugField("URL", unique=True)
	description = models.TextField("Описание", blank=True, null=True)
	image = ImageField("Фото", upload_to=mc_upload_path)
	image_alt = models.CharField("ALT изображения", max_length=255, blank=True, null=True)
	image_title = models.CharField("TITLE изображения", max_length=255, blank=True, null=True)
	add_watermark = models.BooleanField("Добавлять водяной знак?", default=False)
	category = models.ForeignKey(CategoryMC, blank=True, null=True)
	subcategory = models.ForeignKey(SubCategoryMC, blank=True, null=True)
	author = models.ForeignKey(User, verbose_name="Автор")
	published = models.BooleanField("Опубликовано", default=True)
	pub_date = models.DateTimeField("Дата публикации", blank=True, null=True)
	created = models.DateTimeField("Создано", auto_now_add=True)
	updated = models.DateTimeField("Обновлено", auto_now=True)
	for_registered = models.BooleanField("Только для зарегистрированных", default=False)
	ip_addr = models.CharField("IP", max_length=255, blank=True, null=True, editable=False)
	visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)
	is_cake = models.BooleanField("Випечка?", default=False)
	prepare_time_from = models.PositiveIntegerField("Время приготовления: От", default=0)
	prepare_time_to = models.PositiveIntegerField("Время приготовления: До", default=200)

	def get_tags(self):
		content_type = ContentType.objects.get_for_model(self)
		try:
			tagged_item = TaggedItem.objects.get(content_type=content_type, object_id=self.id)
		except TaggedItem.DoesNotExist:
			return []
		return tagged_item.tags.all()

	def get_categories(self):
		return self.category.all()

	def save(self, *args, **kwargs):
		if not self.pub_date:
			self.pub_date = datetime.datetime.now()
		super(MasterClass, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("masterclass_details", args=(self.slug, ))

	def __unicode__(self):
		return self.title

	def inc_visits(self):
		self.visits_num += 1
		self.save()

	def get_ingredients(self):
		return Ingredient.objects.filter(master_class=self)

	def get_steps(self):
		return MCStep.objects.filter(master_class=self).order_by("-step_num")

	def get_votes(self):
		content_type = ContentType.objects.get_for_model(MasterClass)
		return Vote.objects.filter(content_type=content_type, object_id=self.id)

	def get_comments_num(self):
		comments = Comment.objects.filter(content_type_id=self.get_contenttype_id(), object_id=self.id)
		cnt = 0
		for i in range(len(comments)):
			answers = CommentAnswer.objects.filter(comment=comments[i])
			cnt += 1 + len(answers)
		return cnt

	def get_contenttype_id(self):
		return ContentType.objects.get_for_model(MasterClass).id

	@property
	def num_votes(self):
		return len(self.get_votes())

	@staticmethod
	def sort_by_votes(list):
		return sorted(list, key=lambda mc: -mc.num_votes)

	class Meta:
		verbose_name = "Мастер класс"
		verbose_name_plural = "Мастер классы"


def mcstep_uploadpath(instance, filename):
	from utils import timestampbased_filename
	path = os.path.join(
		"master_class",
		"steps",
		slugify(instance.master_class.slug),
		"user_%s" % instance.master_class.author.id,
		timestampbased_filename(filename)
	)
	return path


class MCStep(models.Model):
	step_num = models.PositiveIntegerField()
	description = models.TextField("Описание", blank=True, null=True)
	image = ImageField("Фото", upload_to=mcstep_uploadpath)
	master_class = models.ForeignKey(MasterClass, related_name="masterclasses")
	note = models.TextField("Заметка автора", blank=True, null=True)

	def get_next_step_num(self, master_class):
		present_keys = MCStep.objects.filter(master_class=master_class).order_by('-step_num').values_list('step_num', flat=True)
		if present_keys:
			return present_keys[0] + 1
		else:
			return 0

	def save(self, *args, **kwargs):
		self.step_num = self.get_next_step_num(self.master_class)
		super(MCStep, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.master_class

	class Meta:
		verbose_name = ""
		verbose_name_plural = "Шаги мастер-класса"


class Ingredient(models.Model):
	ingredient_info = models.ForeignKey(USAIngredient,
		verbose_name="Список ингредиентов",
		related_name="usa_ingredients"
	)
	value = models.FloatField("Количество")
	measure = models.CharField("Тип измерения", max_length=255,
		choices=INGREDIENT_MEASURE_CHOICES
	)
	ingredient_group = models.CharField("Группа ингредиентов", max_length=255,
	    blank=True, null=True
	)
	addit_info = models.TextField(u"Дополнительная информация", blank=True, null=True)
	master_class = models.ForeignKey(MasterClass, related_name="ingredients")

	def __unicode__(self):
		return self.ingredient_info.short_description

	class Meta:
		verbose_name = ""
		verbose_name_plural = "Ингредиенты мастер-класса"


@receiver(post_save, sender=MasterClass)
def watermark(sender, instance, created, **kwargs):
	if not instance.add_watermark:
		return
	from utils import add_watermark
	marked_img = add_watermark(instance.image)
	if not marked_img:
		return
	instance.image = marked_img
	instance.save()

