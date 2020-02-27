import logging
from datetime import datetime
from typing import Any, Mapping, Union

import pandas as pd

from kisters.water.time_series.core import (
    TimeSeries,
    TimeSeriesAttributesMixin,
    TimeSeriesCutRangeMixin,
    TimeSeriesItemMixin,
)

logger = logging.getLogger(__name__)


class FlatFileTimeSeries(
    TimeSeriesItemMixin, TimeSeriesAttributesMixin, TimeSeriesCutRangeMixin, TimeSeries,
):
    def __init__(self, meta: Mapping[str, Any], df: pd.DataFrame):
        super().__init__()
        self.__meta = meta
        self.__df = df

    def __refresh_coverage(self):
        return

    @property
    def coverage_from(self) -> Union[datetime, None]:
        return self.__df.index[0]

    @property
    def coverage_until(self) -> Union[datetime, None]:
        return self.__df.index[-1]

    def _raw_metadata(self) -> Mapping[str, str]:
        return self.__meta

    def __format_metadata(self) -> Mapping[str, Any]:
        return self.__meta

    def _load_data_frame(
        self,
        start: datetime = None,
        end: datetime = None,
        params: Mapping[str, str] = None,
        t0: datetime = None,
        dispatch_info: str = None,
        member: str = None,
        _nrows: int = None,
    ) -> pd.DataFrame:

        if start is None and end is None:
            return self.__df
        if start is None:
            mask = self.__df.index <= end
        elif end is None:
            mask = self.__df.index >= start
        else:
            mask = (self.__df.index >= start) & (self.__df.index <= end)
        return self.__df.loc[mask]

    @property
    def path(self) -> str:
        return self.__meta["tsPath"]

    @classmethod
    def write_comments(cls, comments):
        logger.warning("write_comments not implemented. Ignoring {} comments".format(len(comments)))

    @classmethod
    def update_qualities(cls, qualities):
        logger.warning("update_qualities not implemented. Ignoring {} qualities".format(len(qualities)))

    def write_data_frame(
        self, data_frame: pd.DataFrame, start: datetime = None, end: datetime = None, **kwargs,
    ):
        logger.warning("write_data_frame not implemented. Ignoring")
