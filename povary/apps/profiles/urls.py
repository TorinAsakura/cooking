# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

from registration.views import RegistrationView

from profiles.views import RegisterView
from profiles.forms import RegisterForm, ChangePasswordForm


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),
    url(r'^profile/upload_avatar/$', 'profiles.views.upload_avatar', name='upload_avatar'),
    url(r'^profile/recipebox_manage/$', 'profiles.views.recipebox_manage', name='recipebox_manage'),
    url(r'^profile/remove_recipe_from_box/(?P<recipe_slug>.*)/(?P<recipebox_id>.*)$',
        'profiles.views.remove_recipe_from_box',
        name='remove_recipe_from_box'
    ),
    url(r'^profile/recipebox_remove/(?P<recipebox_id>.*)/$',
        'profiles.views.recipebox_remove',
        name='recipebox_remove'
    ),
    url(r'^profile/recipebox_details/(?P<recipebox_id>.*)/$',
        'profiles.views.recipebox_details',
        name='recipebox_details'
    ),
    url(r'^profile/recipebox_edit/(?P<recipebox_id>.*)/$',
        'profiles.views.recipebox_edit',
        name='recipebox_edit'
    ),
	url(r'^profile/$', 'profiles.views.profile', name='profile'),
    url(r'^password_change_done/$', 'profiles.views.password_change_done', name='pass_change_done'),
    url(r'^password_change/$',
        'django.contrib.auth.views.password_change',
        {
            "post_change_redirect": "/accounts/password_change_done",
            "template_name": "profiles/change_password.html",
            "password_change_form": ChangePasswordForm,
        },
        name='povary_password_change',
    ),
    url(r'^crop_avatar/$', 'profiles.views.crop_avatar', name='crop_avatar'),
    url(r'^change_avatar/$', 'profiles.views.change_avatar', name='change_avatar'),
    url(r'^check_user_existence/$', 'profiles.views.check_user_existence',
        name='check_user_existence'
    ),
    url(r'^profile_settings/$', 'profiles.views.profile_settings', name='profile_settings'),
    url(r'^register/$', RegisterView.as_view(), name='registration_register'),

    url(r'', include('registration.backends.simple.urls')),
    url(r'^$', 'profiles.views.list', name='profile_list'),
    url(r'^user/(?P<username>.*)/$', 'profiles.views.public_userpage', name='public_userpage'),
)
