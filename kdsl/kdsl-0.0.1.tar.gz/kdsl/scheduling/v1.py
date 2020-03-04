from __future__ import annotations
import attr
import kdsl.meta.v1
import kdsl.scheduling.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class PriorityClassList(K8sObjectBase):
    """
    | PriorityClassList is a collection of priority classes.
    
    :param items: items is the list of PriorityClasses
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.scheduling.v1.PriorityClass,
        kdsl.scheduling.v1.PriorityClassTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class PriorityClass(K8sResourceBase):
    """
    | PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer.
    
    :param name: metadata.name
    :param value: The value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.
    :param annotations: metadata.annotations
    :param description: description is an arbitrary string that usually provides guidelines on when this priority class should be used.
    :param globalDefault: globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.
    :param labels: metadata.labels
    :param preemptionPolicy: PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.
    """
    apiVersion: ClassVar[str] = 'scheduling.k8s.io/v1'
    kind: ClassVar[str] = 'PriorityClass'
    name: str = attr.ib(metadata={'yaml_name': None})
    value: int = attr.ib(metadata={'yaml_name': 'value'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    description: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'description'})
    globalDefault: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'globalDefault'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    preemptionPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'preemptionPolicy'})


class PriorityClassListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class PriorityClassListTypedDict(PriorityClassListOptionalTypedDict, total=
    (True)):
    items: Sequence[Union[kdsl.scheduling.v1.PriorityClass,
        kdsl.scheduling.v1.PriorityClassTypedDict]]


class PriorityClassOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    description: str
    globalDefault: bool
    labels: Mapping[str, str]
    preemptionPolicy: str


class PriorityClassTypedDict(PriorityClassOptionalTypedDict, total=(True)):
    name: str
    value: int
