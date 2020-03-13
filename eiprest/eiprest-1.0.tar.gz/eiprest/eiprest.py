#!/usr/bin/env python

import base64
import urllib
import json
import requests
from time import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from urllib.parse import quote_plus

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class EipRestException(RuntimeError):
  def __init__(self, arg):
    self.args = arg

class EipRest(object):

  @staticmethod
  def param2str(params):
    '''convert params to string format "key1=val1&key2=val2"'''
    
    if params is None:
      return ''
    elif type(params) is dict:
      tmp_params = [f'{k}={quote_plus(str(params[k]))}' for k in params.keys()]
      return '&'.join(tmp_params)
    elif type(params) is str:
      if params.startswith("{"): # params in json format
        try:
          d = json.loads(params)
          tmp_params = [f'{k}={quote_plus(str(params[k]))}' for k in d.keys()]
          return '&'.join(tmp_params)
        except:
          raise EipRestException("Bad parameter format: {}".format(params))
      else:
        return params
    else:
      raise EipRestException("Bad parameter type: {}".format(type(params)))

  @staticmethod
  def param2dict(params):
    '''convert string format "key1=val1&key2=val2" or json format to dict'''
    
    if params is None:
      return {}
    if type(params) is dict:
      return params

    if isinstance(params, str):
      if params.startswith("{"): # params in json format
        try:
          return json.loads(params)
        except:
          raise EipRestException("Bad parameter format: {}".format(params))
      else:
        dict_params = {}
        for param in params.split('&'):
          kv_pair = param.split('=')
          if len(kv_pair) != 2 or not kv_pair[0].isidentifier() or kv_pair[1] == '':
            raise EipRestException(f"Bad parameter format: {params}")
          key = kv_pair[0]
          value = kv_pair[1]
          if key in ('SELECT','WHERE','GROUPBY','ORDERBY','OPT_SELECT'):
            dict_params[key] = urllib.unquote_plus(value)
          else:
            dict_params[key] = value
            
        return dict_params
    else:
      raise EipRestException("Bad parameter type: {}".format(type(params)))

          
  def __init__(self, host, user, password, debug=False):
    self.debug = debug
    self.host = host
    self.user = user
    self.password = password
    self.prefix = 'https://{}/rest/'.format(host)
    self.headers = {'X-IPM-Username': base64.b64encode(user.encode()),
                    'X-IPM-Password': base64.b64encode(password.encode()),
                    'content-type': 'application/json'}
    self.last_url = ''
    self.resp = None
    self.exec_time = 0

  def getLastUrl(self):
    return self.last_url

  def getData(self):
    if self.resp is not None:
      try:
        data = json.loads(self.resp.content.decode())
      except ValueError:
        #json decoding failed
        data = None
    return data

  def show_result(self):
    if self.resp is not None:
      print("=========================")
      print("Response:")
      print("=========================")
      print(f"status code: {self.resp.status_code}")
      print(f"exec time: {self.exec_time} s")
      try:
        data = json.loads(self.resp.content.decode())
      except ValueError:
        #json decoding failed
        data = None
      if data is None:
        print("content size: 0kB")
        print("nb objects: 0")
      else:
        print(f"content size: {len(self.resp.content)/1024:.2f}kB")
        print(f"nb objects: {len(data)}")
        if self.debug:
          if type(data) is list:
            n = 1
            for d in data:
              print("--------------------------------------------")
              for k in d:
                print(f"{k} => {d[k]}")
              n += 1
          elif type(data) is dict:
            print("--------------------------------------------")
            for d in data:
              print(f"{d} => {data[d]}")
            print("----------")

  def query(self, method, service, params=None, payload=None):
    start = time()
    method = method.upper()
    url = self.prefix + service
    if method == 'GET':
      self.last_url = f"{method} {service} {self.param2str(params)}".strip()
      self.resp = requests.request(method, url,
                                   headers=self.headers,
                                   params=params,
                                   verify=False)
    elif method == 'OPTIONS':
      self.last_url = f"{method} {service}"
      self.resp = requests.request(method, url, headers=self.headers, verify=False)
    else:
      self.last_url = "{method} {service} {self.param2str(params)}".strip()
      if payload:
        self.last_url = f'{self.last_url} {payload}'
      self.resp = requests.request(method, url,
                                   headers=self.headers,
                                   params=params,
                                   data=payload,
                                   verify=False)
    self.exec_time = int(time() - start)

  def rpc(self, method, service, params=None, payload=None):
    start = time()
    method = method.upper()
    self.last_url = f"{method} {service} {self.param2str(params)}".strip()
    if payload:
      self.last_url = f'{self.last_url} {payload}'
    if self.debug:
      print(f"RPC: {self.last_url}")
    self.resp = requests.request(method,
                                 f"https://{self.host}/rpc/{service}",
                                 headers=self.headers,
                                 params=params,
                                 verify=False)
    self.exec_time = int(time() - start)
