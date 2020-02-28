# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
湘财证券量化数据API接口 
Created on 2019/10/20
@author: Tushare
@group : https://tushare.pro
"""

import pandas as pd
import json
from functools import partial
import requests


class DataApi:

    __token = ''
    __http_qa = 'http://124.232.155.79:7172'
    __http_prd = 'http://140.206.243.220:7172'

    def __init__(self, token='', env='', server='', timeout=15):
        """
        Parameters
        ----------
        token: str
            API接口TOKEN，用于用户认证
        """
        if server:
            self.__http_url = server
        else:
            self.__http_url = self.__http_prd if env == 'prd' else self.__http_qa
        self.__token = token
        self.__timeout = timeout

    def query(self, api_name, fields='', **kwargs):
        req_params = {
            'api_name': api_name,
            'token': self.__token,
            'params': kwargs,
            'fields': fields
        }

        res = requests.post(self.__http_url, json=req_params, timeout=self.__timeout, headers={'Connection':'close'})
        result = json.loads(res.text)
        if result['code'] != 0:
            raise Exception(result['msg'])
        data = result['data']
        columns = data['fields']
        items = data['items']

        return pd.DataFrame(items, columns=columns)

    def __getattr__(self, name):
        return partial(self.query, name)
