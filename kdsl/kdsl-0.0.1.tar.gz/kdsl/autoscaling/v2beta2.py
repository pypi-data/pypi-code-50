from __future__ import annotations
import kdsl.autoscaling.v2beta2
import kdsl.meta.v1
import attr
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class ResourceMetricStatus(K8sObjectBase):
    """
    | ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.
    
    :param current: current contains the current value for the given metric
    :param name: Name is the name of the resource in question.
    """
    current: Union[kdsl.autoscaling.v2beta2.MetricValueStatus,
        kdsl.autoscaling.v2beta2.MetricValueStatusTypedDict] = attr.ib(metadata
        ={'yaml_name': 'current'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ResourceMetricSource(K8sObjectBase):
    """
    | ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values will be averaged together before being compared to the target.  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.  Only one "target" type should be set.
    
    :param name: name is the name of the resource in question.
    :param target: target specifies the target value for the given metric
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    target: Union[kdsl.autoscaling.v2beta2.MetricTarget,
        kdsl.autoscaling.v2beta2.MetricTargetTypedDict] = attr.ib(metadata=
        {'yaml_name': 'target'})


@attr.s(kw_only=True)
class PodsMetricStatus(K8sObjectBase):
    """
    | PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second).
    
    :param current: current contains the current value for the given metric
    :param metric: metric identifies the target metric by name and selector
    """
    current: Union[kdsl.autoscaling.v2beta2.MetricValueStatus,
        kdsl.autoscaling.v2beta2.MetricValueStatusTypedDict] = attr.ib(metadata
        ={'yaml_name': 'current'})
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict] = attr.ib(metadata
        ={'yaml_name': 'metric'})


@attr.s(kw_only=True)
class PodsMetricSource(K8sObjectBase):
    """
    | PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value.
    
    :param metric: metric identifies the target metric by name and selector
    :param target: target specifies the target value for the given metric
    """
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict] = attr.ib(metadata
        ={'yaml_name': 'metric'})
    target: Union[kdsl.autoscaling.v2beta2.MetricTarget,
        kdsl.autoscaling.v2beta2.MetricTargetTypedDict] = attr.ib(metadata=
        {'yaml_name': 'target'})


@attr.s(kw_only=True)
class ObjectMetricStatus(K8sObjectBase):
    """
    | ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).
    
    :param current: current contains the current value for the given metric
    :param describedObject: None
    :param metric: metric identifies the target metric by name and selector
    """
    current: Union[kdsl.autoscaling.v2beta2.MetricValueStatus,
        kdsl.autoscaling.v2beta2.MetricValueStatusTypedDict] = attr.ib(metadata
        ={'yaml_name': 'current'})
    describedObject: Union[
        kdsl.autoscaling.v2beta2.CrossVersionObjectReference,
        kdsl.autoscaling.v2beta2.CrossVersionObjectReferenceTypedDict
        ] = attr.ib(metadata={'yaml_name': 'describedObject'})
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict] = attr.ib(metadata
        ={'yaml_name': 'metric'})


@attr.s(kw_only=True)
class ObjectMetricSource(K8sObjectBase):
    """
    | ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).
    
    :param describedObject: None
    :param metric: metric identifies the target metric by name and selector
    :param target: target specifies the target value for the given metric
    """
    describedObject: Union[
        kdsl.autoscaling.v2beta2.CrossVersionObjectReference,
        kdsl.autoscaling.v2beta2.CrossVersionObjectReferenceTypedDict
        ] = attr.ib(metadata={'yaml_name': 'describedObject'})
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict] = attr.ib(metadata
        ={'yaml_name': 'metric'})
    target: Union[kdsl.autoscaling.v2beta2.MetricTarget,
        kdsl.autoscaling.v2beta2.MetricTargetTypedDict] = attr.ib(metadata=
        {'yaml_name': 'target'})


@attr.s(kw_only=True)
class MetricValueStatus(K8sObjectBase):
    """
    | MetricValueStatus holds the current value for a metric
    
    :param averageUtilization: currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.
    :param averageValue: averageValue is the current value of the average of the metric across all relevant pods (as a quantity)
    :param value: value is the current value of the metric (as a quantity).
    """
    averageUtilization: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'averageUtilization'})
    averageValue: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'averageValue'})
    value: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'value'})


@attr.s(kw_only=True)
class MetricTarget(K8sObjectBase):
    """
    | MetricTarget defines the target value, average value, or average utilization of a specific metric
    
    :param type: type represents whether the metric type is Utilization, Value, or AverageValue
    :param averageUtilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type
    :param averageValue: averageValue is the target value of the average of the metric across all relevant pods (as a quantity)
    :param value: value is the target value of the metric (as a quantity).
    """
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    averageUtilization: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'averageUtilization'})
    averageValue: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'averageValue'})
    value: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'value'})


@attr.s(kw_only=True)
class MetricStatus(K8sObjectBase):
    """
    | MetricStatus describes the last-read state of a single metric.
    
    :param type: type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each corresponds to a matching field in the object.
    :param external: external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).
    :param object: object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).
    :param pods: pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.
    :param resource: resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.
    """
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    external: Optional[Union[kdsl.autoscaling.v2beta2.ExternalMetricStatus,
        kdsl.autoscaling.v2beta2.ExternalMetricStatusTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'external'})
    object: Optional[Union[kdsl.autoscaling.v2beta2.ObjectMetricStatus,
        kdsl.autoscaling.v2beta2.ObjectMetricStatusTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'object'})
    pods: Optional[Union[kdsl.autoscaling.v2beta2.PodsMetricStatus,
        kdsl.autoscaling.v2beta2.PodsMetricStatusTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'pods'})
    resource: Optional[Union[kdsl.autoscaling.v2beta2.ResourceMetricStatus,
        kdsl.autoscaling.v2beta2.ResourceMetricStatusTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'resource'})


@attr.s(kw_only=True)
class MetricSpec(K8sObjectBase):
    """
    | MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once).
    
    :param type: type is the type of metric source.  It should be one of "Object", "Pods" or "Resource", each mapping to a matching field in the object.
    :param external: external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).
    :param object: object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).
    :param pods: pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.
    :param resource: resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.
    """
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    external: Optional[Union[kdsl.autoscaling.v2beta2.ExternalMetricSource,
        kdsl.autoscaling.v2beta2.ExternalMetricSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'external'})
    object: Optional[Union[kdsl.autoscaling.v2beta2.ObjectMetricSource,
        kdsl.autoscaling.v2beta2.ObjectMetricSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'object'})
    pods: Optional[Union[kdsl.autoscaling.v2beta2.PodsMetricSource,
        kdsl.autoscaling.v2beta2.PodsMetricSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'pods'})
    resource: Optional[Union[kdsl.autoscaling.v2beta2.ResourceMetricSource,
        kdsl.autoscaling.v2beta2.ResourceMetricSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'resource'})


@attr.s(kw_only=True)
class MetricIdentifier(K8sObjectBase):
    """
    | MetricIdentifier defines the name and optionally selector for a metric
    
    :param name: name is the name of the given metric
    :param selector: selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    selector: Optional[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'selector'})


