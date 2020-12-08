# -*- coding: utf-8 -*-
from haystack.query import SearchQuerySet


faceted_searchqueryset = SearchQuerySet().facet('cuisine')\
    .facet('age_limit').facet('taste').facet('eating_time')\
    .facet('complexity').facet('diet').facet('holiday')\
    .facet('preparation_method')

