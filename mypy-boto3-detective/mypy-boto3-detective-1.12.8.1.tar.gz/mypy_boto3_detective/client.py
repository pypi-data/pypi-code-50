"""
Main interface for detective service client

Usage::

    import boto3
    from mypy_boto3.detective import DetectiveClient

    session = boto3.Session()

    client: DetectiveClient = boto3.client("detective")
    session_client: DetectiveClient = session.client("detective")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError
from mypy_boto3_detective.type_defs import (
    AccountTypeDef,
    CreateGraphResponseTypeDef,
    CreateMembersResponseTypeDef,
    DeleteMembersResponseTypeDef,
    GetMembersResponseTypeDef,
    ListGraphsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
)


__all__ = ("DetectiveClient",)


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ValidationException: Boto3ClientError


class DetectiveClient:
    """
    [Detective.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client)
    """

    exceptions: Exceptions

    def accept_invitation(self, GraphArn: str) -> None:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.accept_invitation)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.can_paginate)
        """

    def create_graph(self) -> CreateGraphResponseTypeDef:
        """
        [Client.create_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.create_graph)
        """

    def create_members(
        self, GraphArn: str, Accounts: List[AccountTypeDef], Message: str = None
    ) -> CreateMembersResponseTypeDef:
        """
        [Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.create_members)
        """

    def delete_graph(self, GraphArn: str) -> None:
        """
        [Client.delete_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.delete_graph)
        """

    def delete_members(self, GraphArn: str, AccountIds: List[str]) -> DeleteMembersResponseTypeDef:
        """
        [Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.delete_members)
        """

    def disassociate_membership(self, GraphArn: str) -> None:
        """
        [Client.disassociate_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.disassociate_membership)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.generate_presigned_url)
        """

    def get_members(self, GraphArn: str, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.get_members)
        """

    def list_graphs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListGraphsResponseTypeDef:
        """
        [Client.list_graphs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.list_graphs)
        """

    def list_invitations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.list_invitations)
        """

    def list_members(
        self, GraphArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.list_members)
        """

    def reject_invitation(self, GraphArn: str) -> None:
        """
        [Client.reject_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.12.8/reference/services/detective.html#Detective.Client.reject_invitation)
        """
