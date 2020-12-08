#!encoding: utf-8
from django.utils.translation import ugettext as _
from django.db import models


class Country(models.Model):
    """
    Information about country
    """
    title = models.CharField(_(u"Название"), max_length=255)

    class Meta:
        verbose_name = _(u"Страна")
        verbose_name_plural = _(u"Страны")

    def __unicode__(self):
        return self.title


class City(models.Model):
    """
    Information about city in specified country
    """
    title = models.CharField(_(u"Название"), max_length=255)
    country = models.ForeignKey("Country", verbose_name=_(u"Страна"))

    class Meta:
        verbose_name = _(u"Город")
        verbose_name_plural = _(u"Города")

    def __unicode__(self):
        return self.title
