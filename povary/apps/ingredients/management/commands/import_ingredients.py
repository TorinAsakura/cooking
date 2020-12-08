# -*- coding: utf-8 -*-
import xlrd

from django.core.management.base import BaseCommand, CommandError

from ingredients.models import USAIngredient


class Command(BaseCommand):
	args = '<xls_file_full_path>'
	help = 'Please provide filename for xls.'

	def handle(self, xls_path=None, *args, **options):
		# xls_path = '/Users/igorpochechuev/Downloads/Abbrev.xls'
		if not xls_path:
			print self.args
			print self.help
			return
		updated_ingredients = 0
		created_ingredients = 0
		exists_ingredients = 0
		book = xlrd.open_workbook(xls_path)
		sheet = book.sheet_by_index(0)
		fields_names = [i.name for i in USAIngredient._meta.fields[1:10]]
		for row_num in range(sheet.nrows)[1:]:
			row = sheet.row(row_num)
			values = []
			for val in row:
				values.append(val.value if val.value != '' else 0.0)
			# model_elements = dict(zip(fields_names, values))
			model_elements = {
				"ndb_no": values[0],
				"short_description": values[1],
				"water": values[2],
				"energy": values[3],
				"protein": values[4],
				"lipid_total": values[5],
				"ash": values[6],
				"carbohydrt": values[7],
				"fiber_td": values[8],
				"sugar_total": values[9],
				"calcium": values[10],
				"iron": values[11],
				"magnesium": values[12],
				"phosphorus": values[13],
				"potassium": values[14],
				"sodium": values[15],
				"zinc": values[16],
				"copper": values[17],
				"manganese": values[18],
				"selenium": values[19],
				"vitamin_c": values[20],
				"thiamin": values[21],
				"riboflavin": values[22],
				"niacin": values[23],
				"panto_acid": values[24],
				"vitamin_b6": values[25],
				"folate_total": values[26],
				"folic_acid": values[27],
				"food_folate": values[28],
				"folate_dfe": values[29],
				"choline_total": values[30],
				"vitamin_b12": values[31],
				"vitamin_a_ui": values[32],
				"vitamin_a_rae": values[33],
				"retinol": values[34],
				"alpha_carot": values[35],
				"beta_carot": values[36],
				"beta_crypt": values[37],
				"lycopene": values[38],
				"lut_zea": values[39],
				"vitamin_e": values[40],
				"vitamin_d": values[41],
				"vi_vit_d_ui": values[42],
				"vitamin_k": values[43],
				"fa_sat": values[44],
				"fa_mono": values[45],
				"fa_poly": values[46],
				"cholestrl": values[47],
				"gm_wt1": values[48],
				"gmwt_desc1": values[49],
				"gmwt_2": values[50],
				"gmwt_desc2": values[51],
				"refuse_pct": values[52],
			}
			ingredient = USAIngredient.objects.filter(ndb_no=values[0])
			if len(ingredient) > 0:
				updatable_ingr = ingredient.filter(updatable=True)
				if len(updatable_ingr):
					update_models_elements = model_elements
					update_models_elements.pop('gmwt_desc1', None)
					update_models_elements.pop('gmwt_desc2', None)
					ingredient.update(**update_models_elements)
					updated_ingredients += 1
				else:
					exists_ingredients += 1
			else:
				ingredient = USAIngredient.objects.create(**model_elements)
				created_ingredients += 1
		print "Exists ingredients: %s" % (exists_ingredients)
		print "Was updated: %s" % (updated_ingredients)
		print "Was created: %s" % (created_ingredients)
