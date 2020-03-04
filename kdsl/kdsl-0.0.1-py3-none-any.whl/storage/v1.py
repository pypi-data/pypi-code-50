from __future__ import annotations
import kdsl.meta.v1
import kdsl.core.v1
import attr
import kdsl.storage.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class VolumeNodeResources(K8sObjectBase):
    """
    | VolumeNodeResources is a set of resource limits for scheduling of volumes.
    
    :param count: Maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded.
    """
    count: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'count'})


@attr.s(kw_only=True)
class VolumeError(K8sObjectBase):
    """
    | VolumeError captures an error encountered during a volume operation.
    
    :param message: String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.
    :param time: Time the error was encountered.
    """
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    time: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'time'})


@attr.s(kw_only=True)
class VolumeAttachmentStatus(K8sObjectBase):
    """
    | VolumeAttachmentStatus is the status of a VolumeAttachment request.
    
    :param attached: Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
    :param attachError: The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
    :param attachmentMetadata: Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
    :param detachError: The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.
    """
    attached: bool = attr.ib(metadata={'yaml_name': 'attached'})
    attachError: Optional[Union[kdsl.storage.v1.VolumeError,
        kdsl.storage.v1.VolumeErrorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'attachError'})
    attachmentMetadata: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'attachmentMetadata'})
    detachError: Optional[Union[kdsl.storage.v1.VolumeError,
        kdsl.storage.v1.VolumeErrorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'detachError'})


@attr.s(kw_only=True)
class VolumeAttachmentSpec(K8sObjectBase):
    """
    | VolumeAttachmentSpec is the specification of a VolumeAttachment request.
    
    :param attacher: Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().
    :param nodeName: The node that the volume should be attached to.
    :param source: Source represents the volume that should be attached.
    """
    attacher: str = attr.ib(metadata={'yaml_name': 'attacher'})
    nodeName: str = attr.ib(metadata={'yaml_name': 'nodeName'})
    source: Union[kdsl.storage.v1.VolumeAttachmentSource,
        kdsl.storage.v1.VolumeAttachmentSourceTypedDict] = attr.ib(metadata
        ={'yaml_name': 'source'})


@attr.s(kw_only=True)
class VolumeAttachmentSource(K8sObjectBase):
    """
    | VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one member can be set.
    
    :param inlineVolumeSpec: inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.
    :param persistentVolumeName: Name of the persistent volume to attach.
    """
    inlineVolumeSpec: Optional[Union[kdsl.core.v1.PersistentVolumeSpec,
        kdsl.core.v1.PersistentVolumeSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'inlineVolumeSpec'})
    persistentVolumeName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'persistentVolumeName'})


@attr.s(kw_only=True)
class VolumeAttachmentList(K8sObjectBase):
    """
    | VolumeAttachmentList is a collection of VolumeAttachment objects.
    
    :param items: Items is the list of VolumeAttachments
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.storage.v1.VolumeAttachment,
        kdsl.storage.v1.VolumeAttachmentTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class VolumeAttachment(K8sResourceBase):
    """
    | VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.
    
    VolumeAttachment objects are non-namespaced.
    
    :param name: metadata.name
    :param spec: Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'storage.k8s.io/v1'
    kind: ClassVar[str] = 'VolumeAttachment'
    name: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.storage.v1.VolumeAttachmentSpec,
        kdsl.storage.v1.VolumeAttachmentSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class StorageClassList(K8sObjectBase):
    """
    | StorageClassList is a collection of storage classes.
    
    :param items: Items is the list of StorageClasses
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.storage.v1.StorageClass,
        kdsl.storage.v1.StorageClassTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class StorageClass(K8sResourceBase):
    """
    | StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.
    
    StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name.
    
    :param name: metadata.name
    :param provisioner: Provisioner indicates the type of the provisioner.
    :param allowVolumeExpansion: AllowVolumeExpansion shows whether the storage class allow volume expand
    :param allowedTopologies: Restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param mountOptions: Dynamically provisioned PersistentVolumes of this storage class are created with these mountOptions, e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid.
    :param parameters: Parameters holds the parameters for the provisioner that should create volumes of this storage class.
    :param reclaimPolicy: Dynamically provisioned PersistentVolumes of this storage class are created with this reclaimPolicy. Defaults to Delete.
    :param volumeBindingMode: VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.
    """
    apiVersion: ClassVar[str] = 'storage.k8s.io/v1'
    kind: ClassVar[str] = 'StorageClass'
    name: str = attr.ib(metadata={'yaml_name': None})
    provisioner: str = attr.ib(metadata={'yaml_name': 'provisioner'})
    allowVolumeExpansion: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'allowVolumeExpansion'})
    allowedTopologies: Optional[Sequence[Union[
        kdsl.core.v1.TopologySelectorTerm,
        kdsl.core.v1.TopologySelectorTermTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'allowedTopologies'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    mountOptions: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'mountOptions'})
    parameters: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'parameters'})
    reclaimPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'reclaimPolicy'})
    volumeBindingMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'volumeBindingMode'})


@attr.s(kw_only=True)
class CSINodeSpec(K8sObjectBase):
    """
    | CSINodeSpec holds information about the specification of all CSI drivers installed on a node
    
    :param drivers: drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.
    """
    drivers: Sequence[Union[kdsl.storage.v1.CSINodeDriver,
        kdsl.storage.v1.CSINodeDriverTypedDict]] = attr.ib(metadata={
        'yaml_name': 'drivers'})


@attr.s(kw_only=True)
class CSINodeList(K8sObjectBase):
    """
    | CSINodeList is a collection of CSINode objects.
    
    :param items: items is the list of CSINode
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.storage.v1.CSINode,
        kdsl.storage.v1.CSINodeTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class CSINodeDriver(K8sObjectBase):
    """
    | CSINodeDriver holds information about the specification of one CSI driver installed on a node
    
    :param name: This is the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver.
    :param nodeID: nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as "node1", but the storage system may refer to the same node as "nodeA". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. "nodeA" instead of "node1". This field is required.
    :param allocatable: allocatable represents the volume resources of a node that are available for scheduling. This field is beta.
    :param topologyKeys: topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. "company.com/zone", "company.com/region"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    nodeID: str = attr.ib(metadata={'yaml_name': 'nodeID'})
    allocatable: Optional[Union[kdsl.storage.v1.VolumeNodeResources,
        kdsl.storage.v1.VolumeNodeResourcesTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'allocatable'})
    topologyKeys: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'topologyKeys'})


@attr.s(kw_only=True)
class CSINode(K8sResourceBase):
    """
    | CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to create the CSINode object directly. As long as they use the node-driver-registrar sidecar container, the kubelet will automatically populate the CSINode object for the CSI driver as part of kubelet plugin registration. CSINode has the same name as a node. If the object is missing, it means either there are no CSI Drivers available on the node, or the Kubelet version is low enough that it doesn't create this object. CSINode has an OwnerReference that points to the corresponding node object.
    
    :param name: metadata.name
    :param spec: spec is the specification of CSINode
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'storage.k8s.io/v1'
    kind: ClassVar[str] = 'CSINode'
    name: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.storage.v1.CSINodeSpec,
        kdsl.storage.v1.CSINodeSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


