# -*- encoding: utf-8 -*-
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
# from django.db.models.signals import pre_save


class CommentBase(models.Model):
    title = models.CharField(u"Заголовок", max_length=255, blank=True,
                             null=True)
    body = models.TextField(u"Текст")
    author = models.ForeignKey(User, blank=True, null=True,
                               verbose_name=u"Автор")
    is_anonymous = models.BooleanField(u"Анонимный коментарий", default=False)
    ip_addr = models.CharField(u"IP адресс того кто комментировал", blank=True,
                               null=True, max_length=20)
    published = models.BooleanField(u"Опубликован", default=True)
    created = models.DateTimeField(u"Добавлено", auto_now_add=True)
    image = models.ImageField(u"Изображение", null=True, blank=True, upload_to='comments_images')


    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.body[:100]


    class Meta:
        abstract = True

class Comment(CommentBase):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    of = generic.GenericForeignKey('content_type', 'object_id')

    def get_answers(self):
        return CommentAnswer.objects.filter(comment=self).order_by("created")

    class Meta:
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"

    def get_absolute_url(self):
        object_model = self.content_type.model_class()
        obj = object_model.objects.get(id=self.object_id)
        object_abs_url = obj.get_absolute_url()
        link = object_abs_url + "#comment_%s" % (self.id)
        return link


class CommentAnswer(CommentBase):
    comment = models.ForeignKey(Comment, verbose_name="Комментарий",
                                related_name="answers")

    class Meta:
        verbose_name = "Ответ к комментарию"
        verbose_name_plural = "Ответы к комментариям"

    @property
    def direct_link(self):
        link = ""
        return link

    def get_absolute_url(self):
        object_model = self.comment.content_type.model_class()
        obj = object_model.objects.get(id=self.comment.object_id)
        object_abs_url = obj.get_absolute_url()
        link = object_abs_url + "#comment_%s" % (self.comment.id)
        return link


@receiver(models.signals.post_save, sender=Comment)
def log_comment_adding(sender, instance, created, **kwargs):
    from statistics.views import comment_added

    if created:
        comment_added(instance)


@receiver(models.signals.pre_save, sender=Comment)
def log_comment_changing(sender, instance, **kwargs):
    from statistics.views import comment_changed

    try:
        old_comment = Comment.objects.get(id=instance.id)
    except Comment.DoesNotExist:
        return
    new_comment = instance
    comment_changed(old_comment, new_comment)


