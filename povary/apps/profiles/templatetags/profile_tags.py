# -*- coding: utf-8 -*-
from django import template

from notifications.models import Notice


register = template.Library()


@register.filter
def get_twi_username(link):
	if link[-1] == '/':
		link = link[:-1]
	username = link.split('/')[-1]
	return username


@register.filter
def get_vk_username(link):
	if link[-1] == '/':
		link = link[:-1]
	username = link.split('/')[-1]
	return username


@register.filter
def get_fb_username(link):
	if link[-1] == '/':
		link = link[:-1]
	username = link.split('/')[-1]
	return username


@register.filter
def parse_books(book_list):
	books = book_list.split(',')
	return books


@register.simple_tag
def unviewed_notice_num(user):
	notice_num = Notice.objects.filter(to_user=user, is_new=True).count()
	return notice_num
