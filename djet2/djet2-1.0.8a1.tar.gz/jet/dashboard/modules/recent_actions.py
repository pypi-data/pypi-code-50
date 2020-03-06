from django import forms
from django.contrib.admin.models import LogEntry
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .base import DashboardModule


class RecentActionsSettingsForm(forms.Form):
    limit = forms.IntegerField(label=_('Items limit'), min_value=1)


class RecentActions(DashboardModule):
    """
    Display list of most recent admin actions with following information:
    entity name, type of action, author, date

    Usage example:

    .. code-block:: python

        from django.utils.translation import gettext_lazy as _
        from jet.dashboard import modules
        from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


        class CustomIndexDashboard(Dashboard):
            columns = 3

            def init_with_context(self, context):
                self.children.append(modules.RecentActions(
                    _('Recent Actions'),
                    10,
                    column=0,
                    order=0
                ))

    """

    title = _('Recent Actions')
    template = 'jet.dashboard/modules/recent_actions.html'

    #: Number if entries to be shown (may be changed by each user personally).
    limit = 10

    #: Specify actions of which models should be displayed. ``include_list`` is an array of string
    #: formatted as ``app_label.model``. Also its possible to specify all application models
    #: with * sign (e.g. ``auth.*``).
    include_list = None

    #: Specify actions of which models should NOT be displayed. ``exclude_list`` is an array of string
    #: formatted as ``app_label.model``. Also its possible to specify all application models
    #: with * sign (e.g. ``auth.*``).
    exclude_list = None
    settings_form = RecentActionsSettingsForm
    user = None

    def __init__(self, title=None, limit=10, **kwargs):
        kwargs.update({'limit': limit})
        super(RecentActions, self).__init__(title, **kwargs)

    def settings_dict(self):
        return {
            'limit': self.limit,
            'include_list': self.include_list,
            'exclude_list': self.exclude_list,
            'user': self.user
        }

    def load_settings(self, settings):
        self.limit = settings.get('limit', self.limit)
        self.include_list = settings.get('include_list')
        self.exclude_list = settings.get('exclude_list')
        self.user = settings.get('user', None)

    def init_with_context(self, context):
        def get_qset(list):
            qset = None
            for contenttype in list:
                try:
                    app_label, model = contenttype.split('.')

                    if model == '*':
                        current_qset = Q(
                            content_type__app_label=app_label
                        )
                    else:
                        current_qset = Q(
                            content_type__app_label=app_label,
                            content_type__model=model
                        )
                except:
                    raise ValueError('Invalid contenttype: "%s"' % contenttype)

                if qset is None:
                    qset = current_qset
                else:
                    qset = qset | current_qset
            return qset

        qs = LogEntry.objects

        if self.user:
            qs = qs.filter(
                user__pk=int(self.user)
            )

        if self.include_list:
            qs = qs.filter(get_qset(self.include_list))
        if self.exclude_list:
            qs = qs.exclude(get_qset(self.exclude_list))

        self.children = qs.select_related('content_type', 'user')[:int(self.limit)]
