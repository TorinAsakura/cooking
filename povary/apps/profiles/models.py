# -*- coding: utf-8 -*-
import time
import datetime
import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.cache import cache

from sorl.thumbnail import ImageField
from uuslug import uuslug as slugify
#from cities_light.models import Country, City
from regions.models import Country, City

from filebrowser.fields import FileBrowseField
from gallery.models import Gallery


SEX = (
    ('male', 'мужской'),
    ('female', 'женский'),
)


class AwardCategory(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Категория наград"
        verbose_name_plural = u"Категории наград"


class Award(models.Model):
    title = models.CharField(u"Заголовок", max_length=255)
    description = models.TextField("Описание", blank=True, null=True)
    icon = models.ImageField("Иконка", upload_to="award_icons")
    category = models.ForeignKey(AwardCategory)
    is_active = models.BooleanField("Активная", default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Награда"
        verbose_name_plural = u"Награды"


class AssignedAward(models.Model):
    award = models.ForeignKey(Award, verbose_name="Награда", related_name="assigned_awards")
    user = models.ForeignKey(User, verbose_name="Пользователь", related_name="awards")
    description = models.TextField("Комментарий", blank=True, null=True)
    is_active = models.BooleanField("Активная", default=True)
    created = models.DateTimeField("Создано", auto_now_add=True)
    updated = models.DateTimeField("Обновленно", auto_now=True)

    def __unicode__(self):
        return self.award.__unicode__()

    class Meta:
        verbose_name = u"Назначенная награда"
        verbose_name_plural = u"Назначенные награды"


def get_upload_path(instance, filename):
    from utils import timestampbased_filename
    path = os.path.join(
        "profiles",
        "avatars",
        slugify(instance.user.username),
        timestampbased_filename(filename)
    )
    return path


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Системный пользователь")
    avatar = ImageField("Аватар", upload_to=get_upload_path, blank=True, null=True)
    original_avatar = ImageField("Оригинал аватара", upload_to=get_upload_path,
        blank=True, null=True
    )
    rating = models.PositiveIntegerField("Рейтинг", default=0)
    twitter_link = models.URLField("Twitter", blank=True, null=True)
    fb_link = models.URLField("Facebook", blank=True, null=True)
    vk_link = models.URLField("ВКонтакте", blank=True, null=True)
    status = models.CharField("Статус/девиз", max_length=255, blank=True, null=True)
    about = models.TextField("О себе", blank=True, null=True )
    cookery_in_life = models.TextField("Кулинария в моей жизни", blank=True, null=True)
    cook = models.BooleanField("Кулинар", default=False)
    cake_master = models.BooleanField("Тортодел", default=False)
    books = models.TextField("Мои любимые книги",
        help_text="Введите названия книг разделяя их запятыми",
        blank=True, null=True
    )
    birthday = models.DateField(u"День рожденья", blank=True, null=True)
    # country = models.CharField(u"Страна", blank=True, null=True, max_length=255)
    # city = models.CharField(u"Город", blank=True, null=True, max_length=255)
    country = models.ForeignKey(Country, verbose_name="Страна", blank=True, null=True)
    city = models.ForeignKey(City, verbose_name="Город", blank=True, null=True)

    sex = models.CharField(u"Пол", choices=SEX, null=True, max_length=6, default='male')

    added_recipes_num = models.PositiveIntegerField(u"Сколько добавил рецептов", default=0)
    gallery = models.OneToOneField(Gallery, blank=True, null=True, verbose_name=u"Галерея")
    # awards = models.ManyToManyField(Award, verbose_name=u"Награды", blank=True, null=True)
    registration_ip = models.CharField(u"IP при регистрации", blank=True, null=True, max_length=255)
    last_login_ip = models.CharField(u"IP последнего входа", blank=True, null=True, max_length=255)
    visits_num = models.PositiveIntegerField("Кол. посещений", default=0, editable=False)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __unicode__(self):
        return self.user.username

    def inc_visits(self):
        self.visits_num += 1
        self.save()

    def get_cake_recipes(self):
        from recipes.models import Recipe
        return Recipe.objects.filter(published=True, author=self.user, is_cake=True)

    def get_cake_recipes_num(self):
        return len(self.get_cake_recipes())

    def get_cake_mcs(self):
        from master_class.models import MasterClass
        return MasterClass.objects.filter(published=True, author=self.user, is_cake=True)

    def get_cake_mcs_num(self):
        return len(self.get_cake_mcs())

    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

ACCESS_CHOICES = (
    ('all', 'Все кулинары'),
    ('none', 'Никто')
)


class ProfileSettings(models.Model):
    profile = models.OneToOneField(Profile, verbose_name="Профиль", null=True, related_name='settings')
    admin_subsctiption = models.BooleanField("Рассылка от администрации", default=True)
    recipes_commented = models.BooleanField("Уведомления о комментариях к своим рецептам", default=True)
    profile_commented = models.BooleanField("Уведомления о новых сообщениях на стене", default=True)
    comment_answer_commented = models.BooleanField("Уведомления об ответах на ваши комментарии на сайте", default=True)
    recipebook_access = models.CharField(
        "Кто может просматривать мою кулинарную книгу",
        choices=ACCESS_CHOICES,
        max_length=255, default='none'
    )
    profile_access = models.CharField(
        "Кто может просматривать мою стену",
        choices=ACCESS_CHOICES,
        max_length=255, default='none'
    )

    class Meta:
        verbose_name = verbose_name_plural = "Настройки профиля"

    def __unicode__(self):
        return str(self.profile)


@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    try:
        Profile.objects.get(user=instance)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_settings_for_profile(sender, instance, created, **kwargs):
    try:
        ProfileSettings.objects.get(profile=instance)
    except ProfileSettings.DoesNotExist:
        profile_settings = ProfileSettings.objects.create(profile=instance)
