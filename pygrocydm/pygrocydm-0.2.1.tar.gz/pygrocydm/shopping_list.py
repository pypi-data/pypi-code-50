from datetime import datetime

from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_bool, parse_date, parse_float, parse_int

SHOPPING_LISTS_ENDPOINT = 'objects/shopping_lists'
SHOPPING_LIST_ENDPOINT = 'objects/shopping_list'


class ShoppingList(GrocyEntity):
    def __init__(self, parsed_json, api: GrocyApiClient):
        self.__id = parse_int(parsed_json.get('id'))
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))
        self.__endpoint = '{}/{}'.format(SHOPPING_LISTS_ENDPOINT, self.__id)
        super().__init__(api, self.__endpoint)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp


class ShoppingListItem(GrocyEntity):
    def __init__(self, parsed_json, api: GrocyApiClient):
        self.__id = parse_int(parsed_json.get('id'))
        self.__product_id = parse_int(parsed_json.get('product_id'), None)
        self.__note = parsed_json.get('note', None)
        self.__amount = parse_float(parsed_json.get('amount'), 0)
        self.__shopping_list_id = parse_int(
            parsed_json.get('shopping_list_id'))
        self.__done = parse_bool(parsed_json.get('done'), False)
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))
        self.__endpoint = '{}/{}'.format(SHOPPING_LIST_ENDPOINT, self.__id)
        super().__init__(api, self.__endpoint)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def product_id(self) -> int:
        return self.__product_id

    @property
    def note(self) -> str:
        return self.__note

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def shopping_list_id(self) -> int:
        return self.__shopping_list_id

    @property
    def done(self) -> bool:
        return self.__done

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp
