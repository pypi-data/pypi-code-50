"""
Main interface for glue service client paginators.

Usage::

    import boto3
    from mypy_boto3.glue import (
        GetClassifiersPaginator,
        GetConnectionsPaginator,
        GetCrawlerMetricsPaginator,
        GetCrawlersPaginator,
        GetDatabasesPaginator,
        GetDevEndpointsPaginator,
        GetJobRunsPaginator,
        GetJobsPaginator,
        GetPartitionsPaginator,
        GetSecurityConfigurationsPaginator,
        GetTableVersionsPaginator,
        GetTablesPaginator,
        GetTriggersPaginator,
        GetUserDefinedFunctionsPaginator,
    )

    client: GlueClient = boto3.client("glue")

    get_classifiers_paginator: GetClassifiersPaginator = client.get_paginator("get_classifiers")
    get_connections_paginator: GetConnectionsPaginator = client.get_paginator("get_connections")
    get_crawler_metrics_paginator: GetCrawlerMetricsPaginator = client.get_paginator("get_crawler_metrics")
    get_crawlers_paginator: GetCrawlersPaginator = client.get_paginator("get_crawlers")
    get_databases_paginator: GetDatabasesPaginator = client.get_paginator("get_databases")
    get_dev_endpoints_paginator: GetDevEndpointsPaginator = client.get_paginator("get_dev_endpoints")
    get_job_runs_paginator: GetJobRunsPaginator = client.get_paginator("get_job_runs")
    get_jobs_paginator: GetJobsPaginator = client.get_paginator("get_jobs")
    get_partitions_paginator: GetPartitionsPaginator = client.get_paginator("get_partitions")
    get_security_configurations_paginator: GetSecurityConfigurationsPaginator = client.get_paginator("get_security_configurations")
    get_table_versions_paginator: GetTableVersionsPaginator = client.get_paginator("get_table_versions")
    get_tables_paginator: GetTablesPaginator = client.get_paginator("get_tables")
    get_triggers_paginator: GetTriggersPaginator = client.get_paginator("get_triggers")
    get_user_defined_functions_paginator: GetUserDefinedFunctionsPaginator = client.get_paginator("get_user_defined_functions")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Generator, List, TYPE_CHECKING
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_glue.type_defs import (
    GetClassifiersResponseTypeDef,
    GetConnectionsFilterTypeDef,
    GetConnectionsResponseTypeDef,
    GetCrawlerMetricsResponseTypeDef,
    GetCrawlersResponseTypeDef,
    GetDatabasesResponseTypeDef,
    GetDevEndpointsResponseTypeDef,
    GetJobRunsResponseTypeDef,
    GetJobsResponseTypeDef,
    GetPartitionsResponseTypeDef,
    GetSecurityConfigurationsResponseTypeDef,
    GetTableVersionsResponseTypeDef,
    GetTablesResponseTypeDef,
    GetTriggersResponseTypeDef,
    GetUserDefinedFunctionsResponseTypeDef,
    PaginatorConfigTypeDef,
    SegmentTypeDef,
)


__all__ = (
    "GetClassifiersPaginator",
    "GetConnectionsPaginator",
    "GetCrawlerMetricsPaginator",
    "GetCrawlersPaginator",
    "GetDatabasesPaginator",
    "GetDevEndpointsPaginator",
    "GetJobRunsPaginator",
    "GetJobsPaginator",
    "GetPartitionsPaginator",
    "GetSecurityConfigurationsPaginator",
    "GetTableVersionsPaginator",
    "GetTablesPaginator",
    "GetTriggersPaginator",
    "GetUserDefinedFunctionsPaginator",
)


class GetClassifiersPaginator(Boto3Paginator):
    """
    [Paginator.GetClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetClassifiers)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetClassifiersResponseTypeDef, None, None]:
        """
        [GetClassifiers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetClassifiers.paginate)
        """


class GetConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetConnections)
    """

    def paginate(
        self,
        CatalogId: str = None,
        Filter: GetConnectionsFilterTypeDef = None,
        HidePassword: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetConnectionsResponseTypeDef, None, None]:
        """
        [GetConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetConnections.paginate)
        """


class GetCrawlerMetricsPaginator(Boto3Paginator):
    """
    [Paginator.GetCrawlerMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics)
    """

    def paginate(
        self, CrawlerNameList: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetCrawlerMetricsResponseTypeDef, None, None]:
        """
        [GetCrawlerMetrics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics.paginate)
        """


class GetCrawlersPaginator(Boto3Paginator):
    """
    [Paginator.GetCrawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetCrawlers)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetCrawlersResponseTypeDef, None, None]:
        """
        [GetCrawlers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetCrawlers.paginate)
        """


class GetDatabasesPaginator(Boto3Paginator):
    """
    [Paginator.GetDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetDatabases)
    """

    def paginate(
        self, CatalogId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetDatabasesResponseTypeDef, None, None]:
        """
        [GetDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetDatabases.paginate)
        """


class GetDevEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.GetDevEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetDevEndpoints)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetDevEndpointsResponseTypeDef, None, None]:
        """
        [GetDevEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetDevEndpoints.paginate)
        """


class GetJobRunsPaginator(Boto3Paginator):
    """
    [Paginator.GetJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetJobRuns)
    """

    def paginate(
        self, JobName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetJobRunsResponseTypeDef, None, None]:
        """
        [GetJobRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetJobRuns.paginate)
        """


class GetJobsPaginator(Boto3Paginator):
    """
    [Paginator.GetJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetJobs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetJobsResponseTypeDef, None, None]:
        """
        [GetJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetJobs.paginate)
        """


class GetPartitionsPaginator(Boto3Paginator):
    """
    [Paginator.GetPartitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetPartitions)
    """

    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        Segment: SegmentTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetPartitionsResponseTypeDef, None, None]:
        """
        [GetPartitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetPartitions.paginate)
        """


class GetSecurityConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.GetSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSecurityConfigurationsResponseTypeDef, None, None]:
        """
        [GetSecurityConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations.paginate)
        """


class GetTableVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetTableVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetTableVersions)
    """

    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTableVersionsResponseTypeDef, None, None]:
        """
        [GetTableVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetTableVersions.paginate)
        """


class GetTablesPaginator(Boto3Paginator):
    """
    [Paginator.GetTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetTables)
    """

    def paginate(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTablesResponseTypeDef, None, None]:
        """
        [GetTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetTables.paginate)
        """


class GetTriggersPaginator(Boto3Paginator):
    """
    [Paginator.GetTriggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetTriggers)
    """

    def paginate(
        self, DependentJobName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetTriggersResponseTypeDef, None, None]:
        """
        [GetTriggers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetTriggers.paginate)
        """


class GetUserDefinedFunctionsPaginator(Boto3Paginator):
    """
    [Paginator.GetUserDefinedFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions)
    """

    def paginate(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetUserDefinedFunctionsResponseTypeDef, None, None]:
        """
        [GetUserDefinedFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions.paginate)
        """
