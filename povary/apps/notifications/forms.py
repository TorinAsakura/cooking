from django import forms
from notifications.models import Notice


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ("from_name", "to_user", "title", "body", "is_question")