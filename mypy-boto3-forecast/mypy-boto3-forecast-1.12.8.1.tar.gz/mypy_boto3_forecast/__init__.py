"""
Main interface for forecast service.

Usage::

    import boto3
    from mypy_boto3.forecast import (
        Client,
        ForecastServiceClient,
        ListDatasetGroupsPaginator,
        ListDatasetImportJobsPaginator,
        ListDatasetsPaginator,
        ListForecastExportJobsPaginator,
        ListForecastsPaginator,
        ListPredictorsPaginator,
        )

    session = boto3.Session()

    client: ForecastServiceClient = boto3.client("forecast")
    session_client: ForecastServiceClient = session.client("forecast")

    list_dataset_groups_paginator: ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
    list_dataset_import_jobs_paginator: ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_forecast_export_jobs_paginator: ListForecastExportJobsPaginator = client.get_paginator("list_forecast_export_jobs")
    list_forecasts_paginator: ListForecastsPaginator = client.get_paginator("list_forecasts")
    list_predictors_paginator: ListPredictorsPaginator = client.get_paginator("list_predictors")
"""
from mypy_boto3_forecast.client import ForecastServiceClient, ForecastServiceClient as Client
from mypy_boto3_forecast.paginator import (
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListForecastExportJobsPaginator,
    ListForecastsPaginator,
    ListPredictorsPaginator,
)


__all__ = (
    "Client",
    "ForecastServiceClient",
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListForecastExportJobsPaginator",
    "ListForecastsPaginator",
    "ListPredictorsPaginator",
)
