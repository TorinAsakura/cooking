# -*- coding: utf-8 -*-
import os
import datetime

from uuslug import uuslug as slugify
from sorl.thumbnail import ImageField

from django.db import models
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save, post_save

from tags.models import Tag, TaggedItem
from gallery.models import Gallery
from ranking.models import Vote
from comments.models import Comment, CommentAnswer
from cakegallery.tasks import publish_cakeimage


def category_uploadto(instance, filename):
    from utils import timestampbased_filename
    path = os.path.join(
        "cakemaster_gallery",
        instance.slug,
        timestampbased_filename(filename)
    )
    return path


class CakeCategory(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("URL", unique=True)
    description = models.TextField("Описание", blank=True, null=True)
    image = ImageField("Изображение", upload_to=category_uploadto)
    published = models.BooleanField("Опубликовано", default=True)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Обновлено", auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Тортодельные категории"


def subcategory_uploadto(instance, filename):
    from utils import timestampbased_filename
    path = os.path.join(
        "subcakemaster_gallery",
        instance.slug,
        timestampbased_filename(filename)
    )
    return path


class CakeSubCategory(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("URL", unique=True)
    description = models.TextField("Описание", blank=True, null=True)
    image = ImageField("Изображение", upload_to=subcategory_uploadto, blank=True)
    category = models.ForeignKey(CakeCategory, verbose_name="Раздел", related_name='subcategories')
    published = models.BooleanField("Опубликовано", default=True)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Обновлено", auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Тортодельные подкатегории"


class CakeGallery(models.Model):
    title = models.CharField("Имя", max_length=255)
    slug = models.SlugField("URL", unique=True, null=True)
    author = models.ForeignKey(User, verbose_name="Автор", null=True)
    category = models.ForeignKey(CakeCategory, verbose_name="Категория", related_name='category')
    subcategory = models.ForeignKey(CakeSubCategory, verbose_name="Подкатегория", related_name='subcategory')
    visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Обновлено", auto_now=True)

    def __unicode__(self):
        return self.title

    def images_num(self):
        return self.images().count()

    def images(self):
        return CakeImage.objects.filter(gallery=self)

    def published_images(self):
        return self.images().filter(published=True)

    def get_absolute_url(self):
        return reverse("cakeimage_gallery", args=(self.slug, ))

    @property
    def num_votes(self):
        votes = 0
        for image in self.images():
            votes += image.num_votes
        return votes

    @property
    def num_comments(self):
        comm = 0
        for image in self.images():
            comm += image.num_comments
        return comm

    @staticmethod
    def sort_by_created(list):
        return list # @todo

    @staticmethod
    def sort_by_votes(list):
        return sorted(list, key=lambda mc: -mc.num_votes)

    @staticmethod
    def sort_by_comments(list):
        return sorted(list, key=lambda mc: -mc.num_comments)

    def inc_visits(self):
        self.visits_num += 1
        self.save()


    class Meta:
        verbose_name = "Галерея изображений"
        verbose_name_plural = "Галереи изображений"

def cakeimage_uploadto(instance, filename):
    from utils import timestampbased_filename
    path = os.path.join(
        "cake_images",
        instance.slug,
        "user_%s" % instance.author.id,
        timestampbased_filename(filename)
    )
    return path


class CakeImage(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("URL", unique=True)
    description = models.TextField("Описание", blank=True, null=True)
    image = ImageField("Изображение", upload_to=cakeimage_uploadto)
    image_alt = models.CharField("ALT изображения", max_length=255, blank=True, null=True)
    image_title = models.CharField("TITLE изображения", max_length=255, blank=True, null=True)
    add_watermark = models.BooleanField("Добавлять водяной знак?", default=False)
    gallery = models.ForeignKey(CakeGallery, verbose_name="Галерея", related_name='gallery', null=True)
    category = models.ForeignKey(CakeCategory, verbose_name="Категория", related_name='images',  blank="True", null=True)
    subcategory = models.ForeignKey(CakeSubCategory, verbose_name="Подкатегория", related_name='images', blank="True", null=True)
    author = models.ForeignKey(User, verbose_name="Автор")
    for_registered = models.BooleanField("Только зарегистрированным", default=False)
    pub_date = models.DateTimeField("Дата публикации", blank=True, null=True)
    published = models.BooleanField("Опубликовано", default=True)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Обновлено", auto_now=True)
    ip_addr = models.CharField("IP", max_length=255, editable=False,
        blank=True, null=True
    )
    visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cakeimage_details", args=(self.slug, ))

    @staticmethod
    def get_gallery_list(images_on_scroll):
        counter = -1
        images = CakeImage.objects.filter(published=True)

        gallery_list = []
        for it, image in enumerate(images):
            if it % images_on_scroll is 0:
                counter += 1
                gallery_list.append([])
            gallery_list[counter].append(image)
        return gallery_list

    @property
    def num_votes(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return len( Vote.objects.filter(content_type=content_type, object_id=self.id) )

    @property
    def num_comments(self):
        comments = Comment.objects.filter(content_type_id=self.get_contenttype_id(), object_id=self.id)
        cnt = 0
        for i in range(len(comments)):
            answers = CommentAnswer.objects.filter(comment=comments[i])
            cnt += 1 + len(answers)
        return cnt

    @staticmethod
    def sort_by_created(list):
        return sorted(list, key=lambda mc: mc.created, reverse=True)

    @staticmethod
    def sort_by_votes(list):
        return sorted(list, key=lambda mc: -mc.num_votes)

    @staticmethod
    def sort_by_comments(list):
        return sorted(list, key=lambda mc: -mc.num_comments)

    @property
    def tags(self):
        content_type = ContentType.objects.get_for_model(self)
        try:
            tagged_item = TaggedItem.objects.get(content_type=content_type, object_id=self.id)
        except TaggedItem.DoesNotExist:
            return []
        return tagged_item.tags.all()

    def inc_visits(self):
        self.visits_num += 1
        self.save()

    def get_contenttype_id(self):
        return ContentType.objects.get_for_model(CakeImage).id

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Тортодельные изображения"

@receiver(post_save, sender=CakeImage)
def plan_publish_image_task(sender, instance, created, **kwargs):
    if not instance.published:
        publish_cakeimage.apply_async(args=(instance, ), eta=instance.pub_date)


@receiver(post_save, sender=CakeImage)
def watermark(sender, instance, created, **kwargs):
    if not instance.add_watermark:
        return
    from utils import add_watermark
    marked_img = add_watermark(instance.image)
    if not marked_img:
        return
    instance.image = marked_img
    instance.save()

