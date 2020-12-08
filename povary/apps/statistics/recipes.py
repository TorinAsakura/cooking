# -*- coding: utf-8 -*-
import datetime

import pymongo


def recipes_coll():
	connection = pymongo.Connection()
	statistics_db = connection.statistic
	recipes = statistics_db.recipes
	return recipes

def recipe_added(recipe):
	recipes = recipes_coll()
	recipe_info = {
		"recipe_id": recipe.id,
		"author": recipe.author.username,
		"created": recipe.created.isoformat(),
		"pub_date": recipe.pub_date.isoformat(),
		"published": recipe.published,
		"action": "created",
	}
	object_id = recipes.insert(recipe_info)
	return object_id

def recipe_changed(old_instance, new_instance):
	field_list = ('created', 'pub_date', 'published', 'updated', 'title', 'description')
	changed_fields = {}
	for field in field_list:
		old_value = getattr(old_instance, field)
		new_value = getattr(new_instance, field)
		if old_value != new_value:
			if isinstance(old_value, datetime.datetime) or isinstance(old_value, datetime.date):
				print "it's date"
				old_value = old_value.isoformat()
				new_value = new_value.isoformat()
			changed_fields[field] = {
				"old_value": old_value,
				"new_value": new_value
			}
	if len(changed_fields) < 1:
		return False
	recipe_info = {
		"recipe_id": new_instance.id,
		"action": "changed",
		"changed_fields": changed_fields
	}
	recipes = recipes_coll()
	object_id = recipes.insert(recipe_info)
	return object_id
