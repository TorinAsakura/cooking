# -*- coding: utf-8 -*-
from itertools import chain
from django.forms import TextInput, Textarea, FileInput, CheckboxSelectMultiple
import os

from django import forms
from django.core.validators import EMPTY_VALUES
from django.utils.encoding import StrAndUnicode, force_unicode
from django.forms.util import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape, format_html

from filebrowser.base import FileObject
import autocomplete_light

from recipes.models import Recipe, Ingredient, RecipeDescStep, RecipesBox, \
    INGREDIENT_MEASURE_CHOICES, PrepMethod, Holiday, DIET_CHOICES, AGE_CHOICES, \
    EATING_TIME_CHOICES
from ingredients.models import USAIngredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('is_photorecipe', 'slug', 'author', 'published')

class PovaryCheckboxSelectMultiple(CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):

        divs = []

        for i, choice in enumerate(self.choices):

            if not choice[0]: continue

            div = format_html(u'<div class="check check2"><input id="{0}_{1}" '
                        u'name="{2}" value="{3}" type="checkbox" {5} />'
                        u'<label>{4}</label> </div>',
                        attrs['id'], i, name, choice[0], choice[1],
                        'checked' if value and choice[0] in value else '')

            divs.append(div)

        return mark_safe(u'\n'.join(divs))


class IngredientSelect(forms.Select):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        # self.choices.queryset = self.choices.queryset
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if value:
            ingr = USAIngredient.objects.get(id=int(value))
            output.append(self.render_option([value], ingr.id, ingr.name_rus))
        if options:
            output.append(options)
        output.append(u'</select>')
        return mark_safe(u'\n'.join(output))


class IngredientForm(forms.ModelForm):
    class IngredientModelChoiceField(forms.ModelChoiceField):
        def to_python(self, value):

            try:
                return USAIngredient.objects.get(name_rus=value)
            except USAIngredient.DoesNotExist:
                raise forms.ValidationError(u"Does not exists")

            return value

    class IngredientGroupChoiceField(forms.ChoiceField):

        def validate(self, value):
            pass

    ingredient_info = IngredientModelChoiceField(
         queryset=USAIngredient.objects.all(),
         widget=autocomplete_light.TextWidget('USAIngredientsAutocomplete',
         attrs={'class': 'input-text input-text2'})
    )

    def _get_choices():
        choices = (
            [(u'Создать новую', u'Создать новую')] +
            map(lambda x: (x[0],x[0]), Ingredient.objects.get_groups())
        )

        if ('', '') in choices:
            i = choices.index(('', ''))
            choices[i] = ('', u'Без группы')

        return choices

    ingredient_group = IngredientGroupChoiceField(
        choices=_get_choices(),
        required=False
    )

    measure = forms.ChoiceField(
        choices=INGREDIENT_MEASURE_CHOICES,
        required=False)

    def __init__(self, *args, **kwargs):

        data = kwargs.get('data')

        if data:
            new_value = ''
            for key, value in kwargs['data'].items():
                if key.endswith('ingredient_group'):
                    new_value = value
                    break
            if new_value:

                field_choices = self.declared_fields['ingredient_group'].choices

                if (new_value, new_value) not in field_choices:
                    self.declared_fields['ingredient_group'].choices.append(
                        (new_value, new_value))

        super(IngredientForm, self).__init__(*args, **kwargs)


    def save(self, recipe, commit=True):
        ingredient = super(IngredientForm, self).save(commit=False)

        if self.cleaned_data:
            ingredient.recipe = recipe
            ingredient.save()
        return ingredient

    class Meta:
        model = Ingredient
        exclude = ('recipe', )
        widgets = {
            "addit_info": Textarea(
                attrs={'placeholder': u"Здесь вы можете подчеркнуть особенность "
                                      u"ингрииента. К примеру: "
                                      u"“Соус купленный только в Мексике”",
                       'class': "textarea"}),
            "value": TextInput(
                attrs={'class': "input-text input-text3",
                       'placeholder': '0'}
            )
            }


class RecipeDescStepForm(forms.ModelForm):
    def save(self, recipe, commit=True):

        step = super(RecipeDescStepForm, self).save(commit=False)
        if self.cleaned_data:
            step.recipe = recipe
            step.save()

        return step

    class Meta:
        model = RecipeDescStep
        exclude = ('recipe', 'step_num')

        widgets = {
            'image': FileInput(attrs={'class': "fileinput"}),

            "description": Textarea(
                attrs={'placeholder': u'Опишите действие которое '
                                      u'необходимо совершить',
                       'class': "textarea"}),
        }


