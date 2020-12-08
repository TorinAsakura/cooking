# -*- coding: utf-8 -*-
from django.contrib import admin

from competitions.models import Competition, CompetitionCategory, CompetitionRequest, \
    MainPageCompetition, CompetitionVote
from sorl.thumbnail.admin import AdminImageMixin
from competitions.models import CompetitionTermStep, CompetitionPrizes, CompetitionSponsors


class CompetitionRequestInline(admin.TabularInline):
    model = CompetitionRequest


class CompetitionTermStepInline(AdminImageMixin, admin.TabularInline):
    model = CompetitionTermStep
    extra = 1


class CompetitionPrizesInline(AdminImageMixin, admin.TabularInline):
    model = CompetitionPrizes
    extra = 1


class CompetitionSponsorsInline(AdminImageMixin, admin.TabularInline):
    model = CompetitionSponsors
    extra = 1


class CompetitionAdmin(admin.ModelAdmin):
    inlines = (CompetitionRequestInline, CompetitionTermStepInline, CompetitionPrizesInline, CompetitionSponsorsInline)
    prepopulated_fields = {"slug": ("title", )}
    list_display = (
    "title", "category", "author", "voting_enabled", "visits_num",
    "requests_num", "published", "image")
    fieldsets = (
    (None, {
    'fields': (
    'title', 'slug', 'category', 'author', 'terms', 'description',
    "image")
    }),
    (u'Временные рамки', {
    'fields': ('start_date', 'end_date'),
    }),
    (u'Голосование', {
    'classes': ('wide',),
    'fields': ('voting_start', 'voting_end', 'voting_enabled')
    }),
    )

    def requests_num(self, obj):
        return obj.competition_requests.all().count()

    requests_num.short_description = "Количество заявок"


class CompetitionCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_display = ("title", "competition_num", "published")

    def competition_num(self, obj):
        return obj.competitions.all().count()

    competition_num.short_description = "Количество конкурсов"


class CompetitionRequestAdmin(admin.ModelAdmin):
    pass


class MainPageCompetitionAdmin(admin.ModelAdmin):
    raw_id_fields = ('competition',)


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(CompetitionCategory, CompetitionCategoryAdmin)
admin.site.register(CompetitionRequest, CompetitionRequestAdmin)
admin.site.register(MainPageCompetition, MainPageCompetitionAdmin)
admin.site.register(CompetitionVote)