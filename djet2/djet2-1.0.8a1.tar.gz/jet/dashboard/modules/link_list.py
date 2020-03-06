from django import forms
from django.utils.translation import gettext_lazy as _

from .base import DashboardModule


class LinkListItemForm(forms.Form):
    url = forms.CharField(label=_('URL'))
    title = forms.CharField(label=_('Title'))
    external = forms.BooleanField(label=_('External link'), required=False)


class LinkListSettingsForm(forms.Form):
    layout = forms.ChoiceField(label=_('Layout'), choices=(('stacked', _('Stacked')), ('inline', _('Inline'))))


class LinkList(DashboardModule):
    """
    List of links widget.

    Usage example:

    .. code-block:: python

        from django.utils.translation import gettext_lazy as _
        from jet.dashboard import modules
        from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


        class CustomIndexDashboard(Dashboard):
            columns = 3

            def init_with_context(self, context):
                self.available_children.append(modules.LinkList)
                self.children.append(modules.LinkList(
                    _('Support'),
                    children=[
                        {
                            'title': _('Django documentation'),
                            'url': 'http://docs.djangoproject.com/',
                            'external': True,
                        },
                        {
                            'title': _('Django "django-users" mailing list'),
                            'url': 'http://groups.google.com/group/django-users',
                            'external': True,
                        },
                        {
                            'title': _('Django irc channel'),
                            'url': 'irc://irc.freenode.net/django',
                            'external': True,
                        },
                    ],
                    column=0,
                    order=0
                ))

    """

    title = _('Links')
    template = 'jet.dashboard/modules/link_list.html'

    #: Specify widget layout.
    #: Allowed values ``stacked`` and ``inline``.
    layout = 'stacked'

    #: Links are contained in ``children`` attribute which you can pass as constructor parameter
    #: to make your own preinstalled link lists.
    #:
    #: ``children`` is an array of dictinaries::
    #:
    #:     [
    #:          {
    #:              'title': _('Django documentation'),
    #:              'url': 'http://docs.djangoproject.com/',
    #:              'external': True,
    #:          },
    #:          ...
    #:     ]
    children = []
    settings_form = LinkListSettingsForm
    child_form = LinkListItemForm
    child_name = _('Link')
    child_name_plural = _('Links')

    def __init__(self, title=None, children=None, **kwargs):
        if children is None:
            children = []
        children = list(map(self.parse_link, children))
        kwargs.update({'children': children})
        super(LinkList, self).__init__(title, **kwargs)

    def settings_dict(self):
        return {
            'draggable': self.draggable,
            'deletable': self.deletable,
            'collapsible': self.collapsible,
            'layout': self.layout
        }

    def load_settings(self, settings):
        self.draggable = settings.get('draggable', self.draggable)
        self.deletable = settings.get('deletable', self.deletable)
        self.collapsible = settings.get('collapsible', self.collapsible)
        self.layout = settings.get('layout', self.layout)

    def store_children(self):
        return True

    def parse_link(self, link):
        if isinstance(link, (tuple, list)):
            link_dict = {'title': link[0], 'url': link[1]}
            if len(link) >= 3:
                link_dict['external'] = link[2]
            return link_dict
        elif isinstance(link, (dict,)):
            return link
