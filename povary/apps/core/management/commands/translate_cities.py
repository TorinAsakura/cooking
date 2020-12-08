import urllib, urllib2
import json

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError

from cities_light.models import City, Country


def get_translate(text):
    url = "http://translate.yandex.net/api/v1/tr.json/translate"
    data = urllib.urlencode({"lang":"en-ru", "text": text})
    link = "%s?%s" % (url, data)
    resp = urllib2.urlopen(link)
    translated = json.loads(resp.read())
    if translated['code'] == 200:
        return (translated['text'][0], True)
    else:
        return (link, False)


def check_city_existance(city_name, level):
    existed = City.objects.filter(name=city_name)
    if existed:
        city_name = "%s %s" % (city_name, existed.count()+level)
        city_name = check_city_existance(city_name, level+1)
        return city_name
    else:
        return city_name


class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for country in Country.objects.all():
            translated, status = get_translate(country.name_ascii)
            if status:
                country.name = translated
                country.save()
                # self.stdout.write('Translated "%s" to "%s"\n' % (country.name_ascii, translated))
            else:
                self.stdout.write('Error!\n %s' % country.name_ascii)
        for city in City.objects.filter(country__id__in=(192, 36, 231)): # get cities only for Ukraine, little hack
            translated, status = get_translate(city.name_ascii)
            if status:
                city.name = check_city_existance(translated, 0)
                city.save()
                # self.stdout.write('Translated "%s" to "%s"\n' % (city.name_ascii, translated))
            else:
                self.stdout.write('Error!\n %s' % city.name_ascii)
