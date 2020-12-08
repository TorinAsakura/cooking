# -*- coding: utf-8 -*-

import os
import json
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from django import forms
from utils import ajax_required
from django.forms.models import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.formtools.wizard.forms import ManagementForm
from master_class.models import MasterClass, CategoryMC, SubCategoryMC
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from search.forms import MCSearchForm
from comments.forms import CommentForm, CommentAnswerForm
from forms import MasterClassForm

from ingredients.models import USAIngredient
from master_class.forms import CakeMCFormStep1, CakeMCFormStep2, CakeMCFormStep3
from master_class.forms import IngredientForm, CakeMCStepForm
from recipes.forms import RecipeForm, RecipeFormStep2, \
	RecipesBoxForm
from tags.models import Tag
from django.core.paginator import Paginator


def masterclass_details(request, mc_slug):
	master_class = get_object_or_404(MasterClass, slug=mc_slug)
	master_class.inc_visits()
	data = {
		"master_class": master_class,
	}
	return render(request, "master_class/details.html", data)


def cake_mc_details(request, mc_slug):
	NUM_SIMILAR_MC = 8
	master_class = get_object_or_404(MasterClass, slug=mc_slug)
	master_class.inc_visits()
	best_mc_list = MasterClass.sort_by_votes(MasterClass.objects.filter(published=True, is_cake=True).exclude(id=master_class.id))[:3]
	similar_mc_list = MasterClass.objects.filter(published=True).order_by("?")[:NUM_SIMILAR_MC]
	author_mc_list = MasterClass.sort_by_votes(MasterClass.objects.filter(published=True, author=master_class.author, is_cake=True).exclude(id=master_class.id))[:3]

	data = {
		"user": request.user,
		"comment_form": CommentForm(),
		"answer_form": CommentAnswerForm(),
		"master_class": master_class,
		"masterclass_list": best_mc_list,
		"author_mc_list": author_mc_list,
		"similar_mc_list": similar_mc_list,
        "seo_obj": master_class,
	}
	return render(request, "master_class/cake_mc_details.html", data)


def mc_category_details(request, mc_category_slug):
	category = get_object_or_404(CategoryMC, slug=mc_category_slug)
	category.inc_visits()
	data = {
		"category": category
	}
	return render(request, "master_class/category_details.html", data)


def mc_subcategory_details(request, mc_subcategory_slug):
	subcategory = get_object_or_404(SubCategoryMC, slug=mc_subcategory_slug)
	subcategory.inc_visits()
	data = {
		"subcategory": subcategory
	}
	return render(request, "master_class/subcategory_details.html", data)


class CakeMCWizard(SessionWizardView):
	template_name = "master_class/add_cake_mc_wizard.html"
	file_storage = FileSystemStorage(
		location=os.path.join(settings.MEDIA_ROOT, 'uploads', 'mc_images')
	)

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(CakeMCWizard, self).dispatch(*args, **kwargs)

	def done(self, form_list, **kwargs):
		step1, step2, step3 = form_list
		mc_data = {}

		# Recipe data edit
		if step1.is_valid():
			mc = step1.save(self.request.user)
		if step2.is_valid():
			pass # mc_data.update(step2.cleaned_data)
		if step3.is_valid():
			mc_data.update(step3.cleaned_data)

		mc = MasterClass.objects.get(id=mc.id)

		# Ingredients adding
		ingred_formset = self.instance_dict.get('ingredients_formset', ())
		for form in ingred_formset:
			if form.is_valid():
				form.save(mc)
		# Step adding
		step_formset = self.instance_dict.get('step_formset', ())
		for form in step_formset:
			if form.is_valid():
				form.save(mc)
		MasterClass.objects.filter(id=mc.id).update(**mc_data)
		return HttpResponseRedirect(reverse('cake_mc_details', args=(mc.slug, )))

	def get_context_data(self, form, **kwargs):
		context = super(CakeMCWizard, self).get_context_data(form=form, **kwargs)

		masterclass_list = MasterClass.sort_by_votes(MasterClass.objects.filter(published=True, is_cake=True))[:3]
		categorymc_list = CategoryMC.objects.filter(is_cake=True).order_by("created")
		context.update({
						"masterclass_list": masterclass_list,
						"categorymc_list": categorymc_list,
						"form_0_valid": self.form_valid('0'),
						"form_1_valid": self.form_valid('1'),
						"form_2_valid": self.form_valid('2'),
						})
		IngredientFormSet = formset_factory(IngredientForm, extra=0)
		if self.steps.current == '1':
			# Ingredients formset
			ingred_formset =  self.instance_dict.get('ingredients_formset', None) or IngredientFormSet(prefix="ingredients")
			context.update({"ingredients_formset": ingred_formset})
			formset_id_list = []
			for form in ingred_formset.forms:
				field = form.visible_fields()[0]
				formset_id_list.append(field.id_for_label)
			context.update({"formset_id_list": formset_id_list})
		CakeMCStepFormSet = formset_factory(CakeMCStepForm, extra=0)
		if self.steps.current == '2':
			# Description steps formset
			step_formset =  self.instance_dict.get('step_formset', None) or CakeMCStepFormSet(prefix="steps")
			context.update({"step_formset": step_formset})
		return context

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

		# get the form for the current step
		form = self.get_form(data=self.request.POST, files=self.request.FILES)

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

		if self.steps.current == '1':
			# Ingredient formset
			IngredientFormSet = formset_factory(IngredientForm)
			ingred_formset = IngredientFormSet(self.request.POST, self.request.FILES, prefix="ingredients")
			ingred_formset_valid = ingred_formset.is_valid()
			self.instance_dict['ingredients_formset'] = ingred_formset
		else:
			ingred_formset_valid = True

		if self.steps.current == '2':
			# Description formset
			CakeMCStepFormSet = formset_factory(CakeMCStepForm)
			step_formset = CakeMCStepFormSet(self.request.POST, self.request.FILES, prefix="steps")
			step_formset_valid = step_formset.is_valid()
			self.instance_dict['step_formset'] = step_formset
		else:
			step_formset_valid = True

		# and try to validate
		if form.is_valid()  and ingred_formset_valid and step_formset_valid:
			# if the form is valid, store the cleaned data and files.
			self.storage.set_step_data(self.steps.current, self.process_step(form))
			self.storage.set_step_files(self.steps.current, self.process_step_files(form))
			# check if the current step is the last step
			wizard_goto_step = self.request.POST.get('next_form', None)
			if wizard_goto_step == -1: wizard_goto_step = None
			if wizard_goto_step and wizard_goto_step in self.get_form_list() and form.is_valid():
				self.storage.current_step = wizard_goto_step
				form = self.get_form(
					data=self.storage.get_step_data(self.steps.current),
					files=self.storage.get_step_files(self.steps.current))
				return self.render(form)
			if self.steps.current == self.steps.last:
				# no more steps, render done view
				return self.render_done(form, **kwargs)
			else:
				# proceed to the next step
				return self.render_next_step(form)
		else:
			self.storage.set_step_data(self.steps.current, self.process_step(form))
			self.storage.set_step_files(self.steps.current, self.process_step_files(form))
			form = self.get_form(
					data=self.storage.get_step_data(self.steps.current),
					files=self.storage.get_step_files(self.steps.current))
		return self.render(form)

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
		self.instance_dict['ingredients_formset'] = None
		self.instance_dict['step_formset'] = None
		return self.render(self.get_form())

	def form_valid(self, step_num):
		return self.storage.get_step_data(str(step_num)) is not None


