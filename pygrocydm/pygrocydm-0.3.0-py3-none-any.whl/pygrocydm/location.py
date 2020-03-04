from datetime import datetime

from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_bool, parse_date, parse_int

LOCATION_ENDPOINT = 'objects/locations'


class Location(GrocyEntity):
    def __init__(self, parsed_json, api: GrocyApiClient):
        self.__id = parse_int(parsed_json.get('id'))
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__is_freezer = parse_bool(parsed_json.get('is_freezer'), False)
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))
        self.__endpoint = '{}/{}'.format(LOCATION_ENDPOINT, self.__id)
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
    def is_freezer(self) -> bool:
        return self.__is_freezer

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp
