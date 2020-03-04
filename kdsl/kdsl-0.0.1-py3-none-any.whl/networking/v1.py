from __future__ import annotations
import attr
import kdsl.meta.v1
import kdsl.networking.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class NetworkPolicySpec(K8sObjectBase):
    """
    | NetworkPolicySpec provides the specification of a NetworkPolicy
    
    :param podSelector: Selects the pods to which this NetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.
    :param egress: List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8
    :param ingress: List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)
    :param policyTypes: List of rule types that the NetworkPolicy relates to. Valid options are "Ingress", "Egress", or "Ingress,Egress". If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include "Egress" (since such a policy would not include an Egress section and would otherwise default to just [ "Ingress" ]). This field is beta-level in 1.8
    """
    podSelector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict] = attr.ib(metadata={
        'yaml_name': 'podSelector'})
    egress: Optional[Sequence[Union[
        kdsl.networking.v1.NetworkPolicyEgressRule,
        kdsl.networking.v1.NetworkPolicyEgressRuleTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'egress'})
    ingress: Optional[Sequence[Union[
        kdsl.networking.v1.NetworkPolicyIngressRule,
        kdsl.networking.v1.NetworkPolicyIngressRuleTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'ingress'})
    policyTypes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'policyTypes'})


@attr.s(kw_only=True)
class NetworkPolicyPort(K8sObjectBase):
    """
    | NetworkPolicyPort describes a port to allow traffic on
    
    :param port: The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers.
    :param protocol: The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.
    """
    port: Optional[Union[int, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'port'})
    protocol: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'protocol'})


@attr.s(kw_only=True)
class NetworkPolicyPeer(K8sObjectBase):
    """
    | NetworkPolicyPeer describes a peer to allow traffic from. Only certain combinations of fields are allowed
    
    :param ipBlock: IPBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be.
    :param namespaceSelector: Selects Namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.
    
    If PodSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods in the Namespaces selected by NamespaceSelector.
    :param podSelector: This is a label selector which selects Pods. This field follows standard label selector semantics; if present but empty, it selects all pods.
    
    If NamespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the Pods matching PodSelector in the policy's own Namespace.
    """
    ipBlock: Optional[Union[kdsl.networking.v1.IPBlock,
        kdsl.networking.v1.IPBlockTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'ipBlock'})
    namespaceSelector: Optional[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'namespaceSelector'})
    podSelector: Optional[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'podSelector'})


@attr.s(kw_only=True)
class NetworkPolicyList(K8sObjectBase):
    """
    | NetworkPolicyList is a list of NetworkPolicy objects.
    
    :param items: Items is a list of schema objects.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.networking.v1.NetworkPolicy,
        kdsl.networking.v1.NetworkPolicyTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class NetworkPolicyIngressRule(K8sObjectBase):
    """
    | NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and from.
    
    :param from_: List of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list.
    :param ports: List of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.
    """
    from_: Optional[Sequence[Union[kdsl.networking.v1.NetworkPolicyPeer,
        kdsl.networking.v1.NetworkPolicyPeerTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'from'})
    ports: Optional[Sequence[Union[kdsl.networking.v1.NetworkPolicyPort,
        kdsl.networking.v1.NetworkPolicyPortTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'ports'})


@attr.s(kw_only=True)
class NetworkPolicyEgressRule(K8sObjectBase):
    """
    | NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and to. This type is beta-level in 1.8
    
    :param ports: List of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.
    :param to: List of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list.
    """
    ports: Optional[Sequence[Union[kdsl.networking.v1.NetworkPolicyPort,
        kdsl.networking.v1.NetworkPolicyPortTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'ports'})
    to: Optional[Sequence[Union[kdsl.networking.v1.NetworkPolicyPeer,
        kdsl.networking.v1.NetworkPolicyPeerTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'to'})


@attr.s(kw_only=True)
class NetworkPolicy(K8sResourceBase):
    """
    | NetworkPolicy describes what network traffic is allowed for a set of Pods
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Specification of the desired behavior for this NetworkPolicy.
    """
    apiVersion: ClassVar[str] = 'networking.k8s.io/v1'
    kind: ClassVar[str] = 'NetworkPolicy'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.networking.v1.NetworkPolicySpec,
        kdsl.networking.v1.NetworkPolicySpecTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class IPBlock(K8sObjectBase):
    """
    | IPBlock describes a particular CIDR (Ex. "192.168.1.1/24") that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The except entry describes CIDRs that should not be included within this rule.
    
    :param cidr: CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24"
    :param except_: Except is a slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" Except values will be rejected if they are outside the CIDR range
    """
    cidr: str = attr.ib(metadata={'yaml_name': 'cidr'})
    except_: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'except'})


class NetworkPolicySpecOptionalTypedDict(TypedDict, total=(False)):
    egress: Sequence[Union[kdsl.networking.v1.NetworkPolicyEgressRule,
        kdsl.networking.v1.NetworkPolicyEgressRuleTypedDict]]
    ingress: Sequence[Union[kdsl.networking.v1.NetworkPolicyIngressRule,
        kdsl.networking.v1.NetworkPolicyIngressRuleTypedDict]]
    policyTypes: Sequence[str]


class NetworkPolicySpecTypedDict(NetworkPolicySpecOptionalTypedDict, total=
    (True)):
    podSelector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]


class NetworkPolicyPortTypedDict(TypedDict, total=(False)):
    port: Union[int, str]
    protocol: str


class NetworkPolicyPeerTypedDict(TypedDict, total=(False)):
    ipBlock: Union[kdsl.networking.v1.IPBlock,
        kdsl.networking.v1.IPBlockTypedDict]
    namespaceSelector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]
    podSelector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]


class NetworkPolicyListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class NetworkPolicyListTypedDict(NetworkPolicyListOptionalTypedDict, total=
    (True)):
    items: Sequence[Union[kdsl.networking.v1.NetworkPolicy,
        kdsl.networking.v1.NetworkPolicyTypedDict]]


class NetworkPolicyIngressRuleTypedDict(TypedDict, total=(False)):
    from_: Sequence[Union[kdsl.networking.v1.NetworkPolicyPeer,
        kdsl.networking.v1.NetworkPolicyPeerTypedDict]]
    ports: Sequence[Union[kdsl.networking.v1.NetworkPolicyPort,
        kdsl.networking.v1.NetworkPolicyPortTypedDict]]


class NetworkPolicyEgressRuleTypedDict(TypedDict, total=(False)):
    ports: Sequence[Union[kdsl.networking.v1.NetworkPolicyPort,
        kdsl.networking.v1.NetworkPolicyPortTypedDict]]
    to: Sequence[Union[kdsl.networking.v1.NetworkPolicyPeer,
        kdsl.networking.v1.NetworkPolicyPeerTypedDict]]


class NetworkPolicyOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.networking.v1.NetworkPolicySpec,
        kdsl.networking.v1.NetworkPolicySpecTypedDict]


class NetworkPolicyTypedDict(NetworkPolicyOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class IPBlockOptionalTypedDict(TypedDict, total=(False)):
    except_: Sequence[str]


class IPBlockTypedDict(IPBlockOptionalTypedDict, total=(True)):
    cidr: str
