# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from recipes.views import RecipeWizard
from recipes.forms import RecipeFormStep1, RecipeFormStep2, RecipeFormStep3


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),
	url(r'^(?P<category_slug>.*)/(?P<subcategory_slug>.*)/$',
		'categories.views.subcategory_details',
		name='subcategory_details'
	),
	
	url(r'^(?P<category_slug>.*)/$',
		'categories.views.category_details',
		name='category_details'
	),
)
