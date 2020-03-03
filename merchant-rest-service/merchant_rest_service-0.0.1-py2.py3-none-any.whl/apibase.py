import requests
import hashlib
import requests


class ApiBase(object):
    """
    Base class for paga connect library
    """

    _CONTENT_TYPE = "application/json"
    _TEST_BASE_API_ENDPOINT = "https://beta.mypaga.com/"
    _LIVE_BASE_API_ENDPOINT = "https://mypaga.com"

    def __init__(self, principal, credentials, is_test_server, api_key):
        """

              args
              ----------
              principal : string
                  your public ID gotten from Paga
              credentials : string
                  your account password
              is_test_server : boolean
                  indicates whether application is in test or live mode
              """
        self.principal = principal
        self.credentials = credentials
        self.is_test_server = is_test_server
        self.api_key = api_key

    def _server_url(self):
        if self.is_test_server:
            return self._TEST_BASE_API_ENDPOINT
        else:
            return self._LIVE_BASE_API_ENDPOINT

    def _headers(self, generated_hash):

        return {
            "Content-Type": self._CONTENT_TYPE,
            'principal': self.principal,
            'Accept': 'application/json',
            'hash': generated_hash,
            'credentials': self.credentials
        }

    def _generate_hash(self, pattern):
        pattern = pattern + self.api_key
        init_hash = hashlib.sha512()
        init_hash.update(('%s' % pattern).encode('utf-8'))
        generated_hash = init_hash.hexdigest()
        return generated_hash

    def _post_request(self, method, url, generated_hash, body):

        response = requests.request(method=method, url=url,
                                    headers=self._headers(generated_hash),
                                    data=body)

        if response.status_code == 400:
            return response.status_code, False, response.text, None

        if response.status_code in [200, 201]:
            return response.text
        else:
            body = response.text
            return response.status_code, body
