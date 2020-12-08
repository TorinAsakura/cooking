# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from filebrowser.fields import FileBrowseField


class BaseCategory(models.Model):
    title = models.CharField("Название", max_length=255)
    slug = models.SlugField("URL", unique=True)
    description = models.TextField("Описание", blank=True, null=True)
    image = FileBrowseField("Изображение", max_length=255, blank=True,
                            null=True)
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    visits_num = models.PositiveIntegerField("Кол. посещений", default=0,
                                             editable=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    def inc_visits(self):
        self.visits_num += 1
        self.save()


class Category(BaseCategory):
    class Meta:
        verbose_name = "Категория рецептов"
        verbose_name_plural = "Категории рецептов"


class SubCategory(BaseCategory):
    category = models.ManyToManyField(Category, verbose_name="Категории")

    def get_absolute_url(self):
        return reverse("category_details", args=(self.slug, ))

    class Meta:
        verbose_name = "Подкатегория рецептов"
        verbose_name_plural = "Подкатегории рецептов"
