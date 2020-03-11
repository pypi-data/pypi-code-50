import logging

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from ... import app_settings
from ...permissions import is_staff
from .utils import get_or_create_user_profile
from .models import Profile

logger = logging.getLogger('django_sso_app.core.apps.profiles')

User = get_user_model()


if app_settings.BACKEND_ENABLED:
    from django.contrib.auth.signals import user_logged_in
    from django.db.models.signals import pre_save

    @receiver(user_logged_in)
    def post_user_login(**kwargs):
        user = kwargs['user']

        if not is_staff(user):
            _profile = get_or_create_user_profile(user, Profile)
            # setattr(user, 'sso_app_profile', profile)

            logger.debug('Profiles, "{}" LOGGED IN!!!'.format(user))


    @receiver(pre_save, sender=Profile)
    def profile_pre_updated(sender, instance, **kwargs):
        """
        Profile model has been updated, updating rev
        """
        if kwargs['raw']:
            # https://github.com/django/django/commit/18a2fb19074ce6789639b62710c279a711dabf97
            return

        if not instance._state.adding:
            user = instance.user

            if not is_staff(instance.user):
                if getattr(user, '__django_sso_app__apigateway_update', False):
                    logger.debug('Profile has been updted by api gateway, skipping rev update')

                elif getattr(user, '__django_sso_app__creating', False):
                    logger.debug('Created, skipping rev update')

                else:
                    logger.debug('Profile model has been updated, updating rev')
                    instance.update_rev(False)


    @receiver(post_save, sender=Profile)
    def profile_updated(sender, instance, created, **kwargs):
        """
        Profile model has been updated, updating rev
        """
        if kwargs['raw'] or is_staff(instance.user):
            # https://github.com/django/django/commit/18a2fb19074ce6789639b62710c279a711dabf97
            return

        if not created and instance:  # if instance.pk:
            logger.debug('Profile model has been updated, refreshing')

            instance.refresh_from_db()

    # user

    @receiver(post_save, sender=User)
    def create_update_user_profile(sender, instance, created, **kwargs):
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

            else:
                logger.debug('user updated, updating profile')
                profile = get_or_create_user_profile(instance, Profile, commit=False)

                email_updated = hasattr(instance, '__django_sso_app__email_updated')
                password_updated = hasattr(instance, '__django_sso_app__password_updated') and not hasattr(instance, '__django_sso_app__password_hardened')
                user_active = instance.is_active and not instance.is_unsubscribed

                update_rev = False

                if email_updated:
                    update_rev = True
                    logger.info('User "{}" updated email'.format(instance))
                if password_updated:
                    update_rev = True
                    logger.info('User "{}" updated password'.format(instance))
                if not user_active:
                    update_rev = True
                    logger.info('User "{}" deactivated'.format(instance))

                # check __django_sso_app__password_hardened

                if update_rev:
                    logger.debug('Update rev by User signal while user fields have been updated')
                    profile.update_rev(True)  # updating rev

else:
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
