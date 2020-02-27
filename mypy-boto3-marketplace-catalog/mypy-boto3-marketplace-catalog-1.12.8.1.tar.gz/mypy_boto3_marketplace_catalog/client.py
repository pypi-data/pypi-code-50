"""
Main interface for marketplace-catalog service client

Usage::

    import boto3
    from mypy_boto3.marketplace_catalog import MarketplaceCatalogClient

    session = boto3.Session()

    client: MarketplaceCatalogClient = boto3.client("marketplace-catalog")
    session_client: MarketplaceCatalogClient = session.client("marketplace-catalog")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError
from mypy_boto3_marketplace_catalog.type_defs import (
    CancelChangeSetResponseTypeDef,
    ChangeTypeDef,
    DescribeChangeSetResponseTypeDef,
    DescribeEntityResponseTypeDef,
    FilterTypeDef,
    ListChangeSetsResponseTypeDef,
    ListEntitiesResponseTypeDef,
    SortTypeDef,
    StartChangeSetResponseTypeDef,
)


__all__ = ("MarketplaceCatalogClient",)


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServiceException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotSupportedException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError


class MarketplaceCatalogClient:
    """
    [MarketplaceCatalog.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.can_paginate)
        """

    def cancel_change_set(self, Catalog: str, ChangeSetId: str) -> CancelChangeSetResponseTypeDef:
        """
        [Client.cancel_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.cancel_change_set)
        """

    def describe_change_set(
        self, Catalog: str, ChangeSetId: str
    ) -> DescribeChangeSetResponseTypeDef:
        """
        [Client.describe_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_change_set)
        """

    def describe_entity(self, Catalog: str, EntityId: str) -> DescribeEntityResponseTypeDef:
        """
        [Client.describe_entity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_entity)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.generate_presigned_url)
        """

    def list_change_sets(
        self,
        Catalog: str,
        FilterList: List[FilterTypeDef] = None,
        Sort: SortTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListChangeSetsResponseTypeDef:
        """
        [Client.list_change_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_change_sets)
        """

    def list_entities(
        self,
        Catalog: str,
        EntityType: str,
        FilterList: List[FilterTypeDef] = None,
        Sort: SortTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListEntitiesResponseTypeDef:
        """
        [Client.list_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_entities)
        """

    def start_change_set(
        self,
        Catalog: str,
        ChangeSet: List[ChangeTypeDef],
        ChangeSetName: str = None,
        ClientRequestToken: str = None,
    ) -> StartChangeSetResponseTypeDef:
        """
        [Client.start_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.start_change_set)
        """
