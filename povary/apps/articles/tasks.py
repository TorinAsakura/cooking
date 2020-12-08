# -*- coding: utf-8 -*-
from celery.task import task


@task
def publish_article(article):
	from articles.models import Article
	try:
		article = Article.objects.get(id=article.id)
		article.published=True
		article.save()
	except Article.DoesNotExist:
		pass