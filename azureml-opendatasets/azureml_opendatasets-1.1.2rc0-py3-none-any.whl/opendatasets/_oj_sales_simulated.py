# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""OJ Sales data."""
from azureml.core import Dataset
from azureml.data import FileDataset
from azureml.telemetry.activity import ActivityType
from .dataaccess._oj_sales_simulated_blob_info import OjSalesSimulatedBlobInfo
from ._utils.telemetry_utils import get_run_common_properties
from .accessories.public_data_telemetry import _PublicDataTelemetry


class OjSalesSimulated:
    """Represents the Sample Orange Juice Sales Simulated data dataset.

    For more information about this dataset, including column descriptions, different ways to access the
    dataset, and examples, see `Sample: OJ Sales Simulated Data <https://azure.microsoft.com/services/
    open-datasets/catalog/sample-oj-sales-simulated/>`_ in the Microsoft Azure Open Datasets catalog.
    """

    _blobInfo = OjSalesSimulatedBlobInfo()

    @staticmethod
    def _get_logger_prop(blobInfo: OjSalesSimulatedBlobInfo):
        log_properties = get_run_common_properties()
        log_properties['RegistryId'] = blobInfo.registry_id
        log_properties['Path'] = blobInfo.get_data_wasbs_path()
        return log_properties

    @staticmethod
    def get_file_dataset(enable_telemetry: bool = True) -> FileDataset:
        """Return a :class:`azureml.data.FileDataset` containing the data.

        :param enable_telemetry: Whether to enable telemetry on this dataset.
        :type enable_telemetry: bool
        :return: A file dataset.
        :rtype: azureml.data.FileDataset
        """
        _url_path = OjSalesSimulated._blobInfo.get_url()
        if enable_telemetry:
            log_properties = OjSalesSimulated._get_logger_prop(
                OjSalesSimulated._blobInfo)
            log_properties['ActivityType'] = ActivityType.PUBLICAPI
            _PublicDataTelemetry.log_event(
                'get_file_dataset', **log_properties)
            return Dataset.File.from_files(path=_url_path)
        else:
            return Dataset.File.from_files(path=_url_path)
