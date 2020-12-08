# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from django.contrib.gis.utils import GeoIP
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType

from django_countries.fields import Country
from file_resubmit.admin import AdminResubmitMixin
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

from master_class.models import CategoryMC, SubCategoryMC, MasterClass, MCTool, MCStep, Ingredient
from master_class.forms import MasterClassForm
from tags.models import Tag
from comments.models import Comment


class IngredientInline(admin.TabularInline):
	model = Ingredient
	raw_id_fields = ('ingredient_info', )


class MCStepInline(AdminImageMixin, admin.TabularInline):
    model = MCStep
    extra = 1


class CommentInline(generic.GenericTabularInline):
    model = Comment
    extra = 1


class CategoryMCAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ('title', 'published', 'created', 'updated', 'direct_link', "visits_num")

	def direct_link(self, obj):
		link = "<a href='%s'>Смотреть</a>" % (obj.get_absolute_url())
		return link
	direct_link.short_description = "На сайте"
	direct_link.allow_tags = True


class SubCategoryMCAdmin(AdminImageMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	list_display = ('title', 'category_link', 'published', 'created', 'updated', 'direct_link', "visits_num")

	def direct_link(self, obj):
		link = "<a href='%s'>Смотреть</a>" % (obj.get_absolute_url())
		return link
	direct_link.short_description = "На сайте"
	direct_link.allow_tags = True

	def category_link(self, obj):
		link = "<a href='%s'>%s</a>" % (
			obj.category.get_absolute_url(),
			obj.category.title
		)
		return link
	category_link.short_description = "Категория"
	category_link.allow_tags = True

class MasterClassAdmin(AdminResubmitMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title", )}
	inlines = (MCStepInline, IngredientInline, CommentInline)
	form = MasterClassForm
	list_display = ("title","category", "subcategory", "author_link", "published",
		"pub_date", "created", "updated", "for_registered", "direct_link",
		"location", "ip_address", "comments_num", "visits_num", "thumbnail",
	)
	list_filter = ("category", "subcategory", "author", "for_registered")
	search_fields = ("title", "description")

	def category(self, obj):
		if(obj.category):
			return obj.category.title
		else:
			return "Нет"
	category.short_description = "Категории"

	def subcategory(self, obj):
		if(obj.subcategory):
			return obj.category.subcategory
		else:
			return "Нет"
	subcategory.short_description = "Подкатегории"

	def tag_list(self, obj):
		if obj.tags:
			return ','.join(obj.tags)
		else:
			return "Нет"
	tag_list.short_description = "Тэги"

	def direct_link(self, obj):
		link = "<a href='%s'>Смотреть</a>" % (obj.get_absolute_url())
		return link
	direct_link.short_description = "Ссылка"
	direct_link.allow_tags = True

	def author_link(self, obj):
		link = "<a href='%s'>%s</a>" % (
			reverse('admin:auth_user_change', args=(obj.author.id,)),
			obj.author.username
		)
		return link
	author_link.short_description = "Автор"
	author_link.allow_tags = True

	def location(self, instance):
		city = GeoIP().city(instance.ip_addr or "")
		if city:
			flag_url = Country(city['country_code']).flag
			city_name = city['city']
			location = """
			<img src="%s"/> %s
			""" % (flag_url, city_name)
			return mark_safe(location)
		return "Не определено"
	location.allow_tags = True
	location.short_description = "Местонах. по IP"

	def ip_address(self, obj):
			if not obj.ip_addr:
				return "Не определено"
			whois_url = "http://whois.domaintools.com/%s" % obj.ip_addr
			link = "<a href='%s'>%s</a>" % (whois_url, obj.ip_addr)
			return link
	ip_address.short_description = "IP"
	ip_address.allow_tags = True


	def comments_num(self, obj):
		recipe_contenttype = ContentType.objects.get_for_model(MasterClass)
		comments = Comment.objects.filter(content_type=recipe_contenttype, object_id=obj.id)
		return comments.count()
	comments_num.short_description = "Комментариев"


        def thumbnail(self, obj):
            if obj.image:
                im = get_thumbnail(obj.image, '150x150', crop='center', quality=80)
                img_location = """<img src="/media/%s" />""" % im.name
                return img_location
            return u''
        thumbnail.short_description = "Превью"
        thumbnail.allow_tags = True


class MCToolAdmin(AdminImageMixin, admin.ModelAdmin):
	pass


admin.site.register(CategoryMC, CategoryMCAdmin)
admin.site.register(SubCategoryMC, SubCategoryMCAdmin)
admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(MCTool, MCToolAdmin)
