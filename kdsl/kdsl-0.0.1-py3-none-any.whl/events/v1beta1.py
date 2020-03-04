from __future__ import annotations
import kdsl.events.v1beta1
import kdsl.meta.v1
import kdsl.core.v1
import attr
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class EventSeries(K8sObjectBase):
    """
    | EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.
    
    :param count: Number of occurrences in this series up to the last heartbeat time
    :param lastObservedTime: Time when last Event from the series was seen before last heartbeat.
    :param state: Information whether this series is ongoing or finished. Deprecated. Planned removal for 1.18
    """
    count: int = attr.ib(metadata={'yaml_name': 'count'})
    lastObservedTime: str = attr.ib(metadata={'yaml_name': 'lastObservedTime'})
    state: str = attr.ib(metadata={'yaml_name': 'state'})


@attr.s(kw_only=True)
class EventList(K8sObjectBase):
    """
    | EventList is a list of Event objects.
    
    :param items: Items is a list of schema objects.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.events.v1beta1.Event,
        kdsl.events.v1beta1.EventTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class Event(K8sResourceBase):
    """
    | Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system.
    
    :param eventTime: Required. Time when this Event was first observed.
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param action: What action was taken/failed regarding to the regarding object.
    :param annotations: metadata.annotations
    :param deprecatedCount: Deprecated field assuring backward compatibility with core.v1 Event type
    :param deprecatedFirstTimestamp: Deprecated field assuring backward compatibility with core.v1 Event type
    :param deprecatedLastTimestamp: Deprecated field assuring backward compatibility with core.v1 Event type
    :param deprecatedSource: Deprecated field assuring backward compatibility with core.v1 Event type
    :param labels: metadata.labels
    :param note: Optional. A human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
    :param reason: Why the action was taken.
    :param regarding: The object this Event is about. In most cases it's an Object reporting controller implements. E.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
    :param related: Optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
    :param reportingController: Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.
    :param reportingInstance: ID of the controller instance, e.g. `kubelet-xyzf`.
    :param series: Data about the Event series this event represents or nil if it's a singleton Event.
    :param type: Type of this event (Normal, Warning), new types could be added in the future.
    """
    apiVersion: ClassVar[str] = 'events.k8s.io/v1beta1'
    kind: ClassVar[str] = 'Event'
    eventTime: str = attr.ib(metadata={'yaml_name': 'eventTime'})
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    action: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'action'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    deprecatedCount: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'deprecatedCount'})
    deprecatedFirstTimestamp: Optional[str] = attr.ib(default=None,
        metadata={'yaml_name': 'deprecatedFirstTimestamp'})
    deprecatedLastTimestamp: Optional[str] = attr.ib(default=None, metadata
        ={'yaml_name': 'deprecatedLastTimestamp'})
    deprecatedSource: Optional[Union[kdsl.core.v1.EventSource,
        kdsl.core.v1.EventSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'deprecatedSource'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    note: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'note'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})
    regarding: Optional[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'regarding'})
    related: Optional[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'related'})
    reportingController: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'reportingController'})
    reportingInstance: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'reportingInstance'})
    series: Optional[Union[kdsl.events.v1beta1.EventSeries,
        kdsl.events.v1beta1.EventSeriesTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'series'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


class EventSeriesTypedDict(TypedDict, total=(True)):
    count: int
    lastObservedTime: str
    state: str


class EventListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class EventListTypedDict(EventListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.events.v1beta1.Event,
        kdsl.events.v1beta1.EventTypedDict]]


class EventOptionalTypedDict(TypedDict, total=(False)):
    action: str
    annotations: Mapping[str, str]
    deprecatedCount: int
    deprecatedFirstTimestamp: str
    deprecatedLastTimestamp: str
    deprecatedSource: Union[kdsl.core.v1.EventSource,
        kdsl.core.v1.EventSourceTypedDict]
    labels: Mapping[str, str]
    note: str
    reason: str
    regarding: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]
    related: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]
    reportingController: str
    reportingInstance: str
    series: Union[kdsl.events.v1beta1.EventSeries,
        kdsl.events.v1beta1.EventSeriesTypedDict]
    type: str


class EventTypedDict(EventOptionalTypedDict, total=(True)):
    eventTime: str
    name: str
    namespace: str
