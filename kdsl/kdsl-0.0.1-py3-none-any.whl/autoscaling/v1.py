from __future__ import annotations
import attr
import kdsl.meta.v1
import kdsl.autoscaling.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class ScaleStatus(K8sObjectBase):
    """
    | ScaleStatus represents the current status of a scale subresource.
    
    :param replicas: actual number of observed instances of the scaled object.
    :param selector: label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors
    """
    replicas: int = attr.ib(metadata={'yaml_name': 'replicas'})
    selector: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'selector'})


@attr.s(kw_only=True)
class ScaleSpec(K8sObjectBase):
    """
    | ScaleSpec describes the attributes of a scale subresource.
    
    :param replicas: desired number of instances for the scaled object.
    """
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})


@attr.s(kw_only=True)
class Scale(K8sObjectBase):
    """
    | Scale represents a scaling request for a resource.
    
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
    :param spec: defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.
    :param status: current status of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. Read-only.
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ObjectMeta,
        kdsl.meta.v1.ObjectMetaTypedDict]] = attr.ib(default=None, metadata
        ={'yaml_name': 'metadata'})
    spec: Optional[Union[kdsl.autoscaling.v1.ScaleSpec,
        kdsl.autoscaling.v1.ScaleSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})
    status: Optional[Union[kdsl.autoscaling.v1.ScaleStatus,
        kdsl.autoscaling.v1.ScaleStatusTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'status'})


@attr.s(kw_only=True)
class HorizontalPodAutoscalerStatus(K8sObjectBase):
    """
    | current status of a horizontal pod autoscaler
    
    :param currentReplicas: current number of replicas of pods managed by this autoscaler.
    :param desiredReplicas: desired number of replicas of pods managed by this autoscaler.
    :param currentCPUUtilizationPercentage: current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.
    :param lastScaleTime: last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.
    :param observedGeneration: most recent generation observed by this autoscaler.
    """
    currentReplicas: int = attr.ib(metadata={'yaml_name': 'currentReplicas'})
    desiredReplicas: int = attr.ib(metadata={'yaml_name': 'desiredReplicas'})
    currentCPUUtilizationPercentage: Optional[int] = attr.ib(default=None,
        metadata={'yaml_name': 'currentCPUUtilizationPercentage'})
    lastScaleTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastScaleTime'})
    observedGeneration: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'observedGeneration'})


@attr.s(kw_only=True)
class HorizontalPodAutoscalerSpec(K8sObjectBase):
    """
    | specification of a horizontal pod autoscaler.
    
    :param maxReplicas: upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.
    :param scaleTargetRef: reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.
    :param minReplicas: minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.
    :param targetCPUUtilizationPercentage: target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.
    """
    maxReplicas: int = attr.ib(metadata={'yaml_name': 'maxReplicas'})
    scaleTargetRef: Union[kdsl.autoscaling.v1.CrossVersionObjectReference,
        kdsl.autoscaling.v1.CrossVersionObjectReferenceTypedDict] = attr.ib(
        metadata={'yaml_name': 'scaleTargetRef'})
    minReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'minReplicas'})
    targetCPUUtilizationPercentage: Optional[int] = attr.ib(default=None,
        metadata={'yaml_name': 'targetCPUUtilizationPercentage'})


@attr.s(kw_only=True)
class HorizontalPodAutoscalerList(K8sObjectBase):
    """
    | list of horizontal pod autoscaler objects.
    
    :param items: list of horizontal pod autoscaler objects.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata.
    """
    items: Sequence[Union[kdsl.autoscaling.v1.HorizontalPodAutoscaler,
        kdsl.autoscaling.v1.HorizontalPodAutoscalerTypedDict]] = attr.ib(
        metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class HorizontalPodAutoscaler(K8sResourceBase):
    """
    | configuration of a horizontal pod autoscaler.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: behaviour of autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.
    """
    apiVersion: ClassVar[str] = 'autoscaling/v1'
    kind: ClassVar[str] = 'HorizontalPodAutoscaler'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.autoscaling.v1.HorizontalPodAutoscalerSpec,
        kdsl.autoscaling.v1.HorizontalPodAutoscalerSpecTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class CrossVersionObjectReference(K8sObjectBase):
    """
    | CrossVersionObjectReference contains enough information to let you identify the referred resource.
    
    :param kind: Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
    :param name: Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names
    :param apiVersion: API version of the referent
    """
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


class ScaleStatusOptionalTypedDict(TypedDict, total=(False)):
    selector: str


class ScaleStatusTypedDict(ScaleStatusOptionalTypedDict, total=(True)):
    replicas: int


class ScaleSpecTypedDict(TypedDict, total=(False)):
    replicas: int


class ScaleTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ObjectMeta, kdsl.meta.v1.ObjectMetaTypedDict]
    spec: Union[kdsl.autoscaling.v1.ScaleSpec,
        kdsl.autoscaling.v1.ScaleSpecTypedDict]
    status: Union[kdsl.autoscaling.v1.ScaleStatus,
        kdsl.autoscaling.v1.ScaleStatusTypedDict]


class HorizontalPodAutoscalerStatusOptionalTypedDict(TypedDict, total=(False)):
    currentCPUUtilizationPercentage: int
    lastScaleTime: str
    observedGeneration: int


class HorizontalPodAutoscalerStatusTypedDict(
    HorizontalPodAutoscalerStatusOptionalTypedDict, total=(True)):
    currentReplicas: int
    desiredReplicas: int


class HorizontalPodAutoscalerSpecOptionalTypedDict(TypedDict, total=(False)):
    minReplicas: int
    targetCPUUtilizationPercentage: int


class HorizontalPodAutoscalerSpecTypedDict(
    HorizontalPodAutoscalerSpecOptionalTypedDict, total=(True)):
    maxReplicas: int
    scaleTargetRef: Union[kdsl.autoscaling.v1.CrossVersionObjectReference,
        kdsl.autoscaling.v1.CrossVersionObjectReferenceTypedDict]


class HorizontalPodAutoscalerListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class HorizontalPodAutoscalerListTypedDict(
    HorizontalPodAutoscalerListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.autoscaling.v1.HorizontalPodAutoscaler,
        kdsl.autoscaling.v1.HorizontalPodAutoscalerTypedDict]]


class HorizontalPodAutoscalerOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.autoscaling.v1.HorizontalPodAutoscalerSpec,
        kdsl.autoscaling.v1.HorizontalPodAutoscalerSpecTypedDict]


class HorizontalPodAutoscalerTypedDict(HorizontalPodAutoscalerOptionalTypedDict
    , total=(True)):
    name: str
    namespace: str


class CrossVersionObjectReferenceOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str


class CrossVersionObjectReferenceTypedDict(
    CrossVersionObjectReferenceOptionalTypedDict, total=(True)):
    kind: str
    name: str
