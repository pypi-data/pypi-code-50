# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor ehe state."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_ehe_state_blob_info import UsLaborEHEStateBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborEHEState(UsLaborBase):
    """Represents the US State Employment Hours and Earnings public dataset.

    This dataset contains industry estimates of nonfarm employment, hours, and earnings of workers on payrolls
    in the United States. For more information about this dataset, including column descriptions, different
    ways to access the dataset, and examples, see `US State Employment Hours and
    Earning <https://azure.microsoft.com/services/open-datasets/catalog/us-employment-hours-earnings-state/>`_
    in the Microsoft Azure Open Datasets catalog.

    :param enable_telemetry: Whether to enable telemetry on this dataset.
    :type enable_telemetry: bool
    """

    _blobInfo = UsLaborEHEStateBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
