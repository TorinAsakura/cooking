from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from seo_v2.models import *
from seo_v2.importpath import importpath


class SeoObjectTemplateInline(generic.GenericStackedInline):
    model = SeoTemplate
    extra = 1
    max_num = 1
    exclude = ("target",)


class SeoTargetTemplateInline(admin.StackedInline):
    model = SeoTemplate
    extra = 1
    max_num = 1
    exclude = ("content_type", "object_id")


class SeoTargetAdmin(admin.ModelAdmin):
    inlines = (SeoTargetTemplateInline,)


class SeoTemplateAdmin(admin.ModelAdmin):
    exclude = ("content_type", "object_id", "target")


admin.site.register(SeoTarget, SeoTargetAdmin)
admin.site.register(SeoTemplate, SeoTemplateAdmin)

if hasattr(settings, 'SEO_FOR_MODELS'):
    for model_name in settings.SEO_FOR_MODELS:
        model = importpath(model_name, 'SEO_FOR_MODELS')
        try:
            model_admin = admin.site._registry[model].__class__
        except KeyError:
            raise ImproperlyConfigured('Please set ``seo`` in your settings.py only as last INSTALLED_APPS')

        admin.site.unregister(model)

        setattr(model_admin, 'inlines', getattr(model_admin, 'inlines', []))
        if not SeoObjectTemplateInline in model_admin.inlines:
            model_admin.inlines = list(model_admin.inlines)[:] + [SeoObjectTemplateInline]

        admin.site.register(model, model_admin)
