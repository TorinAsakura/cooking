# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404


def page_details(request, page_slug):
	page = get_object_or_404(Page, slug=page_slug)
	data = {
		"page": page
	}
	return render(request, "pages/details.html", data)
