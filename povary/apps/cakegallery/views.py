# -*- coding: utf-8 -*-
import os, json
from utils import ajax_required

from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required

from cakegallery.models import CakeImage
from cakegallery.forms import CakeImageForm
from master_class.models import MasterClass
from cakegallery.models import CakeCategory, CakeSubCategory, CakeGallery
from search.forms import CakeGallerySearchForm
from tags.models import Tag


def cakeimage_gallery(request, gallery_slug):
	gallery = get_object_or_404(CakeGallery, slug=gallery_slug)
	gallery.inc_visits()
	page_no = 1
	afilter = "new"
	paginator = cakeimage_paginator(request, gallery, afilter, page_no)
	page = paginator.page(page_no)
	data = {
		"gallery": gallery,
		"afilter": afilter,
		"page":page,
		"paginator":paginator,
	}
	return render(request, "cakegallery/cakeimage_gallery.html", data)

@ajax_required
def cakeimage_filter(request, gallery_slug, afilter="new", page=1):
	gallery = get_object_or_404(CakeGallery, slug=gallery_slug)
	paginator = cakeimage_paginator(request, gallery, afilter, page)
	page_no = page
	page = paginator.page(page_no)
	data = {
		"gallery": gallery,
		"page": page,
		"paginator": paginator,
		"afilter": afilter,
	}
	return render(request, "cakegallery/image_search_result.html", data)

IMAGES_PER_PAGE = 28

def cakeimage_paginator(request, gallery, afilter, page):
	results = gallery.published_images()
	if afilter=="new":
		results = CakeImage.sort_by_created(results)
	if afilter=="top":
		results = CakeImage.sort_by_votes(results)
	if afilter=="comm":
		results = CakeImage.sort_by_comments(results)
	if request.method=="GET":
		return Paginator(results, IMAGES_PER_PAGE)
	else:
		return None

def cakeimage_details(request, image_slug):
	cakeimage = get_object_or_404(CakeImage, slug=image_slug)
	data = {
		"image": cakeimage,
	}
	return render(request, "cakegallery/cakeimage_details.html", data)


RESULTS_PER_PAGE = 10

def filter_gallery_paginator(request, q, cat, afilter):
	data = { 'q': q,
			 'cat':cat,
			 'afilter':afilter }
	form = CakeGallerySearchForm(data)
	if form.is_valid():
		search_results = form.search()
		results = []
		for sres in search_results:
			if len(sres.object.published_images())>0:
				results.append(sres)
		return Paginator(results, RESULTS_PER_PAGE)
	else:
		return None

@ajax_required
def cakeimage_gallery_filter(request, q, cat, afilter="new", page=1):
	page_no = page
	paginator = None
	page = None
	if request.method=="GET":
		paginator = filter_gallery_paginator(request, q, cat, afilter)
		if paginator:
			page = paginator.page(page_no)
			status = "ok"
		else:
			status = "error"
	else:
		status = "Not GET"
	data = {
		"status": status,
		"page":page,
		"paginator":paginator,
		'q': q,
		'cat':cat,
		"afilter":afilter,
	}
	return render(request, "cakegallery/search_result.html", data)

def cakeimage_gallery_filter_start(request):
	user = request.user
	q = ''
	afilter = "new"
	cat = None
	page = 1
	data = { 'q': q,
			 'cat': cat,
			 'afilter': afilter,
	}
	search_form = CakeGallerySearchForm(data)
	masterclass_list = MasterClass.sort_by_votes(MasterClass.objects.filter(published=True, is_cake=True))[:3]
	category_list = CakeCategory.objects.all().order_by("created")
	paginator = filter_gallery_paginator(request, q, cat, afilter)
	page = paginator.page(page)
	data = {
		"user": user,
		"search_form": search_form,
		"masterclass_list": masterclass_list,
	    "category_list": category_list,
	    "page":page,
		"paginator":paginator,
	}
	return render(request, "cakegallery/cakeimage_gallery_filter.html", data)

def add_photo(request, gallery_slug=None):
	gallery = None
	if gallery_slug:
		gallery = CakeGallery.objects.get(slug=gallery_slug)
	if request.method == 'POST':
		form = CakeImageForm(gallery, request.POST, request.FILES)
		form.author = request.user
		if form.is_valid():
			form.save(request.user)
			if gallery:
				return HttpResponseRedirect('/cakegallery/gallery/'+gallery.slug)
			return HttpResponseRedirect('/cakegallery/search')
	else:
		form = CakeImageForm(gallery)
	categorymc_list = CakeCategory.objects.all()
	ltags = [ tag.title for tag in Tag.objects.all()]
	tags = ""
	for tag in ltags:
		tags += tag+",";
	data  = {
		"form": form,
		"gallery": gallery,
		"categorymc_list": categorymc_list,
		"tags": tags,
	}
	return render(request, "cakegallery/add_photo.html", data)

@ajax_required
def get_subcategories(request, cat_slug):
	list = data = json.dumps({
				"subcategories": [{"title":sc.title, "slug":sc.slug}  for sc in CakeSubCategory.objects.filter(category__slug=cat_slug)]
			})
	return HttpResponse(data);
