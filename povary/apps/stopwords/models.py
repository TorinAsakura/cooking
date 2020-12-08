# -*- coding: utf-8 -*-
from django.db import models


class StopWord(models.Model):
	stopword = models.CharField("Стоп слово", max_length=255)
	replaceword = models.CharField("Заменить на", max_length=255)
	active = models.BooleanField("Активно", default=True)

	def __unicode__(self):
		return self.stopword

	class Meta:
		verbose_name = "Стоп слово"
		verbose_name_plural = "Стоп слова"
