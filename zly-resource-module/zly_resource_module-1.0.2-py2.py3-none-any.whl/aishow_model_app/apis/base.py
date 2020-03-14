# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import requests


class BaseAPI(object):

    API_BASE_URL = None

    def __init__(self, client=None):
        self._client = client

    def _get(self, url, params=None, **kwargs):
        from aishow_model_app.baseclient import BaseClient
        bsc = BaseClient()
        self._client = bsc
        if self.API_BASE_URL:
            kwargs['api_base_url'] = self.API_BASE_URL
        # return self._client.get(url, params, **kwargs)
        # return self._client.get(url=none, params={'select_type':select_type,'page':page,'limit':limit}, **kwargs)
        return self._client.get(url, params, **kwargs)

    def _post(self, url, data=None, params=None, **kwargs):
        from aishow_model_app.baseclient import BaseClient
        bsc = BaseClient()
        self._client = bsc
        if self.API_BASE_URL:
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.post(url, data, params, **kwargs)