@attr.s(kw_only=True)
class HorizontalPodAutoscalerStatus(K8sObjectBase):
    """
    | HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.
    
    :param conditions: conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.
    :param currentReplicas: currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.
    :param desiredReplicas: desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.
    :param currentMetrics: currentMetrics is the last read state of the metrics used by this autoscaler.
    :param lastScaleTime: lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.
    :param observedGeneration: observedGeneration is the most recent generation observed by this autoscaler.
    """
    conditions: Sequence[Union[
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerCondition,
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerConditionTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'conditions'})
    currentReplicas: int = attr.ib(metadata={'yaml_name': 'currentReplicas'})
    desiredReplicas: int = attr.ib(metadata={'yaml_name': 'desiredReplicas'})
    currentMetrics: Optional[Sequence[Union[
        kdsl.autoscaling.v2beta2.MetricStatus,
        kdsl.autoscaling.v2beta2.MetricStatusTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'currentMetrics'})
    lastScaleTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastScaleTime'})
    observedGeneration: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'observedGeneration'})


@attr.s(kw_only=True)
class HorizontalPodAutoscalerSpec(K8sObjectBase):
    """
    | HorizontalPodAutoscalerSpec describes the desired functionality of the HorizontalPodAutoscaler.
    
    :param maxReplicas: maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.
    :param scaleTargetRef: scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count.
    :param metrics: metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization.
    :param minReplicas: minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.
    """
    maxReplicas: int = attr.ib(metadata={'yaml_name': 'maxReplicas'})
    scaleTargetRef: Union[
        kdsl.autoscaling.v2beta2.CrossVersionObjectReference,
        kdsl.autoscaling.v2beta2.CrossVersionObjectReferenceTypedDict
        ] = attr.ib(metadata={'yaml_name': 'scaleTargetRef'})
    metrics: Optional[Sequence[Union[kdsl.autoscaling.v2beta2.MetricSpec,
        kdsl.autoscaling.v2beta2.MetricSpecTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'metrics'})
    minReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'minReplicas'})


