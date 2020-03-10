from django.db import models


""" Model Manager """
# Model Manager for ApptwoCategoryModel.
class CategoryModelQuerySet(models.QuerySet):

    def filter_publish(self):
        return self.filter(status='publish')

class CategoryModelManager(models.Manager):

    def get_queryset(self):
        return CategoryModelQuerySet(self.model, using=self._db)

    def filter_publish(self):
        return self.get_queryset().filter_publish()


""" Model manager for ArticleModel. """
# model manager here.
class ArticleModelQuerySet(models.QuerySet):
    
    def filter_publish(self):
        return self.filter(status='publish')

    def is_promoted(self):
        return self.filter_publish().filter(is_promote=True)

    def is_trending(self):
        return self.filter_publish().filter(is_trend=True)

    def by_author(self, username):
        return self.filter_publish().filter(author__username=username)

    def by_promo(self):
        return self.filter_publish().filter(is_promote=True, is_trend=True)

class ArticleModelManager(models.Manager):

    def get_queryset(self):
        return ArticleModelQuerySet(self.model, using=self._db)

    def filter_publish(self):
        return self.get_queryset().filter_publish()

    def is_promoted(self):
        return self.get_queryset().is_promoted()

    def is_trending(self):
        return self.get_queryset().is_trending()

    def by_author(self, username):
        return self.get_queryset().by_author(username)

    def by_promo(self):
        return self.get_queryset().by_promo()
