# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""NYC Taxi yellow trip data."""

from datetime import datetime
from dateutil import parser
from typing import Optional, List

from ._opendataset_factory import TabularOpenDatasetFactory
from .accessories.time_data import TimePublicData
from .dataaccess._nyc_tlc_yellow_blob_info import NycTlcYellowBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor
from .dataaccess.dataset_partition_prep import prep_partition_puYear_puMonth
from .dataaccess.pandas_data_load_limit import PandasDataLoadLimitToMonth
from .environ import SparkEnv, PandasEnv

from multimethods import multimethod


class NycTlcYellow(TimePublicData, TabularOpenDatasetFactory):
    """Represents the NYC Taxi & Limousine Commission yellow taxi trip public dataset.

    The yellow taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up
    and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported
    passenger counts. For more information about this dataset, including column descriptions, different ways
    to access the dataset, and examples, see `NYC Taxi & Limousine Commission - yellow taxi trip
    records <https://azure.microsoft.com/services/open-datasets/catalog/
    nyc-taxi-limousine-commission-yellow-taxi-trip-records/>`_ in the Microsoft Azure Open Datasets catalog.

    .. remarks::

        The example below shows how to access the dataset.

        .. code-block:: python

            from azureml.opendatasets import NycTlcYellow
            from dateutil import parser

            end_date = parser.parse('2018-06-06')
            start_date = parser.parse('2018-05-01')
            nyc_tlc = NycTlcYellow(start_date=start_date, end_date=end_date)
            nyc_tlc_df = nyc_tlc.to_pandas_dataframe()

        For backwards compatibility, the ``filter`` method can also be used to return a dataframe with results between
        a start and end date (inclusive). However, the pattern with ``to_pandas_dataframe`` is recommended.

        .. code-block:: python

            from azureml.opendatasets import NycTlcYellow
            from azureml.opendatasets import environ
            from dateutil import parser

            end_date = parser.parse('2018-06-06')
            start_date = parser.parse('2018-05-01')
            NycTlcYellow.env = environ.PandasEnv()
            nyc_tlc_df = NycTlcYellow().filter(environ.PandasEnv(), start_date, end_date)

    :param start_data: The date at which to start loading data, inclusive. If None, the ``default_start_date``
        is used.
    :type start_data: datetime
    :param end_data: The date at which to end loading data, inclusive. If None, the ``default_end_date``
        is used.
    :type end_data: datetime
    :param cols: A list of columns names to load from the dataset. If None, all columns are loaded. For
        information on the available columns in this dataset, see `NYC Taxi & Limousine Commission -
        yellow taxi trip records <https://azure.microsoft.com/services/open-datasets/catalog/
        nyc-taxi-limousine-commission-yellow-taxi-trip-records/>`__.
    :type cols: builtin.list[str]
    :param limit: A value indicating the number of days of data to load with ``to_pandas_dataframe()``.
        If not specified, the default of -1 means no limit on days loaded.
    :type limit: int
    :param enable_telemetry: Whether to enable telemetry on this dataset.
    :type enable_telemetry: bool
    """

    default_start_date = parser.parse('2001-01-01')
    default_end_date = parser.parse('2099-01-01')

    _blobInfo = NycTlcYellowBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)

    time_column_name = 'tpepPickupDateTime'

    mandatory_columns = [time_column_name]

    partition_prep_func = prep_partition_puYear_puMonth
    fine_grain_timestamp = time_column_name

    def __init__(
            self,
            start_date: datetime = default_start_date,
            end_date: datetime = default_end_date,
            cols: Optional[List[str]] = None,
            limit: Optional[int] = -1,
            enable_telemetry: bool = True):
        """
        Initialize filtering fields.

        :param start_date: start date you'd like to query inclusively.
        :type start_date: datetime
        :param end_date: end date you'd like to query inclusively.
        :type end_date: datetime
        :param cols: a list of column names you'd like to retrieve. None will get all columns.
        :type cols: Optional[List[str]]
        :param limit: to_pandas_dataframe() will load only "limit" months of data. -1 means no limit.
        :type limit: int
        :param enable_telemetry: whether to send telemetry
        :type enable_telemetry: bool
        """
        self._registry_id = self._blobInfo.registry_id
        self.path = self._blobInfo.get_data_wasbs_path()
        self.start_date = start_date\
            if (self.default_start_date < start_date)\
            else self.default_start_date
        self.end_date = end_date\
            if (end_date is None or self.default_end_date > end_date)\
            else self.default_end_date
        super(NycTlcYellow, self).__init__(cols=cols, enable_telemetry=enable_telemetry)
        self.limit = limit
        if enable_telemetry:
            self.log_properties['StartDate'] = self.start_date.strftime("%Y-%m-%dT%H:%M:%S")\
                if self.start_date is not None else ''
            self.log_properties['EndDate'] = self.end_date.strftime("%Y-%m-%dT%H:%M:%S")\
                if self.end_date is not None else ''
            self.log_properties['Path'] = self.path

    @multimethod(SparkEnv, datetime, datetime)
    def filter(self, env, min_date, max_date):
        """Filter time.

        :param min_date: The min date.
        :type min_date: datetime
        :param max_date: The max date.
        :type min_date: datetime

        :return: The filtered data frame.
        """
        self.data = self.data.na.drop(how='all', subset=self.cols).na.drop(how='any', subset=[self.time_column_name])

        ds = super(NycTlcYellow, self).filter(env, min_date, max_date)
        return ds.select(*self.selected_columns)

    @multimethod(PandasEnv, datetime, datetime)
    def filter(self, env, min_date, max_date):
        """Filter time.

        :param min_date: The min date.
        :type min_date: datetime
        :param max_date: The max date.
        :type min_date: datetime

        :return: The filtered data frame.
        """
        ds = super(NycTlcYellow, self).filter(env, min_date, max_date)
        ds = ds.dropna(how='all', axis=0, subset=self.cols).dropna(
            how='any', axis=0, subset=[self.time_column_name])

        return ds[self.selected_columns]

    def get_pandas_limit(self):
        """Get instance of pandas data load limit class."""
        return PandasDataLoadLimitToMonth(self.start_date, self.end_date, path_pattern='/puYear=%d/puMonth=%d/',
                                          limit=self.limit)

    def _to_spark_dataframe(self, activity_logger):
        """To spark dataframe.

        :param activity_logger: activity logger

        :return: SPARK dataframe
        """
        descriptor = BlobParquetDescriptor(self._blobInfo)
        return descriptor.get_spark_dataframe(self)

    def _to_pandas_dataframe(self, activity_logger):
        """
        Get pandas dataframe.

        :param activity_logger: activity logger

        :return: Pandas dataframe based on its own filters.
        :rtype: pandas.DataFrame
        """
        descriptor = BlobParquetDescriptor(self._blobInfo)
        return descriptor.get_pandas_dataframe(self)
