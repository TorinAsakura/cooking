# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from forum_integration.api import get_last_topics
from events.models import EventCategory
from events.models import Event
from search.forms import RecipeSearchForm
from articles.models import Article
from recipes.models import Recipe
from profiles.models import Profile
from master_class.models import MasterClass
from gallery.models import Gallery, GalleryImage
from cakegallery.models import CakeImage
from core.forms import ContactForm


def cake_home(request):
    recipes_total = Recipe.objects.filter(published=True, is_cake=True).count()
    cake_recipes = Recipe.sort_by_votes(
        Recipe.objects.filter(published=True, is_cake=True))[:8]
    masterclass_list = MasterClass.sort_by_votes(
        MasterClass.objects.filter(published=True, is_cake=True))[:6]

    MASTERS_ON_SCROLL = 6
    cakemaster_list = Profile.objects.filter(cake_master=True).order_by(
        "rating")[:12]
    masters = []
    counter = -1
    for it, master in enumerate(cakemaster_list):
        if it % MASTERS_ON_SCROLL is 0:
            counter += 1
            masters.append([])
        masters[counter].append(master)
    now = datetime.datetime.now()
    event_list = Event.objects.filter(published=True, is_cake=True,
                                      start_date__lt=now,
                                      end_date__gt=now).order_by('-start_date')[
                 :2]
    data = {
    "recipes_total": recipes_total,
    "cake_recipes": cake_recipes,
    "masterclass_list": masterclass_list,
    "gallery_list": CakeImage.get_gallery_list(20),
    "event_list": event_list,
    "masters": masters,
    }
    return render(request, 'core/cake_home.html', data)


def home(request):
    #last_topics = get_last_topics()
    last_topics = ()
    # search_form = RecipeSearchForm()

    slideshow_recipes = Recipe.objects.filter(published=True, on_main=True)
    eventcategory_list = EventCategory.objects.filter(published=True)
    article_list = Article.objects.filter(published=True,
                                          verified=True).order_by('-pub_date')[:3]
    RECIPES_TOTAL = 9
    RECIPES_ON_SCROLL = 6
    b_recipes = Recipe.sort_by_votes(Recipe.objects.filter(published=True))[:RECIPES_TOTAL]

    best_recipes = []
    counter = -1
    for it, recipe in enumerate(b_recipes):
        if it % RECIPES_ON_SCROLL is 0:
            counter += 1
            best_recipes.append([])
        best_recipes[counter].append(recipe)
    n_recipes = Recipe.objects.filter(published=True).order_by('-pub_date')[
                :RECIPES_TOTAL]

    new_recipes = []
    counter = -1
    for it, recipe in enumerate(n_recipes):
        if it % RECIPES_ON_SCROLL is 0:
            counter += 1
            new_recipes.append([])
        new_recipes[counter].append(recipe)

    day_recipe = Recipe.objects.filter(published=True).latest('pub_date')
    masterclass_list = MasterClass.objects.filter(published=True)[:4]
    cake_gallery_list = CakeImage.objects.filter(published=True)[:4]
    cakemaster_list = Profile.objects.filter(cake_master=True)[:5]
    povary_list = Profile.objects.filter(cook=True)[:4]
    event_list = Event.objects.filter(
        published=True,
        is_cook=True).order_by('-updated')[:3]

    cake_event_list = Event.objects.filter(
        published=True,
        is_cake=True).order_by('-updated')[:3]

    data = {
        "last_forum_topics": last_topics,
        "search_form": RecipeSearchForm,
        "slideshow_recipes": slideshow_recipes,
        "masterclass_list": masterclass_list,
        "gallery_list": cake_gallery_list,
        "article_list": article_list,
        "best_recipes": best_recipes,
        "new_recipes": new_recipes,
        "day_recipe": day_recipe,
        "cakemaster_list": cakemaster_list,
        "povary_list": povary_list,
        "event_list": event_list,
        "cake_event_list": cake_event_list,
        "eventcategory_list": eventcategory_list,
        "is_home": True,
    }
    return render(request, 'core/home.html', data)


class ContactView(FormView):
    form_class = ContactForm
    template_name = "core/contact_form.html"

    def get_success_url(self):
        return reverse_lazy("core-contact") + "?submited=true"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        context.update({
        "is_submited": self.request.GET.get("submited", "false") == "true"
        })

        return context

    def form_valid(self, form):
        form.send_mail()

        return super(ContactView, self).form_valid(form)


contact = ContactView.as_view()
