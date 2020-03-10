import datetime

from django import forms
from django.utils.translation import gettext_lazy as _

from .base import DashboardModule


class FeedSettingsForm(forms.Form):
    limit = forms.IntegerField(label=_('Items limit'), min_value=1)
    feed_url = forms.URLField(label=_('Feed URL'))


class Feed(DashboardModule):
    """
    Display RSS Feed entries with following information:
    entry title, date and link to the full version

    Usage example:

    .. code-block:: python

        from django.utils.translation import gettext_lazy as _
        from jet.dashboard import modules
        from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


        class CustomIndexDashboard(Dashboard):
            columns = 3

            def init_with_context(self, context):
                self.children.append(modules.Feed(
                    _('Latest Django News'),
                    feed_url='http://www.djangoproject.com/rss/weblog/',
                    limit=5,
                    column=0,
                    order=0
                ))

    """

    title = _('RSS Feed')
    template = 'jet.dashboard/modules/feed.html'

    #: URL of the RSS feed (may be changed by each user personally).
    feed_url = None

    #: Number if entries to be shown (may be changed by each user personally).
    limit = None
    settings_form = FeedSettingsForm
    ajax_load = True

    def __init__(self, title=None, feed_url=None, limit=None, **kwargs):
        kwargs.update({'feed_url': feed_url, 'limit': limit})
        super(Feed, self).__init__(title, **kwargs)

    def settings_dict(self):
        return {
            'feed_url': self.feed_url,
            'limit': self.limit
        }

    def load_settings(self, settings):
        self.feed_url = settings.get('feed_url')
        self.limit = settings.get('limit')

    def init_with_context(self, context):
        if self.feed_url is not None:
            try:
                import feedparser

                feed = feedparser.parse(self.feed_url)

                if self.limit is not None:
                    entries = feed['entries'][:self.limit]
                else:
                    entries = feed['entries']

                for entry in entries:
                    try:
                        entry.date = datetime.date(*entry.published_parsed[0:3])
                    except:
                        pass

                    self.children.append(entry)
            except ImportError:
                self.children.append({
                    'title': _('You must install the FeedParser python module'),
                    'warning': True,
                })
        else:
            self.children.append({
                'title': _('You must provide a valid feed URL'),
                'warning': True,
            })
