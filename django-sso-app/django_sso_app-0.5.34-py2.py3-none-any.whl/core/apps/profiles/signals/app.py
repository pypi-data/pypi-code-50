import logging

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from ....permissions import is_staff
from ..utils import get_or_create_user_profile
from ..models import Profile

logger = logging.getLogger('django_sso_app.core.apps.profiles.signals')

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if kwargs['raw']:
        # https://github.com/django/django/commit/18a2fb19074ce6789639b62710c279a711dabf97
        return

    user = instance

    if not is_staff(user):
        if created:
            logger.debug('user created, creating profile')
            preset_sso_id = getattr(user, '__django_sso_app__profile__sso_id', None)

            if preset_sso_id is not None:
                logger.debug('preset_sso_id "{}"'.format(preset_sso_id))

                preset_sso_rev = getattr(user, '__django_sso_app__profile__sso_rev', 0)

                logger.debug('preset_sso_rev "{}"'.format(preset_sso_rev))

                profile = get_or_create_user_profile(instance, Profile, {
                    'sso_id': preset_sso_id,
                    'sso_rev': preset_sso_rev
                }, commit=True)

            else:
                profile = get_or_create_user_profile(instance, Profile, commit=True)

            logger.debug('new profile created "{}"'.format(profile))

            # refreshing user instance
            instance.sso_app_profile = profile
