from __future__ import annotations
import kdsl.meta.v1
import attr
import kdsl.coordination.v1beta1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class LeaseSpec(K8sObjectBase):
    """
    | LeaseSpec is a specification of a Lease.
    
    :param acquireTime: acquireTime is a time when the current lease was acquired.
    :param holderIdentity: holderIdentity contains the identity of the holder of a current lease.
    :param leaseDurationSeconds: leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed RenewTime.
    :param leaseTransitions: leaseTransitions is the number of transitions of a lease between holders.
    :param renewTime: renewTime is a time when the current holder of a lease has last updated the lease.
    """
    acquireTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'acquireTime'})
    holderIdentity: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'holderIdentity'})
    leaseDurationSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'leaseDurationSeconds'})
    leaseTransitions: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'leaseTransitions'})
    renewTime: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'renewTime'})


@attr.s(kw_only=True)
class LeaseList(K8sObjectBase):
    """
    | LeaseList is a list of Lease objects.
    
    :param items: Items is a list of schema objects.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.coordination.v1beta1.Lease,
        kdsl.coordination.v1beta1.LeaseTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class Lease(K8sResourceBase):
    """
    | Lease defines a lease concept.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'coordination.k8s.io/v1beta1'
    kind: ClassVar[str] = 'Lease'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.coordination.v1beta1.LeaseSpec,
        kdsl.coordination.v1beta1.LeaseSpecTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'spec'})


class LeaseSpecTypedDict(TypedDict, total=(False)):
    acquireTime: str
    holderIdentity: str
    leaseDurationSeconds: int
    leaseTransitions: int
    renewTime: str


class LeaseListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class LeaseListTypedDict(LeaseListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.coordination.v1beta1.Lease,
        kdsl.coordination.v1beta1.LeaseTypedDict]]


class LeaseOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.coordination.v1beta1.LeaseSpec,
        kdsl.coordination.v1beta1.LeaseSpecTypedDict]


class LeaseTypedDict(LeaseOptionalTypedDict, total=(True)):
    name: str
    namespace: str
