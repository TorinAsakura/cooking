#!coding:utf-8
from django.conf import settings
import re
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class SeoTemplateManager(models.Manager):
    def for_object(self, object):
        object_type = ContentType.objects.get_for_model(object)
        return self.get(content_type=object_type, object_id=object.pk)

    def for_url(self, url):
        targets = SeoTarget.objects.filter(name__startswith="/")
        for target in targets:
            if re.match("^"+target.name, url):
                print "FOUND"
                return self.get(target=target)

        raise SeoTemplate.DoesNotExist()

    def for_target(self, name):
        return self.get(target__name=name)


class SeoTarget(models.Model):
    name         = models.CharField(_(u"Имя"), help_text=_(u"Имя или url страницы начинающийся на /"), max_length=128, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = _(u"SEO")
        verbose_name_plural = _(u"SEO")

    def __unicode__(self):
        return "URL: " + self.name if self.name[0] == "/" else self.name


class SeoTemplate(models.Model):
    target       = models.ForeignKey("SeoTarget", verbose_name=_(u"Цель"), null=True, blank=True)

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id    = models.PositiveIntegerField(null=True, blank=True)

    description  = models.TextField(null=True, blank=True)
    keywords     = models.TextField(null=True, blank=True)
    title        = models.TextField(null=True, blank=True)

    objects      = SeoTemplateManager()

    class Meta:
        verbose_name = _(u"SEO шаблон")
        verbose_name_plural = _(u"SEO шаблоны")
        unique_together = ("object_id", "content_type")

    def __unicode__(self):
        return unicode(self.target)


SEO_EXTRA_FIELDS = getattr(settings, "SEO_EXTRA_FIELDS", ())
for field, name in SEO_EXTRA_FIELDS:
    models.TextField(name, null=True, blank=True).contribute_to_class(SeoTemplate, field)
