# -*- coding: utf-8 -*-
import datetime
import os

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator

from sorl.thumbnail import ImageField
from uuslug import uuslug as slugify
from profiles.models import Profile
from gallery.models import Gallery
from recipes.tasks import publish_recipe
from ingredients.models import USAIngredient
from categories.models import Category, SubCategory
from ranking.models import Vote

from django.db.models import Count
from comments.models import Comment, CommentAnswer


MGRAMM = "mgramm"
GRAMM = "gramm"
MKGRAMM = "mkgramm"
MEASURE_CHOICES = (
(GRAMM, "г"),
(MGRAMM, "мг"),
(MKGRAMM, "мкг")
)

NUM = "num"
LOBE = "lobe"
BUNDLE = "bundle"
TEASPOON = "teaspoon"
TABLESPOON = "tablespoon"
COFEESPOON = "cofeespoon"
KG = "kg"
ML = "ml"
LITER = "liter"
GLASS = "glass"
HANDFUL = "handful"

INGREDIENT_MEASURE_CHOICES = (
(NUM, "штук"),
(LOBE, "долька"),
(BUNDLE, "пучок"),
(TEASPOON, "чайная ложка"),
(TABLESPOON, "столовая ложка"),
(COFEESPOON, "кофейная ложка"),
(GRAMM, "грамм"),
(MGRAMM, "мграмм"),
(KG, "кг"),
(ML, "мл"),
(LITER, "л"),
(GLASS, "стакан"),
(HANDFUL, "горсть"),
)