class RecipeFormStep1(forms.ModelForm):
    def clean_prepare_time_to(self):
        data = self.cleaned_data
        timefrom = data.get('prepare_time_from')
        timeto = data.get('prepare_time_to')
        if timefrom > timeto:
            raise forms.ValidationError(u"Время приготовления указано неверно")
        return timeto

    def save(self, author, commit=True):
        recipe = super(RecipeFormStep1, self).save(commit=False)
        recipe.author = author
        recipe.completed = False
        recipe.save()
        return recipe

    class Meta:
        model = Recipe
        fields = (
        "title", "description", "prepare_time_from", "prepare_time_to",
        "category", "sub_category", "portion_num", 'main_image', 'portion_num'
        )

        widgets = {
            "description": Textarea(
                attrs={'placeholder': u'Сделайте хорошее описание вашего '
                                      u'рецепта. Это поможет остальным вкратце '
                                      u'понять общую суть',
                       'class': "textarea"}),

            "title": TextInput(attrs={'class': "input-text"}),

            "prepare_time_from": TextInput(
                attrs={'class': "amount minamount", 'value': "20"}),

            "prepare_time_to": TextInput(
                attrs={'class': "amount maxamount", 'value': "40"}),

            "portion_num": TextInput(
                attrs={'class': "amount amount7", 'value': "1"}),

            "main_image": FileInput(attrs={'class': "fileinput"}),
        }

    def check_lengths(self, data, name,min_len, max_len):
        rules = (
                 u'%s - обязатльное поле, минимальное количество\n' % name +
                 u'символов %s, максимальное %s' % (min_len, max_len)
        )

        if len(data) < min_len:
            raise forms.ValidationError(u"Вы ввели менше %s символов\n" % min_len + rules)
        elif len(data) > max_len:
            raise forms.ValidationError(u"Вы ввели больше %s символов\n" % max_len+ rules)


    def clean_description(self):
        data = self.cleaned_data['description']
        self.check_lengths(data,u'Описание',50, 5000)
        return data

    def clean_title(self):
        data = self.cleaned_data['title']
        self.check_lengths(data,u'Название',3, 120)
        return data

    # class Media:
    #     js = (
    #     '/static/tiny_mce/tiny_mce.js',
    #     '/static/tiny_mce/articles_tinymce_config.js',
    #     )


class RecipeFormStep2(forms.ModelForm):
    main_image = forms.CharField(widget=forms.FileInput, required=False,
                                 label="Главное фото рецепта")

    class Meta:
        model = Recipe
        fields = ('main_image', )


class RecipeFormStep3(forms.ModelForm):

    class CommaSeparetedChoiceField(forms.ChoiceField):
        def to_python(self, value):

            return u','.join(
                [choice[1].decode('utf-8')
                 for choice in self.choices if choice[0] in value])

        def validate(self, value):

            choices = map(lambda x: x[1].decode('utf-8'), self.choices)

            valid = True
            for v in value.split(','):

                if v not in choices:
                    valid = False
                    break

            if not valid:
                return super(self.__class__, self).validate(value)


    preparation_method = forms.ModelChoiceField(
        queryset=PrepMethod.objects.all(), empty_label=u"выберите категорию",
        required=False)

    holiday = forms.ModelChoiceField(
        queryset=Holiday.objects.all(), empty_label=u"выберите категорию",
        required=False)

    diet = CommaSeparetedChoiceField(
        choices=DIET_CHOICES,
        widget=PovaryCheckboxSelectMultiple(),
        required=False
    )

    eating_time = CommaSeparetedChoiceField(
        choices=EATING_TIME_CHOICES,
        widget=PovaryCheckboxSelectMultiple(),
        required=False
    )

    age_limit = CommaSeparetedChoiceField(
        choices=AGE_CHOICES,
        widget=PovaryCheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Recipe
        fields = (
        "cuisine",
        )

        widgets = {
            "cuisine": PovaryCheckboxSelectMultiple(),
        }


class RecipesBoxForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(RecipesBoxForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        title_exists = len(RecipesBox.objects.filter(title__iexact=title,
                                                     author=self.user.profile))
        if title_exists:
            raise forms.ValidationError("У вас уже есть коробка с таким именем")
        if not title:
            raise forms.ValidationError(
                "Название коробки не может быть пустым или состоять только из пробелов")
        return title

    class Meta:
        model = RecipesBox
        exclude = ('followers', 'author', 'recipe_list', 'published')
