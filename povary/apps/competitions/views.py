# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from competitions.models import Competition, CompetitionRequest
from utils.utils import get_complex_paginator
from django.views.generic import DetailView, CreateView
from search.forms import RecipeSearchForm


def competition_list(request):
    competitions = Competition.objects.filter(
        published=True,
        end_date__gt=datetime.date.today()).order_by('start_date')

    ended_competitions = Competition.objects.exclude(
        id__in=competitions.values_list('id', flat=True))

    competitions_per_page = request.GET.get('per_page', 5)
    pages_per_part = 8
    page = request.GET.get('page')
    part = request.GET.get('part', 1)
    ended_page = request.GET.get('ended_page')
    ended_part = request.GET.get('ended_part', 1)

    competitions_list, part_list, prev_base_page, next_base_page = \
        get_complex_paginator(
            competitions,
            page if page else 1,
            part,
            competitions_per_page,
            pages_per_part
        )

    ended_competitions_list, ended_part_list, ended_prev_base_page, ended_next_base_page = \
        get_complex_paginator(
            ended_competitions,
            ended_page if ended_page else 1,
            ended_part,
            competitions_per_page,
            pages_per_part
        )

    data = {
        "ended": True if ended_page else False,
        "competition_list": competitions_list,
        "ended_competition_list": ended_competitions_list,
        "part_list": part_list,
        "prev_base_page": prev_base_page,
        "next_base_page": next_base_page,
        "ended_prev_base_page": ended_prev_base_page,
        "ended_next_base_page": ended_next_base_page,
        "ended_part_list": ended_part_list,
        "competitions_per_page": int(competitions_per_page),
    }
    return render(request, "competitions/competition_list.html", data)


class CompetitionDetailView(DetailView):

    model = Competition
    template_name = 'competitions/competition_details.html'
    context_object_name = 'competition'

    def get_context_data(self, **kwargs):
        context = super(CompetitionDetailView, self).get_context_data(**kwargs)
        opn = False

        competition = self.get_object()

        if competition.end_date.date() > datetime.date.today():
            opn = True
        context['open'] = opn
        context['search_form'] = RecipeSearchForm()
        return context


class CompetitionRequestCreate(CreateView):
    model = CompetitionRequest
    template_name = "competitions/competitionrequest_form.html"

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')