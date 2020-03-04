from typing import Iterable, List, Optional, Union

import requests

from .auth import Authentication


class RESTClient:
    def __init__(self, url: str, authentication: Authentication = None):
        super().__init__()
        self._url = url.rstrip("/")
        self._authentication = authentication
        self._session = requests.Session()

    @property
    def url(self):
        return self._url

    def _construct_url(self, resource: Union[str, Iterable[str]]) -> str:
        if isinstance(resource, str):
            return "/".join((self.url, resource))
        return "/".join((self.url, *resource))

    def _add_auth_header(self, headers: Optional[dict] = None):
        if self._authentication:
            headers = headers or {}
            headers["Authorization"] = "Bearer {}".format(
                self._authentication.get_access_token()
            )
        return headers

    @staticmethod
    def _verify_response(response):
        if response.status_code == 422:
            raise ValueError(response.json())
        response.raise_for_status()

    def get(
        self,
        resource: Union[str, Iterable[str]],
        *,
        parameters: Optional[dict] = None,
        data: Optional[Union[dict, List[dict]]] = None,
    ) -> Union[dict, List[dict]]:
        """Get data located at a resource"""

        resp = self._session.get(
            self._construct_url(resource),
            params=parameters,
            json=data,
            headers=self._add_auth_header(),
        )
        self._verify_response(resp)
        return resp.json()

    def put(
        self,
        resource: Union[str, Iterable[str]],
        *,
        parameters: Optional[dict] = None,
        data: Optional[Union[dict, List[dict]]] = None,
    ):
        """Overwrite data located at a resource"""

        resp = self._session.put(
            self._construct_url(resource),
            params=parameters,
            json=data,
            headers=self._add_auth_header(),
        )
        self._verify_response(resp)
        return resp.json()

    def post(
        self,
        resource: Union[str, Iterable[str]],
        *,
        parameters: Optional[dict] = None,
        data: Optional[Union[dict, List[dict]]] = None,
    ):
        """Send data to a resource"""

        resp = self._session.post(
            self._construct_url(resource),
            params=parameters,
            json=data,
            headers=self._add_auth_header(),
        )
        self._verify_response(resp)
        return resp.json()

    def delete(
        self,
        resource: Union[str, Iterable[str]],
        *,
        parameters: Optional[dict] = None,
        data: Optional[Union[dict, List[dict]]] = None,
    ):
        """Delete data located at a resource"""

        resp = self._session.delete(
            self._construct_url(resource),
            params=parameters,
            json=data,
            headers=self._add_auth_header(),
        )
        self._verify_response(resp)
        return resp.json()