class Cuisine(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField("Описание", blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Кухня"
        verbose_name_plural = "Национальность кухни"


class Holiday(models.Model):
    title = models.CharField("Название праздника", max_length=255,
                             blank=True, null=True)
    icon = ImageField("Иконка праздника", upload_to="holiday_icons")
    start_date = models.DateField("Дата начала праздника", blank=True,
                                  null=True)
    end_date = models.DateField("Дата окончания праздника", blank=True,
                                null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Праздник"
        verbose_name_plural = "Праздники"


class PrepMethod(models.Model):
    title = models.CharField("Способ приготовления", max_length=255)
    icon = ImageField("Иконка", upload_to="recipes/prepmethod_icons/",
                      blank=True, null=True
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Способ приготовления"
        verbose_name_plural = "Способы приготовления"


class Season(models.Model):
    title = models.CharField("Заголовок", max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Сезон"
        verbose_name_plural = "Сезоны"


BREAKFAST = "breakfast"
LUNCH = "lunch"
DINNER = "dinner"
EATING_TIME_CHOICES = (
(BREAKFAST, "Завтрак"),
(LUNCH, "Обед"),
(DINNER, "Ужин")
)

SOFT = "soft"
MEDIUM = "medium"
HARD = "hard"
COMPLEXITY_CHOICES = (
(SOFT, "Просто"),
(MEDIUM, "Нормально"),
(HARD, "Сложно")
)

SOUR = "sour"
ACUTE = "acute"
SWEET = "sweet"
TASTE_CHOICES = (
(SOUR, "Кислое"),
(ACUTE, "Острое"),
(SWEET, "Сладкое")
)

CHILD = "child"
TEEN = "teen"
ADULT = "adult"
AGE_CHOICES = (
(CHILD, "Детское"),
(TEEN, "Подростковое"),
(ADULT, "Взрослое")
)

VEGETERIAN = 'vegeterian'
LEAN = 'lean'
MEAT = 'meat'
VEGETABLE = 'vegetable'
DIET_CHOICES = (
(VEGETERIAN, 'Вегитарианское'),
(LEAN, 'Постное'),
(MEAT, 'Мясное'),
(VEGETABLE, 'Овощное')
)

BRAZIER = "brazier"
PREP_METHOD_CHOICES = (
(BRAZIER, "Мангал"),
)


def recipe_uploadto(instance, filename):
    from utils import timestampbased_filename

    path = os.path.join(
        'recipes',
        instance.slug,
        "user_%s" % instance.author.id,
        timestampbased_filename(filename)
    )
    return path


class Recipe(models.Model):
    title = models.CharField("Название", max_length=100)
    completed = models.BooleanField(default=True)
    slug = models.SlugField("URL рецепта", unique=True)
    main_image = ImageField("Главное фото", upload_to=recipe_uploadto,
                            blank=True, null=True
    )
    image_alt = models.CharField("ALT изображения", max_length=255, blank=True,
                                 null=True)
    image_title = models.CharField("TITLE изображения", max_length=255,
                                   blank=True, null=True)
    add_watermark = models.BooleanField("Добавлять водяной знак?",
                                        default=False)
    description = models.TextField("Краткое описание")
    body = models.TextField("Описание", blank=True, null=True)
    images = models.OneToOneField(Gallery, verbose_name="Фото галерея",
                                  blank=True, null=True)
    is_photorecipe = models.BooleanField("Фоторецепт", default=False)

    cuisine = models.ManyToManyField(Cuisine, related_name='recipes',
                                         blank=True, null=True,
                                         verbose_name="Национальность блюда",)

    complexity = models.CharField("Сложность", max_length=255,
                                  choices=COMPLEXITY_CHOICES, blank=True,
                                  null=True)
    eating_time = models.CharField("Время употребления", max_length=255,
                                   choices=EATING_TIME_CHOICES,
                                   blank=True, null=True)
    taste = models.CharField("Вкус", max_length=255, choices=TASTE_CHOICES,
                             blank=True, null=True)
    age_limit = models.CharField("Возраст", max_length=255, choices=AGE_CHOICES,
                                 blank=True, null=True)
    diet = models.CharField("Диета", max_length=255, choices=DIET_CHOICES,
                            blank=True, null=True)
    holiday = models.ForeignKey(Holiday, verbose_name="Блюдо к празднику",
                                blank=True, null=True)
    prepare_time_from = models.PositiveIntegerField("Время приготовления (от)",
                                                    blank=True, null=True,
                                                    validators=[
                                                        MinValueValidator(1)])
    prepare_time_to = models.PositiveIntegerField("Время приготовления (до)",
                                                  blank=True, null=True)
    preparation_method = models.ForeignKey(PrepMethod,
                                           verbose_name="Способ приготовления",
                                           blank=True, null=True,
                                           related_name="recipes")
    caloric_value = models.PositiveIntegerField("Каллорий на блюдо", blank=True,
                                                null=True)
    portion_num = models.PositiveIntegerField("Количество порций", blank=True,
                                              null=True,
                                              validators=[MinValueValidator(1)])
    season = models.ForeignKey(Season, verbose_name="Сезон", blank=True,
                               null=True)
    category = models.ManyToManyField(Category, verbose_name="Категории")
    sub_category = models.ManyToManyField(SubCategory,
                                          verbose_name="Подкатегории")
    author = models.ForeignKey(User, verbose_name="Автор рецепта")
    published = models.BooleanField("Опубликовано", default=False)
    created = models.DateTimeField("Время добавления", auto_now_add=True)
    pub_date = models.DateField("Время публикации",
                                default=datetime.datetime.now())
    updated = models.DateTimeField("Время последнего изменения", auto_now=True)
    visits_num = models.PositiveIntegerField("Кол. посещений", default=0,
                                             editable=False)
    on_main = models.BooleanField("Разместить на главной", default=False)
    is_cake = models.BooleanField("Випечка?", default=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_from = self.title[:30]
            self.slug = slugify(slug_from, instance=self)
        super(Recipe, self).save(*args, **kwargs)

    @property
    def step_descriptions(self):
        descriptions = '\n'.join(
            [i.description for i in self.steps.all()]
        )
        return descriptions

    @property
    def gallery(self):
        gallery_title = "%s_gallery" % (self.slug)
        gallery, created = Gallery.objects.get_or_create(title=gallery_title)
        return gallery

    @property
    def cover_image(self):
        from setman import settings as custom_settings

        if self.main_image:
            return self.main_image
        else:
            return custom_settings.RECIPE_DEFAULT_IMAGE

    @property
    def get_food_energy(self):
        sum = 0
        for ingredient in self.ingredients.all():
            sum += ingredient.ingredient_info.energy if \
                ingredient.ingredient_info.energy else 0
        return sum, sum * 4.1868

    @property
    def get_food_elements(self):
        protein, lipid_total, carbohydrt, cholestrl = 0, 0, 0, 0

        for ingredient in self.ingredients.all():
            protein += ingredient.ingredient_info.protein if \
                ingredient.ingredient_info.protein else 0
            lipid_total += ingredient.ingredient_info.lipid_total if \
                ingredient.ingredient_info.lipid_total else 0
            carbohydrt += ingredient.ingredient_info.carbohydrt if \
                ingredient.ingredient_info.carbohydrt else 0
            cholestrl += ingredient.ingredient_info.cholestrl if \
                ingredient.ingredient_info.cholestrl else 0

        return {
            'protein': protein,
            'lipid_total': lipid_total,
            'carbohydrt': carbohydrt,
            'cholestrl': cholestrl
        }

    def get_absolute_url(self):
        return reverse("recipe_details", args=(self.slug, ))

    def inc_visits(self):
        self.visits_num += 1
        self.save()

    def get_contenttype_id(self):
        return ContentType.objects.get_for_model(Recipe).id

    def get_votes(self):
        content_type = ContentType.objects.get_for_model(Recipe)
        return Vote.objects.filter(content_type=content_type, object_id=self.id)

    @property
    def num_votes(self):
        return len(self.get_votes())

    @staticmethod
    def sort_by_votes(list):
        return sorted(list, key=lambda recipe: -recipe.num_votes)

    @property
    def num_comments(self):
        comments = Comment.objects.filter(
            content_type_id=ContentType.objects.get_for_model(self).id,
            object_id=self.id
        )
        cnt = 0
        for i in range(len(comments)):
            answers = CommentAnswer.objects.filter(comment=comments[i])
            cnt += 1 + len(answers)
        return cnt


    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class IngredientManager(models.Manager):

    def get_groups(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT ingredient_group
            FROM recipes_ingredient""")

        return cursor.fetchall()


class Ingredient(models.Model):

    objects = IngredientManager()

    ingredient_info = models.ForeignKey(USAIngredient,
                                        verbose_name="Список ингредиентов"
    )
    value = models.FloatField("Количество", blank=True, null=True)
    measure = models.CharField("Тип измерения", max_length=255,
                               choices=INGREDIENT_MEASURE_CHOICES, null=True,
                               blank=True
    )
    ingredient_group = models.CharField("Группа ингредиентов",
                                        max_length=255, blank=True, null=True
    )
    addit_info = models.TextField(u"Дополнительная информация", blank=True,
                                  null=True)
    recipe = models.ForeignKey(Recipe, related_name="ingredients")


    def __unicode__(self):
        return self.ingredient_info.short_description

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Ингредиенты рецептa"


class RecipesBox(models.Model):
    title = models.CharField(verbose_name="Название коробки", max_length=50)
    recipe_list = models.ManyToManyField(Recipe, verbose_name="Список рецептов")
    followers = models.ManyToManyField(Profile,
                                       verbose_name="Пользователи использующие эту коробку",
                                       related_name="recipesboxes",
                                       blank=True, null=True
    )
    author = models.ForeignKey(Profile, verbose_name="Автор коробки",
                               help_text="Имеет право наполнять и изменять",
                               related_name="own_recipesboxes"
    )
    is_public = models.BooleanField(default=False,
                                    verbose_name="Публичная коробка")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


    class Meta:
        verbose_name = "Коробка рецептов"
        verbose_name_plural = "Коробки рецептов"


class WishedRecipes(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name="Рецепт",
        related_name="wished_set"
    )
    cook = models.ForeignKey(
        Profile,
        verbose_name="Повар",
        related_name="wished_set"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.recipe

    class Meta:
        verbose_name = "Желаемый рецепт"
        verbose_name_plural = "Желаемые рецепты"


class RecipeDescStep(models.Model):
    step_num = models.PositiveIntegerField()
    description = models.TextField("Описание")
    image = ImageField("Фото рецепта", upload_to="recipe_steps", blank=True,
                       null=True)
    recipe = models.ForeignKey(Recipe, related_name="steps")

    @property
    def number_of_step(self):
        return self.step_num

    def get_next_step_num(self, recipe, num=None):
        present_keys = RecipeDescStep.objects.filter(recipe=recipe).order_by(
            '-step_num').values_list('step_num', flat=True)
        if num and not num in present_keys:
            return num
        elif present_keys:
            return present_keys[0] + 1
        else:
            return 0

    def save(self, *args, **kwargs):
        if not self.id:
            self.step_num = self.get_next_step_num(self.recipe, self.step_num)
        if self.recipe.body:
            self.recipe.body += self.description
        else:
            self.recipe.body = self.description
        self.recipe.save()
        super(RecipeDescStep, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.recipe_id)

    def get_recipe_url(self):
        return reverse("recipe_details", args=(self.recipe.slug, ))

    class Meta:
        # unique_together = ("recipe", "step_num")
        ordering = ('recipe', )
        verbose_name = "Шаг рецепта"
        verbose_name_plural = "Шаги рецептов"


@receiver(post_save, sender=Recipe)
def plan_publish_recipe_task(sender, instance, created, **kwargs):
    if not instance.published:
        publish_recipe.apply_async(args=(instance, ), eta=instance.pub_date)


@receiver(post_save, sender=Recipe)
def log_recipe_adding(sender, instance, created, **kwargs):
    from statistics.recipes import recipe_added

    if created:
        recipe_added(instance)


@receiver(models.signals.pre_save, sender=Recipe)
def log_recipe_changing(sender, instance, **kwargs):
    from statistics.recipes import recipe_changed

    try:
        old_recipe = Recipe.objects.get(id=instance.id)
    except Recipe.DoesNotExist:
        print 'Recipe not found. Statistic was not aggregated.'
        return
    new_recipe = instance
    recipe_changed(old_recipe, new_recipe)


@receiver(post_save, sender=Recipe)
def watermark(sender, instance, created, **kwargs):
    if not instance.add_watermark:
        return
    from utils import add_watermark

    marked_img = add_watermark(instance.main_image)
    if not marked_img:
        return
    instance.main_image = marked_img
    instance.save()
