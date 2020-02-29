import requests

import bs4


class _WebContent(object):
    """ """

    def __init__(self, soup):
        self._soup = soup
        self.string = soup.string

    def _convert_collection(self, soup_results):
        return [_WebContent(x) for x in soup_results]

    def find_all(self, name, **kwargs):
        return self._convert_collection(self._soup.find_all(name, **kwargs))

    def get(self, key):
        return self._soup.get(key)


class RawWebContent(_WebContent):
    """ """

    def __init__(self):
        self.url = None
        self._soup = None

    def populate(self, url):
        """Populates the object with the HTML content from the supplied URL"""
        self.url = url
        self._soup = self._get_content()

    def _get_content(self):
        """Parses the website content."""
        r = requests.get(self.url)
        return bs4.BeautifulSoup(r.content, 'html.parser')
