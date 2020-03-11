from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ... import app_settings


class DjangoSsoAppUserModelMixin:
    # username = models.CharField(_('username'), max_length=150, unique=True)  # django
    email = models.EmailField(_('email address'), blank=True)  # django
    ssn = models.CharField(_('social security number'), max_length=255, null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=255, null=True, blank=True)

    """
    def natural_key(self):
        key = self.sso_id
        if key is None:
            return getattr(self, app_settings.REQUIRED_USER_FIELDS[0])

        return key
    """

    def save(self, *args, **kwargs):
        super(DjangoSsoAppUserModelMixin, self).save(*args, **kwargs)

    def get_absolute_url(self):
        profile = self.get_sso_app_profile()
        if profile is not None:
            return reverse("django_sso_app_user:detail", kwargs={"sso_id": profile.sso_id})

    def get_sso_app_profile(self):
        return getattr(self, 'sso_app_profile', None)

    @property
    def sso_id(self):
        profile = self.get_sso_app_profile()
        if profile is not None:
            return profile.sso_id

        return None

    @property
    def sso_rev(self):
        profile = self.get_sso_app_profile()
        if profile is not None:
            return profile.sso_rev

        return 0

    @property
    def sso_app_profile__sso_id(self):
        return self.sso_id

    @property
    def is_unsubscribed(self):
        profile = self.get_sso_app_profile()
        if profile is not None:
            return profile.is_unsubscribed

        return not self.is_active