@attr.s(kw_only=True)
class HorizontalPodAutoscalerList(K8sObjectBase):
    """
    | HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects.
    
    :param items: items is the list of horizontal pod autoscaler objects.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: metadata is the standard list metadata.
    """
    items: Sequence[Union[kdsl.autoscaling.v2beta2.HorizontalPodAutoscaler,
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerTypedDict]] = attr.ib(
        metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class HorizontalPodAutoscalerCondition(K8sObjectBase):
    """
    | HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point.
    
    :param status: status is the status of the condition (True, False, Unknown)
    :param type: type describes the current condition
    :param lastTransitionTime: lastTransitionTime is the last time the condition transitioned from one status to another
    :param message: message is a human-readable explanation containing details about the transition
    :param reason: reason is the reason for the condition's last transition.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastTransitionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTransitionTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class HorizontalPodAutoscaler(K8sResourceBase):
    """
    | HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which automatically manages the replica count of any resource implementing the scale subresource based on the metrics specified.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.
    """
    apiVersion: ClassVar[str] = 'autoscaling/v2beta2'
    kind: ClassVar[str] = 'HorizontalPodAutoscaler'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerSpec,
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerSpecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class ExternalMetricStatus(K8sObjectBase):
    """
    | ExternalMetricStatus indicates the current value of a global metric not associated with any Kubernetes object.
    
    :param current: current contains the current value for the given metric
    :param metric: metric identifies the target metric by name and selector
    """
    current: Union[kdsl.autoscaling.v2beta2.MetricValueStatus,
        kdsl.autoscaling.v2beta2.MetricValueStatusTypedDict] = attr.ib(metadata
        ={'yaml_name': 'current'})
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict] = attr.ib(metadata
        ={'yaml_name': 'metric'})


@attr.s(kw_only=True)
class ExternalMetricSource(K8sObjectBase):
    """
    | ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).
    
    :param metric: metric identifies the target metric by name and selector
    :param target: target specifies the target value for the given metric
    """
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict] = attr.ib(metadata
        ={'yaml_name': 'metric'})
    target: Union[kdsl.autoscaling.v2beta2.MetricTarget,
        kdsl.autoscaling.v2beta2.MetricTargetTypedDict] = attr.ib(metadata=
        {'yaml_name': 'target'})


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


class ResourceMetricStatusTypedDict(TypedDict, total=(True)):
    current: Union[kdsl.autoscaling.v2beta2.MetricValueStatus,
        kdsl.autoscaling.v2beta2.MetricValueStatusTypedDict]
    name: str


class ResourceMetricSourceTypedDict(TypedDict, total=(True)):
    name: str
    target: Union[kdsl.autoscaling.v2beta2.MetricTarget,
        kdsl.autoscaling.v2beta2.MetricTargetTypedDict]


class PodsMetricStatusTypedDict(TypedDict, total=(True)):
    current: Union[kdsl.autoscaling.v2beta2.MetricValueStatus,
        kdsl.autoscaling.v2beta2.MetricValueStatusTypedDict]
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict]


class PodsMetricSourceTypedDict(TypedDict, total=(True)):
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict]
    target: Union[kdsl.autoscaling.v2beta2.MetricTarget,
        kdsl.autoscaling.v2beta2.MetricTargetTypedDict]


class ObjectMetricStatusTypedDict(TypedDict, total=(True)):
    current: Union[kdsl.autoscaling.v2beta2.MetricValueStatus,
        kdsl.autoscaling.v2beta2.MetricValueStatusTypedDict]
    describedObject: Union[
        kdsl.autoscaling.v2beta2.CrossVersionObjectReference,
        kdsl.autoscaling.v2beta2.CrossVersionObjectReferenceTypedDict]
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict]


class ObjectMetricSourceTypedDict(TypedDict, total=(True)):
    describedObject: Union[
        kdsl.autoscaling.v2beta2.CrossVersionObjectReference,
        kdsl.autoscaling.v2beta2.CrossVersionObjectReferenceTypedDict]
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict]
    target: Union[kdsl.autoscaling.v2beta2.MetricTarget,
        kdsl.autoscaling.v2beta2.MetricTargetTypedDict]


class MetricValueStatusTypedDict(TypedDict, total=(False)):
    averageUtilization: int
    averageValue: str
    value: str


class MetricTargetOptionalTypedDict(TypedDict, total=(False)):
    averageUtilization: int
    averageValue: str
    value: str


class MetricTargetTypedDict(MetricTargetOptionalTypedDict, total=(True)):
    type: str


class MetricStatusOptionalTypedDict(TypedDict, total=(False)):
    external: Union[kdsl.autoscaling.v2beta2.ExternalMetricStatus,
        kdsl.autoscaling.v2beta2.ExternalMetricStatusTypedDict]
    object: Union[kdsl.autoscaling.v2beta2.ObjectMetricStatus,
        kdsl.autoscaling.v2beta2.ObjectMetricStatusTypedDict]
    pods: Union[kdsl.autoscaling.v2beta2.PodsMetricStatus,
        kdsl.autoscaling.v2beta2.PodsMetricStatusTypedDict]
    resource: Union[kdsl.autoscaling.v2beta2.ResourceMetricStatus,
        kdsl.autoscaling.v2beta2.ResourceMetricStatusTypedDict]


class MetricStatusTypedDict(MetricStatusOptionalTypedDict, total=(True)):
    type: str


class MetricSpecOptionalTypedDict(TypedDict, total=(False)):
    external: Union[kdsl.autoscaling.v2beta2.ExternalMetricSource,
        kdsl.autoscaling.v2beta2.ExternalMetricSourceTypedDict]
    object: Union[kdsl.autoscaling.v2beta2.ObjectMetricSource,
        kdsl.autoscaling.v2beta2.ObjectMetricSourceTypedDict]
    pods: Union[kdsl.autoscaling.v2beta2.PodsMetricSource,
        kdsl.autoscaling.v2beta2.PodsMetricSourceTypedDict]
    resource: Union[kdsl.autoscaling.v2beta2.ResourceMetricSource,
        kdsl.autoscaling.v2beta2.ResourceMetricSourceTypedDict]


class MetricSpecTypedDict(MetricSpecOptionalTypedDict, total=(True)):
    type: str


class MetricIdentifierOptionalTypedDict(TypedDict, total=(False)):
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]


class MetricIdentifierTypedDict(MetricIdentifierOptionalTypedDict, total=(True)
    ):
    name: str


class HorizontalPodAutoscalerStatusOptionalTypedDict(TypedDict, total=(False)):
    currentMetrics: Sequence[Union[kdsl.autoscaling.v2beta2.MetricStatus,
        kdsl.autoscaling.v2beta2.MetricStatusTypedDict]]
    lastScaleTime: str
    observedGeneration: int


class HorizontalPodAutoscalerStatusTypedDict(
    HorizontalPodAutoscalerStatusOptionalTypedDict, total=(True)):
    conditions: Sequence[Union[
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerCondition,
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerConditionTypedDict]]
    currentReplicas: int
    desiredReplicas: int


class HorizontalPodAutoscalerSpecOptionalTypedDict(TypedDict, total=(False)):
    metrics: Sequence[Union[kdsl.autoscaling.v2beta2.MetricSpec,
        kdsl.autoscaling.v2beta2.MetricSpecTypedDict]]
    minReplicas: int


class HorizontalPodAutoscalerSpecTypedDict(
    HorizontalPodAutoscalerSpecOptionalTypedDict, total=(True)):
    maxReplicas: int
    scaleTargetRef: Union[
        kdsl.autoscaling.v2beta2.CrossVersionObjectReference,
        kdsl.autoscaling.v2beta2.CrossVersionObjectReferenceTypedDict]


class HorizontalPodAutoscalerListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class HorizontalPodAutoscalerListTypedDict(
    HorizontalPodAutoscalerListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.autoscaling.v2beta2.HorizontalPodAutoscaler,
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerTypedDict]]


class HorizontalPodAutoscalerConditionOptionalTypedDict(TypedDict, total=(
    False)):
    lastTransitionTime: str
    message: str
    reason: str


class HorizontalPodAutoscalerConditionTypedDict(
    HorizontalPodAutoscalerConditionOptionalTypedDict, total=(True)):
    status: str
    type: str


class HorizontalPodAutoscalerOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerSpec,
        kdsl.autoscaling.v2beta2.HorizontalPodAutoscalerSpecTypedDict]


class HorizontalPodAutoscalerTypedDict(HorizontalPodAutoscalerOptionalTypedDict
    , total=(True)):
    name: str
    namespace: str


class ExternalMetricStatusTypedDict(TypedDict, total=(True)):
    current: Union[kdsl.autoscaling.v2beta2.MetricValueStatus,
        kdsl.autoscaling.v2beta2.MetricValueStatusTypedDict]
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict]


class ExternalMetricSourceTypedDict(TypedDict, total=(True)):
    metric: Union[kdsl.autoscaling.v2beta2.MetricIdentifier,
        kdsl.autoscaling.v2beta2.MetricIdentifierTypedDict]
    target: Union[kdsl.autoscaling.v2beta2.MetricTarget,
        kdsl.autoscaling.v2beta2.MetricTargetTypedDict]


class CrossVersionObjectReferenceOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str


class CrossVersionObjectReferenceTypedDict(
    CrossVersionObjectReferenceOptionalTypedDict, total=(True)):
    kind: str
    name: str
