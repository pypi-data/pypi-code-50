import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class Vertical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
