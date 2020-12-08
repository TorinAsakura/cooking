# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from categories.models import Category, SubCategory


def category_details(request, category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	recipe_list = category.recipe_set.filter(published=True)
	subcategory_list = category.subcategory_set.filter(published=True)
	result_list = list(recipe_list)
	paginator = Paginator(result_list, 10)
	page = request.GET.get('page')
	try:
		recipe_list = paginator.page(page)
	except PageNotAnInteger:
		recipe_list = paginator.page(1)
	except EmptyPage:
		recipe_list = paginator.page(paginator.num_pages)
	category.inc_visits()
	data = {
		"category": category,
		"recipe_list": recipe_list,
		"subcategory_list": subcategory_list,
	}
	return render(request, "categories/category_details.html", data)


def subcategory_details(request, category_slug, subcategory_slug):
	refer = request.META.get('HTTP_REFER')
	category = get_object_or_404(Category, slug=category_slug)
	subcat = get_object_or_404(SubCategory, slug=subcategory_slug, published=True)
	recipe_list = subcat.recipe_set.filter(published=True)
	paginator = Paginator(recipe_list, 10)
	page = request.GET.get('page')
	try:
		recipe_list = paginator.page(page)
	except PageNotAnInteger:
		recipe_list = paginator.page(1)
	except EmptyPage:
		recipe_list = paginator.page(paginator.num_pages)
	subcat.inc_visits()
	data = {
		"category": category,
		"subcategory": subcat,
		"recipe_list": recipe_list

	}
	return render(request, "categories/subcategory_details.html", data)
