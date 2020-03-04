from __future__ import annotations
import kdsl.meta.v1
import kdsl.networking.v1beta1
import attr
import kdsl.core.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class IngressTLS(K8sObjectBase):
    """
    | IngressTLS describes the transport layer security associated with an Ingress.
    
    :param hosts: Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.
    :param secretName: SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.
    """
    hosts: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'hosts'})
    secretName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretName'})


@attr.s(kw_only=True)
class IngressStatus(K8sObjectBase):
    """
    | IngressStatus describe the current state of the Ingress.
    
    :param loadBalancer: LoadBalancer contains the current status of the load-balancer.
    """
    loadBalancer: Optional[Union[kdsl.core.v1.LoadBalancerStatus,
        kdsl.core.v1.LoadBalancerStatusTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'loadBalancer'})


@attr.s(kw_only=True)
class IngressSpec(K8sObjectBase):
    """
    | IngressSpec describes the Ingress the user wishes to exist.
    
    :param backend: A default backend capable of servicing requests that don't match any rule. At least one of 'backend' or 'rules' must be specified. This field is optional to allow the loadbalancer controller or defaulting logic to specify a global default.
    :param rules: A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.
    :param tls: TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.
    """
    backend: Optional[Union[kdsl.networking.v1beta1.IngressBackend,
        kdsl.networking.v1beta1.IngressBackendTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'backend'})
    rules: Optional[Sequence[Union[kdsl.networking.v1beta1.IngressRule,
        kdsl.networking.v1beta1.IngressRuleTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'rules'})
    tls: Optional[Sequence[Union[kdsl.networking.v1beta1.IngressTLS,
        kdsl.networking.v1beta1.IngressTLSTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'tls'})


@attr.s(kw_only=True)
class IngressRule(K8sObjectBase):
    """
    | IngressRule represents the rules mapping the paths under a specified host to the related backend services. Incoming requests are first evaluated for a host match, then routed to the backend associated with the matching IngressRuleValue.
    
    :param host: Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the
    	  IP in the Spec of the parent Ingress.
    2. The `:` delimiter is not respected because ports are not allowed.
    	  Currently the port of an Ingress is implicitly :80 for http and
    	  :443 for https.
    Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.
    :param http: None
    """
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    http: Optional[Union[kdsl.networking.v1beta1.HTTPIngressRuleValue,
        kdsl.networking.v1beta1.HTTPIngressRuleValueTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'http'})


@attr.s(kw_only=True)
class IngressList(K8sObjectBase):
    """
    | IngressList is a collection of Ingress.
    
    :param items: Items is the list of Ingress.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.networking.v1beta1.Ingress,
        kdsl.networking.v1beta1.IngressTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class IngressBackend(K8sObjectBase):
    """
    | IngressBackend describes all endpoints for a given service and port.
    
    :param serviceName: Specifies the name of the referenced service.
    :param servicePort: Specifies the port of the referenced service.
    """
    serviceName: str = attr.ib(metadata={'yaml_name': 'serviceName'})
    servicePort: Union[int, str] = attr.ib(metadata={'yaml_name':
        'servicePort'})


@attr.s(kw_only=True)
class Ingress(K8sResourceBase):
    """
    | Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec is the desired state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'networking.k8s.io/v1beta1'
    kind: ClassVar[str] = 'Ingress'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.networking.v1beta1.IngressSpec,
        kdsl.networking.v1beta1.IngressSpecTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class HTTPIngressRuleValue(K8sObjectBase):
    """
    | HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'.
    
    :param paths: A collection of paths that map requests to backends.
    """
    paths: Sequence[Union[kdsl.networking.v1beta1.HTTPIngressPath,
        kdsl.networking.v1beta1.HTTPIngressPathTypedDict]] = attr.ib(metadata
        ={'yaml_name': 'paths'})


@attr.s(kw_only=True)
class HTTPIngressPath(K8sObjectBase):
    """
    | HTTPIngressPath associates a path regex with a backend. Incoming urls matching the path are forwarded to the backend.
    
    :param backend: Backend defines the referenced service endpoint to which the traffic will be forwarded to.
    :param path: Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a catch all sending traffic to the backend.
    """
    backend: Union[kdsl.networking.v1beta1.IngressBackend,
        kdsl.networking.v1beta1.IngressBackendTypedDict] = attr.ib(metadata
        ={'yaml_name': 'backend'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})


class IngressTLSTypedDict(TypedDict, total=(False)):
    hosts: Sequence[str]
    secretName: str


class IngressStatusTypedDict(TypedDict, total=(False)):
    loadBalancer: Union[kdsl.core.v1.LoadBalancerStatus,
        kdsl.core.v1.LoadBalancerStatusTypedDict]


class IngressSpecTypedDict(TypedDict, total=(False)):
    backend: Union[kdsl.networking.v1beta1.IngressBackend,
        kdsl.networking.v1beta1.IngressBackendTypedDict]
    rules: Sequence[Union[kdsl.networking.v1beta1.IngressRule,
        kdsl.networking.v1beta1.IngressRuleTypedDict]]
    tls: Sequence[Union[kdsl.networking.v1beta1.IngressTLS,
        kdsl.networking.v1beta1.IngressTLSTypedDict]]


class IngressRuleTypedDict(TypedDict, total=(False)):
    host: str
    http: Union[kdsl.networking.v1beta1.HTTPIngressRuleValue,
        kdsl.networking.v1beta1.HTTPIngressRuleValueTypedDict]


class IngressListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class IngressListTypedDict(IngressListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.networking.v1beta1.Ingress,
        kdsl.networking.v1beta1.IngressTypedDict]]


class IngressBackendTypedDict(TypedDict, total=(True)):
    serviceName: str
    servicePort: Union[int, str]


class IngressOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.networking.v1beta1.IngressSpec,
        kdsl.networking.v1beta1.IngressSpecTypedDict]


class IngressTypedDict(IngressOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class HTTPIngressRuleValueTypedDict(TypedDict, total=(True)):
    paths: Sequence[Union[kdsl.networking.v1beta1.HTTPIngressPath,
        kdsl.networking.v1beta1.HTTPIngressPathTypedDict]]


class HTTPIngressPathOptionalTypedDict(TypedDict, total=(False)):
    path: str


class HTTPIngressPathTypedDict(HTTPIngressPathOptionalTypedDict, total=(True)):
    backend: Union[kdsl.networking.v1beta1.IngressBackend,
        kdsl.networking.v1beta1.IngressBackendTypedDict]
