import json
from typing import Tuple
from urllib.parse import urljoin

import requests

from .utils import parse_int

DEFAULT_PORT_NUMBER = 9192


class GrocyApiClient():
    def __init__(
                self, base_url, api_key,
                port: int = DEFAULT_PORT_NUMBER, verify_ssl=True):
        self.__base_url = '{}:{}/api/'.format(base_url, port)
        self.__api_key = api_key
        self.__verify_ssl = verify_ssl
        if self.__api_key == "demo_mode":
            self.__headers = {"accept": "application/json"}
        else:
            self.__headers = {
                "accept": "application/json",
                "GROCY-API-KEY": api_key
            }

    def get_request(self, endpoint: str):
        req_url = urljoin(self.__base_url, endpoint)
        resp = requests.get(
            req_url, verify=self.__verify_ssl, headers=self.__headers)
        if resp.status_code != 200:
            return None
        return resp.json()

    def post_request(self, endpoint: str, data: dict):
        req_url = urljoin(self.__base_url, endpoint)
        return requests.post(
            req_url, verify=self.__verify_ssl,
            headers=self.__headers,
            data=data)

    def delete_request(self, endpoint: str):
        req_url = urljoin(self.__base_url, endpoint)
        resp = requests.delete(
            req_url, verify=self.__verify_ssl,
            headers=self.__headers)
        if resp.status_code != 204:
            return resp.json()
        return True

    def put_request(self, endpoint: str, data: dict):
        up_header = self.__headers.copy()
        up_header['accept'] = '*/*'
        up_header['Content-Type'] = 'application/json'
        req_url = urljoin(self.__base_url, endpoint)
        resp = requests.put(
            req_url, verify=self.__verify_ssl,
            headers=up_header,
            data=json.dumps(data))
        if resp.status_code != 204:
            return resp.json()
        return True


class GrocyEntity():
    def __init__(self, api: GrocyApiClient, endpoint: str):
        self.__api = api
        self.__endpoint = endpoint

    def edit(self, data: dict):
        return self.__api.put_request(self.__endpoint, data)

    def delete(self):
        return self.__api.delete_request(self.__endpoint)


class GrocyEntityList():
    def __init__(self, api: GrocyApiClient, cls, endpoint: str):
        self.__api = api
        self.__cls = cls
        self.__endpoint = endpoint
        self.__list = None
        self.refresh()

    def refresh(self):
        parsed_json = self.__api.get_request(self.__endpoint)
        if parsed_json:
            self.__list = tuple(
                [self.__cls(response, self.__api) for response in parsed_json])

    def add(self, item: dict):
        resp = self.__api.post_request(self.__endpoint, item)
        if resp.status_code == 200:
            self.refresh()
            return parse_int(resp.json().get('created_object_id'))
        return resp

    @property
    def list(self) -> Tuple[GrocyEntity]:
        return self.__list
