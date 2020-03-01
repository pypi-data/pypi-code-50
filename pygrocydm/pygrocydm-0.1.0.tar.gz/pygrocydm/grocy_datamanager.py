from datetime import datetime

from .chore import CHORES_ENDPOINT, Chore
from .grocy_api_client import (DEFAULT_PORT_NUMBER, GrocyApiClient,
                               GrocyEntityList)
from .product import PRODUCTS_ENDPOINT, Product


class GrocyDataManager(object):
    def __init__(self, base_url, api_key, port: int = DEFAULT_PORT_NUMBER, verify_ssl=True):
        self.__api = GrocyApiClient(base_url, api_key, port, verify_ssl)

    def products(self) -> GrocyEntityList:
        cls = Product
        return GrocyEntityList(self.__api, cls, PRODUCTS_ENDPOINT)

    def chores(self) -> GrocyEntityList:
        cls = Chore
        return GrocyEntityList(self.__api, cls, CHORES_ENDPOINT)
