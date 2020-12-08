# -*- coding: utf-8 -*-
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.conf import settings

from registration.backends.default import DefaultBackend

from forum_integration.api import register_forum_user
from core.tasks import send_mail, async_func
from gallery.models import Gallery


class RegistrationBackend(DefaultBackend):
    def __init__(self):
        from registration.models import RegistrationProfile
        super(RegistrationBackend, self).__init__()
        def async_email_send(self, site):
            ctx_dict = {'activation_key': self.activation_key,
            'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
            'site': site}
            subject = render_to_string('registration/activation_email_subject.txt',
                                       ctx_dict)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            ctx_dict['user'] = self.user
            message = render_to_string('registration/activation_email.txt',
                                       ctx_dict)
            send_mail.delay(subject, message, settings.DEFAULT_FROM_EMAIL, (self.user.email, ))
        RegistrationProfile.send_activation_email = async_email_send

    def get_user(self, user_id):
        user = User.objects.get(id=user_id)
        return user

    def register(self, request, **kwargs):
        user = super(RegistrationBackend, self).register(request, **kwargs)
        user.is_active = True
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()
        user_password = request.POST['password1']
        user_ip_addr = request.META['REMOTE_ADDR']
        # register_forum_user(user.username, user_password, user_ip_addr)
        async_func.delay(register_forum_user, user.username, user_password, user_ip_addr)
        login(request, user)
        gallery_title = user.username+'_gallery'
        gallery, created = Gallery.objects.get_or_create(title=gallery_title)
        user.profile.gallery = gallery
        user.profile.save()
        return user
