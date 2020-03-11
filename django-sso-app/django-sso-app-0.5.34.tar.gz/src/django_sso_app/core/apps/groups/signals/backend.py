import logging

from django.contrib.auth.models import Group as GroupModel
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from ....permissions import is_staff
from ..models import Group
from ...profiles.models import Profile

logger = logging.getLogger('django_sso_app.core.apps.groups.signals')


@receiver(m2m_changed)
def signal_handler_when_user_is_added_or_removed_from_group(action, instance, pk_set, model, **kwargs):
    is_loaddata = getattr(instance, '__django_sso_app__loaddata', False)

    if model == Group and instance.__class__ == Profile:
        if not is_staff(instance.user):
            profile_updated = False

            if action == 'pre_add':
                profile_updated = True
                for pk in pk_set:
                    _group = Group.objects.get(id=pk)
                    logger.info('Profile "{}" entered group "{}"'.format(instance, _group))

            elif action == 'pre_remove':
                profile_updated = True
                for pk in pk_set:
                    _group = Group.objects.get(id=pk)
                    logger.info('Profile "{}" exited from group "{}"'.format(instance, _group))

            if profile_updated and not is_loaddata:
                    instance.update_rev(True)

