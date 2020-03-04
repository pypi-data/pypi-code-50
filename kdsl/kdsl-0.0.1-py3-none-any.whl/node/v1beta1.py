from __future__ import annotations
import kdsl.meta.v1
import kdsl.node.v1beta1
import kdsl.core.v1
import attr
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class Scheduling(K8sObjectBase):
    """
    | Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass.
    
    :param nodeSelector: nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.
    :param tolerations: tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.
    """
    nodeSelector: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeSelector'})
    tolerations: Optional[Sequence[Union[kdsl.core.v1.Toleration,
        kdsl.core.v1.TolerationTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'tolerations'})


@attr.s(kw_only=True)
class RuntimeClassList(K8sObjectBase):
    """
    | RuntimeClassList is a list of RuntimeClass objects.
    
    :param items: Items is a list of schema objects.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.node.v1beta1.RuntimeClass,
        kdsl.node.v1beta1.RuntimeClassTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class RuntimeClass(K8sResourceBase):
    """
    | RuntimeClass defines a class of container runtime supported in the cluster. The RuntimeClass is used to determine which container runtime is used to run all containers in a pod. RuntimeClasses are (currently) manually defined by a user or cluster provisioner, and referenced in the PodSpec. The Kubelet is responsible for resolving the RuntimeClassName reference before running the pod.  For more details, see https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md
    
    :param handler: Handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must conform to the DNS Label (RFC 1123) requirements, and is immutable.
    :param name: metadata.name
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param overhead: Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.15, and is only honored by servers that enable the PodOverhead feature.
    :param scheduling: Scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.
    """
    apiVersion: ClassVar[str] = 'node.k8s.io/v1beta1'
    kind: ClassVar[str] = 'RuntimeClass'
    handler: str = attr.ib(metadata={'yaml_name': 'handler'})
    name: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    overhead: Optional[Union[kdsl.node.v1beta1.Overhead,
        kdsl.node.v1beta1.OverheadTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'overhead'})
    scheduling: Optional[Union[kdsl.node.v1beta1.Scheduling,
        kdsl.node.v1beta1.SchedulingTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'scheduling'})


@attr.s(kw_only=True)
class Overhead(K8sObjectBase):
    """
    | Overhead structure represents the resource overhead associated with running a pod.
    
    :param podFixed: PodFixed represents the fixed resource overhead associated with running a pod.
    """
    podFixed: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'podFixed'})


class SchedulingTypedDict(TypedDict, total=(False)):
    nodeSelector: Mapping[str, str]
    tolerations: Sequence[Union[kdsl.core.v1.Toleration,
        kdsl.core.v1.TolerationTypedDict]]


class RuntimeClassListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class RuntimeClassListTypedDict(RuntimeClassListOptionalTypedDict, total=(True)
    ):
    items: Sequence[Union[kdsl.node.v1beta1.RuntimeClass,
        kdsl.node.v1beta1.RuntimeClassTypedDict]]


class RuntimeClassOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    overhead: Union[kdsl.node.v1beta1.Overhead,
        kdsl.node.v1beta1.OverheadTypedDict]
    scheduling: Union[kdsl.node.v1beta1.Scheduling,
        kdsl.node.v1beta1.SchedulingTypedDict]


class RuntimeClassTypedDict(RuntimeClassOptionalTypedDict, total=(True)):
    handler: str
    name: str


class OverheadTypedDict(TypedDict, total=(False)):
    podFixed: Mapping[str, str]
