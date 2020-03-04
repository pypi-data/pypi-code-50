from datetime import datetime

from .grocy_api_client import GrocyApiClient, GrocyEntity
from .utils import parse_date, parse_int

BATTERIES_ENDPOINT = 'objects/batteries'


class Battery(GrocyEntity):
    def __init__(self, parsed_json, api: GrocyApiClient):
        self.__id = parse_int(parsed_json.get('id'))
        self.__name = parsed_json.get('name')
        self.__description = parsed_json.get('description', None)
        self.__used_in = parsed_json.get('used_in', None)
        self.__charge_interval_days = parse_int(
            parsed_json.get('charge_interval_days'),
            0)
        self.__row_created_timestamp = parse_date(
            parsed_json.get('row_created_timestamp'))
        self.__endpoint = '{}/{}'.format(BATTERIES_ENDPOINT, self.__id)
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
    def used_in(self) -> str:
        return self.__used_in

    @property
    def charge_interval_days(self) -> int:
        return self.__charge_interval_days

    @property
    def row_created_timestamp(self) -> datetime:
        return self.__row_created_timestamp
