# -*- coding: utf-8 -*-
from celery.task import task


@task
def publish_recipe(recipe):
	from recipes.models import Recipe
	try:
		recipe = Recipe.objects.get(id=recipe.id)
		recipe.published=True
		recipe.save()
	except Recipe.DoesNotExist:
		pass