# -*- coding: utf-8 -*-
from django.core.mail import send_mail as django_send_mail

from celery.task import task


@task
def send_mail(*args, **kwargs):
    django_send_mail(*args, **kwargs)


@task
def async_func(func, *args, **kwargs):
	func(*args, **kwargs)