# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


from recipes.views import RecipeWizard
from recipes.forms import RecipeFormStep1, RecipeFormStep2, RecipeFormStep3, IngredientForm
from django.forms.formsets import formset_factory


FORMS = [("first", RecipeFormStep1),
         ("second", formset_factory(IngredientForm)),
         ("third", RecipeFormStep3)]

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'povary.views.home', name='home'),
    # url(r'^povary/', include('povary.foo.urls')),
    
    url(r'add_recipe_to_box/(?P<recipe_slug>.*)/$', 'recipes.views.add_recipe_to_box', name='add_recipe_to_box'),
    url(r'^$', 'recipes.views.recipe_list', name='recipe_list'),
    url(r'^add/$', RecipeWizard.as_view(FORMS), name="recipe-add"),
    url(r'^cakes/$', 'recipes.views.cake_recipe_list', name='cake_recipe_list'),
    # url(r'^categories/(?P<category_slug>.*)/(?P<subcategory_slug>.*)/$',
    #     'recipes.views.subcategory_details',
    #     name='subcategory_details'),
    # url(r'^categories/(?P<category_slug>.*)/$', 'recipes.views.category_details', name='category_details'),
    url(r'^ajax/(?P<recipe_slug>.*)/set_portion/$', 'recipes.views.set_portion', name='set_portion'),
    url(r'^ajax/(?P<recipe_slug>.*)/wish/$', 'recipes.views.wish', name='wish'),
    url(r'^(?P<recipe_slug>.*)/$', 'recipes.views.recipe_details', name='recipe_details'),
)
