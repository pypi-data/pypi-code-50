"""
Main interface for sagemaker-a2i-runtime service type definitions.

Usage::

    from mypy_boto3.sagemaker_a2i_runtime.type_defs import HumanLoopInputContentTypeDef

    data: HumanLoopInputContentTypeDef = {...}
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
    "HumanLoopInputContentTypeDef",
    "HumanLoopOutputContentTypeDef",
    "DescribeHumanLoopResponseTypeDef",
    "HumanReviewDataAttributesTypeDef",
    "HumanLoopSummaryTypeDef",
    "ListHumanLoopsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "HumanLoopActivationReasonTypeDef",
    "HumanLoopActivationResultsTypeDef",
    "StartHumanLoopResponseTypeDef",
)

HumanLoopInputContentTypeDef = TypedDict("HumanLoopInputContentTypeDef", {"InputContent": str})

HumanLoopOutputContentTypeDef = TypedDict("HumanLoopOutputContentTypeDef", {"OutputS3Uri": str})

_RequiredDescribeHumanLoopResponseTypeDef = TypedDict(
    "_RequiredDescribeHumanLoopResponseTypeDef",
    {
        "CreationTimestamp": datetime,
        "HumanLoopStatus": Literal["InProgress", "Failed", "Completed", "Stopped", "Stopping"],
        "HumanLoopName": str,
        "HumanLoopArn": str,
        "FlowDefinitionArn": str,
        "HumanLoopInput": HumanLoopInputContentTypeDef,
    },
)
_OptionalDescribeHumanLoopResponseTypeDef = TypedDict(
    "_OptionalDescribeHumanLoopResponseTypeDef",
    {"FailureReason": str, "FailureCode": str, "HumanLoopOutput": HumanLoopOutputContentTypeDef},
    total=False,
)


class DescribeHumanLoopResponseTypeDef(
    _RequiredDescribeHumanLoopResponseTypeDef, _OptionalDescribeHumanLoopResponseTypeDef
):
    pass


HumanReviewDataAttributesTypeDef = TypedDict(
    "HumanReviewDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
)

HumanLoopSummaryTypeDef = TypedDict(
    "HumanLoopSummaryTypeDef",
    {
        "HumanLoopName": str,
        "HumanLoopStatus": Literal["InProgress", "Failed", "Completed", "Stopped", "Stopping"],
        "CreationTime": datetime,
        "FailureReason": str,
        "FlowDefinitionArn": str,
    },
    total=False,
)

_RequiredListHumanLoopsResponseTypeDef = TypedDict(
    "_RequiredListHumanLoopsResponseTypeDef", {"HumanLoopSummaries": List[HumanLoopSummaryTypeDef]}
)
_OptionalListHumanLoopsResponseTypeDef = TypedDict(
    "_OptionalListHumanLoopsResponseTypeDef", {"NextToken": str}, total=False
)


class ListHumanLoopsResponseTypeDef(
    _RequiredListHumanLoopsResponseTypeDef, _OptionalListHumanLoopsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

HumanLoopActivationReasonTypeDef = TypedDict(
    "HumanLoopActivationReasonTypeDef", {"ConditionsMatched": bool}, total=False
)

HumanLoopActivationResultsTypeDef = TypedDict(
    "HumanLoopActivationResultsTypeDef",
    {
        "HumanLoopActivationReason": HumanLoopActivationReasonTypeDef,
        "HumanLoopActivationConditionsEvaluationResults": str,
    },
    total=False,
)

StartHumanLoopResponseTypeDef = TypedDict(
    "StartHumanLoopResponseTypeDef",
    {"HumanLoopArn": str, "HumanLoopActivationResults": HumanLoopActivationResultsTypeDef},
    total=False,
)
