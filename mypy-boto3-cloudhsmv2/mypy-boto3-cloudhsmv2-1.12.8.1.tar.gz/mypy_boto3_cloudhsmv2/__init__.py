"""
Main interface for cloudhsmv2 service.

Usage::

    import boto3
    from mypy_boto3.cloudhsmv2 import (
        Client,
        CloudHSMV2Client,
        DescribeBackupsPaginator,
        DescribeClustersPaginator,
        ListTagsPaginator,
        )

    session = boto3.Session()

    client: CloudHSMV2Client = boto3.client("cloudhsmv2")
    session_client: CloudHSMV2Client = session.client("cloudhsmv2")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
"""
from mypy_boto3_cloudhsmv2.client import CloudHSMV2Client, CloudHSMV2Client as Client
from mypy_boto3_cloudhsmv2.paginator import (
    DescribeBackupsPaginator,
    DescribeClustersPaginator,
    ListTagsPaginator,
)


__all__ = (
    "Client",
    "CloudHSMV2Client",
    "DescribeBackupsPaginator",
    "DescribeClustersPaginator",
    "ListTagsPaginator",
)
