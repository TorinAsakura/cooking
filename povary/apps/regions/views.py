import json
from django.http import HttpResponse
from regions.models import City


def feed_city_list(request):
    country = request.GET.get("country", None)
    query = request.GET.get("query", "")

    kwargs = {
        "title__istartswith": query
    }

    if not country:
        city_list = []
    else:
        kwargs["country_id"] = country
        city_list = list(City.objects.filter(**kwargs).values_list("title", flat=True).distinct()[:20])

    return HttpResponse(json.dumps(city_list))