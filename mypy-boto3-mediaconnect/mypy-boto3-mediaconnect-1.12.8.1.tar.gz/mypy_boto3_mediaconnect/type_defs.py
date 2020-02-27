"""
Main interface for mediaconnect service type definitions.

Usage::

    from mypy_boto3.mediaconnect.type_defs import EncryptionTypeDef

    data: EncryptionTypeDef = {...}
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EncryptionTypeDef",
    "TransportTypeDef",
    "OutputTypeDef",
    "AddFlowOutputsResponseTypeDef",
    "AddOutputRequestTypeDef",
    "EntitlementTypeDef",
    "SourceTypeDef",
    "FlowTypeDef",
    "CreateFlowResponseTypeDef",
    "DeleteFlowResponseTypeDef",
    "MessagesTypeDef",
    "DescribeFlowResponseTypeDef",
    "GrantEntitlementRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "ListedEntitlementTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListedFlowTypeDef",
    "ListFlowsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RevokeFlowEntitlementResponseTypeDef",
    "SetSourceRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowResponseTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "UpdateFlowSourceResponseTypeDef",
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef",
    {"Algorithm": Literal["aes128", "aes192", "aes256"], "RoleArn": str},
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass


_RequiredTransportTypeDef = TypedDict(
    "_RequiredTransportTypeDef",
    {"Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"]},
)
_OptionalTransportTypeDef = TypedDict(
    "_OptionalTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class TransportTypeDef(_RequiredTransportTypeDef, _OptionalTransportTypeDef):
    pass


_RequiredOutputTypeDef = TypedDict("_RequiredOutputTypeDef", {"Name": str, "OutputArn": str})
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": EncryptionTypeDef,
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Port": int,
        "Transport": TransportTypeDef,
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass


AddFlowOutputsResponseTypeDef = TypedDict(
    "AddFlowOutputsResponseTypeDef", {"FlowArn": str, "Outputs": List[OutputTypeDef]}, total=False
)

_RequiredAddOutputRequestTypeDef = TypedDict(
    "_RequiredAddOutputRequestTypeDef",
    {"Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"]},
)
_OptionalAddOutputRequestTypeDef = TypedDict(
    "_OptionalAddOutputRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": EncryptionTypeDef,
        "MaxLatency": int,
        "Name": str,
        "Port": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class AddOutputRequestTypeDef(_RequiredAddOutputRequestTypeDef, _OptionalAddOutputRequestTypeDef):
    pass


_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef", {"EntitlementArn": str, "Name": str, "Subscribers": List[str]}
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {"DataTransferSubscriberFeePercent": int, "Description": str, "Encryption": EncryptionTypeDef},
    total=False,
)


class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass


_RequiredSourceTypeDef = TypedDict("_RequiredSourceTypeDef", {"Name": str, "SourceArn": str})
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": EncryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Transport": TransportTypeDef,
        "WhitelistCidr": str,
    },
    total=False,
)


class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass


_RequiredFlowTypeDef = TypedDict(
    "_RequiredFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List[EntitlementTypeDef],
        "FlowArn": str,
        "Name": str,
        "Outputs": List[OutputTypeDef],
        "Source": SourceTypeDef,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
)
_OptionalFlowTypeDef = TypedDict(
    "_OptionalFlowTypeDef", {"Description": str, "EgressIp": str}, total=False
)


class FlowTypeDef(_RequiredFlowTypeDef, _OptionalFlowTypeDef):
    pass


CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef", {"Flow": FlowTypeDef}, total=False
)

DeleteFlowResponseTypeDef = TypedDict(
    "DeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

MessagesTypeDef = TypedDict("MessagesTypeDef", {"Errors": List[str]})

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef", {"Flow": FlowTypeDef, "Messages": MessagesTypeDef}, total=False
)

_RequiredGrantEntitlementRequestTypeDef = TypedDict(
    "_RequiredGrantEntitlementRequestTypeDef", {"Subscribers": List[str]}
)
_OptionalGrantEntitlementRequestTypeDef = TypedDict(
    "_OptionalGrantEntitlementRequestTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": EncryptionTypeDef,
        "Name": str,
    },
    total=False,
)


class GrantEntitlementRequestTypeDef(
    _RequiredGrantEntitlementRequestTypeDef, _OptionalGrantEntitlementRequestTypeDef
):
    pass


GrantFlowEntitlementsResponseTypeDef = TypedDict(
    "GrantFlowEntitlementsResponseTypeDef",
    {"Entitlements": List[EntitlementTypeDef], "FlowArn": str},
    total=False,
)

_RequiredListedEntitlementTypeDef = TypedDict(
    "_RequiredListedEntitlementTypeDef", {"EntitlementArn": str, "EntitlementName": str}
)
_OptionalListedEntitlementTypeDef = TypedDict(
    "_OptionalListedEntitlementTypeDef", {"DataTransferSubscriberFeePercent": int}, total=False
)


class ListedEntitlementTypeDef(
    _RequiredListedEntitlementTypeDef, _OptionalListedEntitlementTypeDef
):
    pass


ListEntitlementsResponseTypeDef = TypedDict(
    "ListEntitlementsResponseTypeDef",
    {"Entitlements": List[ListedEntitlementTypeDef], "NextToken": str},
    total=False,
)

ListedFlowTypeDef = TypedDict(
    "ListedFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": Literal["OWNED", "ENTITLED"],
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef", {"Flows": List[ListedFlowTypeDef], "NextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RemoveFlowOutputResponseTypeDef = TypedDict(
    "RemoveFlowOutputResponseTypeDef", {"FlowArn": str, "OutputArn": str}, total=False
)

RevokeFlowEntitlementResponseTypeDef = TypedDict(
    "RevokeFlowEntitlementResponseTypeDef", {"EntitlementArn": str, "FlowArn": str}, total=False
)

SetSourceRequestTypeDef = TypedDict(
    "SetSourceRequestTypeDef",
    {
        "Decryption": EncryptionTypeDef,
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "Name": str,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "StreamId": str,
        "WhitelistCidr": str,
    },
    total=False,
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

UpdateEncryptionTypeDef = TypedDict(
    "UpdateEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

UpdateFlowEntitlementResponseTypeDef = TypedDict(
    "UpdateFlowEntitlementResponseTypeDef",
    {"Entitlement": EntitlementTypeDef, "FlowArn": str},
    total=False,
)

UpdateFlowOutputResponseTypeDef = TypedDict(
    "UpdateFlowOutputResponseTypeDef", {"FlowArn": str, "Output": OutputTypeDef}, total=False
)

UpdateFlowSourceResponseTypeDef = TypedDict(
    "UpdateFlowSourceResponseTypeDef", {"FlowArn": str, "Source": SourceTypeDef}, total=False
)
