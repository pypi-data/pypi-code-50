"""
Main interface for globalaccelerator service type definitions.

Usage::

    from mypy_boto3.globalaccelerator.type_defs import IpSetTypeDef

    data: IpSetTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "IpSetTypeDef",
    "AcceleratorTypeDef",
    "CreateAcceleratorResponseTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "CreateEndpointGroupResponseTypeDef",
    "PortRangeTypeDef",
    "ListenerTypeDef",
    "CreateListenerResponseTypeDef",
    "AcceleratorAttributesTypeDef",
    "DescribeAcceleratorAttributesResponseTypeDef",
    "DescribeAcceleratorResponseTypeDef",
    "DescribeEndpointGroupResponseTypeDef",
    "DescribeListenerResponseTypeDef",
    "EndpointConfigurationTypeDef",
    "ListAcceleratorsResponseTypeDef",
    "ListEndpointGroupsResponseTypeDef",
    "ListListenersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateAcceleratorAttributesResponseTypeDef",
    "UpdateAcceleratorResponseTypeDef",
    "UpdateEndpointGroupResponseTypeDef",
    "UpdateListenerResponseTypeDef",
)

IpSetTypeDef = TypedDict("IpSetTypeDef", {"IpFamily": str, "IpAddresses": List[str]}, total=False)

AcceleratorTypeDef = TypedDict(
    "AcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
        "IpSets": List[IpSetTypeDef],
        "DnsName": str,
        "Status": Literal["DEPLOYED", "IN_PROGRESS"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

CreateAcceleratorResponseTypeDef = TypedDict(
    "CreateAcceleratorResponseTypeDef", {"Accelerator": AcceleratorTypeDef}, total=False
)

EndpointDescriptionTypeDef = TypedDict(
    "EndpointDescriptionTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": Literal["INITIAL", "HEALTHY", "UNHEALTHY"],
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

EndpointGroupTypeDef = TypedDict(
    "EndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[EndpointDescriptionTypeDef],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": Literal["TCP", "HTTP", "HTTPS"],
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)

CreateEndpointGroupResponseTypeDef = TypedDict(
    "CreateEndpointGroupResponseTypeDef", {"EndpointGroup": EndpointGroupTypeDef}, total=False
)

PortRangeTypeDef = TypedDict("PortRangeTypeDef", {"FromPort": int, "ToPort": int}, total=False)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[PortRangeTypeDef],
        "Protocol": Literal["TCP", "UDP"],
        "ClientAffinity": Literal["NONE", "SOURCE_IP"],
    },
    total=False,
)

CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef", {"Listener": ListenerTypeDef}, total=False
)

AcceleratorAttributesTypeDef = TypedDict(
    "AcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
    total=False,
)

DescribeAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeAcceleratorAttributesResponseTypeDef",
    {"AcceleratorAttributes": AcceleratorAttributesTypeDef},
    total=False,
)

DescribeAcceleratorResponseTypeDef = TypedDict(
    "DescribeAcceleratorResponseTypeDef", {"Accelerator": AcceleratorTypeDef}, total=False
)

DescribeEndpointGroupResponseTypeDef = TypedDict(
    "DescribeEndpointGroupResponseTypeDef", {"EndpointGroup": EndpointGroupTypeDef}, total=False
)

DescribeListenerResponseTypeDef = TypedDict(
    "DescribeListenerResponseTypeDef", {"Listener": ListenerTypeDef}, total=False
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {"EndpointId": str, "Weight": int, "ClientIPPreservationEnabled": bool},
    total=False,
)

ListAcceleratorsResponseTypeDef = TypedDict(
    "ListAcceleratorsResponseTypeDef",
    {"Accelerators": List[AcceleratorTypeDef], "NextToken": str},
    total=False,
)

ListEndpointGroupsResponseTypeDef = TypedDict(
    "ListEndpointGroupsResponseTypeDef",
    {"EndpointGroups": List[EndpointGroupTypeDef], "NextToken": str},
    total=False,
)

ListListenersResponseTypeDef = TypedDict(
    "ListListenersResponseTypeDef",
    {"Listeners": List[ListenerTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateAcceleratorAttributesResponseTypeDef",
    {"AcceleratorAttributes": AcceleratorAttributesTypeDef},
    total=False,
)

UpdateAcceleratorResponseTypeDef = TypedDict(
    "UpdateAcceleratorResponseTypeDef", {"Accelerator": AcceleratorTypeDef}, total=False
)

UpdateEndpointGroupResponseTypeDef = TypedDict(
    "UpdateEndpointGroupResponseTypeDef", {"EndpointGroup": EndpointGroupTypeDef}, total=False
)

UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef", {"Listener": ListenerTypeDef}, total=False
)
