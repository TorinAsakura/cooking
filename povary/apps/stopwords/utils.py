# -*- coding: utf-8 -*-
import re
import sys, os
# sys.path.append("/Users/igorpochechuev/Development/lineout/povary.ru/povary/apps")
# sys.path.append("/Users/igorpochechuev/Development/lineout/povary.ru/")
# os.environ['DJANGO_SETTINGS_MODULE'] = 'povary.settings'

from stopwords.models import StopWord
from pymorphy.django_conf import default_morph as morph


def replace_stopwords(text):	
	word_list = []
	stopword_list = []
	for stopword in StopWord.objects.filter(active=True):
		normalized = morph.normalize(stopword.stopword.upper())
		if not normalized:
			normalized = stopword.stopword.upper()
		if type(normalized) == set:
			normalized = [i for i in normalized][0]
		stopword_details = {
			"stopword": stopword.stopword,
			"replaceword": stopword.replaceword,
			"normalized": normalized
		}
		stopword_list.append(stopword_details)

	for word in text.split():
		normalized = morph.normalize(word.upper())
		if not normalized:
			normalized = word.upper()
		if type(normalized) == set:
			normalized = [i for i in normalized][0]
		word_details = {
			"word": word,
			"normalized": normalized
		}
		word_list.append(word_details)	
	result = []
	
	for word in word_list:
		replaced = False
		for stopword in stopword_list:			
			if word['normalized'].find(stopword['normalized']) >= 0:
				import ipdb; ipdb.set_trace()
				r = re.compile("(%s)" % stopword['normalized'], re.IGNORECASE)
				prepared_word = re.sub(r, stopword['replaceword'], word['word'])
				result.append(prepared_word)
				replaced = True
				break
		if not replaced:
			result.append(word['word'])
	return ' '.join(result)


# if __name__ == "__main__":
# 	from recipes.models import Recipe
# 	r = Recipe.objects.get(id=1)
# 	import time
# 	s_time = time.time()
# 	a = replace_stopwords(r.description)
