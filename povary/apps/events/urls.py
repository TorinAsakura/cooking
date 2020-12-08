# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('events.views',
    # cakes
    url(r'^add_cake_event/$', 'add_cake_event', name='add_cake_event'),
    url(r'^cake_events/$', 'cake_event_list', name='cake_event_list'),
    url(r'^(?P<event_slug>.*)/$', 'cake_event_details', name='cake_event_details'),



    # povary
    url(r'^$', 'event_list', name='event_list'),
    url(r'^country_autocomplete/$', 'country_autocomplete', name='country_autocomplete'),
    url(r'^city_autocomplete/$', 'city_autocomplete', name='city_autocomplete'),
    url(r'^check_country_existence/$', 'check_country_existence', name='check_country_existence'),
    url(r'^category/$', 'eventcategory_list', name='eventcategory_list'),
    url(r'^category/(?P<eventcategory_slug>.*)/$', 'eventcategory_details', name='eventcategory_details'),
    url(r'^(?P<event_slug>.*)/$', 'event_details', name='event_details'),

)
