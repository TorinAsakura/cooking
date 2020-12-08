# -*- coding: utf-8 -*-
from django.db import models

class SubscriptionArchiv(models.Model):
	number = models.PositiveIntegerField("Номер рассылки")
	created = models.DateTimeField("Дата создания рассылки")
	date_send = models.DateTimeField("Дата отправки рассылки")
	subscription = models.TextField("Текст рассылки")

	def __unicode__(self):
		return unicode(self.number)

	class Meta:
		verbose_name = "Архив рассылок"
		verbose_name_plural = "Архивы рассылок"
