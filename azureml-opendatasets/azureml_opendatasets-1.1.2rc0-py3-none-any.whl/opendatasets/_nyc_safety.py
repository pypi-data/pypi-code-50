# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""New York City safety."""

from .dataaccess._nyc_safety_blob_info import NycSafetyBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor
from ._city_safety import CitySafety
from datetime import datetime
from dateutil import parser


class NycSafety(CitySafety):
    """Represents the New York City Safety public dataset.

    This dataset contains all New York City 311 service requests from 2010 to the present.
    For more information about this dataset, including column descriptions, different ways to access the dataset,
    and examples, see `New York City Safety Data <https://azure.microsoft.com/services/open-datasets/catalog/
    new-york-city-safety-data/>`_ in the Microsoft Azure Open Datasets catalog.

    :param start_data: The date at which to start loading data, inclusive. If None, the ``default_start_date``
        is used.
    :type start_data: datetime
    :param end_data: The date at which to end loading data, inclusive. If None, the ``default_end_date``
        is used.
    :type end_data: datetime
    :param cols: A list of columns names to load from the dataset. If None, all columns are loaded. For
        information on the available columns in this dataset, see `New York City Safety
        Data <https://azure.microsoft.com/services/open-datasets/catalog/new-york-city-safety-data/>`_.
    :type cols: builtin.list[str]
    :param enable_telemetry: Whether to enable telemetry on this dataset.
    :type enable_telemetry: bool
    """

    default_start_date = parser.parse('2000-01-01')
    default_end_date = datetime.today()

    """const instance of blobInfo."""
    _blobInfo = NycSafetyBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
