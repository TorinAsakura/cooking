# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'povary.views.home', name='home'),
                       # url(r'^povary/', include('povary.foo.urls')),

                       url(r'^add/(?P<contenttype_id>.*)/(?P<obj_id>.*)/$', 'comments.views.add_comment',
                           name='add_comment'),
                       url(r'^add/(?P<contenttype_id>.*)/(?P<obj_id>.*)/(?P<is_cake>.*)$', 'comments.views.add_comment',
                           name='add_comment'),
                       url(r'^add_answer/(?P<contenttype_id>.*)/(?P<obj_id>.*)/(?P<comment_id>.*)/$',
                           'comments.views.add_commentanswer', name='add_commentanswer'),
                       url(r'^add_answer/(?P<contenttype_id>.*)/(?P<obj_id>.*)/(?P<comment_id>.*)/(?P<is_cake>.*)$',
                           'comments.views.add_commentanswer', name='add_commentanswer'),
)
