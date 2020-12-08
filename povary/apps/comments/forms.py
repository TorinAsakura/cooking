# -*- coding: utf-8 -*-
from django import forms

from comments.models import Comment, CommentAnswer


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("title", "body", "image")

    class Media:
        js = (
        #'/static/tiny_mce/tiny_mce.js',
        #'/static/tiny_mce/articles_tinymce_config.js',
        )


class CommentAnswerForm(forms.ModelForm):
    class Meta:
        model = CommentAnswer
        fields = ("title", "body")

    class Media:
        js = (
        #'/static/tiny_mce/tiny_mce.js',
        #'/static/tiny_mce/articles_tinymce_config.js',
        )
