from django.db import models
from django_tree_materialized.models import MPTree


class Tree(MPTree):
    name = models.CharField(max_length=200)
