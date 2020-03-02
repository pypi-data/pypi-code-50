# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""US labor ppi industry."""

from ._us_labor_base import UsLaborBase
from .dataaccess._us_labor_ppi_industry_blob_info import UsLaborPPIIndustryBlobInfo
from .dataaccess.blob_parquet_descriptor import BlobParquetDescriptor


class UsLaborPPIIndustry(UsLaborBase):
    """Represents the US Producer Price Index (PPI) - Industry public dataset.

    The Producer Price Index (PPI) is a measure of average change over time in the selling prices received
    by domestic producers for their output. The prices included in the PPI are from the first commercial
    transaction for products and services covered. This dataset contains PPIs for a wide range of industry
    sectors of the U.S. economy. For more information about this dataset, including column descriptions,
    different ways to access the dataset, and examples, see `US Producer Price Index -
    Industry <https://azure.microsoft.com/services/open-datasets/catalog/us-producer-price-index-industry/>`_
    in the Microsoft Azure Open Datasets catalog.

    For general information about Azure Open Datasets, see `Azure Open Datasets
    Documentation <https://docs.microsoft.com/azure/open-datasets/>`_.

    :param enable_telemetry: Whether to enable telemetry on this dataset.
    :type enable_telemetry: bool
    """

    _blobInfo = UsLaborPPIIndustryBlobInfo()

    data = BlobParquetDescriptor(_blobInfo)
