from __future__ import annotations
import kdsl.meta.v1
import kdsl.core.v1
import kdsl.discovery.v1beta1
import attr
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class EndpointSliceList(K8sObjectBase):
    """
    | EndpointSliceList represents a list of endpoint slices
    
    :param items: List of endpoint slices
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata.
    """
    items: Sequence[Union[kdsl.discovery.v1beta1.EndpointSlice,
        kdsl.discovery.v1beta1.EndpointSliceTypedDict]] = attr.ib(metadata=
        {'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class EndpointSlice(K8sResourceBase):
    """
    | EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.
    
    :param addressType: addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.
    :param endpoints: endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param ports: ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
    """
    apiVersion: ClassVar[str] = 'discovery.k8s.io/v1beta1'
    kind: ClassVar[str] = 'EndpointSlice'
    addressType: str = attr.ib(metadata={'yaml_name': 'addressType'})
    endpoints: Sequence[Union[kdsl.discovery.v1beta1.Endpoint,
        kdsl.discovery.v1beta1.EndpointTypedDict]] = attr.ib(metadata={
        'yaml_name': 'endpoints'})
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    ports: Optional[Sequence[Union[kdsl.discovery.v1beta1.EndpointPort,
        kdsl.discovery.v1beta1.EndpointPortTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'ports'})


@attr.s(kw_only=True)
class EndpointPort(K8sObjectBase):
    """
    | EndpointPort represents a Port used by an EndpointSlice
    
    :param appProtocol: The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and http://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names. Default is empty string.
    :param name: The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
    :param port: The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
    :param protocol: The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
    """
    appProtocol: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'appProtocol'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    port: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'port'})
    protocol: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'protocol'})


@attr.s(kw_only=True)
class EndpointConditions(K8sObjectBase):
    """
    | EndpointConditions represents the current condition of an endpoint.
    
    :param ready: ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready.
    """
    ready: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'ready'})


@attr.s(kw_only=True)
class Endpoint(K8sObjectBase):
    """
    | Endpoint represents a single logical "backend" implementing a service.
    
    :param addresses: addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
    :param conditions: conditions contains information about the current status of the endpoint.
    :param hostname: hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.
    :param targetRef: targetRef is a reference to a Kubernetes object that represents this endpoint.
    :param topology: topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node
      where the endpoint is located. This should match the corresponding
      node label.
    * topology.kubernetes.io/zone: the value indicates the zone where the
      endpoint is located. This should match the corresponding node label.
    * topology.kubernetes.io/region: the value indicates the region where the
      endpoint is located. This should match the corresponding node label.
    """
    addresses: Sequence[str] = attr.ib(metadata={'yaml_name': 'addresses'})
    conditions: Optional[Union[kdsl.discovery.v1beta1.EndpointConditions,
        kdsl.discovery.v1beta1.EndpointConditionsTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'conditions'})
    hostname: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'hostname'})
    targetRef: Optional[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'targetRef'})
    topology: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'topology'})


class EndpointSliceListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class EndpointSliceListTypedDict(EndpointSliceListOptionalTypedDict, total=
    (True)):
    items: Sequence[Union[kdsl.discovery.v1beta1.EndpointSlice,
        kdsl.discovery.v1beta1.EndpointSliceTypedDict]]


class EndpointSliceOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    ports: Sequence[Union[kdsl.discovery.v1beta1.EndpointPort,
        kdsl.discovery.v1beta1.EndpointPortTypedDict]]


class EndpointSliceTypedDict(EndpointSliceOptionalTypedDict, total=(True)):
    addressType: str
    endpoints: Sequence[Union[kdsl.discovery.v1beta1.Endpoint,
        kdsl.discovery.v1beta1.EndpointTypedDict]]
    name: str
    namespace: str


class EndpointPortTypedDict(TypedDict, total=(False)):
    appProtocol: str
    name: str
    port: int
    protocol: str


class EndpointConditionsTypedDict(TypedDict, total=(False)):
    ready: bool


class EndpointOptionalTypedDict(TypedDict, total=(False)):
    conditions: Union[kdsl.discovery.v1beta1.EndpointConditions,
        kdsl.discovery.v1beta1.EndpointConditionsTypedDict]
    hostname: str
    targetRef: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]
    topology: Mapping[str, str]


class EndpointTypedDict(EndpointOptionalTypedDict, total=(True)):
    addresses: Sequence[str]
