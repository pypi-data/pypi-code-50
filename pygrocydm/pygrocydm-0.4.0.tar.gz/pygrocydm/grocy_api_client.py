import json
from datetime import datetime
from typing import Tuple
from urllib.parse import urljoin

import requests

from .utils import parse_date, parse_int

DEFAULT_PORT_NUMBER = 9192


class GrocyApiClient():
    def __init__(
                self, base_url, api_key,
                port: int = DEFAULT_PORT_NUMBER, verify_ssl=True):
        self.__base_url = f"{base_url}:{port}/api/"
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
        resp.raise_for_status()
        if len(resp.content) > 0:
            return resp.json()

    def post_request(self, endpoint: str, data: dict):
        req_url = urljoin(self.__base_url, endpoint)
        resp = requests.post(
            req_url, verify=self.__verify_ssl,
            headers=self.__headers,
            data=data)
        resp.raise_for_status()
        if len(resp.content) > 0:
            return resp.json()

    def delete_request(self, endpoint: str):
        req_url = urljoin(self.__base_url, endpoint)
        resp = requests.delete(
            req_url, verify=self.__verify_ssl,
            headers=self.__headers)
        resp.raise_for_status()

    def put_request(self, endpoint: str, data: dict):
        up_header = self.__headers.copy()
        up_header['accept'] = '*/*'
        up_header['Content-Type'] = 'application/json'
        req_url = urljoin(self.__base_url, endpoint)
        resp = requests.put(
            req_url, verify=self.__verify_ssl,
            headers=up_header,
            data=json.dumps(data))
        resp.raise_for_status()


class GrocyEntity():
    def __init__(self, api: GrocyApiClient, endpoint: str, parsed_json: json):
        self.__api = api
        self.__parsed_json = parsed_json
        self.__id = parse_int(parsed_json.get('id'))
        self.__endpoint = f"{endpoint}/{self.__id}"
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))

    def edit(self, data: dict):
        return self.__api.put_request(self.__endpoint, data)

    def delete(self):
        return self.__api.delete_request(self.__endpoint)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp


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
                [self.__cls(
                    self.__api, self.__endpoint,
                    response) for response in parsed_json])

    def add(self, item: dict):
        resp = self.__api.post_request(self.__endpoint, item)
        if resp:
            self.refresh()
            return parse_int(resp.get('created_object_id'))

    def search(self, search_str: str) -> Tuple[GrocyEntity]:
        endpoint = f"{self.__endpoint}/search/{search_str}"
        parsed_json = self.__api.get_request(endpoint)
        if parsed_json:
            return tuple(
                [self.__cls(
                    self.__api, self.__endpoint,
                    response) for response in parsed_json])
        return None

    @property
    def list(self) -> Tuple[GrocyEntity]:
        return self.__list
