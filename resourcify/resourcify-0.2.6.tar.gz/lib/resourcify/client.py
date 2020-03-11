import abc
import requests


class HTTPClientBase(metaclass=abc.ABCMeta):
    """
    HTTP API client
    """

    @abc.abstractmethod
    def request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Request function for resourcify

        HTTPResourceAccesor in ResourceDescriptor will use this function for
        HTTP request. It returns Response in 'requests' library.
        """
        raise NotImplementedError


class DatabaseClientBase(metaclass=abc.ABCMeta):
    """
    Database API client
    """

    # TODO(Yan): Not yet implemented
    pass


class ExternalClientBase(metaclass=abc.ABCMeta):
    """
    External library API client
    """

    # TODO(Yan): Not yet implemented
    pass


class HTTPClient(HTTPClientBase):

    def __init__(self, url: str):
        if not url:
            raise TypeError('HTTPCilent must have URL')

        self._endpoint = url
        self._headers = {} # type: dict

        self.session = requests.Session()

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str):
        self._endpoint = endpoint

    @property
    def headers(self) -> dict:
        return self._headers

    @headers.setter
    def headers(self, headers: dict):
        self._headers = headers

    def request(self, method: str, url: str, **kwargs: dict):
        url = self.endpoint + url
        headers = self.headers

        return self.session.request(method, url, headers=headers, **kwargs)
