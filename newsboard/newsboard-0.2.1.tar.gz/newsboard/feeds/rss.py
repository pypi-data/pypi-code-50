from time import mktime
from datetime import datetime
import dateparser
import feedparser
from newsboard.feeds.base import BaseFeed


class RssFeed(BaseFeed):
    def _get_entry_url(self, entry):
        return entry['link']

    def _get_entry_date_key(self, entry):
        if entry.get('published_parsed'):
            return mktime(entry['published_parsed'])
        elif entry.get('published'):
            return dateparser.parse(entry['published'])

    def _get_entries(self, limit):
        feed = feedparser.parse(self.stream.remote_id)
        entries = feed['entries'][:limit]
        try:
            entries = sorted(entries, key=self._get_entry_date_key)
        except:
            pass
        return entries

    def _get_post_attrs(self, entry):
        # XXX: Do not take description from RSS
        attrs = {
            'title': entry['title'],
            # 'tags': [t['term'] for t in entry['tags']],
        }
        if entry.get('updated_parsed'):
            attrs['modified_time'] = datetime.fromtimestamp(mktime(entry['updated_parsed']))
        if entry.get('published_parsed'):
            attrs['published_time'] = datetime.fromtimestamp(mktime(entry['published_parsed']))
        if not attrs.get('published_time') and entry.get('published'):
            attrs['published_time'] = dateparser.parse(entry['published'])
        if entry.get('author'):
            attrs['author'] = entry['author']
        return attrs
