from dataclasses import dataclass, field
from logging import getLogger

from .tokens_api import TokenClient


logger = getLogger(__name__)


@dataclass
class TranslatorClient(TokenClient):
    """Client for querying the translation service."""

    translator_api_base: str = field(default=None)
    translate_endpoint: str = field(default=None)
    works_endpoint: str = field(default=None)
    uris_endpoint: str = field(default=None)
    titles_endpoint: str = field(default=None)

    def __post_init__(self):
        if self.translator_api_base:

            api_base = self.translator_api_base.rstrip('/')

            if not self.translate_endpoint:
                self.translate_endpoint = f'{api_base}/translate'
            if not self.works_endpoint:
                self.works_endpoint = f'{api_base}/works'
            if not self.uris_endpoint:
                self.uris_endpoint = f'{api_base}/uris'
            if not self.titles_endpoint:
                self.titles_endpoint = f'{api_base}/titles'

        super().__post_init__()

    def uri_to_id(self, uri, uri_scheme, uri_strict=False):
        """Query translator to convert book DOI to specified schema.

        Args:
            uri (str): URI to query against.
            uri_scheme (str): URI scheme to normalise to.
            uri_strict (bool): Output errors with ambiguous translation queries.

        Returns:
            list: URIs matching the schema specified.
        """
        if uri_scheme not in self._cache.get(uri, {}):
            params = {
                'uri': uri,
                'filter': f'uri_scheme:{uri_scheme}',
                'strict': uri_strict
            }
            response = self.get(self.translate_endpoint, params=params)

            if response.status_code != 200:
                logger.error(f"{response.json()['message']}: {uri}")
                return []

            uri_cache = self._cache.setdefault(uri, {})
            uri_cache[uri_scheme] = response.json()['data']

        return self._cache[uri][uri_scheme]

    def get_all_books(self):
        """Fetch all books stored in the translator."""

        filters = (
            'work_type:monograph,work_type:book,uri_scheme:info:doi,'
            'uri_scheme:urn:isbn,uri_scheme:http,uri_scheme:https'
        )
        response = self.get(self.works_endpoint, params={'filter': filters})

        if response.status_code != 200:
            raise ValueError(response.content.decode('utf-8'))

        return response.json()['data']

    def post_new_uri(self, work_uuid, uri):
        """Post new URI to the translator for a given work.

        Args:
            work_uuid (str): uuid of work to add new URI to.
            uri (str):  new URI to send.
        """
        data = {'UUID': work_uuid, 'URI': uri}
        self.post(self.uris_endpoint, json=data)

    def post_new_title(self, work_uuid, title):
        """Post new Title to the translator for a given work.

        Args:
            work_uuid (str): uuid of work to add new title to.
            title (dict):  new Uri to send, including UUID of work.
        """
        data = {'UUID': work_uuid, 'title': title}
        self.post(self.titles_endpoint, json=data)
