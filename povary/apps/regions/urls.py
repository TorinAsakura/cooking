from django.conf.urls import patterns, url


urlpatterns = patterns(
    "regions.views",
    url(r"^feed/city-list/$", "feed_city_list", name="city-list"),
)