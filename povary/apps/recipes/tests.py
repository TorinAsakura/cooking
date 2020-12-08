# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


# class RecipeAddTest(TestCase):
#     def test_recipe_adding_form(self):
#         response = self.client.get(reverse('recipe-add'))
#         self.assertEqual(response.status_code, 200)
#         step1_formdata = {
#         	"title": "Test title Recipe",
#         	"description": "Test description",
#         	"prepare_time_from": 10,
#         	"prepare_time_to": 30,
# 			"portion_num": 2
#         }
#         response = self.client.post(reverse('recipe-add'), step1_formdata)
#         import ipdb
#         ipdb.set_trace()
