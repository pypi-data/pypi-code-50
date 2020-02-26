"""
Main interface for appstream service.

Usage::

    import boto3
    from mypy_boto3.appstream import (
        AppStreamClient,
        Client,
        DescribeDirectoryConfigsPaginator,
        DescribeFleetsPaginator,
        DescribeImageBuildersPaginator,
        DescribeImagesPaginator,
        DescribeSessionsPaginator,
        DescribeStacksPaginator,
        DescribeUserStackAssociationsPaginator,
        DescribeUsersPaginator,
        FleetStartedWaiter,
        FleetStoppedWaiter,
        ListAssociatedFleetsPaginator,
        ListAssociatedStacksPaginator,
        )

    session = boto3.Session()

    client: AppStreamClient = boto3.client("appstream")
    session_client: AppStreamClient = session.client("appstream")

    fleet_started_waiter: FleetStartedWaiter = client.get_waiter("fleet_started")
    fleet_stopped_waiter: FleetStoppedWaiter = client.get_waiter("fleet_stopped")

    describe_directory_configs_paginator: DescribeDirectoryConfigsPaginator = client.get_paginator("describe_directory_configs")
    describe_fleets_paginator: DescribeFleetsPaginator = client.get_paginator("describe_fleets")
    describe_image_builders_paginator: DescribeImageBuildersPaginator = client.get_paginator("describe_image_builders")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_sessions_paginator: DescribeSessionsPaginator = client.get_paginator("describe_sessions")
    describe_stacks_paginator: DescribeStacksPaginator = client.get_paginator("describe_stacks")
    describe_user_stack_associations_paginator: DescribeUserStackAssociationsPaginator = client.get_paginator("describe_user_stack_associations")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    list_associated_fleets_paginator: ListAssociatedFleetsPaginator = client.get_paginator("list_associated_fleets")
    list_associated_stacks_paginator: ListAssociatedStacksPaginator = client.get_paginator("list_associated_stacks")
"""
from mypy_boto3_appstream.client import AppStreamClient as Client, AppStreamClient
from mypy_boto3_appstream.paginator import (
    DescribeDirectoryConfigsPaginator,
    DescribeFleetsPaginator,
    DescribeImageBuildersPaginator,
    DescribeImagesPaginator,
    DescribeSessionsPaginator,
    DescribeStacksPaginator,
    DescribeUserStackAssociationsPaginator,
    DescribeUsersPaginator,
    ListAssociatedFleetsPaginator,
    ListAssociatedStacksPaginator,
)
from mypy_boto3_appstream.waiter import FleetStartedWaiter, FleetStoppedWaiter


__all__ = (
    "AppStreamClient",
    "Client",
    "DescribeDirectoryConfigsPaginator",
    "DescribeFleetsPaginator",
    "DescribeImageBuildersPaginator",
    "DescribeImagesPaginator",
    "DescribeSessionsPaginator",
    "DescribeStacksPaginator",
    "DescribeUserStackAssociationsPaginator",
    "DescribeUsersPaginator",
    "FleetStartedWaiter",
    "FleetStoppedWaiter",
    "ListAssociatedFleetsPaginator",
    "ListAssociatedStacksPaginator",
)
