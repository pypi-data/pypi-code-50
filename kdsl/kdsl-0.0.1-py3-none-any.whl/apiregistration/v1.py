from __future__ import annotations
import kdsl.meta.v1
import kdsl.apiregistration.v1
import attr
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class ServiceReference(K8sObjectBase):
    """
    | ServiceReference holds a reference to Service.legacy.k8s.io
    
    :param name: Name is the name of the service
    :param namespace: Namespace is the namespace of the service
    :param port: If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive).
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    namespace: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'namespace'})
    port: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'port'})


@attr.s(kw_only=True)
class APIServiceStatus(K8sObjectBase):
    """
    | APIServiceStatus contains derived information about an API server
    
    :param conditions: Current service state of apiService.
    """
    conditions: Optional[Sequence[Union[
        kdsl.apiregistration.v1.APIServiceCondition,
        kdsl.apiregistration.v1.APIServiceConditionTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'conditions'})


@attr.s(kw_only=True)
class APIServiceSpec(K8sObjectBase):
    """
    | APIServiceSpec contains information for locating and communicating with a server. Only https is supported, though you are able to disable certificate verification.
    
    :param groupPriorityMinimum: GroupPriorityMininum is the priority this group should have at least. Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s
    :param service: Service is a reference to the service for this API server.  It must communicate on port 443 If the Service is nil, that means the handling for the API groupversion is handled locally on this server. The call will simply delegate to the normal handler chain to be fulfilled.
    :param versionPriority: VersionPriority controls the ordering of this API version inside of its group.  Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.
    :param caBundle: CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate. If unspecified, system trust roots on the apiserver are used.
    :param group: Group is the API group name this server hosts
    :param insecureSkipTLSVerify: InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged.  You should use the CABundle instead.
    :param version: Version is the API version this server hosts.  For example, "v1"
    """
    groupPriorityMinimum: int = attr.ib(metadata={'yaml_name':
        'groupPriorityMinimum'})
    service: Union[kdsl.apiregistration.v1.ServiceReference,
        kdsl.apiregistration.v1.ServiceReferenceTypedDict] = attr.ib(metadata
        ={'yaml_name': 'service'})
    versionPriority: int = attr.ib(metadata={'yaml_name': 'versionPriority'})
    caBundle: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caBundle'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    insecureSkipTLSVerify: Optional[bool] = attr.ib(default=None, metadata=
        {'yaml_name': 'insecureSkipTLSVerify'})
    version: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'version'})


@attr.s(kw_only=True)
class APIServiceList(K8sObjectBase):
    """
    | APIServiceList is a list of APIService objects.
    
    :param items: None
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: None
    """
    items: Sequence[Union[kdsl.apiregistration.v1.APIService,
        kdsl.apiregistration.v1.APIServiceTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class APIServiceCondition(K8sObjectBase):
    """
    | APIServiceCondition describes the state of an APIService at a particular point
    
    :param status: Status is the status of the condition. Can be True, False, Unknown.
    :param type: Type is the type of the condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
    :param message: Human-readable message indicating details about last transition.
    :param reason: Unique, one-word, CamelCase reason for the condition's last transition.
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
class APIService(K8sResourceBase):
    """
    | APIService represents a server for a particular GroupVersion. Name must be "version.group".
    
    :param name: metadata.name
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec contains information for locating and communicating with a server
    """
    apiVersion: ClassVar[str] = 'apiregistration.k8s.io/v1'
    kind: ClassVar[str] = 'APIService'
    name: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.apiregistration.v1.APIServiceSpec,
        kdsl.apiregistration.v1.APIServiceSpecTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'spec'})


class ServiceReferenceTypedDict(TypedDict, total=(False)):
    name: str
    namespace: str
    port: int


class APIServiceStatusTypedDict(TypedDict, total=(False)):
    conditions: Sequence[Union[kdsl.apiregistration.v1.APIServiceCondition,
        kdsl.apiregistration.v1.APIServiceConditionTypedDict]]


class APIServiceSpecOptionalTypedDict(TypedDict, total=(False)):
    caBundle: str
    group: str
    insecureSkipTLSVerify: bool
    version: str


class APIServiceSpecTypedDict(APIServiceSpecOptionalTypedDict, total=(True)):
    groupPriorityMinimum: int
    service: Union[kdsl.apiregistration.v1.ServiceReference,
        kdsl.apiregistration.v1.ServiceReferenceTypedDict]
    versionPriority: int


class APIServiceListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class APIServiceListTypedDict(APIServiceListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.apiregistration.v1.APIService,
        kdsl.apiregistration.v1.APIServiceTypedDict]]


class APIServiceConditionOptionalTypedDict(TypedDict, total=(False)):
    lastTransitionTime: str
    message: str
    reason: str


class APIServiceConditionTypedDict(APIServiceConditionOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class APIServiceOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.apiregistration.v1.APIServiceSpec,
        kdsl.apiregistration.v1.APIServiceSpecTypedDict]


class APIServiceTypedDict(APIServiceOptionalTypedDict, total=(True)):
    name: str