class VolumeNodeResourcesTypedDict(TypedDict, total=(False)):
    count: int


class VolumeErrorTypedDict(TypedDict, total=(False)):
    message: str
    time: str


class VolumeAttachmentStatusOptionalTypedDict(TypedDict, total=(False)):
    attachError: Union[kdsl.storage.v1.VolumeError,
        kdsl.storage.v1.VolumeErrorTypedDict]
    attachmentMetadata: Mapping[str, str]
    detachError: Union[kdsl.storage.v1.VolumeError,
        kdsl.storage.v1.VolumeErrorTypedDict]


class VolumeAttachmentStatusTypedDict(VolumeAttachmentStatusOptionalTypedDict,
    total=(True)):
    attached: bool


class VolumeAttachmentSpecTypedDict(TypedDict, total=(True)):
    attacher: str
    nodeName: str
    source: Union[kdsl.storage.v1.VolumeAttachmentSource,
        kdsl.storage.v1.VolumeAttachmentSourceTypedDict]


class VolumeAttachmentSourceTypedDict(TypedDict, total=(False)):
    inlineVolumeSpec: Union[kdsl.core.v1.PersistentVolumeSpec,
        kdsl.core.v1.PersistentVolumeSpecTypedDict]
    persistentVolumeName: str


class VolumeAttachmentListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class VolumeAttachmentListTypedDict(VolumeAttachmentListOptionalTypedDict,
    total=(True)):
    items: Sequence[Union[kdsl.storage.v1.VolumeAttachment,
        kdsl.storage.v1.VolumeAttachmentTypedDict]]


class VolumeAttachmentOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class VolumeAttachmentTypedDict(VolumeAttachmentOptionalTypedDict, total=(True)
    ):
    name: str
    spec: Union[kdsl.storage.v1.VolumeAttachmentSpec,
        kdsl.storage.v1.VolumeAttachmentSpecTypedDict]


class StorageClassListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class StorageClassListTypedDict(StorageClassListOptionalTypedDict, total=(True)
    ):
    items: Sequence[Union[kdsl.storage.v1.StorageClass,
        kdsl.storage.v1.StorageClassTypedDict]]


class StorageClassOptionalTypedDict(TypedDict, total=(False)):
    allowVolumeExpansion: bool
    allowedTopologies: Sequence[Union[kdsl.core.v1.TopologySelectorTerm,
        kdsl.core.v1.TopologySelectorTermTypedDict]]
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    mountOptions: Sequence[str]
    parameters: Mapping[str, str]
    reclaimPolicy: str
    volumeBindingMode: str


class StorageClassTypedDict(StorageClassOptionalTypedDict, total=(True)):
    name: str
    provisioner: str


class CSINodeSpecTypedDict(TypedDict, total=(True)):
    drivers: Sequence[Union[kdsl.storage.v1.CSINodeDriver,
        kdsl.storage.v1.CSINodeDriverTypedDict]]


class CSINodeListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class CSINodeListTypedDict(CSINodeListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.storage.v1.CSINode,
        kdsl.storage.v1.CSINodeTypedDict]]


class CSINodeDriverOptionalTypedDict(TypedDict, total=(False)):
    allocatable: Union[kdsl.storage.v1.VolumeNodeResources,
        kdsl.storage.v1.VolumeNodeResourcesTypedDict]
    topologyKeys: Sequence[str]


class CSINodeDriverTypedDict(CSINodeDriverOptionalTypedDict, total=(True)):
    name: str
    nodeID: str


class CSINodeOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class CSINodeTypedDict(CSINodeOptionalTypedDict, total=(True)):
    name: str
    spec: Union[kdsl.storage.v1.CSINodeSpec,
        kdsl.storage.v1.CSINodeSpecTypedDict]
