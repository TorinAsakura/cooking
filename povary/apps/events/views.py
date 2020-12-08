# -*- coding: utf-8 -*-
import json

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from events.models import Event, EventCategory
from regions.models import Country, City


def add_cake_event(request):
	data = {
		"a": "a",
		"b": "b",
	}
	# todo # создать форму и вьюху добавления события
	return render(request, "events/add_cake_event.html", data)

def cake_event_list(request):
	cake_event_list = Event.objects.filter(published=True, is_cake=True)
	data = {
		"cake_event_list": cake_event_list
	}
	return render(request, "events/cake_event_list.html", data)

def cake_event_details(request, event_slug):
	cake_event = get_object_or_404(Event, slug=event_slug, published=True)
	data = {
		"cake_event": cake_event
	}
	return render(request, "events/cake_event_details.html", data)


def event_list(request):
	event_list = Event.objects.filter(published=True)
	data = {
		"event_list": event_list
	}
	return render(request, "events/event_list.html", data)


def event_details(request, event_slug):
	event = get_object_or_404(Event, slug=event_slug, published=True)
	data = {
		"event": event
	}
	return render(request, "events/event_details.html", data)


def eventcategory_list(request):
	eventcategory_list = EventCategory.objects.filter(published=True)
	data = {
		"eventcategory_list": eventcategory_list,
	}
	return render(request, "events/eventcategory_list.html", data)


def eventcategory_details(request, eventcategory_slug):
	eventcategory = get_object_or_404(EventCategory, slug=eventcategory_slug, published=True)
	category_events = eventcategory.events.filter(published=True)
	data = {
		"eventcategory": eventcategory,
		"category_events": category_events,
	}
	return render(request, "events/eventcategory_details.html", data)


def country_autocomplete(request):
	query = request.GET.get('query')
	if not query:
		raise Http404
	country_list = Country.objects.filter(title__istartswith=query)
	result = json.dumps({
		"query": query,
		"suggestions": [country.title for country in country_list],
		"data": [country.id for country in country_list]
	})
	return HttpResponse(result, mimetype="application/json")


def city_autocomplete(request):
	query = request.GET.get('query')
	country = request.GET.get('country')
	if not query:
		raise Http404
	city_list = City.objects.filter(title__istartswith=query, country__title=country)
	result = json.dumps({
		"query": query,
		"suggestions": [city.title for city in city_list],
		"data": [city.id for city in city_list]
	})
	return HttpResponse(result, mimetype="application/json")


def check_country_existence(request):
	country = request.GET.get("country")
	country_list = Country.objects.filter(title=country)
	status = True
	if not country_list:
		status = False
	return HttpResponse(
		json.dumps({"status": status, "message": "Выберите правильную страну"}),
		mimetype="application/json"
	)


