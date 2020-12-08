# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from master_class.views import CakeMCWizard
from master_class.forms import CakeMCFormStep1, CakeMCFormStep2, CakeMCFormStep3


urlpatterns = patterns('master_class.views',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),

 	# url(r'^$', 'article_list', name='article_list'),
	# url(r'^category/$', 'articlecategory_list', name='articlecategory_list'),
	url(r'^get_mcsubcategories/(?P<cat_slug>.*)/$', 'get_mcsubcategories', name='get_mcsubcategories'),
	url(r'^validate/$', CakeMCWizard.as_view([CakeMCFormStep1, CakeMCFormStep2, CakeMCFormStep3]), name='validate_form'),
	url(r'^subcategory/(?P<mc_subcategory_slug>.*)/$', 'mc_subcategory_details', name='mc_subcategory_details'),
	url(r'^category/(?P<mc_category_slug>.*)/$', 'mc_category_details', name='mc_category_details'),
	url(r'^add/$', 'cake_mc_add', name="cake_mc-add"),
	url(r'^cake_mc/(?P<mc_slug>.*)/$', 'cake_mc_details', name='cake_mc_details'),

	url(r'^search/$', 'mc_filter_start', name='cake_mc_filter'),
    url(r'^search/filter/(?P<q>.*)/(?P<cat>.*)/(?P<ing>.*)/(?P<afilter>.*)/(?P<page>.*)/$',
    	'mc_filter', name='get_cake_mc'
    ),
	url(r'^(?P<mc_slug>.*)/$', 'masterclass_details', name='masterclass_details'),

)
