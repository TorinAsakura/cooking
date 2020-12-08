# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),
	
	url(r'autocomplete/$', 'ingredients.views.ingredients_autocomplete', name='ingredients_autocomplete'),
)
