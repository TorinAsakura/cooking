# -*- coding: utf-8 -*-
from django import forms

from wiki.models import WikiPage, WikiDiscussion


class WikiPageForm(forms.ModelForm):
	reason = forms.CharField(widget=forms.Textarea, label="Описание изменений",
		required=False)
	class Meta:
		model = WikiPage
		fields = ('title', 'image', 'body', 'warnings', 'prooflinks',
			'category', 'subcategory', 'subsubcategory')


class WikiDiscussionForm(forms.ModelForm):
	class Meta:
		model = WikiDiscussion
		fields = ("text", )