# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers

from notifications.models import Notice
from core.tasks import send_mail
from utils import ajax_required
from notifications.forms import NoticeForm
from competitions.models import Competition

def send_notice(title, message, to_user):
	notice = Notice.objects.create(title=title, body=message, to_user=to_user)
	try:
		if to_user.profile.settings.recipes_commented:
			send_mail.delay(title, message, 'support@povary.ru', [to_user.email, ])
	except Exception:
		pass
	return notice

@ajax_required
def ajax_send_question(request, competition_id):
    competition = get_object_or_404(Competition, id=competition_id)
    form = NoticeForm(request.POST)
    if form.is_valid():
        notice = form.save()
        competition.questions.add(notice)
        return HttpResponse(json.dumps(
            {"status": "success",
             "title": notice.title,
             "id": notice.id
            }))
    else:
        return HttpResponse(json.dumps({"status": "error",}))

@login_required
def profile_notices(request):
	notice_list = Notice.objects.filter(to_user=request.user).order_by('-is_new')
	newnotice_num = notice_list.filter(is_new=True).count()
	data = {
		"notice_list": notice_list,
		"newnotice_num": newnotice_num
	}
	return render(request, "messages/profile_notices.html", data)


@login_required
def notice_details(request, notice_id):
	notice = get_object_or_404(Notice, id=notice_id)
	if request.user != notice.to_user:
		return HttpResponseForbidden("Нет доступа к этому уведомлению")
	newnotice_num = Notice.objects.filter(to_user=request.user).filter(is_new=True).count()
	notice.is_new = False
	notice.save()
	data = {
		"notice": notice,
		"newnotice_num": newnotice_num,
	}
	return render(request, "messages/notice_details.html", data)
