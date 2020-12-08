# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db.models import ImageField
import os

from django.db import models
from django.contrib.auth.models import User

from recipes.models import Recipe
from gallery.models import Gallery
from notifications.models import Notice


def comp_cat_upload(obj, filename):
    from utils import timestampbased_filename

    path = os.path.join(
        "competitions",
        "category",
        obj.slug,
        timestampbased_filename(filename)
    )
    return path


class CompetitionCategory(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("URL", unique=True)
    image = models.ImageField("Изображение", upload_to=comp_cat_upload)
    description = models.TextField("Описание")
    published = models.BooleanField("Опубликовано", default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Категория конкурсов"
        verbose_name_plural = "Категории конкурсов"


def comp_upload_path(instance, filename):
    from utils import timestampbased_filename
    path = os.path.join(
        'competitions',
        instance.slug,
        timestampbased_filename(filename)
    )
    return path


class Competition(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("URL", unique=True)
    description = models.TextField("Описание")
    terms = models.TextField("Условия конкурса")
    category = models.ForeignKey(CompetitionCategory,
                                 verbose_name="Категория конкурса",
                                 related_name='competitions'
    )
    author = models.ForeignKey(User, verbose_name="Автор",
                               related_name="competitions")
    start_date = models.DateTimeField("Дата начала")
    end_date = models.DateTimeField("Дата окончания")
    voting_start = models.DateTimeField("Начало голосования")
    voting_end = models.DateTimeField("Окончание голосования")
    voting_enabled = models.BooleanField("Голосование активно", default=False)
    visits_num = models.PositiveIntegerField("Кол. посещений", default=0,
                                             editable=False)
    published = models.BooleanField("Опубликовано", default=True)

    image = models.ImageField("Изображение", upload_to=comp_upload_path)

    questions = models.ManyToManyField(Notice, related_name='competition')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("competition_details", args=(self.slug, ))

    def inc_visits(self):
        self.visits_num += 1
        self.save()

    class Meta:
        verbose_name = "Конкурс"
        verbose_name_plural = "Конкурсы"


BIDDER = '0'
FIRST_PLACE = '1'
SECOND_PLACE = '2'
THIRD_PLACE = '3'
FOURTH_PLACE = '4'
FIFTH_PLACE = '5'

WINNER_PLACES = (
(BIDDER, "Участник"),
(FIRST_PLACE, "Первое место"),
(SECOND_PLACE, "Второе место"),
(THIRD_PLACE, "Третье место"),
(FOURTH_PLACE, "Четвертое место"),
(FIFTH_PLACE, "Пятое место")
)

WAITING = '0'
ACCEPTED = '1'
REJECTED = '2'
EDITED = '3'

REQUEST_STATUS = (
(WAITING, "Ожидает"),
(ACCEPTED, "Принято"),
(REJECTED, "Отклонено"),
(EDITED, "Редактируется")
)


def comp_req_upload(obj, filename):
    from utils import timestampbased_filename

    path = os.path.join(
        "competitions",
        "requests",
        timestampbased_filename(filename)
    )
    return path


class CompetitionRequest(models.Model):
    competition = models.ForeignKey(Competition, verbose_name="Конкурс",
                                    related_name="competition_requests")
    # recipe = models.ForeignKey(Recipe, verbose_name="Рецепт", related_name="competition_requests")
    title = models.CharField("Заголовок", max_length=255)
    image = models.ImageField("Изображение", upload_to=comp_req_upload)
    description = models.TextField("Описание", blank=True, null=True)
    body = models.TextField("Текст")
    image1 = models.ImageField("Изображение #1", upload_to=comp_req_upload,
                               blank=True, null=True)
    image2 = models.ImageField("Изображение #2", upload_to=comp_req_upload,
                               blank=True, null=True)
    image3 = models.ImageField("Изображение #3", upload_to=comp_req_upload,
                               blank=True, null=True)
    image4 = models.ImageField("Изображение #4", upload_to=comp_req_upload,
                               blank=True, null=True)
    image5 = models.ImageField("Изображение #5", upload_to=comp_req_upload,
                               blank=True, null=True)
    show_till_voting_start = models.BooleanField(default=False)
    show_my_name = models.BooleanField(default=True)
    author = models.ForeignKey(User, verbose_name="Пользователь", blank=True,
                               null=True)
    ip_addr = models.CharField("IP", max_length=255, blank=True, null=True)
    adding_date = models.DateTimeField("Дата добавления заявки",
                                       auto_now_add=True)
    status = models.CharField("Статус", max_length=255, choices=REQUEST_STATUS,
                              default=WAITING)
    place_number = models.CharField("Место победителя", max_length=255,
                                    choices=WINNER_PLACES, default=BIDDER
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Заявка на участие"
        verbose_name_plural = "Заявки на участие"


class CompetitionVote(models.Model):
    user = models.ForeignKey(User, verbose_name="Голосующий",
                             related_name="competition_votes")
    competition_request = models.ForeignKey(CompetitionRequest,
                                            verbose_name="Заявка",
                                            related_name="votes")
    date = models.DateTimeField("Время голосования")
    published = models.BooleanField("Считается", default=True)

    class Meta:
        verbose_name = "Голос за участие в конкурсе"
        verbose_name_plural = "Управление голосами"


class MainPageCompetition(models.Model):
    competition = models.ForeignKey(Competition, verbose_name="Конкурс",
                                    related_name="mainpage_competition")
    title = models.CharField("Заголовок", max_length=255, blank=True, null=True)
    gallery = models.ForeignKey(Gallery, verbose_name="Галлерея конкурса",
                                related_name="mainpage_competition")
    text = models.TextField("Тест")
    published = models.BooleanField("Опубликовано", default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Конкурс на главной"
        verbose_name_plural = "Конкурсы на главной"


class CompetitionTermStep(models.Model):
    step_num = models.PositiveIntegerField()
    description = models.TextField("Описание")
    competition = models.ForeignKey(Competition, related_name="term_steps")

    def __unicode__(self):
        return str(self.competition_id)

    class Meta:
        unique_together = ("competition", "step_num")
        ordering = ('step_num', )
        verbose_name = "Шаг условия принятия участия"
        verbose_name_plural = "Шаги условия принятия участия"


class CompetitionPrizes(models.Model):
    place = models.PositiveIntegerField()
    description = models.TextField("Описание")

    image = ImageField("Фото приза", upload_to="prizes", blank=True,
                       null=True)

    competition = models.ForeignKey(Competition, related_name="prizes")

    def __unicode__(self):
        return str(self.competition_id)

    class Meta:
        unique_together = ("competition", "place")
        ordering = ('place', )
        verbose_name = "Приз за занятое место"
        verbose_name_plural = "Призы за занятое место"


class CompetitionSponsors(models.Model):


    description = models.TextField("Описание")

    image = ImageField("Фото приза", upload_to="sponsors", blank=True,
                       null=True)

    competition = models.ForeignKey(Competition, related_name="sponsors")

    def __unicode__(self):
        return str(self.competition_id)

    class Meta:
        verbose_name = "Спонсор конкурса"
        verbose_name_plural = "Споносоры конкурса"