from datetime import datetime

from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_date, parse_int

QUANTITY_UNITS_ENDPOINT = 'objects/quantity_units'


class QuantityUnit(GrocyEntity):
    def __init__(self, parsed_json, api: GrocyApiClient):
        self.__id = parse_int(parsed_json.get('id'))
        self.__name = parsed_json.get('name')
        self.__name_plural = parsed_json.get('name_plural')
        self.__description = parsed_json.get('description', None)
        self.__plural_forms = parsed_json.get('plural_forms', None)
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))
        self.__endpoint = '{}/{}'.format(QUANTITY_UNITS_ENDPOINT, self.__id)
        super().__init__(api, self.__endpoint)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def name_plural(self) -> str:
        return self.__name_plural

    @property
    def plural_forms(self) -> str:
        return self.__plural_forms

    @property
    def description(self) -> str:
        return self.__description

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp
