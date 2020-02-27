"""
Main interface for forecast service client

Usage::

    import boto3
    from mypy_boto3.forecast import ForecastServiceClient

    session = boto3.Session()

    client: ForecastServiceClient = boto3.client("forecast")
    session_client: ForecastServiceClient = session.client("forecast")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING, overload
from botocore.exceptions import ClientError as Boto3ClientError
from mypy_boto3_forecast.paginator import (
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListForecastExportJobsPaginator,
    ListForecastsPaginator,
    ListPredictorsPaginator,
)
from mypy_boto3_forecast.type_defs import (
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateForecastExportJobResponseTypeDef,
    CreateForecastResponseTypeDef,
    CreatePredictorResponseTypeDef,
    DataDestinationTypeDef,
    DataSourceTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeForecastExportJobResponseTypeDef,
    DescribeForecastResponseTypeDef,
    DescribePredictorResponseTypeDef,
    EncryptionConfigTypeDef,
    EvaluationParametersTypeDef,
    FeaturizationConfigTypeDef,
    FilterTypeDef,
    GetAccuracyMetricsResponseTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    InputDataConfigTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsResponseTypeDef,
    ListPredictorsResponseTypeDef,
    SchemaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ForecastServiceClient",)


class Exceptions:
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError


class ForecastServiceClient:
    """
    [ForecastService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.can_paginate)
        """

    def create_dataset(
        self,
        DatasetName: str,
        Domain: Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        DatasetType: Literal["TARGET_TIME_SERIES", "RELATED_TIME_SERIES", "ITEM_METADATA"],
        Schema: SchemaTypeDef,
        DataFrequency: str = None,
        EncryptionConfig: EncryptionConfigTypeDef = None,
    ) -> CreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.create_dataset)
        """

    def create_dataset_group(
        self,
        DatasetGroupName: str,
        Domain: Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        DatasetArns: List[str] = None,
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        [Client.create_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.create_dataset_group)
        """

    def create_dataset_import_job(
        self,
        DatasetImportJobName: str,
        DatasetArn: str,
        DataSource: DataSourceTypeDef,
        TimestampFormat: str = None,
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        [Client.create_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.create_dataset_import_job)
        """

    def create_forecast(
        self, ForecastName: str, PredictorArn: str, ForecastTypes: List[str] = None
    ) -> CreateForecastResponseTypeDef:
        """
        [Client.create_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.create_forecast)
        """

    def create_forecast_export_job(
        self, ForecastExportJobName: str, ForecastArn: str, Destination: DataDestinationTypeDef
    ) -> CreateForecastExportJobResponseTypeDef:
        """
        [Client.create_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.create_forecast_export_job)
        """

    def create_predictor(
        self,
        PredictorName: str,
        ForecastHorizon: int,
        InputDataConfig: InputDataConfigTypeDef,
        FeaturizationConfig: FeaturizationConfigTypeDef,
        AlgorithmArn: str = None,
        PerformAutoML: bool = None,
        PerformHPO: bool = None,
        TrainingParameters: Dict[str, str] = None,
        EvaluationParameters: EvaluationParametersTypeDef = None,
        HPOConfig: HyperParameterTuningJobConfigTypeDef = None,
        EncryptionConfig: EncryptionConfigTypeDef = None,
    ) -> CreatePredictorResponseTypeDef:
        """
        [Client.create_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.create_predictor)
        """

    def delete_dataset(self, DatasetArn: str) -> None:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.delete_dataset)
        """

    def delete_dataset_group(self, DatasetGroupArn: str) -> None:
        """
        [Client.delete_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.delete_dataset_group)
        """

    def delete_dataset_import_job(self, DatasetImportJobArn: str) -> None:
        """
        [Client.delete_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.delete_dataset_import_job)
        """

    def delete_forecast(self, ForecastArn: str) -> None:
        """
        [Client.delete_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.delete_forecast)
        """

    def delete_forecast_export_job(self, ForecastExportJobArn: str) -> None:
        """
        [Client.delete_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.delete_forecast_export_job)
        """

    def delete_predictor(self, PredictorArn: str) -> None:
        """
        [Client.delete_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.delete_predictor)
        """

    def describe_dataset(self, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.describe_dataset)
        """

    def describe_dataset_group(self, DatasetGroupArn: str) -> DescribeDatasetGroupResponseTypeDef:
        """
        [Client.describe_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.describe_dataset_group)
        """

    def describe_dataset_import_job(
        self, DatasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        [Client.describe_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.describe_dataset_import_job)
        """

    def describe_forecast(self, ForecastArn: str) -> DescribeForecastResponseTypeDef:
        """
        [Client.describe_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.describe_forecast)
        """

    def describe_forecast_export_job(
        self, ForecastExportJobArn: str
    ) -> DescribeForecastExportJobResponseTypeDef:
        """
        [Client.describe_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.describe_forecast_export_job)
        """

    def describe_predictor(self, PredictorArn: str) -> DescribePredictorResponseTypeDef:
        """
        [Client.describe_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.describe_predictor)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.generate_presigned_url)
        """

    def get_accuracy_metrics(self, PredictorArn: str) -> GetAccuracyMetricsResponseTypeDef:
        """
        [Client.get_accuracy_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.get_accuracy_metrics)
        """

    def list_dataset_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        [Client.list_dataset_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.list_dataset_groups)
        """

    def list_dataset_import_jobs(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        [Client.list_dataset_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.list_dataset_import_jobs)
        """

    def list_datasets(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.list_datasets)
        """

    def list_forecast_export_jobs(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListForecastExportJobsResponseTypeDef:
        """
        [Client.list_forecast_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.list_forecast_export_jobs)
        """

    def list_forecasts(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListForecastsResponseTypeDef:
        """
        [Client.list_forecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.list_forecasts)
        """

    def list_predictors(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListPredictorsResponseTypeDef:
        """
        [Client.list_predictors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.list_predictors)
        """

    def update_dataset_group(self, DatasetGroupArn: str, DatasetArns: List[str]) -> Dict[str, Any]:
        """
        [Client.update_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Client.update_dataset_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_forecast_export_jobs"]
    ) -> ListForecastExportJobsPaginator:
        """
        [Paginator.ListForecastExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_forecasts"]) -> ListForecastsPaginator:
        """
        [Paginator.ListForecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_predictors"]) -> ListPredictorsPaginator:
        """
        [Paginator.ListPredictors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)
        """
