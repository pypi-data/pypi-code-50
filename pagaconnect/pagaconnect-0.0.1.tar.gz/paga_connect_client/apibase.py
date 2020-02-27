import requests
# import os
# import json
# from paga_connect_client import version
from base64 import b64encode


def _perform_basic_authorization(client_id, password):
    base64_string = b64encode(str.encode(client_id + ":" + password)).\
        decode("ascii")
    return base64_string


class ApiBase(object):
    """
    Base class for paga connect library
    """

    _CONTENT_TYPE = "application/json"
    _TEST_BASE_API_ENDPOINT = "http://localhost:8080"
    _LIVE_BASE_API_ENDPOINT = "https://mypaga.com"

    def __init__(self, client_id, password, is_test_server):
        """

              args
              ----------
              client_id : string
                  your public ID gotten from Paga
              password : string
                  your account password
              is_test_server : boolean
                  indicates whether application is in test or live mode
              """
        self.client_id = client_id
        self.password = password
        self.is_test_server = is_test_server

    def _server_url(self):
        if self.is_test_server:
            return self._TEST_BASE_API_ENDPOINT
        else:
            return self._LIVE_BASE_API_ENDPOINT

    def _headers(self):

        basic_auth = _perform_basic_authorization(self.client_id,
                                                  self.password)
        print(basic_auth)

        return {
            "Content-Type": self._CONTENT_TYPE,
            'Authorization': "Basic " + basic_auth,
        }

    def _headers_token(self, access_token):

        return {
            'Authorization': "Bearer " + access_token,
            'Accept': 'application/json'
        }

    def _post_request(self, method, url, access_token):

        if access_token is None:
            response = requests.request(method=method, url=url, headers=self._headers())
        else:
            response = requests.request(method=method, url=url, headers=self._headers_token(access_token))

        if response.status_code == 404:
            return response.status_code, False, "Request Not Found", None

        if response.status_code in [200, 201]:
            return response.text
        else:
            body = response.text
            return response.status_code, body
