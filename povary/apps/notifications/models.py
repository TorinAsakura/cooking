# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Notice(models.Model):
    from_name = models.CharField(max_length=255, default="Администрация")
    to_user = models.ForeignKey(User, verbose_name="Получатель")
    title = models.CharField("Заголовок", max_length=255)
    body = models.TextField("Сообщение")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    is_new = models.BooleanField("Новое сообщение", default=True)
    is_question = models.BooleanField("Вопрос", default=False)


class Meta:
    verbose_name = "Уведомление"
    verbose_name_plural = "Уведомления"


def __unicode__(self):
    return self.title
