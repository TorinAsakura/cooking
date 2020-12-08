# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('wiki.views',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),
    # url(r'^$', 'article_list', name='article_list'),
	# url(r'^category/$', 'articlecategory_list', name='articlecategory_list'),
	# url(r'^category/(?P<articlecategory_slug>.*)/$', 'articlecategory_details', name='articlecategory_details'),
	url(r'^ajax_commentversion/(?P<version_id>.*)/$', 'ajax_commentversion', name='ajaxcomment_wikiversion'),
	url(r'^version_discussion/(?P<version_id>.*)/$', 'version_discussion', name='version_discussion'),
	url(r'^comment_version/(?P<version_id>.*)/$', 'comment_version', name='comment_wikiversion'),
	url(r'^versions_compare/(?P<wikipage_slug>.*)/$', 'versions_compare', name='versions_compare'),
	url(r'^rm_compare/(?P<wikipage_slug>.*)/$', 'rm_compare', name='rm_compare'),
	url(r'^add2cmp/(?P<wikipage_slug>.*)/$', 'add2compare', name='add2compare'),
	url(r'^edit/(?P<wikipage_slug>.*)/$', 'wikipage_edit', name='wikipage_edit'),
	url(r'^history/(?P<wikipage_slug>.*)/$', 'wikipage_history', name='wikipage_history'),
	url(r'^markdown_preview/', 'markdown_preview', name='markdown_preview'),
	url(r'^(?P<wikipage_slug>.*)/$', 'wikipage_details', name='wikipage_details'),

)