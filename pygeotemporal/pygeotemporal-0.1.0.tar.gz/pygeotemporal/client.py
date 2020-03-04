"""
    Geostreams Client
    ~~~
    This module contains a basic client to interact with the Geostreams API.
"""


from builtins import object
import json
import logging
import time
import requests


class GeostreamsClient(object):
    """
    Client to Geostreams API to store connection information.

    The `path` parameter used by many of the methods in this class call a specific path relative to the host + "api".
    For example passing in "/version" for host "https://seagrant-dev.ncsa.illinois.edu/" will call
    "https://seagrant-dev.ncsa.illinois.edu/api/version". Make sure to include the slash at the beginning of
    the fragment.
    """
    logger = logging.getLogger(__name__)
    api_fragment = "/api"
    max_retries = 10
    call_timeout = 5

    def __init__(self, *args, **kwargs):
        """
        Create an instance of `GeostreamsClient`.

        :param string host: The root host url of the specific geostreaming API we are connecting to.
        :param string key: The API key used to write to the API. Set this or `username`/`password` below.
        :param string username: HTTP Basic Authentication username.
        :param string password: HTTP Basic Authentication password.
         """
        self.host = kwargs.get('host')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.user = {'identifier': self.username, 'password': self.password}

        login_url = self.host + "/api/authenticate"
        r = requests.post(login_url, json=self.user, headers={'Content-Type': 'application/json'})

        self.headers = {"x-auth-token": r.headers["x-auth-token"], "Content-Encoding": "application/json"}

    def version(self):
        """Return Geostreams version info."""
        url = self.host + self.api_fragment + "/version"
        self.logger.debug("GET %s", url)
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            try:
                json = r.json()
                self.logger.debug("Version: %s", json)
                return json
            except ValueError:
                self.logger.error("GET %s. Could not parse JSON. Status %s.", url, r.status_code)
                r.raise_for_status()
        else:
            r.raise_for_status()

    def get_json(self, path):
        """
        Call HTTP GET against `path`. This version returns a JSON object.

        :param path: Endpoint path relative to Geostreams api.
        :return: JSON from body of response
        :rtype: JSON
        :raises: `requests.HTTPError`
        """
        url = self.host + self.api_fragment + path
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        return r.json()

    def get(self, path):
        """
        Call HTTP GET against `path`. This version returns a `requests.Response` object.

        :param path: Endpoint path relative to Geostreams api.
        :return: Full response object so that we can check status on it and then retrieve the JSON body.
        :rtype: `requests.Response`
        :raises: `requests.HTTPError`
        """
        url = self.host + self.api_fragment + path
        try:
            return requests.get(url, headers=self.headers)
        except Exception as e:
            logging.exception("Error calling GET url %s: %s" % url, e.message)

    def get_retry(self, path):
        """
        Call HTTP GET against `path`. This version returns a `requests.Response` object. Useful in case of temporary
        network issues.

        :param path: Endpoint path relative to Geostreams api.
        :return: Full response object so that we can check status on it and then retrieve the JSON body.
        :rtype: `requests.Response`
        :raises: `requests.HTTPError`
        """
        url = self.host + self.api_fragment + path
        count = 0
        while True:
            try:
                if count > self.max_retries:
                    return None
                r = requests.get(url, headers=self.headers)
                count += 1
                if 200 <= r.status_code < 300:
                    return r.json()
                else:
                    logging.warning("Error calling GET url %s" % url)
                    logging.warning("Waiting %i seconds and will try again" % self.call_timeout)
                    time.sleep(self.call_timeout)
            except Exception as e:
                logging.exception("Error calling GET url %s: %s" % url, e.message)

    def post(self, path, content):
        """
        Call HTTP POST against `path` with `content` in body.

        :param path: Endpoint path relative to Geostreams api.
        :param content: Content to send as the body of the request.
        :return: Full response object so that we can check status on it and then retrieve the JSON body.
        :rtype: `requests.Response`
        :raises: `requests.HTTPError`
        """
        url = self.host + self.api_fragment + path

        try:
            k = requests.post(url, json=content, headers=self.headers)
            return k
        except Exception as e:
            self.logger.error("POST %s: %s", url, e.message)

    def put(self, path, content):
        """
        Call HTTP POST against `path` with `content` in body.

        :param path: Endpoint path relative to Geostreams api.
        :param content: Content to send as the body of the request.
        :return: Full response object so that we can check status on it and then retrieve the JSON body.
        :rtype: `requests.Response`
        :raises: `requests.HTTPError`
        """
        url = self.host + self.api_fragment + path

        try:
            k = requests.put(url, json=content, headers=self.headers)
            return k
        except Exception as e:
            self.logger.error("PUT %s: %s", url, e.message)

    def post_file(self, path, filename):
        """
        Call HTTP POST against `path` with `content` in body. Header with content-type is not required.

        :param path: Endpoint path relative to Geostreams api.
        :param content: Content to send as the body of the request.
        :return: Full response object so that we can check status on it and then retrieve the JSON body.
        :rtype: `requests.Response`
        :raises: `requests.HTTPError`
        """

        url = self.host + self.api_fragment + path

        try:
            return requests.post(url, files={"File": open(filename, 'rb')},
                                 headers=self.headers)
        except Exception as e:
            self.logger.error("POST %s: %s", (url, e.message))

    def post_retry(self, path, content):
        """
        Call HTTP POST against `path` with `content` in body. Retry up to a certain number of times if necessary. Useful
        in case of temporary network issues.

        :param path: Endpoint path relative to Geostreams api.
        :param content: Content to send as the body of the request.
        :return: Full response object so that we can check status on it and then retrieve the JSON body.
        :rtype: `requests.Response`
        :raises: `requests.HTTPError`
        """
        url = self.host + self.api_fragment + path
        count = 0
        while True:
            try:
                if count > self.max_retries:
                    return None
                r = requests.post(url, data=json.dumps(content), headers=self.headers)
                count += 1
                if 200 <= r.status_code < 300:
                    return r.json()
                else:
                    logging.warning("Error calling POST url %s" % url)
                    logging.warning("Waiting %i seconds and will try again" % self.call_timeout)
                    time.sleep(self.call_timeout)
            except Exception as e:
                logging.exception("Error calling POST url %s: %s" % url, e.message)

    def delete(self, path):
        """
        Call HTTP DELETE against `path`.

        :param path: Endpoint path relative to Geostreams api.
        :return: Full response object so that we can check status on it and then retrieve the JSON body.
        :rtype: `requests.Response`
        :raises: `requests.HTTPError`
        """
        url = self.host + self.api_fragment + path

        try:
            return requests.delete(url, headers=self.headers)
        except Exception as e:
            self.logger.error("DELETE %s: %s", url, e.message)

    def delete_retry(self, path):
        """
        Call HTTP DELETE against `path`. Retry up to a certain number of times if necessary. Useful in case of temporary
        network issues.

        :param path: Endpoint path relative to Geostream api.
        :return: Full response object so that we can check status on it and then retrieve the JSON body.
        :rtype: `requests.Response`
        :raises: `requests.HTTPError`
        """
        url = self.host + self.api_fragment + path
        count = 0
        while True:
            try:
                if count > self.max_retries:
                    return None
                r = requests.delete(url, headers=self.headers)
                count += 1
                if 200 <= r.status_code < 300:
                    return r.json()
                else:
                    logging.warning("Error calling DELETE url %s" % url)
                    logging.warning("Waiting %i seconds and will try again" % self.call_timeout)
                    time.sleep(self.call_timeout)
            except Exception as e:
                logging.exception("Error calling DELETE url %s: %s" % url, e.message)
