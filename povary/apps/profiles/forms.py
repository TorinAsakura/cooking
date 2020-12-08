# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationForm
from regions.models import City, Country

from profiles.models import Profile, ProfileSettings
from profiles.widgets import AvatarWidget
from events.widgets import CountryWidget, CityWidget


class ProfileFormAdmin(forms.ModelForm):
	country = forms.CharField(widget=CountryWidget, label='Страна')
	city = forms.CharField(widget=CityWidget, label='Город')

	def clean_country(self):
		country = self.cleaned_data['country']
		if not country:
			raise forms.ValidationError("Обязательное поле")
		return Country.objects.get(id=country)

	def clean_city(self):
		city = self.cleaned_data['city']
		country = self.cleaned_data['country']
		if not city:
			raise forms.ValidationError("Обязательное поле")
		if not country:
			raise forms.ValidationError("Сначала заполните страну")
		return City.objects.get(id=city, country=country)


class ProfileForm(forms.ModelForm):
	user = forms.ModelChoiceField(
		queryset=User.objects.all(),
		widget=forms.HiddenInput()
	)
	status = forms.CharField(widget=forms.TextInput({"size": 50}),
		label=u"Статус", max_length=255, required=False
	)

	class Meta:
		model = Profile
		exclude = ('rating', 'cook', 'cake_master', 'registration_ip',
			'last_login_ip', 'gallery', 'awards', 'added_recipes_num',
			'avatar', 'original_avatar',
		)


class RegisterForm(RegistrationForm):
	password2 = forms.CharField(
		widget=forms.HiddenInput(),
		label=_("Password (again)"),
		required=False
	)
	sex = forms.CharField(
		label=_("Sex"),
		required=False
	)

	def clean_password1(self):
		password = self.cleaned_data.get('password1')
		if not password.strip() or len(password) < 3:
			raise forms.ValidationError("Пароль не может быть меньше 3х символов и не должен состоять из пробелов")
		return password

	def clean(self):
		email = self.cleaned_data.get('email')
		try:
			if User.objects.filter(email=email):
				raise forms.ValidationError("Пользователь с таким email уже зарегестрирован.")
		except User.DoesNotExist:
			pass
		if self.cleaned_data.get('sex'):
			raise forms.ValidationError(_("ValidationError"))

		username = self.cleaned_data.get('username', '')
		password = self.cleaned_data.get('password1', '')

		if username.lower() == password.lower():
			raise forms.ValidationError("Нельзя использовать имя пользователя в качестве пароля")
		return self.cleaned_data


class ProfileSettingsForm(forms.ModelForm):
	class Meta:
		model = ProfileSettings
		exclude = ('profile', )


class AvatarForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('avatar', 'original_avatar')


class ChangePasswordForm(PasswordChangeForm):
	def clean_new_password1(self):
		password = self.cleaned_data.get('new_password1')
		if not password.strip() or len(password) < 3:
			raise forms.ValidationError("Пароль не может быть меньше 3х символов и не должен состоять из пробелов")
		return password

	def clean_new_password2(self):
		password = self.cleaned_data.get('new_password2')
		if not password.strip() or len(password) < 3:
			raise forms.ValidationError("Пароль не может быть меньше 3х символов и не должен состоять из пробелов")
		return password

	def clean(self):
		data = super(ChangePasswordForm, self).clean()
		password = data.get('new_password1', '')

		if self.user.username.lower() == password.lower():
			raise forms.ValidationError("Нельзя использовать имя пользователя в качестве пароля")
		return self.cleaned_data
