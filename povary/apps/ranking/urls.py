# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('ranking.views',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),

    url(r'^add/(?P<contenttype_id>.*)/(?P<obj_id>.*)/$', 'add_vote', name='add_vote'),
)
