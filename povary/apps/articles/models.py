# -*- coding: utf-8 -*-
import datetime
from django.db.models import Count
import os

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

from uuslug import uuslug as slugify
from sorl.thumbnail import ImageField

from tags.models import Tag, TaggedItem
from comments.models import Comment, CommentAnswer


def category_upload_path(instance, filename):
    from utils import timestampbased_filename

    category_slug = slugify(instance.title)
    path = os.path.join(
        'article_category',
        category_slug,
        timestampbased_filename(filename)
    )
    return path


def article_upload_path(instance, filename):
    from utils import timestampbased_filename

    article_slug = slugify(instance.title)
    path = os.path.join(
        'articles',
        article_slug,
        timestampbased_filename(filename)
    )
    return path


class ArticleCategory(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("URL", unique=True)
    image = ImageField("Изображение", upload_to=category_upload_path, blank=True, null=True)
    image_alt = models.CharField("ALT изображения", max_length=255, blank=True, null=True)
    image_title = models.CharField("TITLE изображения", max_length=255, blank=True, null=True)
    add_watermark = models.BooleanField("Добавлять водяной знак?", default=False)
    description = models.TextField("Описание", blank=True, null=True)
    author = models.ForeignKey(User, verbose_name="Автор")
    published = models.BooleanField("Опубликовано", default=True)
    created = models.DateTimeField("Время создания", auto_now_add=True)
    updated = models.DateTimeField("Время последнего обновления", auto_now=True)
    visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)

    def inc_visits(self):
        self.visits_num += 1
        self.save()

    @property
    def tags(self):
        content_type = ContentType.objects.get_for_model(self)
        try:
            tagged_item = TaggedItem.objects.get(content_type=content_type, object_id=self.id)\
            .prefetch_related('tags')
        except TaggedItem.DoesNotExist:
            return []
        return tagged_item.tags.all()

    def get_absolute_url(self):
        return reverse("articlecategory_details", args=(self.slug, ))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"


class Article(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("URL", unique=True)
    old_id = models.IntegerField("Старый ID", unique=True, blank=True, null=True)
    image = models.ImageField("Изображение", upload_to=article_upload_path,
                              blank=True, null=True
    )
    image_alt = models.CharField("ALT изображения", max_length=255, blank=True, null=True)
    image_title = models.CharField("TITLE изображения", max_length=255, blank=True, null=True)
    add_watermark = models.BooleanField("Добавлять водяной знак?", default=False)
    description = models.TextField("Описание", blank=True, null=True)
    body = models.TextField("Текст статьи")
    author = models.ForeignKey(User, verbose_name="Автор")
    category = models.ForeignKey(ArticleCategory, verbose_name="Категория", related_name="articles")
    verified = models.BooleanField("Проверена", default=False)
    published = models.BooleanField("Опубликовано", default=True)
    pub_date = models.DateTimeField("Опубликовано", blank=True)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Обновлено", auto_now=True)
    visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)
    comments_num = models.PositiveIntegerField(u"Кол. коментариев", default=0, editable=False)

    def inc_visits(self):
        self.visits_num += 1
        self.save()

    @property
    def num_comments(self):
        comments = Comment.objects.filter(
            content_type_id=ContentType.objects.get_for_model(self).id,
            object_id=self.id
        ).annotate(answer_count=Count('answers')).values_list('answer_count', flat=True)
        cnt = 0

        for i in range(len(comments)):
            cnt += 1 + comments[i]

        return cnt

    @property
    def tags(self):
        content_type = ContentType.objects.get_for_model(self)
        try:
            tagged_item = TaggedItem.objects.get(content_type=content_type, object_id=self.id)
        except TaggedItem.DoesNotExist:
            return []
        return tagged_item.tags.all()

    def save(self, *args, **kwargs):
        if not self.pub_date:
            self.pub_date = datetime.datetime.now()
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_details", args=(self.slug, ))

    def get_contenttype_id(self):
        return ContentType.objects.get_for_model(Article).id

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


@receiver(post_save, sender=Article)
def publish_article_task(sender, instance, created, **kwargs):
    from articles.tasks import publish_article

    if not instance.published:
        publish_article.apply_async(args=(instance, ), eta=instance.pub_date)


@receiver(post_save, sender=Article)
def article_watermark(sender, instance, created, **kwargs):
    if not instance.add_watermark:
        return
    from utils import add_watermark

    marked_img = add_watermark(instance.image)
    if not marked_img:
        return
    instance.image = marked_img
    instance.save()


@receiver(post_save, sender=ArticleCategory)
def articlecategory_watermark(sender, instance, created, **kwargs):
    if not instance.add_watermark:
        return
    from utils import add_watermark

    marked_img = add_watermark(instance.image)
    if not marked_img:
        return
    instance.image = marked_img
    instance.save()
