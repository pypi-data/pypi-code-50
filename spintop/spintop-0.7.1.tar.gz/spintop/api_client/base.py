import os

import requests 
import platform
import functools

from contextlib import contextmanager
from pprint import pformat
from json.decoder import JSONDecodeError
from uuid import uuid4

from functools import partial
from ..errors import SpintopException

from ..auth import AuthModule
from ..services.auth0 import Auth0Provider

from ..logs import _logger
from ..compat import VERSION
from ..storage import TEMP_DIR
from .tests_facade import SpintopAPIPersistenceFacade

logger = _logger('spintop-api')

TEMPORARY_DOWNLOAD_FOLDER = os.path.join(TEMP_DIR, '.spintop-api-download-cache')
if not os.path.exists(TEMPORARY_DOWNLOAD_FOLDER):
    os.makedirs(TEMPORARY_DOWNLOAD_FOLDER)
    
class SpintopClientError(SpintopException):
    pass

class SpintopAPIError(SpintopException):
    def __init__(self, resp):
        try:
            json = resp.json()
        except JSONDecodeError:
            json = {}
        
        error_type = json.get('error_type', 'UNKNOWN')
        error_messages = json.get('error_messages', {})
        messages_as_string = '\n\t'.join(['%s: %s' % (key, value) for key, value in error_messages.items()])
        
        if not messages_as_string:
            messages_as_string = json.get('error_message') # singular, the direct exception message
            
        message = f'Request {resp.request.method} {resp.url} A {resp.status_code} error of type "{error_type}" occured while contacting API.\n\t{messages_as_string}'
        
        super().__init__(message)

        self.error_type = error_type
        self.resp = resp

def refresh_if_fail_gen(auth_module):
    try:
        yield
    except SpintopAPIError as e:
        if e.resp.status_code == 401 and e.error_type in ('auth_token_verification_failed',) :
            # Attempt ONCE to refresh the credentials and retry.
            auth_module.refresh_credentials()
            yield
        else:
            raise

def SpintopAPISession(prefix, auth_module):
    if prefix is None:                                                                                                                                                                                                                                                                                                                             
        prefix = ""                                                                                                                                                                                                                                                                                                                                
    else:                                                                                                                                                                                                                                                                                                                                          
        prefix = prefix.rstrip('/')                                                                                                                                                                                                                                                                                                      

    def attempt_request(f, method, url, *args, **kwargs):
        if 'headers' not in kwargs: kwargs['headers'] = {}
        kwargs['headers'].update(auth_module.get_auth_headers())
        resp = f(method, prefix + url, *args, **kwargs)           
        if not resp.ok:
            raise SpintopAPIError(resp)
        return resp
    
    def new_request(prefix, *args, **kwargs):
        
        try:
            resp = attempt_request(*args, **kwargs)
        except SpintopAPIError as e:
            if e.resp.status_code == 401 and e.error_type in ('auth_token_verification_failed',) :
                # Attempt ONCE to refresh the credentials and retry.
                auth_module.refresh_credentials()
                resp = attempt_request(*args, **kwargs)
            else:
                raise
        return resp
    
    s = requests.Session()                                                                                                                                                                                                                                                                                                                     
    s.request = partial(new_request, prefix, s.request)                                                                                                                                                                                                                                                                                            
    return s  

class NoAuthModule(object):
    def get_auth_headers(self):
        return {}

    def refresh_credentials(self):
        raise NotImplementedError('Cannot refresh credentials without an auth module.')

class SpintopAPIAuthProvider(Auth0Provider):
    @functools.lru_cache(maxsize=128)
    def get_user_orgs(self, access_token):
        token_payload = self.jwt_verify(access_token)
        return token_payload.get('https://spinhub.ca/authorization', {}).get('groups', [])

class SpintopAPIClientModule(object):
    def __init__(self, api_url, selected_org_id=None, auth=None):
        self._session = None

        self.auth = auth
        
        self._selected_org_id = selected_org_id
        self.tests_facade = SpintopAPIPersistenceFacade(self)
        
        self._api_url = api_url
        self._user_info = None
        self._api_spec = None
        self._default_org = None
        self._machine = None
    
    @classmethod
    def init(cls, config, auth):
        return cls(
            api_url=lambda: config.get_selected_profile()['spintop_api_url'],
            auth=auth
        )

    @property
    def api_url(self):
        if callable(self._api_url):
            return self._api_url()
        else:
            return self._api_url

    @api_url.setter
    def api_url(self, value):
        self._session = None
        self._api_url = value

    @property
    def session(self):
        if not self._session:
            self._session = self.new_session()
        return self._session

    @property
    def user_info(self):
        if self._user_info is None:
            self._user_info = self.session.get(self.get_link('tenancy.user_info')).json()
        return self._user_info

    @property
    def api_spec(self):
        if self._api_spec is None:
            # Use a new session here, since we need api_spec to init auth during session retrival.
            self._api_spec = self.new_session().get('/api/').json()
        return self._api_spec
    
    @property
    def selected_org_id(self):
        if self._selected_org_id is None:
            possible_orgs = [org['key'] for org in self.user_info['organizations']]
            selected_org = possible_orgs[0]
            logger.info('No org specified, using the first defined by the API for this user: %s' % selected_org)
            self._selected_org_id = selected_org
        
        return self._selected_org_id

    @property
    def tests(self):
        return self.tests_facade

    def new_session(self):
        return SpintopAPISession(self.api_url, self.auth)
    
    def reset_session(self):
        self._session = None

    def test_private_endpoint(self):
        resp = self.session.get(self.get_link('core.private'))
        return resp

    def get_org_info(self, org_name):
        return self.session.get(self.get_link('tenancy.org_info', org_id=org_name)).json()

    def get_link(self, link_name, org_id=None, **kwargs):
        links = self.api_spec['_links']
        base_link = links[link_name]

        if '<org_id>' in base_link:
            if org_id is None:
                org_id = self.selected_org_id

            kwargs['org_id'] = org_id

        link = base_link
        for key, value in kwargs.items():
            link = link.replace(f'<{key}>', value)

        if '<' in link or '>' in link:
            raise SpintopClientError(f'Link {base_link!r} is missing placeholder values. Received {kwargs.keys()!r}')

        return link
        
        