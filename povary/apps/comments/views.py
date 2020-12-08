# -*- coding: utf-8 -*-
import json
from django.conf import settings
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType

from utils import ajax_required, get_avatar
#from setman import settings as custom_settings

from comments.forms import CommentForm, CommentAnswerForm
from comments.models import Comment, CommentAnswer
from recipes.models import Recipe
from statistics.tasks import track_event
from notifications.views import send_notice
from pymorphy.django_conf import default_morph


@ajax_required
def add_comment(request, contenttype_id, obj_id, is_cake=False):
    form = CommentForm(request.POST, request.FILES)
    if request.method == "POST":
        is_detail_page = request.POST.get('is_detail_page', None)
        if form.is_valid():
            contenttype = ContentType.objects.get(id=contenttype_id)
            obj_model = contenttype.model_class()
            try:
                obj = obj_model.objects.get(id=obj_id)
            except obj_model.DoesNotExist:
                data = json.dumps({
                "status": "error",
                "message": "Object doesn't exist"
                })
                return HttpResponse(data, mimetype="application/json")
            comment = form.save(commit=False)
            if request.user.is_authenticated():
                comment.author = request.user
                username = comment.author.username
            else:
                username = "Anonymous"
                comment.is_anonymous = True
            comment.ip_addr = request.META.get("REMOTE_ADDR")
            avatar = get_avatar(request, '60x60')

            comment.of = obj

            if hasattr(obj, 'comments_num'):
                obj.comments_num += 1
                obj.save()

            comment.save()
            site = Site.objects.get_current()
            send_notice(
                title=u"Новый комментарий",
                message=u"""Ваш рецепт "%s" был прокомментирован "%s". http://%s%s """ %
                        (
                        obj.title,
                        comment.author.username if comment.author else u'Аноним',
                        site.domain, comment.get_absolute_url()
                        ),
                to_user=obj.author
            )
            tracking_data = {
            "object_id": comment.id,
            "model": Comment,
            "tracking_type": "comment"
            }
            track_event.delay(tracking_data)
            data = json.dumps({
            "status": "ok",
            "message": "Комментарий добавлен",
            "id": comment.id,
            "title": comment.title,
            "body": mark_safe(comment.body),
            "author_name": username,
            "author_avatar": avatar.url,
            })
        else:
            data = json.dumps({
            "status": "validation_error",
            "message": "Ошибка валидации"
            })
            return HttpResponse(data, mimetype="application/json")
        if is_cake:
            callback_template = "comments/cake_comment_details.html"
        else:
            callback_template = "comments/comment_details.html" if not \
                is_detail_page else 'comments/comment_details2.html'
        rendered_comment = render_to_string(callback_template,
                                            {
                                            "comment": comment,
                                            "commentanswer_form": CommentAnswerForm,
                                            "item_obj": obj,
                                            "comm_title": "Teeeest",
                                            },
                                            context_instance=RequestContext(
                                                request)
        )

        morph = default_morph
        contenttype = ContentType.objects.get(id=contenttype_id)
        comments = Comment.objects.filter(object_id=obj_id,
                                          content_type=contenttype)
        comm_num = 0
        for i in range(len(comments)):
            answers = CommentAnswer.objects.filter(comment=comments[i])
            comm_num += 1 + len(answers)
        comm_caption = morph.pluralize_inflected_ru(u'КОММЕНТАРИЙ', comm_num)
        data = json.dumps({
        "data": rendered_comment,
        "comm_caption": comm_caption,
        })
        return HttpResponse(data, mimetype="application/json")
    else:
        data = json.dumps({
        "status": "error",
        "message": "Only POST request"
        })
        return HttpResponse(data, mimetype="application/json")


@ajax_required
def add_commentanswer(request, contenttype_id, obj_id, comment_id,
                      is_cake=False):
    form = CommentAnswerForm(request.POST or None)
    answer = ''
    if request.method == "POST":
        if form.is_valid():
            contenttype = ContentType.objects.get(id=contenttype_id)
            obj_model = contenttype.model_class()
            try:
                obj = obj_model.objects.get(id=obj_id)
            except obj_model.DoesNotExist:
                data = json.dumps({
                "status": "error",
                "message": "Object doesn't exist"
                })
                return HttpResponse(data, mimetype="application/json")

            try:
                comment = Comment.objects.get(id=comment_id)
            except Comment.DoesNotExist:
                data = json.dumps({
                "status": "error",
                "message": "Comment doesn't exist"
                })
                return HttpResponse(data, mimetype="application/json")

            answer = form.save(commit=False)
            answer.ip_addr = request.META.get("REMOTE_ADDR")
            if request.user.is_authenticated():
                answer.author = request.user
                username = answer.author.username
            else:
                username = "Anonymous"
                answer.is_anonymous = True
            avatar = get_avatar(request, '60x60')

            answer.comment = comment
            answer.save()
            site = Site.objects.get_current()
            send_notice(
                title=u"Новый комментарий",
                message=u""" "%s" ответил на Ваш комментарий к рецепту "%s". http://%s%s """ % (
                answer.author.username if answer.author else u"Аноним",
                obj.title,
                site.domain, answer.get_absolute_url()
                ),
                to_user=obj.author
            )
            tracking_data = {
            "object_id": answer.id,
            "model": answer,
            "tracking_type": "answer"
            }
            track_event.delay(tracking_data)
            data = json.dumps({
            "status": "ok",
            "message": "Комментарий добавлен",
            "id": answer.id,
            "title": answer.title,
            "body": mark_safe(answer.body),
            "author_name": username,
            "author_avatar": avatar.url
            })
        else:
            data = json.dumps({
            "status": "validation_error",
            "message": "Ошибка валидации"
            })
        if is_cake:
            callback_template = "comments/cake_answer_details.html"
        else:
            callback_template = "comments/commentanswer_details.html"
        morph = default_morph
        contenttype = ContentType.objects.get(id=contenttype_id)
        comments = Comment.objects.filter(object_id=obj_id,
                                          content_type=contenttype)
        comm_num = 0
        for i in range(len(comments)):
            answers = CommentAnswer.objects.filter(comment=comments[i])
            comm_num += 1 + len(answers)
        comm_caption = morph.pluralize_inflected_ru(u'КОММЕНТАРИЙ', comm_num)
        rendered_answer = render_to_string(callback_template,
                                           {"answer": answer},
                                           context_instance=RequestContext(
                                               request)
        )
        data = json.dumps({
        "data": rendered_answer,
        "comm_caption": comm_caption,
        })
        return HttpResponse(data, mimetype="application/json")
    else:
        data = json.dumps({
        "status": "error",
        "message": "Only POST request"
        })
        return HttpResponse(data, mimetype="application/json")
