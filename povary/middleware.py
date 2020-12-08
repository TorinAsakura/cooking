# -*- coding: utf-8 -*-
import time
import datetime

from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.conf import settings

from forum_integration.api import DB, forum_login, forum_logout


class LoginUserOnForum(object):
    def process_response(self, request, response):
        if response.status_code == 301:
            return response

        is_authenticated = request.user.is_authenticated()
        logged_on_forum = request.COOKIES.get('logged_on_forum', None)
        pass_hash = request.COOKIES.get('pass_hash', None)
        member_id = request.COOKIES.get('member_id', None)
        if request.path == reverse(
                'django.contrib.auth.views.login') and is_authenticated:
            response = forum_login(request, response)
        if request.path == reverse('django.contrib.auth.views.logout'):
            response = forum_logout(request, response)
        return response


class ActiveUserMiddleware:

    def process_request(self, request):
        current_user = request.user
        if request.user.is_authenticated():
            now = datetime.datetime.now()
            cache.set('seen_%s' % (current_user.username), now,
                           settings.USER_LASTSEEN_TIMEOUT)