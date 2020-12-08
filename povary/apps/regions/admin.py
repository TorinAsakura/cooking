from django.contrib import admin
from regions.models import *


class CountryAdmin(admin.ModelAdmin):
    search_fields = ("title",)


class CityAdmin(admin.ModelAdmin):
    list_filter = ("country",)
    search_fields = ("title",)


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)