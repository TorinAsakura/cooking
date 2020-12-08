# -*- coding: utf-8 -*-
from django.template.loader import render_to_string
import os
import json

from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.formtools.wizard.views import SessionWizardView
from django.forms.models import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.formtools.wizard.forms import ManagementForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from recipes.forms import RecipeForm, IngredientForm, RecipeFormStep2, RecipeDescStepForm, \
    RecipesBoxForm
from recipes.models import Recipe, Ingredient, RecipesBox, Cuisine, DIET_CHOICES, PrepMethod, Holiday, EATING_TIME_CHOICES, WishedRecipes
from categories.models import Category, SubCategory
from filebrowser.base import FileObject
from comments.forms import CommentForm, CommentAnswerForm
from comments.models import Comment
from statistics.tasks import track_event
from utils.utils import get_complex_paginator
from utils import ajax_required
from utils.utils import search
from search.forms import RecipeSearchForm


def recipe_details(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    ingredient_list = recipe.ingredients.all()
    # ingredient_groups = ingredient_list.distinct("ingredient_group").values(
    #     'ingredient_group')
    ingredient_groups = ingredient_list.values("ingredient_group")
    ingredients = {}
    for group in [i['ingredient_group'] for i in ingredient_groups]:
        ingredients[group] = ingredient_list.filter(ingredient_group=group)
    refer = request.META.get("HTTP_REFERER")
    breadcrumbs = None
    if refer:
        current_domain = Site.objects.get_current().domain
        refer_url = refer.partition(current_domain)[2]
        if refer_url == reverse('recipe_list'):
            breadcrumbs = """<a href="%s">Все рецепты</a>""" % (
            reverse('recipe_list'))

    if request.user.is_authenticated():
        recipebox_list = request.user.profile.recipesboxes.all()
    else:
        recipebox_list = False
    comment_form = CommentForm(request.POST or None)
    commentanswer_form = CommentAnswerForm()
    if request.method == "POST":
        if comment_form.is_valid() and request.user.is_authenticated():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.of = recipe
            comment = comment.save()
            tracking_data = {
            "object_id": comment.id,
            "model": Comment,
            "tracking_type": "comment added"
            }
            track_event.delay(tracking_data)
            return HttpResponseRedirect(
                reverse('recipe_details', args=(recipe.slug, )))
    recipe_type = ContentType.objects.get_for_model(Recipe)
    comment_list = Comment.objects.filter(content_type=recipe_type,
                                          object_id=recipe.id).order_by(
        "-created")
    step_list = recipe.steps.order_by('step_num')
    gallery_images = recipe.gallery.images.order_by('?')[:10]
    recipe.inc_visits()

    similar_recipies = Recipe.objects.exclude(id=recipe.id).filter(
        ingredients__ingredient_info__in=recipe.ingredients.values_list(
            'ingredient_info', flat=True))


    data = {
        "recipe": recipe,
        "ingredient_list": ingredient_list,
        "comment_form": comment_form,
        "comment_list": comment_list,
        "step_list": step_list,
        "recipebox_list": recipebox_list,
        "breadcrumbs": breadcrumbs,
        "commentanswer_form": commentanswer_form,
        "gallery_images": gallery_images,
        "ingredients": ingredients,
        "item_obj": recipe,
        'similar_recipies': similar_recipies,
    }
    return render(request, "recipes/details.html", data)


def recipe_list(request):
    #List for chosen cuisines and diets by user
    chosen_cuisine_list = []
    chosen_diet_list = []

    # List with switched on HTML filters by user
    filters = []
    order = request.GET.get('order')
    category = None

    query = request.GET.get('query')

    if query:
        filtered_recipe_list = search(
            query, 'body', Recipe.objects.all()
        )
    else:
        # Get filters parameters from request
        holiday = request.GET.get('to_holiday')
        preparation_method = request.GET.get('preparation_method')
        include_ing = request.GET.get('include_ing')
        exclude_ing = request.GET.get('exclude_ing')
        category = request.GET.get('category')

        protein = request.GET.get('protein')
        lipid_total = request.GET.get('lipid_total')
        carbohydrt = request.GET.get('carbohydrt')
        cholestrl = request.GET.get('cholestrl')
        time_from = request.GET.get('time')

        #Converting from "on" to 1 of 4 choises. HTML form returning on at checkboxes
        time = ['supper' if request.GET.get('supper') else None,
                'breakfast' if request.GET.get('breakfast') else None,
                'lunch' if request.GET.get('lunch') else None,
                'dinner' if request.GET.get('dinner') else None]

        #Omitting None elements
        time = filter(None, time)

        #Gettings cuisines and diets id`s
        for key in request.GET.keys():
            if str(key).startswith('cuisine'):
                chosen_cuisine_list.append(str(key).split('_')[1])
            if str(key).startswith('diet'):
                chosen_diet_list.append(str(key).split('_')[1])

        # Lookup dict (it`s may be dynamic, some parameters may be omitted)
        lookup_params = {'published': True}

        #Next tests fill in lookup dict.
        if holiday:
            lookup_params['holiday_id'] = int(holiday)
            filters.append(('to_holiday', holiday, Holiday.objects.get(id=holiday).title))
        if preparation_method:
            lookup_params['preparation_method_id'] = int(preparation_method)
            filters.append(('preparation_method', preparation_method, PrepMethod.objects.get(id=preparation_method).title))
        if include_ing:
            lookup_params['ingredients__ingredient_info__name_rus'] = include_ing
            filters.append(('include_ing', include_ing, include_ing))
        if time:
            lookup_params['eating_time__in'] = time
            filters += [(x[0], 'on', x[1]) for x in EATING_TIME_CHOICES if x[0] in time]
        if chosen_cuisine_list:
            lookup_params['cuisine__in'] = chosen_cuisine_list
            cuisines = Cuisine.objects.filter(
                id__in=chosen_cuisine_list
            )
            for c in cuisines:
                filters.append(('cuisine_%s' % c.id, 'on', c.title))

        if chosen_diet_list:
            filters += [('diet_%s' % i, 'on', x[1]) for i, x in enumerate(DIET_CHOICES) if str(i) in chosen_diet_list]
            chosen_diet_list = map(lambda j: DIET_CHOICES[int(j)][0], chosen_diet_list)
            lookup_params['diet__in'] = chosen_diet_list

        if category:
            lookup_params['category__id'] = int(category)

        if time_from:
            lookup_params['prepare_time_from__lte'] = time_from

        filtered_recipe_list = Recipe.objects.filter(**lookup_params)

        if exclude_ing:
            filtered_recipe_list.exclude(
                ingredients__ingredient_info__name_rus=exclude_ing
            )

        #comparison function for food elements
        def comp(item):
            result = False

            if (
                (not protein or item.get_food_elements['protein'] <= int(protein)) and
                (not lipid_total or item.get_food_elements['lipid_total'] <= int(lipid_total)) and
                (not carbohydrt or item.get_food_elements['carbohydrt'] <= int(carbohydrt)) and
                (not cholestrl or item.get_food_elements['cholestrl'] <= int(cholestrl))
            ):
                result = True

            return result

        if order:
            filtered_recipe_list = filtered_recipe_list.order_by(
                '-created' if order == 'down' else 'created')

        filtered_recipe_list = filter(comp, filtered_recipe_list)

    per_page = 5
    pages_per_part = 8
    page = request.GET.get('page', 1)
    part = request.GET.get('part', 1)

    recipes_list, part_list, prev_base_page, next_base_page = \
        get_complex_paginator(filtered_recipe_list, page, part, per_page, pages_per_part)

    categories = Category.objects.all()

    if Category.objects.filter(id=category).exists():
        category = Category.objects.get(id=category)

    data = {
        "order": order,
        "filters": filters,
        "categories": categories,
        'chosen_category': category,
        "recipe_list": recipes_list,
        "part_list": part_list,
        "prev_base_page": prev_base_page,
        "next_base_page": next_base_page,
        "per_page": per_page,
        "cuisines": Cuisine.objects.all(),
        "prep_methods": PrepMethod.objects.all(),
        "holidays": Holiday.objects.all(),
        "diets": [x[1] for x in DIET_CHOICES],
    }

    if request.is_ajax():
        rendered = render_to_string(
            'recipes/recipe_list_central_block.html',
            data
        )

        return HttpResponse(rendered)

    return render(request, "recipes/list.html", data)


def cake_recipe_list(request):
    recipe_list = Recipe.objects.filter(published=True, is_cake=True).order_by(
        '-created')
    paginator = Paginator(recipe_list, 10)
    page = request.GET.get('page')
    try:
        recipe_list = paginator.page(page)
    except PageNotAnInteger:
        recipe_list = paginator.page(1)
    except EmptyPage:
        recipe_list = paginator.page(paginator.num_pages)
    data = {
    "recipe_list": recipe_list,
    }
    return render(request, "recipes/list.html", data)


@login_required
def add_recipe_to_box(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    create_box_form = RecipesBoxForm(request.user, request.POST or None)
    referer = request.POST.get('referer', None)
    if request.is_ajax():
        box_to_add = request.POST.getlist('box_to_add')
        if box_to_add:
            boxes_to_remove = recipe.recipesbox_set.filter(author=request.user)
            [i.recipe_list.remove(recipe) for i in boxes_to_remove]
            for box_id in box_to_add:
                try:
                    recipebox = RecipesBox.objects.get(id=int(box_id))
                    recipebox.recipe_list.add(recipe)
                    data = json.dumps({
                    "status": True,
                    "referer": referer
                    })
                except RecipesBox.DoesNotExist:
                    data = json.dumps({
                    "status": True,
                    "error": True
                    })
            return HttpResponse(data, mimetype="application/json")

        if create_box_form.is_valid():
            recipe_box = create_box_form.save(commit=False)
            recipe_box.author = request.user.profile
            recipe_box.save()

            data = json.dumps({
            "status": True,
            "referer": referer,
            "box_id": recipe_box.id,
            "box_title": recipe_box.title
            })
            return HttpResponse(data, mimetype="application/json")
    if request.method == "POST":
        if create_box_form.is_valid():
            recipe_box = create_box_form.save(commit=False)
            recipe_box.author = request.user.profile
            recipe_box.save()
            recipe_box.recipe_list.add(recipe)
            recipe_box.save()
    recipebox_list = request.user.profile.own_recipesboxes.all()
    data = {
        "recipebox_list": recipebox_list,
        "create_box_form": create_box_form,
        "recipe": recipe,
        "referer": referer
    }
    return render(request, "recipes/recipe_to_box.html", data)


def recipe_add(request):
    form = RecipeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    data = {
    "form": form,
    }
    return render(request, 'recipes/recipe-add.html', data)

TEMPLATES = {"first": "recipes/first.html",
             "second": "recipes/second.html",
             "third": "recipes/third.html"}


class RecipeWizard(SessionWizardView):
    template_name = "recipes/wizard_form.html"
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'uploads', 'recipe_images')
    )

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecipeWizard, self).dispatch(*args, **kwargs)

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):

        # import ipdb; ipdb.set_trace()

        step1, step2, step3 = form_list
        recipe_data = {}

        # Recipe data edit
        if step1.is_valid():
            recipe = step1.save(self.request.user)

        if step2.is_valid():
            for form in step2:
                if form.is_valid():
                    form.save(recipe)

        if step3.is_valid():
            recipe_data.update(step3.cleaned_data)

        # Step adding
        # import ipdb; ipdb.set_trace()

        RecipeDescStepFormSet = formset_factory(RecipeDescStepForm)
        step_formset = RecipeDescStepFormSet(
            prefix="steps",
            data=self.request.POST,
            files=self.request.FILES
        )

        for form in step_formset:
            if form.is_valid():
                form.save(recipe)

        recipe_data['completed'] = True

        try:

            for key, value in recipe_data.items():
                if key == 'cuisine':
                    for cuisine in value:
                        recipe.cuisine.add(cuisine)
                    continue
                setattr(recipe, key, value)
            recipe.save()

        except Exception:
            pass


        tracking_data = {
        "model": Recipe,
        "object_id": recipe.id,
        "tracking_type": "recipe added"
        }
        track_event(tracking_data)
        self.storage.reset()
        return HttpResponseRedirect(
            reverse('recipe_details', args=(recipe.slug, )))

    def get_context_data(self, form, **kwargs):
        context = super(RecipeWizard, self).get_context_data(form=form,
                                                             **kwargs)
        # IngredientFormSet = formset_factory(IngredientForm)

        RecipeDescStepFormSet = formset_factory(RecipeDescStepForm)

        if self.steps.current == 'third':

            # Description steps formset
            step_formset = self.instance_dict.get(
                'step_formset', None) or RecipeDescStepFormSet(prefix="steps")
            context.update({"step_formset": step_formset})

        context['search_form'] = RecipeSearchForm()

        return context

    def get(self, request, *args, **kwargs):
        """
        This method handles GET requests.

        If a GET request reaches this point, the wizard assumes that the user
        just starts at the first step or wants to restart the process.
        The data of the wizard will be resetted before rendering the first step.
        """
        self.storage.reset()

        # reset the current step to the first step.
        self.storage.current_step = self.steps.first
        # self.instance_dict['ingredients_formset'] = None
        # self.instance_dict['step_formset'] = None
        return self.render(self.get_form())

    def post(self, *args, **kwargs):
        """
        This method handles POST requests.

        The wizard will render either the current step (if form validation
        wasn't successful), the next step (if the current step was stored
        successful) or the done view (if no more steps are available)
        """
        # Look for a wizard_goto_step element in the posted data which
        # contains a valid step name. If one was found, render the requested
        # form. (This makes stepping back a lot easier).

        wizard_goto_step = self.request.POST.get('wizard_goto_step', None)
        if wizard_goto_step and wizard_goto_step in self.get_form_list():
            self.storage.current_step = wizard_goto_step

            # import ipdb; ipdb.set_trace()

            form = self.get_form(
                data=self.storage.get_step_data(self.steps.current),
                files=self.storage.get_step_files(self.steps.current))

            return self.render(form)

        # Check if form was refreshed
        management_form = ManagementForm(self.request.POST, prefix=self.prefix)
        if not management_form.is_valid():
            raise forms.ValidationError(
                'ManagementForm data is missing or has been tampered.')

        form_current_step = management_form.cleaned_data['current_step']
        if (form_current_step != self.steps.current and
                    self.storage.current_step is not None):
            # form refreshed, change current step
            self.storage.current_step = form_current_step

        # get the form for the current step

        # import ipdb; ipdb.set_trace()

        form = self.get_form(data=self.request.POST, files=self.request.FILES)

        step_formset_valid = True

        if self.steps.current == 'third':
            # Description formset
            RecipeDescStepFormSet = formset_factory(RecipeDescStepForm)
            step_formset = RecipeDescStepFormSet(self.request.POST,
                                                 self.request.FILES,
                                                 prefix="steps")
            step_formset_valid = step_formset.is_valid()

        # and try to validate
        if form.is_valid() and step_formset_valid:
            # if the form is valid, store the cleaned data and files.
            self.storage.set_step_data(self.steps.current,
                                       self.process_step(form))
            self.storage.set_step_files(self.steps.current,
                                        self.process_step_files(form))

            # check if the current step is the last step
            if self.steps.current == self.steps.last:
                # no more steps, render done view
                return self.render_done(form, **kwargs)
            else:
                # proceed to the next step
                return self.render_next_step(form)
        return self.render(form)


@ajax_required
def set_portion(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    data = json.dumps({"error": False})
    try:
        portion = int(request.POST.get('portion', 0))
        recipe.portion_num = portion
        recipe.save()
    except Exception:
        data = json.dumps({"error": True})
    finally:
        return HttpResponse(data, mimetype="application/json")


@ajax_required
def wish(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    data = json.dumps({"error": False})
    try:
        WishedRecipes.objects.create(
            recipe=recipe,
            cook=request.user.profile
        )
    except Exception:
        data = json.dumps({"error": True})
    finally:
        return HttpResponse(data, mimetype="application/json")

