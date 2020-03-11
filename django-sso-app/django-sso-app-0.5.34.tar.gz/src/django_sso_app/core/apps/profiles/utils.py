import logging

# import pyximport
# pyximport.install()

from django.contrib.auth import get_user_model

from ...utils import is_test_user
from ... import app_settings

User = get_user_model()

logger = logging.getLogger('django_sso_app.core.apps.profiles')


def get_or_create_user_profile(user, ProfileModel, initials=None, commit=True):
    logger.debug('get or create user profile')
    try:
        profile = user.sso_app_profile

    except ProfileModel.DoesNotExist:
        logger.info('User "{}" has no profile, creating one'.format(user))
        profile = ProfileModel(user=user)

        if initials is not None:
            profile = ProfileModel(**initials)

        if is_test_user(user):
            logger.info('User "{}" is TEST_USER, setting sso_id="{}"'.format(user, app_settings.TEST_USER_USERNAME))
            setattr(user, '__django_sso_app__creating', True)

            profile.sso_id = app_settings.TEST_USER_USERNAME

        user.sso_app_profile = profile

        if commit:
            profile.save()

    return profile


def update_profile(profile, update_object, commit=True):
    logger.info('Updating profile fields for "{}"'.format(profile))

    for f in app_settings.PROFILE_FIELDS + ('sso_rev', ):
        if hasattr(profile, f):
            new_val = update_object.get(f, None)
            if new_val is not None:
                setattr(profile, f, new_val)
                logger.debug('profile field updated "{}":"{}"'.format(f, new_val if f != 'password' else '*'))

    if commit:
        profile.save()

    return profile
