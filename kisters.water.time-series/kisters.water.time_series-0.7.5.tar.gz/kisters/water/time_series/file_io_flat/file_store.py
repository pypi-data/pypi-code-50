import json
import logging
import os
import re
from typing import Any, Iterable, List, Mapping, Union

import pyarrow.parquet as pq

from kisters.water.time_series.core.time_series import TimeSeries
from kisters.water.time_series.core.time_series_store import TimeSeriesStore
from kisters.water.time_series.file_io_flat.file_time_series import FlatFileTimeSeries

logger = logging.getLogger(__name__)


# TODO: standardize into a TSFormat
class FlatFileStore(TimeSeriesStore):
    """FileStore provides a TimeSeriesStore for your local time series data files

    Args:
        filename: The path to your time series data splited into
                  meta data <filename>.json and binary data <filename>.pq

    Examples:
        .. code-block:: python

            from kisters.water.file_io_flat import FlatFileStore
            fs = FlatFileStore('test_flat_buffer')
            ts = fs.get_by_path('validation/inner_consistency1/station1/H')
    """

    def __init__(self, filename: str):
        self.__filename_json = filename + ".json"
        if not os.path.isfile(self.__filename_json):
            raise FileNotFoundError("File " + os.path.abspath(self.__filename_json) + " does not exist")
        self.__filename_pq = filename + ".pq"
        if not os.path.isfile(self.__filename_pq):
            raise FileNotFoundError("File " + os.path.abspath(self.__filename_pq) + " does not exist")
        with open(filename + ".json", "r") as json_file:
            self.__meta_list = json.load(json_file)
        table = pq.read_table(self.__filename_pq)
        self.__df = table.to_pandas()
        self.__df["timestamp"] = self.__df.index
        self.__df.set_index(["tsPath", "timestamp"], inplace=True)
        self.__ts_list = []
        for meta in self.__meta_list:
            df_ts = self.__df.loc[meta["tsPath"]].copy()
            self.__ts_list.append(FlatFileTimeSeries(meta, df_ts))

    def create_time_series(
        self,
        path: str,
        display_name: str,
        attributes: Mapping[str, Any] = None,
        params: Mapping[str, Any] = None,
    ) -> TimeSeries:
        raise NotImplementedError

    def _get_time_series_list(
        self, ts_filter: str = None, id_list: List[int] = None, params: Mapping[str, Any] = None
    ) -> Iterable[TimeSeries]:
        ts_list = self._filter(self.__ts_list, ts_filter)
        ts_list = self._filter_id_list(ts_list, id_list)
        return ts_list

    @classmethod
    def _filter(cls, ts_list: Iterable[TimeSeries], ts_filter: str) -> Iterable[TimeSeries]:
        if ts_filter is None:
            return ts_list
        result = []
        exp = re.compile(
            ts_filter.replace(".", "\\.").replace("/", "\\/").replace("?", "\\?").replace("*", ".*")
        )
        for ts in ts_list:
            path = ts.path
            if exp.match(path):
                result.append(ts)
        return result

    @classmethod
    def _filter_id_list(cls, ts_list: Iterable[TimeSeries], id_list: Iterable[int]) -> Iterable[TimeSeries]:
        if id_list is None:
            return ts_list
        result = []
        for ts in ts_list:
            ts_id = ts.id
            if (ts_id is not None) and (ts_id in id_list):
                result.append(ts)
        return result

    def _get_time_series(
        self, ts_id: int = None, path: str = None, params: Mapping[str, Any] = None
    ) -> Union[TimeSeries, None]:
        if params is None:
            params = {"includeDataCoverage": True}
        ts_list = list(
            self._get_time_series_list(ts_filter=path, id_list=[ts_id] if ts_id else None, params=params)
        )
        if len(ts_list) == 0:
            raise KeyError("Requested TimeSeries does not exist.")
        else:
            return ts_list[0]
