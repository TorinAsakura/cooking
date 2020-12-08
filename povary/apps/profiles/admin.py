# -*- coding: utf-8 -*-
from django.contrib import admin

from sorl.thumbnail import get_thumbnail

from recipes.models import Recipe
from profiles.models import Profile, Award, ProfileSettings, AwardCategory, AssignedAward
from profiles.forms import ProfileFormAdmin

ADMIN_THUMBS_SIZE = '60x60'


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'user_email', 'rating', 'cake_master', 'cook', 'image_thumb', 'sex',
		'date_joined', 'last_login', 'country', 'city', 'recipe_num', "visits_num")
	#form = ProfileFormAdmin
	
	def user_email(self, obj):
		return obj.user.email
	user_email.short_description = 'EMail'

	def image_thumb(self, obj):
		if obj.avatar:
			thumb = get_thumbnail(obj.avatar, ADMIN_THUMBS_SIZE)
			return u'<img width="%s" src="%s" />' % (thumb.width, thumb.url)
		else:
			return u"Пусто" 
	image_thumb.short_description = u'Аватар'
	image_thumb.allow_tags = True

	def date_joined(self, obj):
		return obj.user.date_joined
	date_joined.short_description = "Дата регистрации"

	def last_login(self, obj):
		return obj.user.last_login
	last_login.short_description = "Последний вход"

	def recipe_num(self, obj):
		recipes = Recipe.objects.filter(author=obj.user)
		return recipes.count()
	recipe_num.short_description = "Количество рецептов"


class AwardAdmin(admin.ModelAdmin):
	pass


class ProfileSettingsAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'profile', 'admin_subsctiption', 'recipes_commented',
		'profile_commented', 'comment_answer_commented', 'recipebook_access',
		'profile_access'
	)
	

class AwardCategoryAdmin(admin.ModelAdmin):
	pass


class AssignedAwardAdmin(admin.ModelAdmin):
	list_display = ("__unicode__", "user", "is_active", "created", "updated")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(ProfileSettings, ProfileSettingsAdmin)
admin.site.register(AwardCategory, AwardCategoryAdmin)
admin.site.register(AssignedAward, AssignedAwardAdmin)
