# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('tags.views',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),
	
	url(r'^search_tag/$', 'search_tag', name="search_tag"),
	url(r'^(?P<tag_slug>.*)/(?P<contenttype_id>.*)/$', 'tag_details', name='tag_details'),
)
