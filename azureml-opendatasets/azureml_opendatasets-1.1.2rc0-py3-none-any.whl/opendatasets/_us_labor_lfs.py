# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor lfs."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_lfs_blob_info import UsLaborLFSBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborLFS(UsLaborBase):
    """Represents the US Labor Force Statistics public dataset.

    This dataset contains data about the labor force in the United States, including labor force
    participation rates, and the civilian noninstitutional population by age, gender, race, and ethnic
    groups. For more information about this dataset, including column descriptions, different ways to
    access the dataset, and examples, see `US Labor Force Statistics <https://azure.microsoft.com/
    services/open-datasets/catalog/us-labor-force-statistics/>`_ in the Microsoft Azure Open Datasets catalog.

    :param enable_telemetry: Whether to enable telemetry on this dataset.
    :type enable_telemetry: bool
    """

    _blobInfo = UsLaborLFSBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
