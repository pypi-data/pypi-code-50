# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Wikipedia."""

from azureml.data import FileDataset
from azureml.data._dataset import _DatasetTelemetryInfo
from azureml.core.dataset import Dataset
from azureml.telemetry.activity import ActivityType

from ._utils.telemetry_utils import get_run_common_properties
from .accessories.public_data_telemetry import _PublicDataTelemetry
from .dataaccess._wikipedia_blob_info import WikipediaBlobInfo


class Wikipedia:
    """Represents the Wikipedia dataset."""
    _blobInfo = WikipediaBlobInfo()

    @staticmethod
    def get_file_dataset(enable_telemetry: bool = True) -> FileDataset:
        """Return a :class:`azureml.data.FileDataset` containing the data.

        :param enable_telemetry: Whether to enable telemetry on this dataset.
        :type enable_telemetry: bool
        :return: A file dataset.
        :rtype: azureml.data.FileDataset
        """
        blobInfo = Wikipedia._blobInfo
        url_paths = blobInfo.get_url()
        if enable_telemetry:
            log_properties = get_run_common_properties()
            log_properties['RegistryId'] = blobInfo.registry_id
            log_properties['Path'] = url_paths
            log_properties['ActivityType'] = ActivityType.PUBLICAPI
            ds = Dataset.File.from_files(path=url_paths)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            _PublicDataTelemetry.log_event('get_file_dataset', **log_properties)
            return ds
        else:
            ds = Dataset.File.from_files(path=url_paths)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            return ds
