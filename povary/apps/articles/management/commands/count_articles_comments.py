from django.core.management import BaseCommand
from articles.models import Article


class Command(BaseCommand):
    help = ("count articles comments")
    args = ''

    def handle(self, *args, **options):
        for article in Article.objects.all():
            article.comments_num = article.num_comments
            article.save()