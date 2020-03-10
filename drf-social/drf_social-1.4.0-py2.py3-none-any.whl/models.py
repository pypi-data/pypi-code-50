import enum

from django.db import models
from django.db.models import UniqueConstraint


class Providers(str, enum.Enum):
    Facebook = "Facebook"
    Google = "Google"
    Instagram = "Instagram"

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class AuthProvider(models.Model):
    provider = models.CharField(choices=((p, p) for p in Providers), max_length=10, null=False, blank=False)
    client_id = models.CharField(max_length=200, null=False, blank=False)
    client_secret = models.CharField(max_length=200, null=False, blank=False)
    scopes = models.TextField(default="[]", null=False, blank=False)

    class Meta:
        constraints = [UniqueConstraint(fields=("provider",), name="provider")]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        from drf_social.utils import load_providers
        load_providers()

    def __str__(self):
        return self.provider
