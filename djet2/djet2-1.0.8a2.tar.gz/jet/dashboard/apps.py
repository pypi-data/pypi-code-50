from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class JetDashboardConfig(AppConfig):
    name = 'jet.dashboard'
    label = 'jet.dashboard'
    verbose_name = _('Jet Dashboard')

    # noinspection PyUnresolvedReferences
    def ready(self):
        from . import checks
