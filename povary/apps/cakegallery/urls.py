# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


from cakegallery.forms import CakeImageForm

urlpatterns = patterns('cakegallery.views',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),

	# url(r'^$', 'article_list', name='article_list'),
	# url(r'^category/$', 'articlecategory_list', name='articlecategory_list'),
	# url(r'^category/(?P<articlecategory_slug>.*)/$', 'articlecategory_details', name='articlecategory_details'),
	url(r'^get_subcategories/(?P<cat_slug>.*)/$', 'get_subcategories', name='get_subcategories'),
	url(r'^gallery/(?P<gallery_slug>.*)/$', 'cakeimage_gallery', name='cakeimage_gallery'),
	url(r'^photo/add/(?P<gallery_slug>.*)/$', 'add_photo', name='cakeimage-add'),
	url(r'^photo/add/$', 'add_photo', name='cakeimage-add'),
	url(r'^search/$', 'cakeimage_gallery_filter_start', name='cakeimage_gallery_search'),
	url(r'^get_images/(?P<gallery_slug>.*)/(?P<afilter>.*)/(?P<page>.*)/$', 'cakeimage_filter', name='cakeimage_filter'),
	url(r'^search/filter/(?P<q>.*)/(?P<cat>.*)/(?P<afilter>.*)/(?P<page>.*)/$',
    	'cakeimage_gallery_filter', name='get_cake_gallery'
    ),
	url(r'^(?P<image_slug>.*)/$', 'cakeimage_details', name='cakeimage_details'),
)
