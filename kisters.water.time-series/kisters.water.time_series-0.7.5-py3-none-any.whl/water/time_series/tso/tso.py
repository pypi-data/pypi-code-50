import re
from typing import Any, Iterable, Mapping, Optional

import requests
from requests import HTTPError

from kisters.water.time_series.core.time_series import TimeSeries
from kisters.water.time_series.core.time_series_store import TimeSeriesStore, deprecated
from kisters.water.time_series.tso.tso_location import TSOLocation
from kisters.water.time_series.tso.tso_time_series import TSOTimeSeries


class TSOStore(TimeSeriesStore):
    """
    Class to provide a simple backend for TimeSeries.Online to retrieve time series data via REST interfaces.
    """

    def __init__(self, user: str, password: str, base_url: str, organisation: str = None):
        """
        Initialize login data and establish connection via TSO REST interface.

        Args:
            user: username for TimeSeriesOnline.
            password: password for the TimeSeriesOnline user.
            organisation: TimeSeriesOnline organization to access.
            base_url: TimeSeriesOnline base url.
        """
        super(TSOStore, self).__init__()
        self._user = user
        self._password = password
        self._base_url = base_url if base_url.endswith("/") else base_url + "/"
        self._connect(user, password)
        self._organization = organisation if organisation is not None else self.__get_organization()["id"]
        self.json_header = {"content-type": "application/json"}

    def _connect(self, user: str, password: str):
        login_credentials = {"userName": user, "password": password}
        self._session = requests.Session()
        self._session.post(self._base_url + "auth/login/", json=login_credentials)

    def __get_organization(self) -> Mapping:
        return self._session.get(self._base_url + "organizations/current").json()

    def _get_time_series(
        self, ts_id: str = None, path: str = None, params: Mapping[str, Any] = None
    ) -> TSOTimeSeries:
        """
            Method to return a TSO time series object.
        Args:
            ts_id: the ts id (e.g. "8a021695-96bb-484f-ba00-818edf2c1967").
            path: the ts path (e.g. "68/190/Bue/Cmd.P").
            params: the additional parameters which are passed to the REST API.

        Returns:
            The selected TimeSeries object with the id given.
        """
        try:
            ts = []
            if ts_id is not None:
                ts = self._get_time_series_list(id_list=[ts_id])
            elif path is not None:
                ts = self._get_time_series_list(ts_filter=path)
            ts = ts[0]
        except (HTTPError, IndexError):
            raise KeyError("Requested TimeSeries does not exist.")
        return ts

    @classmethod
    def _filter_by_pattern(cls, ts_list_json: Iterable[Mapping[str, Any]], ts_filter: str):
        filtered_list = []
        if ts_filter is not None:
            exp = re.compile(
                ts_filter.replace(".", "\\.").replace("/", "\\/").replace("?", "\\?").replace("*", ".*")
            )
            for ts in ts_list_json:
                path = ts.get("tsPath", "")
                if path == ts_filter or exp.match(str(path)):
                    filtered_list.append(ts)
            return filtered_list
        else:
            return ts_list_json

    @classmethod
    def _filter_by_id_list(cls, ts_list_json: Iterable[Mapping[str, Any]], id_list: Iterable[str] = None):
        filtered_list = []
        if ts_list_json is not None and id_list is not None:
            for item in ts_list_json:
                if item["id"] in id_list:
                    filtered_list.append(item)
            return filtered_list
        else:
            return ts_list_json

    def _get_time_series_list(
        self, ts_filter: str = None, id_list: Iterable[str] = None, params: Mapping[str, Any] = None
    ) -> Iterable[TimeSeries]:
        """
            Get a TSO time series list and return a list of (selected/filtered) TimeSeries objects (as json/dict's).
        Args:
            ts_filter: the filtering key for the time series JSON representation (masking the PATH of a single ts).
            id_list: the filtering keys [list] for the time series JSON representations (multiple ts selection).
            params: the additional parameters which are passed to the rest api.

        Returns:
            The list of TimeSeries objects corresponding to the ts_filter and id_list.
        """

        resource = self._session.get(
            self._base_url + "organizations/" + self._organization + "/timeSeries/", params=params
        )
        ts_list = resource.json()
        tso_list = []
        ts_list = self._filter_by_pattern(ts_list, ts_filter)
        ts_list = self._filter_by_id_list(ts_list, id_list)
        for dict_item in ts_list:
            tso_list.append(TSOTimeSeries(self, dict_item))
        return tso_list

    def get_locations_list(self, filter: dict = None):
        locations_url = self._base_url + f"organizations/{self._organization}/locations"
        loc_list = [TSOLocation(loc) for loc in self._session.get(locations_url, params=filter).json()]
        return loc_list

    def get_entity_list(
        self, entity_filter: str = None, entities_id: Iterable[int] = None, **kwargs
    ) -> Iterable[TSOLocation]:
        _filter = kwargs.get("filter", {})
        return self.get_locations_list(_filter)

    @deprecated(message="use delete_location instead")
    def elim_location(self, location_id):
        return self.delete_location(location_id)

    def delete_location(self, location_id):
        locations_url = self._base_url + f"organizations/{self._organization}/locations/{location_id}"
        loc_list = self._session.delete(locations_url)
        return loc_list

    def create_location_by_data_dict(self, location_dict: dict):
        return self.create_location(TSOLocation(location_dict))

    def create_location(self, location: TSOLocation):
        locations_url = self._base_url + f"organizations/{self._organization}/locations"
        resource = self._session.post(locations_url, data=location.to_json(), headers=self.json_header)
        return resource

    def get_location(self, location_id) -> Optional[TSOLocation]:
        url = f"{self._base_url}organizations/{self._organization}/locations/{location_id}"
        res = self._session.get(url)
        if res.status_code == 200:
            return TSOLocation(res.json())
        else:
            return None

    def get_entity(self, entity_path: str = None, entity_id: int = None, **kwargs) -> TSOLocation:
        entity = self.get_location(entity_id)
        if entity is None:
            raise KeyError
        return entity

    def create_time_series(self, data=None, **kwargs):
        resource = self._session.post(
            self._base_url + "organizations/" + self._organization + "/timeSeries/",
            data=data,
            headers=self.json_header,
        )
        return resource

    @deprecated(message="use create_time_series_from instead")
    def create_time_series_by_ts(self, ts, **kwargs):
        return self.create_time_series_from(ts, **kwargs)

    # TODO make this method return a TSOTimeSeries
    def create_time_series_from(self, copy_from: TSOTimeSeries, **kwargs):
        ts_url = f"{self._base_url}organizations/{self._organization}/timeSeries/"
        resource = self._session.post(ts_url, data=copy_from.to_json(), headers=self.json_header)
        return resource

    def write_ts_metadata(self, ts: TSOTimeSeries, md: dict):
        ts_url = f"{self._base_url}organizations/{self._organization}/timeSeries/{ts.id}"
        self._session.post(ts_url, )

    def write_time_series(self, ts: TSOTimeSeries, start=None, end=None, auto_create=False):
        ts_url = f"{self._base_url}organizations/{self._organization}/timeSeries/{ts.id}"
        response = self._session.post(ts_url, ts.to_json())
        return response

    @deprecated(message="use delete_time_series instead")
    def elim_time_series(self, ts: TSOTimeSeries):
        return self.delete_time_series(ts)

    def delete_time_series(self, ts: TSOTimeSeries):
        ts_url = self._base_url + f"organizations/{self._organization}/timeSeries/{ts.id}"
        return self._session.delete(ts_url)