RESULTS_PER_PAGE = 28


def filter(request, q, cat, ing, afilter, page):
	data = {
		'q': q,
		'cat': cat,
		'ing': ing,
		'afilter': afilter
	}
	form = MCSearchForm(data)
	page_no = page
	paginator = None
	page = None
	if request.method == "GET":
		if form.is_valid():
			results = form.search()
			paginator = Paginator(results, RESULTS_PER_PAGE)
			page = paginator.page(page_no)
			status = "Ok"
		else:
			status = "Form not valid"
	else:
		status = "Not GET"

	data = {
		"page": page,
		"paginator": paginator,
		'q': q,
		'cat': cat,
		'ing': ing,
		"afilter": afilter,
	}
	return render(request, "master_class/search_result.html", data)


@ajax_required
def get_mcsubcategories(request, cat_slug):
	data = json.dumps({
		"subcategories": [{"title": sc.title, "slug": sc.slug} for sc in SubCategoryMC.objects.filter(category__slug=cat_slug)]
	})
	return HttpResponse(data)


@ajax_required
def mc_filter(request, q, cat, ing, afilter="new", page=1):
	return filter(request, q, cat, ing, afilter, page)


def mc_filter_start(request):
	masterclass_list = MasterClass.sort_by_votes(MasterClass.objects.filter(published=True, is_cake=True))[:3]
	category_list_all = CategoryMC.objects.filter(is_cake=True).order_by("created")
	category_list = []
	for cat in category_list_all:
		if len(MasterClass.objects.filter(category=cat)) > 0:
			category_list.append(cat)
	ingredient_list = USAIngredient.objects.all()
	data = {'q': ''}
	form = MCSearchForm(data)
	results = form.search()
	paginator = Paginator(results, RESULTS_PER_PAGE)
	page = paginator.page(1)
	data = {
		'search_form': MCSearchForm(),
		'masterclass_list': masterclass_list,
		'category_list': category_list,
		'ingredient_list': ingredient_list,
		"page": page,
		"paginator": paginator,
	}
	return render(request, "master_class/cake_mc_filter.html", data)


def cake_mc_add(request):
	masterclass_list = MasterClass.sort_by_votes(MasterClass.objects.filter(published=True, is_cake=True))[:3]
	categorymc_list = CategoryMC.objects.filter(is_cake=True).order_by("created")
	ltags = [tag.title for tag in Tag.objects.all()]
	tags = ""
	for tag in ltags:
		tags += tag + ","
	data = {
		"masterclass_list": masterclass_list,
		"categorymc_list": categorymc_list,
		"tags": tags,
	}
	return render(request, "master_class/cake_mc_wizard_form.html", data)
