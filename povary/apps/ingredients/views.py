# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse

from ingredients.models import USAIngredient
from utils import ajax_required


@ajax_required
def ingredients_autocomplete(request):
	query = request.GET.get('term', '')
	data = []
	if query:
		ingredients = USAIngredient.objects.filter(name_rus__istartswith=query)
		data = [{"id": i.id, "value": i.name_rus} for i in ingredients]
	return HttpResponse(json.dumps(data), mimetype="application/json")
