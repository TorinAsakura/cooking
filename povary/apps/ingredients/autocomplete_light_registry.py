import autocomplete_light
from ingredients.models import USAIngredient


class USAIngredientsAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name_rus', ]

autocomplete_light.register(USAIngredient, USAIngredientsAutocomplete)