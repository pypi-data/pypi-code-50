# Copyright 2013, Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Author: Josef Skladanka <jskladan@redhat.com>

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
import inspect
import simplejson
import logging

try:
    # make strings unicode on Python 2
    str = unicode
except NameError:
    # except on Python 3 they already are, name 'unicode' is not defined
    pass

logger = logging.getLogger('resultsdb_api')
logger.addHandler(logging.NullHandler())

_KEEP = object()

def _fparams(expand_kwargs=True):
    """Gets the parameters of the function, from which _fparams is called
    and returns the list of params, minus `self`"""
    frame = inspect.currentframe().f_back
    args, varargs, keywords, values = inspect.getargvalues(frame)

    params = {}

    for key in args:
        if key == 'self':
            continue
        params[key] = values[key]

    if keywords:
        if expand_kwargs:
            for key, value in values[keywords].items():
                params[key] = value
        else:
            params[keywords] = values[keywords]

    return params


class ResultsDBapiException(Exception):

    def __init__(self, message='', response=None):
        ''':param response: :class:`requests.Response` object'''
        self.message = message
        self.response = response

    def __str__(self):
        return repr(self.message)


class _ResultsDBSession(requests.Session):
    def __resultsdb_raise_on_error(self, r):
        if r.ok:
            return r

        try:
            logger.warn('Received HTTP failure status code %s for request: %s',
                        r.status_code, r.url)
            raise ResultsDBapiException(
                '%s (HTTP %s)' % (r.json()['message'], r.status_code), r)
        except simplejson.JSONDecodeError as e:
            logger.debug('Could not parse JSON data: %s\n%s', e, r.text)
            raise ResultsDBapiException(
                '(HTTP %s)' % r.status_code, r)
        except KeyError:
            logger.debug('JSON data in unexpected format: %s\n%s', e, r.text)
            raise ResultsDBapiException('Unexpected JSON data (HTTP %s): %s' % (r.status_code, r.json()), r)

        raise ResultsDBapiException('Unknown Error', r)

    def get(self, *args, **kwargs):
        try:
            r = super(_ResultsDBSession, self).get(*args, **kwargs)
        except requests.exceptions.RetryError as e:
            try:
                message = e.message
            except AttributeError:
                message = str(e)
            raise ResultsDBapiException('Maximum number of retries exceeded: %s' % message, None)
        return self.__resultsdb_raise_on_error(r)

    def post(self, *args, **kwargs):
        try:
            r = super(_ResultsDBSession, self).post(*args, **kwargs)
        except requests.exceptions.RetryError as e:
            try:
                message = e.message
            except AttributeError:
                message = str(e)
            raise ResultsDBapiException('Maximum number of retries exceeded: %s' % message, None)
        return self.__resultsdb_raise_on_error(r)

class ResultsDBapi(object):

    def __init__(self, api_url, auth_token=None, max_retries=3, backoff_factor=1.0):
        # remove trailing slash(es), so we don't generate
        # urls with a double slash which breaks werkzeug
        # https://github.com/mitsuhiko/werkzeug/issues/491
        self.url = api_url.rstrip('/')
        self.auth_token = auth_token

        self._retry = Retry(
                total=max_retries,
                backoff_factor=backoff_factor,
                status_forcelist=(500, 502, 503, 504),
                method_whitelist=False # Enables POST retries
                )
        self._adapter = HTTPAdapter(max_retries=self._retry)
        self.session = _ResultsDBSession()
        self.session.mount("http://", self._adapter)
        self.session.mount("https://", self._adapter)

    def __prepare_params(self, params_all):
        params = {}
        for key, value in params_all.items():
            if value is None:
                continue
            if key == 'raw_params':
                continue

            # if a param's name ends with _like, we treat it as if :like filter should be applied
            #  for the rare case, where it really is supposed to be the name, user should provide
            #  it in the 'raw_params' dict
            if key.endswith('_like'):
                key = "%s:like" % key[:-len('_like')]

            if type(value) in (list, tuple):
                params[key] = ','.join([str(v) for v in value])
            else:
                params[key] = str(value)

        if 'raw_params' in params_all.keys() and params_all['raw_params']:
            raw_params = {
                key: str(value) for key, value in params_all['raw_params'].items()}
            params.update(raw_params)
        return params

    def create_group(self, uuid=None, ref_url=None, description=None):
        url = "%s/groups" % self.url
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = _fparams()
        data['_auth_token'] = self.auth_token
        r = self.session.post(url, data=json.dumps(data), headers=headers)

        return r.json()

    def update_group(self, uuid, ref_url=_KEEP, description=_KEEP):
        data = {}
        if ref_url is not _KEEP:
            data['ref_url'] = ref_url
        if description is not _KEEP:
            data['description'] = description
        if not data:
            return self.get_group(uuid)

        data['uuid'] = uuid
        data['_auth_token'] = self.auth_token

        url = "%s/groups" % self.url
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = self.session.post(url, data=json.dumps(data), headers=headers)

        return r.json()

    def get_group(self, uuid):
        url = "%s/groups/%s" % (self.url, uuid)
        r = self.session.get(url)

        return r.json()

    def get_groups(self, page=None, limit=None, description=None, description_like=None, uuid=None):
        url = "%s/groups" % self.url
        r = self.session.get(url, params=self.__prepare_params(_fparams()))

        return r.json()

    def create_result(self, outcome, testcase, groups=None, note=None, ref_url=None, **data):
        url = "%s/results" % self.url
        data = _fparams(expand_kwargs=False)
        data['_auth_token'] = self.auth_token
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = self.session.post(url, data=json.dumps(data), headers=headers)

        return r.json()

    def get_result(self, id):
        url = "%s/results/%s" % (self.url, id)
        r = self.session.get(url)

        return r.json()

    def get_results(self, page=None, limit=None, since=None, outcome=None, groups=None, testcases=None, testcases_like=None, raw_params=None, **kwargs):
        url = "%s/results" % self.url
        r = self.session.get(url, params=self.__prepare_params(_fparams()))

        return r.json()

    def create_testcase(self, name, ref_url=None):
        url = "%s/testcases" % self.url
        data = _fparams()
        data['_auth_token'] = self.auth_token
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = self.session.post(url, data=json.dumps(data), headers=headers)

        return r.json()

    def update_testcase(self, name, url=_KEEP):
        data = {}
        if ref_url is not _KEEP:
            data['ref_url'] = ref_url
        if not data:
            return self.get_testcase(name)

        data['name'] = name
        data['_auth_token'] = self.auth_token

        url = "%s/testcases" % self.url
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = self.session.post(url, data=json.dumps(data), headers=headers)

        return r.json()

    def get_testcase(self, name):
        url = "%s/testcases/%s" % (self.url, name)
        r = self.session.get(url)

        return r.json()

    def get_testcases(self, page=None, limit=None, name=None, name_like=None):
        url = "%s/testcases" % self.url
        r = self.session.get(url, params=self.__prepare_params(_fparams()))

        return r.json()
