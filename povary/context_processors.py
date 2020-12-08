# -*- coding: utf-8 -*-
from categories.models import Category
from comments.forms import CommentForm, CommentAnswerForm


def default_avatar(request):
    # FIXME
    #from setman import settings as custom_settings

    return {"anonymous_avatar": 'http://collegeinn.com/images/recipes/recipe-default.jpg'}


def category_list(request):
    category_list = Category.objects.filter(published=True)
    return {"category_list": category_list}


def comment_form(request):
    return {"comment_form": CommentForm,
            "commentanswer_form": CommentAnswerForm
    }
