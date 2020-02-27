import json
from datetime import datetime
from typing import Any, Mapping, MutableMapping, Optional, TYPE_CHECKING

import dateutil
import pandas as pd

from kisters.water.time_series.core.time_series_attributes_mixin import TimeSeriesAttributesMixin
from kisters.water.time_series.core.time_series_cut_range_mixin import TimeSeriesCutRangeMixin
from kisters.water.time_series.core.time_series_item_mixin import TimeSeriesItemMixin
from kisters.water.time_series.core.time_series_store import TimeSeries, deprecated
from kisters.water.time_series.tso.tso_location import TSOLocation

if TYPE_CHECKING:
    from kisters.water.time_series.tso.tso import TSOStore


class TSOTimeSeries(TimeSeriesItemMixin, TimeSeriesAttributesMixin, TimeSeriesCutRangeMixin, TimeSeries):
    """
    Class for TimeSeries.Online (TSOStore) TimeSeries objects
    """

    def __init__(self, tso: "TSOStore", ts_json: MutableMapping[str, Any]):
        super(TSOTimeSeries, self).__init__()
        self.__TSO = tso
        self.__data = ts_json

    @property
    def id(self):
        return self.__data["id"] if "id" in self.__data else None

    @property
    def creation_time(self):
        return self.__data.get("creationTime")

    @property
    def creator(self):
        return self.__data.get("creator")

    @property
    def edit_time(self):
        return self.__data.get("editTime")

    @property
    def editor(self):
        return self.__data.get("editor")

    @property
    def coverage_from(self) -> Optional[datetime]:
        if self.__data.get("dataFrom") is None:
            return None
        try:
            c_f = datetime.fromtimestamp(self.__data["dataFrom"] / 1e3)
        except (OverflowError, OSError, TypeError):
            c_f = dateutil.parser.parse(self.__data["dataFrom"])
        return c_f

    @property
    def coverage_until(self) -> Optional[datetime]:
        if self.__data.get("dataTo") is None:
            return None
        try:
            c_u = datetime.fromtimestamp(self.__data["dataTo"] / 1e3)
        except (OverflowError, OSError, TypeError):
            c_u = dateutil.parser.parse(self.__data["dataTo"])
        return c_u

    @property
    def origin_node_id(self):
        return self.__data.get("originNodeId")

    @property
    def location(self) -> TSOLocation:
        return self.__TSO.get_location(self.__data["locationId"])

    @property
    def location_id(self) -> str:
        return self.__data.get("locationId")

    @property
    def path(self) -> str:
        return self.__data.get("tsPath")

    @property
    def short_name(self) -> str:
        short_name = self.path.split("/")[-1:][0]  # rsplit("/", -1)
        return short_name

    @property
    def name(self) -> str:
        # NEXT: check _safe_meta correspondence; recursion errors => workaround @mrd: / @rs: acceptable?
        return self.__data.get("name")

    @property
    def description(self):
        return self.__data.get("description")

    @property
    def variable(self):
        return self.__data.get("variable")

    @property
    def unit(self):
        return self.__data.get("unit")

    @property
    def resolution(self):
        return self.__data.get("resolution")

    @property
    def exchange_id(self):
        return self.__data.get("exchangeID")

    @property
    def remark(self):
        return self.__data.get("remark")

    @property
    def tags(self):
        return self.__data.get("tags")

    @property
    def metadata(self):
        if self.__data["metadata"]:
            return self.__data["metadata"]
        else:
            return None

    @metadata.setter
    def metadata(self, metadata):
        self.__data["metadata"] = metadata

    @property
    def value_type(self):
        return self.__data.get("valueType")

    @property
    def standard_transformation(self):
        return self.__data.get("standardTransformation")

    @property
    def graph_aggregation_periods(self):
        return self.__data.get("graphAggregationPeriods")

    @property
    def graph_config(self):
        return self.__data.get("graphConfig")

    @property
    def storage_type(self):
        return self.__data.get("storageType")

    @property
    def configuration(self):
        return self.__data.get("configuration")

    @property
    def interpolation_type(self):
        return self.__data.get("interpolationType")

    @property
    def ts_data_service(self):
        return self.__data.get("tsDataService")

    @property
    def organization(self):
        return self.__data.get("organization")

    def _load_data_frame(
        self,
        start: datetime = None,
        end: datetime = None,
        params: Mapping[str, Any] = None,
        t0: datetime = None,
        dispatch_info: str = None,
        member: str = None,
    ) -> pd.DataFrame:
        url = (
            self.__TSO._base_url
            + "organizations/"
            + self.__data["organization"]
            + "/timeSeries/"
            + str(self.id)
            + "/data/"
        )
        params = {}
        if start is not None:
            params["from"] = start.isoformat()
        if end is not None:
            params["to"] = end.isoformat()
        r = self.__TSO._session.get(url, params=params)
        j = r.json()
        raw_data = pd.DataFrame(
            j.get("data", self.__data.get("data", None)),
            columns=j.get("columns", self.__data.get("columns", "timestamp,value")).split(","),
        )
        raw_data["timestamp"] = pd.to_datetime(raw_data["timestamp"], utc=True)
        raw_data = raw_data.set_index("timestamp")
        return raw_data

    def _raw_metadata(self):
        """
        :return: the metadata stored on the time series and location level
        """
        raw_metadata = self.__data
        r = self.__TSO._session.get(
            self.__TSO._base_url
            + "organizations/"
            + self.__data["organization"]
            + "/locations/"
            + self.__data["locationId"]
        )
        raw_metadata.update({"location": r.json()})
        return raw_metadata

    def __refresh(self):
        self.__data = self.__TSO._filter_by_id_list(
            self.__TSO._session.get(
                self.__TSO._base_url + "organizations/" + self.__TSO._organization + "/timeSeries/"
            ).json(),
            [str(self.id)],
        )[0]

    def write_data_frame(self, data_frame: pd.DataFrame, **kwargs):
        headers = {"content-type": "application/json"}
        newdata = []
        data_frame.dropna(inplace=True)
        for row in data_frame.iterrows():
            try:
                timestamp = row[0].isoformat()
            except AttributeError:
                timestamp = row[1]["dateTime"].isoformat()
            value = row[1]["value"]
            list = [timestamp, value]
            newdata.append(list)
        r = self.__TSO._session.put(
            self.__TSO._base_url
            + "organizations/"
            + self.__data["organization"]
            + "/timeSeries/"
            + str(self.id)
            + "/data",
            json=newdata,
            headers=headers,
        )
        if r.status_code == 401 and r.json()["message"] == "Not logged in":
            self.__TSO._connect(self.__TSO._user, self.__TSO._password)
            r = self.write_data_frame(data_frame, **kwargs)
        self.__refresh()
        return r

    @deprecated(message="use delete_time_series instead")
    def eliminate_ts(self):
        return self.delete_time_series()

    def delete_time_series(self):
        r = self.__TSO._session.delete(
            self.__TSO._base_url + "organizations/" + self.__data["organization"] + "/timeSeries/" + self.id
        )
        return r

    def to_dict(self):
        self_dict = {
            "id": self.id,
            "creationTime": self.creation_time,
            "creator": self.creator,
            "editTime": self.edit_time,
            "editor": self.editor,
            "dataFrom": self.coverage_from.isoformat() if self.coverage_from else None,
            "dataTo": self.coverage_until.isoformat() if self.coverage_until else None,
            "originNodeId": self.origin_node_id,
            "locationId": self.location.id,
            "tsPath": self.path,
            "name": self.name,
            "description": self.description,
            "variable": self.variable,
            "unit": self.unit,
            "resolution": self.resolution,
            "exchangeID": self.exchange_id,
            "remark": self.remark,
            "tags": self.tags,
            "metadata": self.metadata,
            "valueType": self.value_type,
            "standardTransformation": self.standard_transformation,
            "graphAggregationPeriods": self.graph_aggregation_periods,
            "configuration": self.configuration,
            "storageType": self.storage_type,
            "interpolationType": self.interpolation_type,
            "tsDataService": self.ts_data_service,
            "organization": self.organization,
        }
        return self_dict

    def to_json(self):
        def clean_dict(d):
            if not isinstance(d, dict):
                return d
            return {k: clean_dict(v) for k, v in d.items() if v is not None}

        return json.dumps(clean_dict(self.to_dict()))
