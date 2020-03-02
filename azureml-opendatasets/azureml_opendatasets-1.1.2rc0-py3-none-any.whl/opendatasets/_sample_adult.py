# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Sample Adult data."""

from azureml.core import Dataset
from azureml.data import TabularDataset
from azureml.data._dataset import _DatasetTelemetryInfo
from azureml.telemetry.activity import ActivityType

from ._utils.telemetry_utils import get_run_common_properties
from .accessories.public_data_telemetry import _PublicDataTelemetry
from .dataaccess._sample_adult_blob_info import SampleAdultBlobInfo


class SampleAdult:
    """Represents the Sample Adult dataset."""
    _blobInfo = SampleAdultBlobInfo()

    @staticmethod
    def get_tabular_dataset(enable_telemetry: bool = True) -> TabularDataset:
        """Return a :class:`azureml.data.TabularDataset` containing the data.

        :param enable_telemetry: Whether to enable telemetry on this dataset.
        :type enable_telemetry: bool
        :return: A tabular dataset.
        :rtype: azureml.data.TabularDataset
        """
        blobInfo = SampleAdult._blobInfo
        url_path = blobInfo.get_url()
        if enable_telemetry:
            log_properties = get_run_common_properties()
            log_properties['RegistryId'] = blobInfo.registry_id
            log_properties['Path'] = url_path
            log_properties['ActivityType'] = ActivityType.PUBLICAPI
            ds = Dataset.Tabular.from_delimited_files(path=url_path)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            _PublicDataTelemetry.log_event('get_tabular_dataset', **log_properties)
            return ds
        else:
            ds = Dataset.Tabular.from_delimited_files(path=url_path)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            return ds
