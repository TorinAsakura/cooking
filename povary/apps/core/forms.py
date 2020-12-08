#!coding:utf-8
from django.core.mail import mail_managers, mail_admins
from django.utils.translation import ugettext as _
from django import forms

class ContactForm(forms.Form):

    SUBJECTS = (
        (u'Выберите тему', u'Выберите тему'),
        (u'Проблема с размещеним рецепта/МК/фото', u'Проблема с размещеним рецепта/МК/фото'),
        (u'Заблокирована учетная запись', u'Заблокирована учетная запись'),
        (u'Размещение рекламы', u'Размещение рекламы'),
        (u'Другое', u'Другое'),
    )

    sub = forms.ChoiceField(choices=(SUBJECTS),widget=forms.Select, required=True)
    name = forms.CharField(label=_(u"Ваше имя"), widget=forms.TextInput)
    email = forms.EmailField(label=_(u"Ваш E-mail"), widget=forms.TextInput)
    text = forms.CharField(label=_(u"Ваше сообщение"), widget=forms.Textarea)

    def send_mail(self):
        context = {
            "sub": self.cleaned_data["sub"],
            "name": self.cleaned_data["name"],
            "email": self.cleaned_data["email"],
            "text": self.cleaned_data["text"]
        }

        EMAIL_CONTACT_SUBJECT = _(u"%(sub)s : [povary.ru]")
        EMAIL_CONTACT_BODY = _(u"Отправитель: %(name)s <%(email)s>\n\n\nСообщение:\n%(text)s")

        subject = EMAIL_CONTACT_SUBJECT % context
        body = EMAIL_CONTACT_BODY % context

        mail_admins(subject, body)
#        mail_managers(subject, body)
