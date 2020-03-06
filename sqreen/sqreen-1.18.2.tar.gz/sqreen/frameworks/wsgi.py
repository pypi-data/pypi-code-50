# -*- coding: utf-8 -*-
# Copyright (c) 2016, 2017, 2018, 2019 Sqreen. All rights reserved.
# Please refer to our terms for more information:
#
#     https://www.sqreen.io/terms.html
#
""" Generic WSGI HTTP Request / Response stuff
"""
import logging
from itertools import chain

from ..utils import Iterable, Mapping, to_unicode_safe
from .base import BaseRequest, BaseResponse
from .ip_utils import get_real_user_ip

try:
    from Cookie import SimpleCookie
except ImportError:
    from http.cookies import SimpleCookie

try:
    from urllib.parse import parse_qs, quote
except ImportError:
    from urlparse import parse_qs
    from urllib import quote


LOGGER = logging.getLogger(__name__)


class WSGIRequest(BaseRequest):
    """ Helper around raw wsgi environ
    """

    def __init__(self, environ, storage=None):
        super(WSGIRequest, self).__init__(storage=storage)
        self.environ = environ

    @staticmethod
    def _parse_cookies(cookies):
        if not cookies:
            return {}

        cookie = SimpleCookie()
        cookie.load(cookies)

        return {key: cookie[key].coded_value for key in cookie.keys()}

    @property
    def query_params(self):
        """ Return parsed query string from request
        """
        raw_query = self.environ.get("QUERY_STRING", "")
        try:
            return parse_qs(raw_query)
        except Exception:
            LOGGER.warning(
                "Exception while parsing %s", raw_query, exc_info=True
            )
            return {}

    @property
    def form_params(self):
        # TODO: Reactivate reading the body
        return {}

    @property
    def cookies_params(self):
        return self._parse_cookies(self.environ.get("HTTP_COOKIES"))

    @property
    def query_params_values(self):
        """ Return only query values as a list
        """
        return list(chain.from_iterable(self.query_params.values()))

    @property
    def remote_addr(self):
        """Remote IP address."""
        return to_unicode_safe(self.get_raw_header("REMOTE_ADDR"))

    @property
    def raw_client_ip(self):
        return get_real_user_ip(
            self.remote_addr, self.environ.get("HTTP_X_FORWARDED_FOR", "")
        )

    @property
    def hostname(self):
        return to_unicode_safe(self.environ.get("HTTP_HOST", self.environ.get("SERVER_NAME")))

    @property
    def method(self):
        return to_unicode_safe(self.get_raw_header("REQUEST_METHOD"))

    @property
    def client_user_agent(self):
        return to_unicode_safe(self.get_raw_header("HTTP_USER_AGENT"))

    @property
    def referer(self):
        return to_unicode_safe(self.get_raw_header("HTTP_REFERER"))

    @property
    def scheme(self):
        return to_unicode_safe(self.get_raw_header("wsgi.url_scheme"))

    @property
    def server_port(self):
        return to_unicode_safe(self.get_raw_header("SERVER_PORT"))

    @property
    def remote_port(self):
        return to_unicode_safe(self.get_raw_header("REMOTE_PORT"))

    @property
    def path(self):
        return quote(self.environ.get("SCRIPT_NAME", "")) + quote(
            self.environ.get("PATH_INFO", "")
        )

    @property
    def raw_headers(self):
        return self.environ

    @property
    def view_params(self):
        return {}

    @property
    def json_params(self):
        return {}


class WSGIResponse(BaseResponse):
    """Helper around raw WSGI response."""

    def __init__(self, status, response_headers={}, body=None):
        self.status = status
        self.body = body
        if isinstance(response_headers, Mapping):
            self.headers = response_headers
        elif isinstance(response_headers, Iterable):
            self.headers = dict(response_headers)
        else:
            raise ValueError("Unknown WSGI response header type")

    @property
    def status_code(self):
        try:
            status = self.status
            if isinstance(self.status, bytes):
                status = status.decode("latin_1")
            return int(status.split(" ", 1)[0])
        except Exception:
            LOGGER.debug("cannot parse HTTP status", exc_info=True)
            return None

    @property
    def content_type(self):
        return self.headers.get("Content-Type")

    @property
    def content_length(self):
        try:
            return int(self.headers.get("Content-Length"))
        except (ValueError, TypeError):
            return None
