import logging

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

from ....utils import set_session_key
from ....permissions import is_staff

logger = logging.getLogger('django_sso_app.core.apps.users.signals')


@receiver(user_logged_in)
def post_user_login(**kwargs):
    user = kwargs['user']

    if not is_staff(user):
        logger.debug('Users, "{}" LOGGED IN!!!'.format(user))

        request = kwargs['request']
        setattr(request, 'user', user)
        set_session_key(request, '__django_sso_app__user_logged_in', True)


@receiver(user_logged_out)
def post_user_logout(**kwargs):
    user = kwargs['user']

    if not is_staff(user):
        logger.debug('Users, "{}" LOGGED OUT!!!'.format(user))

        request = kwargs['request']
        setattr(request, 'user', user)
        set_session_key(request, '__django_sso_app__user_logged_out', True)
