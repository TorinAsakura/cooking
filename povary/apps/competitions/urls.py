# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from competitions.views import CompetitionDetailView, CompetitionRequestCreate


urlpatterns = patterns('',
	url(r'^$', 'competitions.views.competition_list', name='competition_list'),
    url(r'^competition_request/add/$', CompetitionRequestCreate.as_view(), name='competition_request_add'),
    url(r'^(?P<slug>.*)/$', CompetitionDetailView.as_view(), name='competition_details'),
)
