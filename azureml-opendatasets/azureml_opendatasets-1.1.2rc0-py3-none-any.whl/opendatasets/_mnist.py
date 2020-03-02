# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""MNIST data."""

from azureml.core import Dataset
from azureml.data import FileDataset, TabularDataset
from azureml.data._dataset import _DatasetTelemetryInfo
from azureml.telemetry.activity import ActivityType

from ._utils.telemetry_utils import get_run_common_properties
from .accessories.public_data_telemetry import _PublicDataTelemetry
from .dataaccess._mnist_blob_info import MNISTBlobInfo


class MNIST:
    """Represents the MNIST dataset of handwritten digits.

    The MNIST database of handwritten digits has a training set of 60,000 examples and a test set of
    10,000 examples. The digits have been size-normalized and centered in a fixed-size image. For more
    information about this dataset, including column descriptions, different ways to access the dataset,
    and examples, see `The MNIST database of handwritten digits <https://azure.microsoft.com/services/
    open-datasets/catalog/mnist/>`_ in the Microsoft Azure Open Datasets catalog.

    For an example of using the MNIST dataset, see the tutorial `Train image classification models with
    MNIST data and scikit-learn using Azure Machine Learning <https://docs.microsoft.com/azure/
    machine-learning/tutorial-train-models-with-aml>`_.
    """

    _blobInfo = MNISTBlobInfo()

    @staticmethod
    def _get_logger_prop(blobInfo: MNISTBlobInfo, dataset_filter: str = 'all'):
        log_properties = get_run_common_properties()
        log_properties['RegistryId'] = blobInfo.registry_id
        log_properties['Path'] = blobInfo.get_data_wasbs_path()
        log_properties['dataset_filter'] = dataset_filter
        return log_properties

    @staticmethod
    def get_tabular_dataset(
            dataset_filter='all',
            enable_telemetry: bool = True) -> TabularDataset:
        """Return a :class:`azureml.data.TabularDataset` containing the data.

        :param dataset_filter: A filter that determines what data is returned. Can be "all" (the default),
            "train", or "test".
        :type dataset_filter: str
        :param enable_telemetry: Whether to enable telemetry on this dataset.
        :type enable_telemetry: bool
        :return: A tabular dataset.
        :rtype: azureml.data.TabularDataset
        """
        _url_path = MNIST._blobInfo.get_csv_url(dataset_filter=dataset_filter)
        if enable_telemetry:
            log_properties = MNIST._get_logger_prop(MNIST._blobInfo, dataset_filter)
            log_properties['ActivityType'] = ActivityType.PUBLICAPI
            ds = Dataset.Tabular.from_delimited_files(path=_url_path)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            _PublicDataTelemetry.log_event('get_tabular_dataset', **log_properties)
            return ds
        else:
            ds = Dataset.Tabular.from_delimited_files(path=_url_path)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            return ds

    @staticmethod
    def get_file_dataset(
            dataset_filter='all',
            enable_telemetry: bool = True) -> FileDataset:
        """Return a :class:`azureml.data.FileDataset` containing the data.

        :param dataset_filter: A filter that determines what data is returned. Can be "all" (the default),
            "train", or "test".
        :type dataset_filter: str
        :param enable_telemetry: Whether to enable telemetry on this dataset.
        :type enable_telemetry: bool
        :return: A file dataset.
        :rtype: azureml.data.FileDataset
        """

        _url_path = MNIST._blobInfo.get_raw_url(dataset_filter=dataset_filter)
        if enable_telemetry:
            log_properties = MNIST._get_logger_prop(MNIST._blobInfo, dataset_filter)
            log_properties['ActivityType'] = ActivityType.PUBLICAPI
            ds = Dataset.File.from_files(path=_url_path)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            _PublicDataTelemetry.log_event('get_file_dataset', **log_properties)
            return ds
        else:
            ds = Dataset.File.from_files(path=_url_path)
            ds._telemetry_info = _DatasetTelemetryInfo(entry_point='PythonSDK.OpenDataset')
            return ds
