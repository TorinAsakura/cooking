# -*- coding: utf-8 -*-
from django.template import RequestContext

from haystack.views import FacetedSearchView
from forms import MCSearchForm, FacetSearchForm
from master_class.models import MasterClass, CategoryMC
from ingredients.models import USAIngredient
from django.core.paginator import Paginator


class FacetRequestContext(RequestContext):
    def __init__(self, request, *args, **kwargs):
        super(FacetRequestContext, self).__init__(request, *args, **kwargs)
        self.update({"filter_form": FacetSearchForm(request.GET or None)})

