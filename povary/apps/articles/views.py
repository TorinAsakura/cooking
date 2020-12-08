# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponsePermanentRedirect, Http404

from articles.models import Article, ArticleCategory
from utils.utils import get_complex_paginator
from utils.utils import search
from tags.models import TaggedItem


def article_list(request):
    articles = Article.objects.filter(published=True, verified=True)

    q = request.GET.get('query', None)
    srt = request.GET.get('sort', 'pub_date')
    order = request.GET.get('order', 'down')

    if q:
        articles = search(q, 'body', articles)

    popular_articles_list = articles.filter(visits_num__gte=100)[:5]

    # if srt and srt != 'comm':
    #     articles = list(articles.order_by(
    #         srt if order == 'up' else '-'+srt))
    # else:
    #     articles = sorted(
    #         articles,
    #         key=lambda x: x.num_comments,
    #         reverse=True if order == 'up' else False)

    if srt:
        articles = list(articles.order_by(
            srt if order == 'up' else '-'+srt))

    articles_per_page = request.GET.get('per_page', 5)
    pages_per_part = 8
    page = request.GET.get('page', 1)
    part = request.GET.get('part', 1)

    categories = ArticleCategory.objects.all()

    articles_list, part_list, prev_base_page, next_base_page = \
        get_complex_paginator(articles, page, part, articles_per_page, pages_per_part)

    data = {
        "article_list": articles_list,
        "part_list": part_list,
        "prev_base_page": prev_base_page,
        "next_base_page": next_base_page,
        "articles_per_page": int(articles_per_page),
        'categories': categories,
        'popular_articles_list': popular_articles_list,
        'sort': srt,
        'order': order
    }

    return render(request, "articles/article_list.html", data)


def articlecategory_list(request):
    category_list = ArticleCategory.objects.filter(published=True)
    data = {
        "category_list": category_list
    }
    return render(request, "articles/articlecategory_list.html", data)


def articlecategory_details(request, articlecategory_slug):
    category = get_object_or_404(ArticleCategory, slug=articlecategory_slug, published=True)
    category.inc_visits()
    article_list = category.articles.filter(published=True, verified=True)
    data = {
        "category": category,
        "article_list": article_list
    }
    return render(request, "articles/articlecategory_details.html", data)


def article_details(request, article_slug):
    article = get_object_or_404(Article,
                                slug=article_slug,
                                published=True,
                                verified=True)

    article.inc_visits()
    categories = ArticleCategory.objects.all()
    popular_articles_list = Article.objects.filter(
        visits_num__gte=100,
        published=True,
        verified=True)[:5]

    similar_article = TaggedItem.objects.filter(
        tags__in=article.tags).distinct().prefetch_related('content_object')[:6]

    data = {
        'article': article,
        'categories': categories,
        'popular_articles_list': popular_articles_list,
        'similar_article': similar_article
    }
    return render(request, "articles/article_details.html", data)


def old_article(request):
    old_id = request.GET.get('id')
    if not old_id:
        raise Http404
    article = get_object_or_404(Article, old_id=old_id)
    return HttpResponsePermanentRedirect(article.get_absolute_url())
