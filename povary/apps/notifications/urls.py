# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),
	
	url(r'^notices/(?P<notice_id>.*)/$', 'notifications.views.notice_details', name='notice_details'),
	url(r'^notices/$', 'notifications.views.profile_notices', name='profile_notices'),
    url(r'^ajax_send_question/(?P<competition_id>.*)/$', 'notifications.views.ajax_send_question', name='ajax_send_question'),
	# url(r'^$', 'recipes.views.recipe_list', name='recipe_list'),
	# url(r'^(?P<recipe_slug>.*)/$', 'recipes.views.recipe_details', name='recipe_details'),
)
