# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('pages.views',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),
    # url(r'^$', 'article_list', name='article_list'),
	# url(r'^category/$', 'articlecategory_list', name='articlecategory_list'),
	# url(r'^category/(?P<articlecategory_slug>.*)/$', 'articlecategory_details', name='articlecategory_details'),
	url(r'^(?P<page_slug>.*)/$', 'page_details', name='page_details'),
)