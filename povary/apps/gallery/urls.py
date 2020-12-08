# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),

	url(r'^recipe_gallery/(?P<recipe_slug>.*)/$',
		'gallery.views.recipe_gallery_upload',
		name='recipe_gallery_upload'
	),
	# url(r'^$', 'recipes.views.recipe_list', name='recipe_list'),
	# url(r'^(?P<recipe_slug>.*)/$', 'recipes.views.recipe_details', name='recipe_details'),
)
