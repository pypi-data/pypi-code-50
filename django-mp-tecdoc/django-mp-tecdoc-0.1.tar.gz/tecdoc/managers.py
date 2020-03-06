
from django.db import models

from tecdoc.querysets import CrossQuerySet


class CrossManager(models.Manager):

    def get_queryset(self):
        return CrossQuerySet(self.model, using=self._db)

    def find(self, query):
        return self.get_queryset().find(query)

    def codes(self):
        return self.get_queryset().codes()
