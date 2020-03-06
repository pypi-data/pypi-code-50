
from django.db import models

from tecdoc.managers import CrossManager


class Cross(models.Model):

    src_code = models.CharField(max_length=255, db_index=True)
    dst_code = models.CharField(max_length=255, db_index=True)

    objects = CrossManager()
