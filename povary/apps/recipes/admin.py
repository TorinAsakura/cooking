# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from sorl.thumbnail.admin import AdminImageMixin

from recipes.models import Recipe, Ingredient, Cuisine, Holiday, \
	RecipesBox, RecipeDescStep, PrepMethod, Season, WishedRecipes
from comments.models import Comment


class CommentInline(generic.GenericTabularInline):
    model = Comment
    extra = 1


class IngredientInline(admin.TabularInline):
	model = Ingredient
	raw_id_fields = ('ingredient_info', )


class RecipeDescStepInline(AdminImageMixin, admin.TabularInline):
    model = RecipeDescStep
    extra = 1


class RecipeAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	raw_id_fields = ('author', 'images', 'holiday', 'cuisine')
	inlines = (IngredientInline, CommentInline, RecipeDescStepInline)
	exclude = ('completed', )
	list_display = ('title', 'completed', 'published', 'author', 'pub_date',
		'comments_num', 'recipe_link', "visits_num"
	)
	search_fields = ("title", "description", "body")

	def comments_num(self, obj):
		recipe_contenttype = ContentType.objects.get_for_model(Recipe)
		comments = Comment.objects.filter(content_type=recipe_contenttype, object_id=obj.id)
		return comments.count()
	comments_num.short_description = "Количество комментариев"

	def recipe_link(self, obj):
		link = "<a href='%s'>Смотреть на сайте</a>" % (reverse("recipe_details", args=[obj.slug,]))
		return link
	recipe_link.short_description = "Ссылка на сайт"
	recipe_link.allow_tags = True	


class CuisineAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class RecipesBoxAdmin(admin.ModelAdmin):
	raw_id_fields = ('followers', 'recipe_list', 'author')
	list_display = ('title','author', 'followers_num', 'recipes_num', 'published')


	def followers_num(self, obj):
		return obj.followers.count()
	followers_num.short_description = "Количество фоловеров"

	def recipes_num(self, obj):
			return obj.recipe_list.count()
	recipes_num.short_description = "Количество рецептов"


class PrepMethodAdmin(AdminImageMixin, admin.ModelAdmin):
	pass


class SeasonAdmin(admin.ModelAdmin):
	pass


class HolidayAdmin(AdminImageMixin, admin.ModelAdmin):
	pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(RecipesBox, RecipesBoxAdmin)
admin.site.register(PrepMethod, PrepMethodAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(WishedRecipes)
