import base64
import hashlib
import hmac
import json
import random
import re
import string
from urllib.parse import urljoin

from requests import Session, Response as BaseResponse

from .resources import SubscriptionProduct, SubscriptionCustomer, Subscription, CheckoutForm
from .pki_builder import PKIBuilder


class Iyzipy:
    def __init__(self, options: dict):
        self.base_url: str = options["base_url"]
        self.api_key: str = options["api_key"]
        self.secret_key: str = options["secret_key"]

        self.client = Client(self)

        self.subscription_product = SubscriptionProduct(self)
        self.subscription_customer = SubscriptionCustomer(self)
        self.subscription = Subscription(self)
        self.checkout_form = CheckoutForm(self)


class Response(dict):
    def __init__(self, res: BaseResponse):
        data = res.json()
        super().__init__(data)

        self.response = res

    @property
    def status_code(self):
        return self.response.status_code


class Client:
    RANDOM_STRING_SIZE = 8
    RE_SEARCH_V2 = r'/v2/'
    header = {
        "Accept": "application/json",
        "Content-type": "application/json",
        'x-iyzi-client-version': 'iyzipay-python-1.0.32'
    }

    def __init__(self, iyzipy: 'Iyzipy'):
        self.session = Session()
        self.iyzipy = iyzipy

    def get_url(self, url):
        return urljoin(self.iyzipy.base_url, url)

    def request(self, method, url, request_body_dict=None, pki=None):
        body_str = json.dumps(request_body_dict)
        header = self.get_http_header(url, body_str, pki)

        url = self.get_url(url)

        response = self.session.request(method, url, data=body_str, headers=header)

        return Response(response)

    def get_http_header(self, url, body_str=None, pki_string=None):
        random_str = self.generate_random_string(self.RANDOM_STRING_SIZE)
        self.header.update({'x-iyzi-rnd': random_str})
        if re.search(self.RE_SEARCH_V2, url, re.IGNORECASE) is not None:
            return self.get_http_header_v2(url, random_str, body_str)
        else:
            return self.get_http_header_v1(pki_string, random_str)

    def get_http_header_v1(self, pki_string, random_str=None):
        if pki_string is not None:
            self.header.update(
                {'Authorization': self.prepare_auth_string(random_str, pki_string)})
        return self.header

    def get_http_header_v2(self, url, random_str, body_str):
        url = url.split('?')[0]
        hashed_v2_str = self.generate_v2_hash(url, random_str, body_str)
        self.header.update(
            {'Authorization': 'IYZWSv2 %s' % hashed_v2_str})
        return self.header

    def generate_v2_hash(self, url, random_str, body_str):
        secret_key = bytes(self.iyzipy.secret_key.encode('utf-8'))
        msg = (random_str + url + body_str).encode('utf-8')

        hmac_obj = hmac.new(secret_key, digestmod=hashlib.sha256)
        hmac_obj.update(msg)
        signature = hmac_obj.hexdigest()
        authorization_params = [
            'apiKey:' + self.iyzipy.api_key,
            'randomKey:' + random_str,
            'signature:' + signature
        ]
        return base64.b64encode('&'.join(authorization_params).encode()).decode()

    def get_plain_http_header(self):
        return self.get_http_header_v1(None)

    def prepare_auth_string(self, random_str, pki_string):
        hashed = self.generate_hash(self.iyzipy.api_key, self.iyzipy.secret_key, random_str, pki_string)
        return self.format_header_string(self.iyzipy.api_key, hashed)

    @staticmethod
    def generate_random_string(size):
        return "".join(
            random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
            range(size))

    @staticmethod
    def generate_hash(api_key, secret_key, random_string, pki_string):
        hash_str = api_key + random_string + secret_key + pki_string
        hex_dig = hashlib.sha1(hash_str.encode()).digest()

        return base64.b64encode(hex_dig)

    @staticmethod
    def format_header_string(api_key, hashed):
        hashed = hashed.decode('utf-8')
        return 'IYZWS %s:%s' % (api_key, hashed)

    @staticmethod
    def resource_pki(request):
        return 'locale=' + request.get('locale', "") + \
               (',conversationId=' + request.get('conversationId') + ',' if request.get('conversationId') else ',')
