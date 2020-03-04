from __future__ import annotations
import kdsl.core.v1
import kdsl.meta.v1
import attr
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class WindowsSecurityContextOptions(K8sObjectBase):
    """
    | WindowsSecurityContextOptions contain Windows-specific options and credentials.
    
    :param gmsaCredentialSpec: GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param gmsaCredentialSpecName: GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.
    :param runAsUserName: The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. This field is beta-level and may be disabled with the WindowsRunAsUserName feature flag.
    """
    gmsaCredentialSpec: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'gmsaCredentialSpec'})
    gmsaCredentialSpecName: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'gmsaCredentialSpecName'})
    runAsUserName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsUserName'})


@attr.s(kw_only=True)
class WeightedPodAffinityTerm(K8sObjectBase):
    """
    | The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)
    
    :param podAffinityTerm: Required. A pod affinity term, associated with the corresponding weight.
    :param weight: weight associated with matching the corresponding podAffinityTerm, in the range 1-100.
    """
    podAffinityTerm: Union[kdsl.core.v1.PodAffinityTerm,
        kdsl.core.v1.PodAffinityTermTypedDict] = attr.ib(metadata={
        'yaml_name': 'podAffinityTerm'})
    weight: int = attr.ib(metadata={'yaml_name': 'weight'})


@attr.s(kw_only=True)
class VsphereVirtualDiskVolumeSource(K8sObjectBase):
    """
    | Represents a vSphere volume resource.
    
    :param volumePath: Path that identifies vSphere volume vmdk
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param storagePolicyID: Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.
    :param storagePolicyName: Storage Policy Based Management (SPBM) profile name.
    """
    volumePath: str = attr.ib(metadata={'yaml_name': 'volumePath'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    storagePolicyID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePolicyID'})
    storagePolicyName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePolicyName'})


@attr.s(kw_only=True)
class VolumeProjection(K8sObjectBase):
    """
    | Projection that may be projected along with other supported volume types
    
    :param configMap: information about the configMap data to project
    :param downwardAPI: information about the downwardAPI data to project
    :param secret: information about the secret data to project
    :param serviceAccountToken: information about the serviceAccountToken data to project
    """
    configMap: Optional[Union[kdsl.core.v1.ConfigMapProjection,
        kdsl.core.v1.ConfigMapProjectionTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'configMap'})
    downwardAPI: Optional[Union[kdsl.core.v1.DownwardAPIProjection,
        kdsl.core.v1.DownwardAPIProjectionTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'downwardAPI'})
    secret: Optional[Union[kdsl.core.v1.SecretProjection,
        kdsl.core.v1.SecretProjectionTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secret'})
    serviceAccountToken: Optional[Union[
        kdsl.core.v1.ServiceAccountTokenProjection,
        kdsl.core.v1.ServiceAccountTokenProjectionTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'serviceAccountToken'})


@attr.s(kw_only=True)
class VolumeNodeAffinity(K8sObjectBase):
    """
    | VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.
    
    :param required: Required specifies hard node constraints that must be met.
    """
    required: Optional[Union[kdsl.core.v1.NodeSelector,
        kdsl.core.v1.NodeSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'required'})


@attr.s(kw_only=True)
class VolumeMount(K8sObjectBase):
    """
    | VolumeMount describes a mounting of a Volume within a container.
    
    :param mountPath: Path within the container at which the volume should be mounted.  Must not contain ':'.
    :param name: This must match the Name of a Volume.
    :param mountPropagation: mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.
    :param readOnly: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.
    :param subPath: Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).
    :param subPathExpr: Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.
    """
    mountPath: str = attr.ib(metadata={'yaml_name': 'mountPath'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    mountPropagation: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'mountPropagation'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    subPath: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'subPath'})
    subPathExpr: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'subPathExpr'})


@attr.s(kw_only=True)
class VolumeDevice(K8sObjectBase):
    """
    | volumeDevice describes a mapping of a raw block device within a container.
    
    :param devicePath: devicePath is the path inside of the container that the device will be mapped to.
    :param name: name must match the name of a persistentVolumeClaim in the pod
    """
    devicePath: str = attr.ib(metadata={'yaml_name': 'devicePath'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class Volume(K8sObjectBase):
    """
    | Volume represents a named volume in a pod that may be accessed by any container in the pod.
    
    :param name: Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param awsElasticBlockStore: AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param azureDisk: AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    :param azureFile: AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    :param cephfs: CephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    :param cinder: Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param configMap: ConfigMap represents a configMap that should populate this volume
    :param csi: CSI (Container Storage Interface) represents storage that is handled by an external CSI driver (Alpha feature).
    :param downwardAPI: DownwardAPI represents downward API about the pod that should populate this volume
    :param emptyDir: EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param fc: FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    :param flexVolume: FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    :param flocker: Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    :param gcePersistentDisk: GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param gitRepo: GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    :param glusterfs: Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    :param hostPath: HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    :param iscsi: ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    :param nfs: NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param persistentVolumeClaim: PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param photonPersistentDisk: PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    :param portworxVolume: PortworxVolume represents a portworx volume attached and mounted on kubelets host machine
    :param projected: Items for all in one resources secrets, configmaps, and downward API
    :param quobyte: Quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    :param rbd: RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    :param scaleIO: ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    :param secret: Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    :param storageos: StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    :param vsphereVolume: VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    awsElasticBlockStore: Optional[Union[
        kdsl.core.v1.AWSElasticBlockStoreVolumeSource,
        kdsl.core.v1.AWSElasticBlockStoreVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'awsElasticBlockStore'})
    azureDisk: Optional[Union[kdsl.core.v1.AzureDiskVolumeSource,
        kdsl.core.v1.AzureDiskVolumeSourceTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'azureDisk'})
    azureFile: Optional[Union[kdsl.core.v1.AzureFileVolumeSource,
        kdsl.core.v1.AzureFileVolumeSourceTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'azureFile'})
    cephfs: Optional[Union[kdsl.core.v1.CephFSVolumeSource,
        kdsl.core.v1.CephFSVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'cephfs'})
    cinder: Optional[Union[kdsl.core.v1.CinderVolumeSource,
        kdsl.core.v1.CinderVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'cinder'})
    configMap: Optional[Union[kdsl.core.v1.ConfigMapVolumeSource,
        kdsl.core.v1.ConfigMapVolumeSourceTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'configMap'})
    csi: Optional[Union[kdsl.core.v1.CSIVolumeSource,
        kdsl.core.v1.CSIVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'csi'})
    downwardAPI: Optional[Union[kdsl.core.v1.DownwardAPIVolumeSource,
        kdsl.core.v1.DownwardAPIVolumeSourceTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'downwardAPI'})
    emptyDir: Optional[Union[kdsl.core.v1.EmptyDirVolumeSource,
        kdsl.core.v1.EmptyDirVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'emptyDir'})
    fc: Optional[Union[kdsl.core.v1.FCVolumeSource,
        kdsl.core.v1.FCVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'fc'})
    flexVolume: Optional[Union[kdsl.core.v1.FlexVolumeSource,
        kdsl.core.v1.FlexVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'flexVolume'})
    flocker: Optional[Union[kdsl.core.v1.FlockerVolumeSource,
        kdsl.core.v1.FlockerVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'flocker'})
    gcePersistentDisk: Optional[Union[
        kdsl.core.v1.GCEPersistentDiskVolumeSource,
        kdsl.core.v1.GCEPersistentDiskVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'gcePersistentDisk'})
    gitRepo: Optional[Union[kdsl.core.v1.GitRepoVolumeSource,
        kdsl.core.v1.GitRepoVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'gitRepo'})
    glusterfs: Optional[Union[kdsl.core.v1.GlusterfsVolumeSource,
        kdsl.core.v1.GlusterfsVolumeSourceTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'glusterfs'})
    hostPath: Optional[Union[kdsl.core.v1.HostPathVolumeSource,
        kdsl.core.v1.HostPathVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'hostPath'})
    iscsi: Optional[Union[kdsl.core.v1.ISCSIVolumeSource,
        kdsl.core.v1.ISCSIVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'iscsi'})
    nfs: Optional[Union[kdsl.core.v1.NFSVolumeSource,
        kdsl.core.v1.NFSVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'nfs'})
    persistentVolumeClaim: Optional[Union[
        kdsl.core.v1.PersistentVolumeClaimVolumeSource,
        kdsl.core.v1.PersistentVolumeClaimVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'persistentVolumeClaim'})
    photonPersistentDisk: Optional[Union[
        kdsl.core.v1.PhotonPersistentDiskVolumeSource,
        kdsl.core.v1.PhotonPersistentDiskVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'photonPersistentDisk'})
    portworxVolume: Optional[Union[kdsl.core.v1.PortworxVolumeSource,
        kdsl.core.v1.PortworxVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'portworxVolume'})
    projected: Optional[Union[kdsl.core.v1.ProjectedVolumeSource,
        kdsl.core.v1.ProjectedVolumeSourceTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'projected'})
    quobyte: Optional[Union[kdsl.core.v1.QuobyteVolumeSource,
        kdsl.core.v1.QuobyteVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'quobyte'})
    rbd: Optional[Union[kdsl.core.v1.RBDVolumeSource,
        kdsl.core.v1.RBDVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'rbd'})
    scaleIO: Optional[Union[kdsl.core.v1.ScaleIOVolumeSource,
        kdsl.core.v1.ScaleIOVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'scaleIO'})
    secret: Optional[Union[kdsl.core.v1.SecretVolumeSource,
        kdsl.core.v1.SecretVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secret'})
    storageos: Optional[Union[kdsl.core.v1.StorageOSVolumeSource,
        kdsl.core.v1.StorageOSVolumeSourceTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'storageos'})
    vsphereVolume: Optional[Union[
        kdsl.core.v1.VsphereVirtualDiskVolumeSource,
        kdsl.core.v1.VsphereVirtualDiskVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'vsphereVolume'})


@attr.s(kw_only=True)
class TypedLocalObjectReference(K8sObjectBase):
    """
    | TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.
    
    :param kind: Kind is the type of resource being referenced
    :param name: Name is the name of resource being referenced
    :param apiGroup: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.
    """
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    apiGroup: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiGroup'})


@attr.s(kw_only=True)
class TopologySpreadConstraint(K8sObjectBase):
    """
    | TopologySpreadConstraint specifies how to spread matching pods among the given topology.
    
    :param maxSkew: MaxSkew describes the degree to which pods may be unevenly distributed. It's the maximum permitted difference between the number of matching pods in any two topology domains of a given topology type. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | |   P   |   P   |       | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. It's a required field. Default value is 1 and 0 is not allowed.
    :param topologyKey: TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. It's a required field.
    :param whenUnsatisfiable: WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it - ScheduleAnyway tells the scheduler to still schedule it It's considered as "Unsatisfiable" if and only if placing incoming pod on any topology violates "MaxSkew". For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.
    :param labelSelector: LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.
    """
    maxSkew: int = attr.ib(metadata={'yaml_name': 'maxSkew'})
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    whenUnsatisfiable: str = attr.ib(metadata={'yaml_name':
        'whenUnsatisfiable'})
    labelSelector: Optional[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'labelSelector'})


@attr.s(kw_only=True)
class TopologySelectorTerm(K8sObjectBase):
    """
    | A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future.
    
    :param matchLabelExpressions: A list of topology selector requirements by labels.
    """
    matchLabelExpressions: Optional[Sequence[Union[
        kdsl.core.v1.TopologySelectorLabelRequirement,
        kdsl.core.v1.TopologySelectorLabelRequirementTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'matchLabelExpressions'})


@attr.s(kw_only=True)
class TopologySelectorLabelRequirement(K8sObjectBase):
    """
    | A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future.
    
    :param key: The label key that the selector applies to.
    :param values: An array of string values. One value must match the label to be selected. Each entry in Values is ORed.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    values: Sequence[str] = attr.ib(metadata={'yaml_name': 'values'})


@attr.s(kw_only=True)
class Toleration(K8sObjectBase):
    """
    | The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.
    
    :param effect: Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.
    :param key: Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.
    :param operator: Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.
    :param tolerationSeconds: TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.
    :param value: Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.
    """
    effect: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'effect'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})
    operator: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'operator'})
    tolerationSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'tolerationSeconds'})
    value: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'value'})


@attr.s(kw_only=True)
class Taint(K8sObjectBase):
    """
    | The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint.
    
    :param effect: Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.
    :param key: Required. The taint key to be applied to a node.
    :param timeAdded: TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.
    :param value: Required. The taint value corresponding to the taint key.
    """
    effect: str = attr.ib(metadata={'yaml_name': 'effect'})
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    timeAdded: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'timeAdded'})
    value: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'value'})


@attr.s(kw_only=True)
class TCPSocketAction(K8sObjectBase):
    """
    | TCPSocketAction describes an action based on opening a socket
    
    :param port: Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Optional: Host name to connect to, defaults to the pod IP.
    """
    port: Union[int, str] = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class Sysctl(K8sObjectBase):
    """
    | Sysctl defines a kernel parameter to be set
    
    :param name: Name of a property to set
    :param value: Value of a property to set
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class StorageOSVolumeSource(K8sObjectBase):
    """
    | Represents a StorageOS persistent volume resource.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    :param volumeName: VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    :param volumeNamespace: VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})
    volumeNamespace: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'volumeNamespace'})


@attr.s(kw_only=True)
class StorageOSPersistentVolumeSource(K8sObjectBase):
    """
    | Represents a StorageOS persistent volume resource.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    :param volumeName: VolumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    :param volumeNamespace: VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})
    volumeNamespace: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'volumeNamespace'})


@attr.s(kw_only=True)
class SessionAffinityConfig(K8sObjectBase):
    """
    | SessionAffinityConfig represents the configurations of session affinity.
    
    :param clientIP: clientIP contains the configurations of Client IP based session affinity.
    """
    clientIP: Optional[Union[kdsl.core.v1.ClientIPConfig,
        kdsl.core.v1.ClientIPConfigTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'clientIP'})


@attr.s(kw_only=True)
class ServiceStatus(K8sObjectBase):
    """
    | ServiceStatus represents the current status of a service.
    
    :param loadBalancer: LoadBalancer contains the current status of the load-balancer, if one is present.
    """
    loadBalancer: Optional[Union[kdsl.core.v1.LoadBalancerStatus,
        kdsl.core.v1.LoadBalancerStatusTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'loadBalancer'})


@attr.s(kw_only=True)
class ServiceSpec(K8sObjectBase):
    """
    | ServiceSpec describes the attributes that a user creates on a service.
    
    :param clusterIP: clusterIP is the IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are "None", empty string (""), or a valid IP address. "None" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    :param externalIPs: externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.
    :param externalName: externalName is the external reference that kubedns or equivalent will return as a CNAME record for this service. No proxying will be involved. Must be a valid RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires Type to be ExternalName.
    :param externalTrafficPolicy: externalTrafficPolicy denotes if this Service desires to route external traffic to node-local or cluster-wide endpoints. "Local" preserves the client source IP and avoids a second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced traffic spreading. "Cluster" obscures the client source IP and may cause a second hop to another node, but should have good overall load-spreading.
    :param healthCheckNodePort: healthCheckNodePort specifies the healthcheck nodePort for the service. If not specified, HealthCheckNodePort is created by the service api backend with the allocated nodePort. Will use user-specified nodePort value if specified by the client. Only effects when Type is set to LoadBalancer and ExternalTrafficPolicy is set to Local.
    :param ipFamily: ipFamily specifies whether this Service has a preference for a particular IP family (e.g. IPv4 vs. IPv6).  If a specific IP family is requested, the clusterIP field will be allocated from that family, if it is available in the cluster.  If no IP family is requested, the cluster's primary IP family will be used. Other IP fields (loadBalancerIP, loadBalancerSourceRanges, externalIPs) and controllers which allocate external load-balancers should use the same IP family.  Endpoints for this Service will be of this family.  This field is immutable after creation. Assigning a ServiceIPFamily not available in the cluster (e.g. IPv6 in IPv4 only cluster) is an error condition and will fail during clusterIP assignment.
    :param loadBalancerIP: Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.
    :param loadBalancerSourceRanges: If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature." More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/
    :param ports: The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    :param publishNotReadyAddresses: publishNotReadyAddresses, when set to true, indicates that DNS implementations must publish the notReadyAddresses of subsets for the Endpoints associated with the Service. The default value is false. The primary use case for setting this field is to use a StatefulSet's Headless Service to propagate SRV records for its Pods without respect to their readiness for purpose of peer discovery.
    :param selector: Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/
    :param sessionAffinity: Supports "ClientIP" and "None". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    :param sessionAffinityConfig: sessionAffinityConfig contains the configurations of session affinity.
    :param topologyKeys: topologyKeys is a preference-order list of topology keys which implementations of services should use to preferentially sort endpoints when accessing this Service, it can not be used at the same time as externalTrafficPolicy=Local. Topology keys must be valid label keys and at most 16 keys may be specified. Endpoints are chosen based on the first topology key with available backends. If this field is specified and all entries have no backends that match the topology of the client, the service has no backends for that client and connections should fail. The special value "*" may be used to mean "any topology". This catch-all value, if used, only makes sense as the last value in the list. If this is not specified or empty, no topology constraints will be applied.
    :param type: type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. "ExternalName" maps to the specified externalName. "ClusterIP" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object. If clusterIP is "None", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a stable IP. "NodePort" builds on ClusterIP and allocates a port on every node which routes to the clusterIP. "LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the clusterIP. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types
    """
    clusterIP: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'clusterIP'})
    externalIPs: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'externalIPs'})
    externalName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'externalName'})
    externalTrafficPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'externalTrafficPolicy'})
    healthCheckNodePort: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'healthCheckNodePort'})
    ipFamily: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'ipFamily'})
    loadBalancerIP: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'loadBalancerIP'})
    loadBalancerSourceRanges: Optional[Sequence[str]] = attr.ib(default=
        None, metadata={'yaml_name': 'loadBalancerSourceRanges'})
    ports: Optional[Sequence[Union[kdsl.core.v1.ServicePort,
        kdsl.core.v1.ServicePortTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ports'})
    publishNotReadyAddresses: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'publishNotReadyAddresses'})
    selector: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'selector'})
    sessionAffinity: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'sessionAffinity'})
    sessionAffinityConfig: Optional[Union[
        kdsl.core.v1.SessionAffinityConfig,
        kdsl.core.v1.SessionAffinityConfigTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'sessionAffinityConfig'})
    topologyKeys: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'topologyKeys'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class ServicePort(K8sObjectBase):
    """
    | ServicePort contains information on service's port.
    
    :param port: The port that will be exposed by this service.
    :param name: The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service.
    :param nodePort: The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
    :param protocol: The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP.
    :param targetPort: Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service
    """
    port: int = attr.ib(metadata={'yaml_name': 'port'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    nodePort: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'nodePort'})
    protocol: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'protocol'})
    targetPort: Optional[Union[int, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'targetPort'})


@attr.s(kw_only=True)
class ServiceList(K8sObjectBase):
    """
    | ServiceList holds a list of services.
    
    :param items: List of services
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.Service, kdsl.core.v1.ServiceTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ServiceAccountTokenProjection(K8sObjectBase):
    """
    | ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise).
    
    :param path: Path is the path relative to the mount point of the file to project the token into.
    :param audience: Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.
    :param expirationSeconds: ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    audience: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'audience'})
    expirationSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'expirationSeconds'})


@attr.s(kw_only=True)
class ServiceAccountList(K8sObjectBase):
    """
    | ServiceAccountList is a list of ServiceAccount objects
    
    :param items: List of ServiceAccounts. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.ServiceAccount,
        kdsl.core.v1.ServiceAccountTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ServiceAccount(K8sResourceBase):
    """
    | ServiceAccount binds together: * a name, understood by users, and perhaps by peripheral systems, for an identity * a principal that can be authenticated and authorized * a set of secrets
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param automountServiceAccountToken: AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level.
    :param imagePullSecrets: ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod
    :param labels: metadata.labels
    :param secrets: Secrets is the list of secrets allowed to be used by pods running using this ServiceAccount. More info: https://kubernetes.io/docs/concepts/configuration/secret
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'ServiceAccount'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    automountServiceAccountToken: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'automountServiceAccountToken'})
    imagePullSecrets: Optional[Sequence[Union[
        kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'imagePullSecrets'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    secrets: Optional[Sequence[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'secrets'})


@attr.s(kw_only=True)
class Service(K8sResourceBase):
    """
    | Service is a named abstraction of software service (for example, mysql) consisting of local port (for example 3306) that the proxy listens on, and the selector that determines which pods will answer requests sent through the proxy.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the behavior of a service. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'Service'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.ServiceSpec,
        kdsl.core.v1.ServiceSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class SecurityContext(K8sObjectBase):
    """
    | SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext.  When both are set, the values in SecurityContext take precedence.
    
    :param allowPrivilegeEscalation: AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN
    :param capabilities: The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.
    :param privileged: Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.
    :param procMount: procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.
    :param readOnlyRootFilesystem: Whether this container has a read-only root filesystem. Default is false.
    :param runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param seLinuxOptions: The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    allowPrivilegeEscalation: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'allowPrivilegeEscalation'})
    capabilities: Optional[Union[kdsl.core.v1.Capabilities,
        kdsl.core.v1.CapabilitiesTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'capabilities'})
    privileged: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'privileged'})
    procMount: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'procMount'})
    readOnlyRootFilesystem: Optional[bool] = attr.ib(default=None, metadata
        ={'yaml_name': 'readOnlyRootFilesystem'})
    runAsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsGroup'})
    runAsNonRoot: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsNonRoot'})
    runAsUser: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsUser'})
    seLinuxOptions: Optional[Union[kdsl.core.v1.SELinuxOptions,
        kdsl.core.v1.SELinuxOptionsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'seLinuxOptions'})
    windowsOptions: Optional[Union[
        kdsl.core.v1.WindowsSecurityContextOptions,
        kdsl.core.v1.WindowsSecurityContextOptionsTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'windowsOptions'})


@attr.s(kw_only=True)
class SecretVolumeSource(K8sObjectBase):
    """
    | Adapts a Secret into a volume.
    
    The contents of the target Secret's Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param optional: Specify whether the Secret or its keys must be defined
    :param secretName: Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[kdsl.core.v1.KeyToPath,
        kdsl.core.v1.KeyToPathTypedDict]]] = attr.ib(default=None, metadata
        ={'yaml_name': 'items'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})
    secretName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretName'})


@attr.s(kw_only=True)
class SecretReference(K8sObjectBase):
    """
    | SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace
    
    :param name: Name is unique within a namespace to reference a secret resource.
    :param namespace: Namespace defines the space within which the secret name must be unique.
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    namespace: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'namespace'})


@attr.s(kw_only=True)
class SecretProjection(K8sObjectBase):
    """
    | Adapts a secret into a projected volume.
    
    The contents of the target Secret's Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.
    
    :param items: If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param optional: Specify whether the Secret or its key must be defined
    """
    items: Optional[Sequence[Union[kdsl.core.v1.KeyToPath,
        kdsl.core.v1.KeyToPathTypedDict]]] = attr.ib(default=None, metadata
        ={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class SecretList(K8sObjectBase):
    """
    | SecretList is a list of Secret.
    
    :param items: Items is a list of secret objects. More info: https://kubernetes.io/docs/concepts/configuration/secret
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.Secret, kdsl.core.v1.SecretTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class SecretKeySelector(K8sObjectBase):
    """
    | SecretKeySelector selects a key of a Secret.
    
    :param key: The key of the secret to select from.  Must be a valid secret key.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param optional: Specify whether the Secret or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class SecretEnvSource(K8sObjectBase):
    """
    | SecretEnvSource selects a Secret to populate the environment variables with.
    
    The contents of the target Secret's Data field will represent the key-value pairs as environment variables.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param optional: Specify whether the Secret must be defined
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class Secret(K8sResourceBase):
    """
    | Secret holds secret data of a certain type. The total bytes of the values in the Data field must be less than MaxSecretSize bytes.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param data: Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4
    :param labels: metadata.labels
    :param stringData: stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.
    :param type: Used to facilitate programmatic handling of secret data.
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'Secret'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    data: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'data'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    stringData: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'stringData'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class ScopedResourceSelectorRequirement(K8sObjectBase):
    """
    | A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values.
    
    :param operator: Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.
    :param scopeName: The name of the scope that the selector applies to.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    scopeName: str = attr.ib(metadata={'yaml_name': 'scopeName'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class ScopeSelector(K8sObjectBase):
    """
    | A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.
    
    :param matchExpressions: A list of scope selector requirements by scope of the resources.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.core.v1.ScopedResourceSelectorRequirement,
        kdsl.core.v1.ScopedResourceSelectorRequirementTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'matchExpressions'})


@attr.s(kw_only=True)
class ScaleIOVolumeSource(K8sObjectBase):
    """
    | ScaleIOVolumeSource represents a persistent ScaleIO volume
    
    :param gateway: The host address of the ScaleIO API Gateway.
    :param secretRef: SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    :param system: The name of the storage system as configured in ScaleIO.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".
    :param protectionDomain: The name of the ScaleIO Protection Domain for the configured storage.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param sslEnabled: Flag to enable/disable SSL communication with Gateway, default false
    :param storageMode: Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    :param storagePool: The ScaleIO Storage Pool associated with the protection domain.
    :param volumeName: The name of a volume already created in the ScaleIO system that is associated with this volume source.
    """
    gateway: str = attr.ib(metadata={'yaml_name': 'gateway'})
    secretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict] = attr.ib(metadata={
        'yaml_name': 'secretRef'})
    system: str = attr.ib(metadata={'yaml_name': 'system'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    protectionDomain: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'protectionDomain'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    sslEnabled: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'sslEnabled'})
    storageMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageMode'})
    storagePool: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePool'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class ScaleIOPersistentVolumeSource(K8sObjectBase):
    """
    | ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume
    
    :param gateway: The host address of the ScaleIO API Gateway.
    :param secretRef: SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    :param system: The name of the storage system as configured in ScaleIO.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"
    :param protectionDomain: The name of the ScaleIO Protection Domain for the configured storage.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param sslEnabled: Flag to enable/disable SSL communication with Gateway, default false
    :param storageMode: Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    :param storagePool: The ScaleIO Storage Pool associated with the protection domain.
    :param volumeName: The name of a volume already created in the ScaleIO system that is associated with this volume source.
    """
    gateway: str = attr.ib(metadata={'yaml_name': 'gateway'})
    secretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict] = attr.ib(metadata={
        'yaml_name': 'secretRef'})
    system: str = attr.ib(metadata={'yaml_name': 'system'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    protectionDomain: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'protectionDomain'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    sslEnabled: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'sslEnabled'})
    storageMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageMode'})
    storagePool: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storagePool'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class SELinuxOptions(K8sObjectBase):
    """
    | SELinuxOptions are the labels to be applied to the container
    
    :param level: Level is SELinux level label that applies to the container.
    :param role: Role is a SELinux role label that applies to the container.
    :param type: Type is a SELinux type label that applies to the container.
    :param user: User is a SELinux user label that applies to the container.
    """
    level: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'level'})
    role: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'role'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class ResourceRequirements(K8sObjectBase):
    """
    | ResourceRequirements describes the compute resource requirements.
    
    :param limits: Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param requests: Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    """
    limits: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'limits'})
    requests: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'requests'})


@attr.s(kw_only=True)
class ResourceQuotaStatus(K8sObjectBase):
    """
    | ResourceQuotaStatus defines the enforced hard limits and observed use.
    
    :param hard: Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
    :param used: Used is the current observed total usage of the resource in the namespace.
    """
    hard: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'hard'})
    used: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'used'})


@attr.s(kw_only=True)
class ResourceQuotaSpec(K8sObjectBase):
    """
    | ResourceQuotaSpec defines the desired hard limits to enforce for Quota.
    
    :param hard: hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
    :param scopeSelector: scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.
    :param scopes: A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.
    """
    hard: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'hard'})
    scopeSelector: Optional[Union[kdsl.core.v1.ScopeSelector,
        kdsl.core.v1.ScopeSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'scopeSelector'})
    scopes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'scopes'})


@attr.s(kw_only=True)
class ResourceQuotaList(K8sObjectBase):
    """
    | ResourceQuotaList is a list of ResourceQuota items.
    
    :param items: Items is a list of ResourceQuota objects. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.ResourceQuota,
        kdsl.core.v1.ResourceQuotaTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ResourceQuota(K8sResourceBase):
    """
    | ResourceQuota sets aggregate quota restrictions enforced per namespace
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the desired quota. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'ResourceQuota'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.ResourceQuotaSpec,
        kdsl.core.v1.ResourceQuotaSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class ResourceFieldSelector(K8sObjectBase):
    """
    | ResourceFieldSelector represents container resources (cpu, memory) and their output format
    
    :param resource: Required: resource to select
    :param containerName: Container name: required for volumes, optional for env vars
    :param divisor: Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: str = attr.ib(metadata={'yaml_name': 'resource'})
    containerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerName'})
    divisor: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'divisor'})


@attr.s(kw_only=True)
class ReplicationControllerStatus(K8sObjectBase):
    """
    | ReplicationControllerStatus represents the current status of a replication controller.
    
    :param replicas: Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller
    :param availableReplicas: The number of available replicas (ready for at least minReadySeconds) for this replication controller.
    :param conditions: Represents the latest available observations of a replication controller's current state.
    :param fullyLabeledReplicas: The number of pods that have labels matching the labels of the pod template of the replication controller.
    :param observedGeneration: ObservedGeneration reflects the generation of the most recently observed replication controller.
    :param readyReplicas: The number of ready replicas for this replication controller.
    """
    replicas: int = attr.ib(metadata={'yaml_name': 'replicas'})
    availableReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'availableReplicas'})
    conditions: Optional[Sequence[Union[
        kdsl.core.v1.ReplicationControllerCondition,
        kdsl.core.v1.ReplicationControllerConditionTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'conditions'})
    fullyLabeledReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'fullyLabeledReplicas'})
    observedGeneration: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'observedGeneration'})
    readyReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'readyReplicas'})


@attr.s(kw_only=True)
class ReplicationControllerSpec(K8sObjectBase):
    """
    | ReplicationControllerSpec is the specification of a replication controller.
    
    :param minReadySeconds: Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    :param replicas: Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller
    :param selector: Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    :param template: Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    """
    minReadySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'minReadySeconds'})
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})
    selector: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'selector'})
    template: Optional[Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'template'})


@attr.s(kw_only=True)
class ReplicationControllerList(K8sObjectBase):
    """
    | ReplicationControllerList is a collection of replication controllers.
    
    :param items: List of replication controllers. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.ReplicationController,
        kdsl.core.v1.ReplicationControllerTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ReplicationControllerCondition(K8sObjectBase):
    """
    | ReplicationControllerCondition describes the state of a replication controller at a certain point.
    
    :param status: Status of the condition, one of True, False, Unknown.
    :param type: Type of replication controller condition.
    :param lastTransitionTime: The last time the condition transitioned from one status to another.
    :param message: A human readable message indicating details about the transition.
    :param reason: The reason for the condition's last transition.
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
class ReplicationController(K8sResourceBase):
    """
    | ReplicationController represents the configuration of a replication controller.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the specification of the desired behavior of the replication controller. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'ReplicationController'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.ReplicationControllerSpec,
        kdsl.core.v1.ReplicationControllerSpecTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class RBDVolumeSource(K8sObjectBase):
    """
    | Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.
    
    :param image: The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param monitors: A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd
    :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param pool: The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param secretRef: SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param user: The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    image: str = attr.ib(metadata={'yaml_name': 'image'})
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    keyring: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyring'})
    pool: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'pool'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class RBDPersistentVolumeSource(K8sObjectBase):
    """
    | Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.
    
    :param image: The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param monitors: A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd
    :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param pool: The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param secretRef: SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    :param user: The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    image: str = attr.ib(metadata={'yaml_name': 'image'})
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    keyring: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'keyring'})
    pool: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'pool'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class QuobyteVolumeSource(K8sObjectBase):
    """
    | Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.
    
    :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes
    :param volume: Volume is a string that references an already created Quobyte volume by name.
    :param group: Group to map volume access to Default is no group
    :param readOnly: ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.
    :param tenant: Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin
    :param user: User to map volume access to Defaults to serivceaccount user
    """
    registry: str = attr.ib(metadata={'yaml_name': 'registry'})
    volume: str = attr.ib(metadata={'yaml_name': 'volume'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    tenant: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'tenant'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class ProjectedVolumeSource(K8sObjectBase):
    """
    | Represents a projected volume source
    
    :param sources: list of volume projections
    :param defaultMode: Mode bits to use on created files by default. Must be a value between 0 and 0777. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    sources: Sequence[Union[kdsl.core.v1.VolumeProjection,
        kdsl.core.v1.VolumeProjectionTypedDict]] = attr.ib(metadata={
        'yaml_name': 'sources'})
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})


@attr.s(kw_only=True)
class Probe(K8sObjectBase):
    """
    | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param failureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param initialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    :param successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported
    :param timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    exec: Optional[Union[kdsl.core.v1.ExecAction,
        kdsl.core.v1.ExecActionTypedDict]] = attr.ib(default=None, metadata
        ={'yaml_name': 'exec'})
    failureThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'failureThreshold'})
    httpGet: Optional[Union[kdsl.core.v1.HTTPGetAction,
        kdsl.core.v1.HTTPGetActionTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'httpGet'})
    initialDelaySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'initialDelaySeconds'})
    periodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'periodSeconds'})
    successThreshold: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'successThreshold'})
    tcpSocket: Optional[Union[kdsl.core.v1.TCPSocketAction,
        kdsl.core.v1.TCPSocketActionTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'tcpSocket'})
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class PreferredSchedulingTerm(K8sObjectBase):
    """
    | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
    
    :param preference: A node selector term, associated with the corresponding weight.
    :param weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.
    """
    preference: Union[kdsl.core.v1.NodeSelectorTerm,
        kdsl.core.v1.NodeSelectorTermTypedDict] = attr.ib(metadata={
        'yaml_name': 'preference'})
    weight: int = attr.ib(metadata={'yaml_name': 'weight'})


@attr.s(kw_only=True)
class PortworxVolumeSource(K8sObjectBase):
    """
    | PortworxVolumeSource represents a Portworx volume resource.
    
    :param volumeID: VolumeID uniquely identifies a Portworx volume
    :param fsType: FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PodTemplateSpec(K8sObjectBase):
    """
    | PodTemplateSpec describes the data a pod should have when created from a template
    
    :param metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    :param spec: Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    metadata: Optional[Union[kdsl.meta.v1.ObjectMeta,
        kdsl.meta.v1.ObjectMetaTypedDict]] = attr.ib(default=None, metadata
        ={'yaml_name': 'metadata'})
    spec: Optional[Union[kdsl.core.v1.PodSpec, kdsl.core.v1.PodSpecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class PodTemplateList(K8sObjectBase):
    """
    | PodTemplateList is a list of PodTemplates.
    
    :param items: List of pod templates
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.PodTemplate,
        kdsl.core.v1.PodTemplateTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class PodTemplate(K8sResourceBase):
    """
    | PodTemplate describes a template for creating copies of a predefined pod.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param template: Template defines the pods that will be created from this pod template. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'PodTemplate'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    template: Optional[Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'template'})


@attr.s(kw_only=True)
class PodStatus(K8sObjectBase):
    """
    | PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane.
    
    :param conditions: Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions
    :param containerStatuses: The list has one entry per container in the manifest. Each entry is currently the output of `docker inspect`. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status
    :param ephemeralContainerStatuses: Status for any ephemeral containers that have run in this pod. This field is alpha-level and is only populated by servers that enable the EphemeralContainers feature.
    :param hostIP: IP address of the host to which the pod is assigned. Empty if not yet scheduled.
    :param initContainerStatuses: The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status
    :param message: A human readable message indicating details about why the pod is in this condition.
    :param nominatedNodeName: nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.
    :param phase: The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:
    
    Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.
    
    More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase
    :param podIP: IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.
    :param podIPs: podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.
    :param qosClass: The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md
    :param reason: A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'
    :param startTime: RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.
    """
    conditions: Optional[Sequence[Union[kdsl.core.v1.PodCondition,
        kdsl.core.v1.PodConditionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'conditions'})
    containerStatuses: Optional[Sequence[Union[kdsl.core.v1.ContainerStatus,
        kdsl.core.v1.ContainerStatusTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'containerStatuses'})
    ephemeralContainerStatuses: Optional[Sequence[Union[
        kdsl.core.v1.ContainerStatus, kdsl.core.v1.ContainerStatusTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'ephemeralContainerStatuses'})
    hostIP: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'hostIP'})
    initContainerStatuses: Optional[Sequence[Union[
        kdsl.core.v1.ContainerStatus, kdsl.core.v1.ContainerStatusTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'initContainerStatuses'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    nominatedNodeName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'nominatedNodeName'})
    phase: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'phase'})
    podIP: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'podIP'})
    podIPs: Optional[Sequence[Union[kdsl.core.v1.PodIP,
        kdsl.core.v1.PodIPTypedDict]]] = attr.ib(default=None, metadata={
        'yaml_name': 'podIPs'})
    qosClass: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'qosClass'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})
    startTime: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'startTime'})


@attr.s(kw_only=True)
class PodSpec(K8sObjectBase):
    """
    | PodSpec is a description of a pod.
    
    :param containers: List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.
    :param activeDeadlineSeconds: Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.
    :param affinity: If specified, the pod's scheduling constraints
    :param automountServiceAccountToken: AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.
    :param dnsConfig: Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.
    :param dnsPolicy: Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.
    :param enableServiceLinks: EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.
    :param ephemeralContainers: List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. This field is alpha-level and is only honored by servers that enable the EphemeralContainers feature.
    :param hostAliases: HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.
    :param hostIPC: Use the host's ipc namespace. Optional: Default to false.
    :param hostNetwork: Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.
    :param hostPID: Use the host's pid namespace. Optional: Default to false.
    :param hostname: Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.
    :param imagePullSecrets: ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod
    :param initContainers: List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
    :param nodeName: NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.
    :param nodeSelector: NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
    :param overhead: Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.16, and is only honored by servers that enable the PodOverhead feature.
    :param preemptionPolicy: PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.
    :param priority: The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.
    :param priorityClassName: If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.
    :param readinessGates: If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/0007-pod-ready%2B%2B.md
    :param restartPolicy: Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
    :param runtimeClassName: RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md This is a beta feature as of Kubernetes v1.14.
    :param schedulerName: If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.
    :param securityContext: SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.
    :param serviceAccount: DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.
    :param serviceAccountName: ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
    :param shareProcessNamespace: Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.
    :param subdomain: If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.
    :param terminationGracePeriodSeconds: Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.
    :param tolerations: If specified, the pod's tolerations.
    :param topologySpreadConstraints: TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. This field is alpha-level and is only honored by clusters that enables the EvenPodsSpread feature. All topologySpreadConstraints are ANDed.
    :param volumes: List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes
    """
    containers: Sequence[Union[kdsl.core.v1.Container,
        kdsl.core.v1.ContainerTypedDict]] = attr.ib(metadata={'yaml_name':
        'containers'})
    activeDeadlineSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'activeDeadlineSeconds'})
    affinity: Optional[Union[kdsl.core.v1.Affinity,
        kdsl.core.v1.AffinityTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'affinity'})
    automountServiceAccountToken: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'automountServiceAccountToken'})
    dnsConfig: Optional[Union[kdsl.core.v1.PodDNSConfig,
        kdsl.core.v1.PodDNSConfigTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'dnsConfig'})
    dnsPolicy: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'dnsPolicy'})
    enableServiceLinks: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'enableServiceLinks'})
    ephemeralContainers: Optional[Sequence[Union[
        kdsl.core.v1.EphemeralContainer,
        kdsl.core.v1.EphemeralContainerTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ephemeralContainers'})
    hostAliases: Optional[Sequence[Union[kdsl.core.v1.HostAlias,
        kdsl.core.v1.HostAliasTypedDict]]] = attr.ib(default=None, metadata
        ={'yaml_name': 'hostAliases'})
    hostIPC: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'hostIPC'})
    hostNetwork: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'hostNetwork'})
    hostPID: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'hostPID'})
    hostname: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'hostname'})
    imagePullSecrets: Optional[Sequence[Union[
        kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'imagePullSecrets'})
    initContainers: Optional[Sequence[Union[kdsl.core.v1.Container,
        kdsl.core.v1.ContainerTypedDict]]] = attr.ib(default=None, metadata
        ={'yaml_name': 'initContainers'})
    nodeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'nodeName'})
    nodeSelector: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeSelector'})
    overhead: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'overhead'})
    preemptionPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'preemptionPolicy'})
    priority: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'priority'})
    priorityClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'priorityClassName'})
    readinessGates: Optional[Sequence[Union[kdsl.core.v1.PodReadinessGate,
        kdsl.core.v1.PodReadinessGateTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'readinessGates'})
    restartPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'restartPolicy'})
    runtimeClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'runtimeClassName'})
    schedulerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'schedulerName'})
    securityContext: Optional[Union[kdsl.core.v1.PodSecurityContext,
        kdsl.core.v1.PodSecurityContextTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'securityContext'})
    serviceAccount: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'serviceAccount'})
    serviceAccountName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'serviceAccountName'})
    shareProcessNamespace: Optional[bool] = attr.ib(default=None, metadata=
        {'yaml_name': 'shareProcessNamespace'})
    subdomain: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'subdomain'})
    terminationGracePeriodSeconds: Optional[int] = attr.ib(default=None,
        metadata={'yaml_name': 'terminationGracePeriodSeconds'})
    tolerations: Optional[Sequence[Union[kdsl.core.v1.Toleration,
        kdsl.core.v1.TolerationTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'tolerations'})
    topologySpreadConstraints: Optional[Sequence[Union[
        kdsl.core.v1.TopologySpreadConstraint,
        kdsl.core.v1.TopologySpreadConstraintTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'topologySpreadConstraints'})
    volumes: Optional[Sequence[Union[kdsl.core.v1.Volume,
        kdsl.core.v1.VolumeTypedDict]]] = attr.ib(default=None, metadata={
        'yaml_name': 'volumes'})


@attr.s(kw_only=True)
class PodSecurityContext(K8sObjectBase):
    """
    | PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext.  Field values of container.securityContext take precedence over field values of PodSecurityContext.
    
    :param fsGroup: A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:
    
    1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----
    
    If unset, the Kubelet will not modify the ownership and permissions of any volume.
    :param runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    :param runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param seLinuxOptions: The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
    :param supplementalGroups: A list of groups applied to the first process run in each container, in addition to the container's primary GID.  If unspecified, no groups will be added to any container.
    :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.
    :param windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    fsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'fsGroup'})
    runAsGroup: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsGroup'})
    runAsNonRoot: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'runAsNonRoot'})
    runAsUser: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'runAsUser'})
    seLinuxOptions: Optional[Union[kdsl.core.v1.SELinuxOptions,
        kdsl.core.v1.SELinuxOptionsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'seLinuxOptions'})
    supplementalGroups: Optional[Sequence[int]] = attr.ib(default=None,
        metadata={'yaml_name': 'supplementalGroups'})
    sysctls: Optional[Sequence[Union[kdsl.core.v1.Sysctl,
        kdsl.core.v1.SysctlTypedDict]]] = attr.ib(default=None, metadata={
        'yaml_name': 'sysctls'})
    windowsOptions: Optional[Union[
        kdsl.core.v1.WindowsSecurityContextOptions,
        kdsl.core.v1.WindowsSecurityContextOptionsTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'windowsOptions'})


@attr.s(kw_only=True)
class PodReadinessGate(K8sObjectBase):
    """
    | PodReadinessGate contains the reference to a pod condition
    
    :param conditionType: ConditionType refers to a condition in the pod's condition list with matching type.
    """
    conditionType: str = attr.ib(metadata={'yaml_name': 'conditionType'})


@attr.s(kw_only=True)
class PodList(K8sObjectBase):
    """
    | PodList is a list of Pods.
    
    :param items: List of pods. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.Pod, kdsl.core.v1.PodTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class PodIP(K8sObjectBase):
    """
    | IP address information for entries in the (plural) PodIPs field. Each entry includes:
       IP: An IP address allocated to the pod. Routable at least within the cluster.
    
    :param ip: ip is an IP address (IPv4 or IPv6) assigned to the pod
    """
    ip: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'ip'})


@attr.s(kw_only=True)
class PodDNSConfigOption(K8sObjectBase):
    """
    | PodDNSConfigOption defines DNS resolver options of a pod.
    
    :param name: Required.
    :param value: None
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    value: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'value'})


@attr.s(kw_only=True)
class PodDNSConfig(K8sObjectBase):
    """
    | PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.
    
    :param nameservers: A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.
    :param options: A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.
    :param searches: A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.
    """
    nameservers: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'nameservers'})
    options: Optional[Sequence[Union[kdsl.core.v1.PodDNSConfigOption,
        kdsl.core.v1.PodDNSConfigOptionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'options'})
    searches: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'searches'})


@attr.s(kw_only=True)
class PodCondition(K8sObjectBase):
    """
    | PodCondition contains details for the current condition of this pod.
    
    :param status: Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions
    :param type: Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions
    :param lastProbeTime: Last time we probed the condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
    :param message: Human-readable message indicating details about last transition.
    :param reason: Unique, one-word, CamelCase reason for the condition's last transition.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastProbeTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastProbeTime'})
    lastTransitionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTransitionTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class PodAntiAffinity(K8sObjectBase):
    """
    | Pod anti affinity is a group of inter pod anti affinity scheduling rules.
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[kdsl.core.v1.WeightedPodAffinityTerm,
        kdsl.core.v1.WeightedPodAffinityTermTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [kdsl.core.v1.PodAffinityTerm, kdsl.core.v1.PodAffinityTermTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class PodAffinityTerm(K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class PodAffinity(K8sObjectBase):
    """
    | Pod affinity is a group of inter pod affinity scheduling rules.
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[kdsl.core.v1.WeightedPodAffinityTerm,
        kdsl.core.v1.WeightedPodAffinityTermTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [kdsl.core.v1.PodAffinityTerm, kdsl.core.v1.PodAffinityTermTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class Pod(K8sResourceBase):
    """
    | Pod is a collection of containers that can run on a host. This resource is created by clients and scheduled onto hosts.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'Pod'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.PodSpec, kdsl.core.v1.PodSpecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class PhotonPersistentDiskVolumeSource(K8sObjectBase):
    """
    | Represents a Photon Controller persistent disk resource.
    
    :param pdID: ID that identifies Photon Controller persistent disk
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    pdID: str = attr.ib(metadata={'yaml_name': 'pdID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})


@attr.s(kw_only=True)
class PersistentVolumeStatus(K8sObjectBase):
    """
    | PersistentVolumeStatus is the current status of a persistent volume.
    
    :param message: A human-readable message indicating details about why the volume is in this state.
    :param phase: Phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase
    :param reason: Reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.
    """
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    phase: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'phase'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class PersistentVolumeSpec(K8sObjectBase):
    """
    | PersistentVolumeSpec is the specification of a persistent volume.
    
    :param accessModes: AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
    :param awsElasticBlockStore: AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param azureDisk: AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    :param azureFile: AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    :param capacity: A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity
    :param cephfs: CephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    :param cinder: Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param claimRef: ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
    :param csi: CSI represents storage that is handled by an external CSI driver (Beta feature).
    :param fc: FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    :param flexVolume: FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    :param flocker: Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running
    :param gcePersistentDisk: GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param glusterfs: Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    :param hostPath: HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    :param iscsi: ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.
    :param local: Local represents directly-attached storage with node affinity
    :param mountOptions: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
    :param nfs: NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param nodeAffinity: NodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.
    :param persistentVolumeReclaimPolicy: What happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
    :param photonPersistentDisk: PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    :param portworxVolume: PortworxVolume represents a portworx volume attached and mounted on kubelets host machine
    :param quobyte: Quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    :param rbd: RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    :param scaleIO: ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    :param storageClassName: Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.
    :param storageos: StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md
    :param volumeMode: volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec. This is a beta feature.
    :param vsphereVolume: VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    awsElasticBlockStore: Optional[Union[
        kdsl.core.v1.AWSElasticBlockStoreVolumeSource,
        kdsl.core.v1.AWSElasticBlockStoreVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'awsElasticBlockStore'})
    azureDisk: Optional[Union[kdsl.core.v1.AzureDiskVolumeSource,
        kdsl.core.v1.AzureDiskVolumeSourceTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'azureDisk'})
    azureFile: Optional[Union[kdsl.core.v1.AzureFilePersistentVolumeSource,
        kdsl.core.v1.AzureFilePersistentVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'azureFile'})
    capacity: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'capacity'})
    cephfs: Optional[Union[kdsl.core.v1.CephFSPersistentVolumeSource,
        kdsl.core.v1.CephFSPersistentVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'cephfs'})
    cinder: Optional[Union[kdsl.core.v1.CinderPersistentVolumeSource,
        kdsl.core.v1.CinderPersistentVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'cinder'})
    claimRef: Optional[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'claimRef'})
    csi: Optional[Union[kdsl.core.v1.CSIPersistentVolumeSource,
        kdsl.core.v1.CSIPersistentVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'csi'})
    fc: Optional[Union[kdsl.core.v1.FCVolumeSource,
        kdsl.core.v1.FCVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'fc'})
    flexVolume: Optional[Union[kdsl.core.v1.FlexPersistentVolumeSource,
        kdsl.core.v1.FlexPersistentVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'flexVolume'})
    flocker: Optional[Union[kdsl.core.v1.FlockerVolumeSource,
        kdsl.core.v1.FlockerVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'flocker'})
    gcePersistentDisk: Optional[Union[
        kdsl.core.v1.GCEPersistentDiskVolumeSource,
        kdsl.core.v1.GCEPersistentDiskVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'gcePersistentDisk'})
    glusterfs: Optional[Union[kdsl.core.v1.GlusterfsPersistentVolumeSource,
        kdsl.core.v1.GlusterfsPersistentVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'glusterfs'})
    hostPath: Optional[Union[kdsl.core.v1.HostPathVolumeSource,
        kdsl.core.v1.HostPathVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'hostPath'})
    iscsi: Optional[Union[kdsl.core.v1.ISCSIPersistentVolumeSource,
        kdsl.core.v1.ISCSIPersistentVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'iscsi'})
    local: Optional[Union[kdsl.core.v1.LocalVolumeSource,
        kdsl.core.v1.LocalVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'local'})
    mountOptions: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'mountOptions'})
    nfs: Optional[Union[kdsl.core.v1.NFSVolumeSource,
        kdsl.core.v1.NFSVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'nfs'})
    nodeAffinity: Optional[Union[kdsl.core.v1.VolumeNodeAffinity,
        kdsl.core.v1.VolumeNodeAffinityTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeAffinity'})
    persistentVolumeReclaimPolicy: Optional[str] = attr.ib(default=None,
        metadata={'yaml_name': 'persistentVolumeReclaimPolicy'})
    photonPersistentDisk: Optional[Union[
        kdsl.core.v1.PhotonPersistentDiskVolumeSource,
        kdsl.core.v1.PhotonPersistentDiskVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'photonPersistentDisk'})
    portworxVolume: Optional[Union[kdsl.core.v1.PortworxVolumeSource,
        kdsl.core.v1.PortworxVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'portworxVolume'})
    quobyte: Optional[Union[kdsl.core.v1.QuobyteVolumeSource,
        kdsl.core.v1.QuobyteVolumeSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'quobyte'})
    rbd: Optional[Union[kdsl.core.v1.RBDPersistentVolumeSource,
        kdsl.core.v1.RBDPersistentVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'rbd'})
    scaleIO: Optional[Union[kdsl.core.v1.ScaleIOPersistentVolumeSource,
        kdsl.core.v1.ScaleIOPersistentVolumeSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'scaleIO'})
    storageClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageClassName'})
    storageos: Optional[Union[kdsl.core.v1.StorageOSPersistentVolumeSource,
        kdsl.core.v1.StorageOSPersistentVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'storageos'})
    volumeMode: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeMode'})
    vsphereVolume: Optional[Union[
        kdsl.core.v1.VsphereVirtualDiskVolumeSource,
        kdsl.core.v1.VsphereVirtualDiskVolumeSourceTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'vsphereVolume'})


@attr.s(kw_only=True)
class PersistentVolumeList(K8sObjectBase):
    """
    | PersistentVolumeList is a list of PersistentVolume items.
    
    :param items: List of persistent volumes. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.PersistentVolume,
        kdsl.core.v1.PersistentVolumeTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class PersistentVolumeClaimVolumeSource(K8sObjectBase):
    """
    | PersistentVolumeClaimVolumeSource references the user's PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system).
    
    :param claimName: ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param readOnly: Will force the ReadOnly setting in VolumeMounts. Default false.
    """
    claimName: str = attr.ib(metadata={'yaml_name': 'claimName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class PersistentVolumeClaimStatus(K8sObjectBase):
    """
    | PersistentVolumeClaimStatus is the current status of a persistent volume claim.
    
    :param accessModes: AccessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    :param capacity: Represents the actual resources of the underlying volume.
    :param conditions: Current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'.
    :param phase: Phase represents the current phase of PersistentVolumeClaim.
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    capacity: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'capacity'})
    conditions: Optional[Sequence[Union[
        kdsl.core.v1.PersistentVolumeClaimCondition,
        kdsl.core.v1.PersistentVolumeClaimConditionTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'conditions'})
    phase: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'phase'})


@attr.s(kw_only=True)
class PersistentVolumeClaimSpec(K8sObjectBase):
    """
    | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes
    
    :param accessModes: AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    :param dataSource: This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and currently VolumeSnapshot is the only supported data source. If the provisioner can support VolumeSnapshot data source, it will create a new volume and data will be restored to the volume at the same time. If the provisioner does not support VolumeSnapshot data source, volume will not be created and the failure will be reported as an event. In the future, we plan to support more data source types and the behavior of the provisioner may change.
    :param resources: Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    :param selector: A label query over volumes to consider for binding.
    :param storageClassName: Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1
    :param volumeMode: volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. This is a beta feature.
    :param volumeName: VolumeName is the binding reference to the PersistentVolume backing this claim.
    """
    accessModes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'accessModes'})
    dataSource: Optional[Union[kdsl.core.v1.TypedLocalObjectReference,
        kdsl.core.v1.TypedLocalObjectReferenceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'dataSource'})
    resources: Optional[Union[kdsl.core.v1.ResourceRequirements,
        kdsl.core.v1.ResourceRequirementsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'resources'})
    selector: Optional[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'selector'})
    storageClassName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageClassName'})
    volumeMode: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeMode'})
    volumeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'volumeName'})


@attr.s(kw_only=True)
class PersistentVolumeClaimList(K8sObjectBase):
    """
    | PersistentVolumeClaimList is a list of PersistentVolumeClaim items.
    
    :param items: A list of persistent volume claims. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.PersistentVolumeClaim,
        kdsl.core.v1.PersistentVolumeClaimTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class PersistentVolumeClaimCondition(K8sObjectBase):
    """
    | PersistentVolumeClaimCondition contails details about state of pvc
    
    :param status: None
    :param type: None
    :param lastProbeTime: Last time we probed the condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
    :param message: Human-readable message indicating details about last transition.
    :param reason: Unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastProbeTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastProbeTime'})
    lastTransitionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTransitionTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class PersistentVolumeClaim(K8sResourceBase):
    """
    | PersistentVolumeClaim is a user's request for and claim to a persistent volume
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'PersistentVolumeClaim'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.PersistentVolumeClaimSpec,
        kdsl.core.v1.PersistentVolumeClaimSpecTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class PersistentVolume(K8sResourceBase):
    """
    | PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes
    
    :param name: metadata.name
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines a specification of a persistent volume owned by the cluster. Provisioned by an administrator. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'PersistentVolume'
    name: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.PersistentVolumeSpec,
        kdsl.core.v1.PersistentVolumeSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class ObjectReference(K8sObjectBase):
    """
    | ObjectReference contains enough information to let you inspect or modify the referred object.
    
    :param apiVersion: API version of the referent.
    :param fieldPath: If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.
    :param kind: Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param namespace: Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
    :param resourceVersion: Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    :param uid: UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    fieldPath: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fieldPath'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    namespace: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'namespace'})
    resourceVersion: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'resourceVersion'})
    uid: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'uid'})


@attr.s(kw_only=True)
class ObjectFieldSelector(K8sObjectBase):
    """
    | ObjectFieldSelector selects an APIVersioned field of an object.
    
    :param fieldPath: Path of the field to select in the specified API version.
    :param apiVersion: Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    fieldPath: str = attr.ib(metadata={'yaml_name': 'fieldPath'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})


@attr.s(kw_only=True)
class NodeSystemInfo(K8sObjectBase):
    """
    | NodeSystemInfo is a set of ids/uuids to uniquely identify the node.
    
    :param architecture: The Architecture reported by the node
    :param bootID: Boot ID reported by the node.
    :param containerRuntimeVersion: ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0).
    :param kernelVersion: Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).
    :param kubeProxyVersion: KubeProxy Version reported by the node.
    :param kubeletVersion: Kubelet Version reported by the node.
    :param machineID: MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html
    :param operatingSystem: The Operating System reported by the node
    :param osImage: OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).
    :param systemUUID: SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/getting-system-uuid.html
    """
    architecture: str = attr.ib(metadata={'yaml_name': 'architecture'})
    bootID: str = attr.ib(metadata={'yaml_name': 'bootID'})
    containerRuntimeVersion: str = attr.ib(metadata={'yaml_name':
        'containerRuntimeVersion'})
    kernelVersion: str = attr.ib(metadata={'yaml_name': 'kernelVersion'})
    kubeProxyVersion: str = attr.ib(metadata={'yaml_name': 'kubeProxyVersion'})
    kubeletVersion: str = attr.ib(metadata={'yaml_name': 'kubeletVersion'})
    machineID: str = attr.ib(metadata={'yaml_name': 'machineID'})
    operatingSystem: str = attr.ib(metadata={'yaml_name': 'operatingSystem'})
    osImage: str = attr.ib(metadata={'yaml_name': 'osImage'})
    systemUUID: str = attr.ib(metadata={'yaml_name': 'systemUUID'})


@attr.s(kw_only=True)
class NodeStatus(K8sObjectBase):
    """
    | NodeStatus is information about the current status of a node.
    
    :param addresses: List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See http://pr.k8s.io/79391 for an example.
    :param allocatable: Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.
    :param capacity: Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity
    :param conditions: Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition
    :param config: Status of the config assigned to the node via the dynamic Kubelet config feature.
    :param daemonEndpoints: Endpoints of daemons running on the Node.
    :param images: List of container images on this node
    :param nodeInfo: Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#info
    :param phase: NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.
    :param volumesAttached: List of volumes that are attached to the node.
    :param volumesInUse: List of attachable volumes in use (mounted) by the node.
    """
    addresses: Optional[Sequence[Union[kdsl.core.v1.NodeAddress,
        kdsl.core.v1.NodeAddressTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'addresses'})
    allocatable: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'allocatable'})
    capacity: Optional[Mapping[str, str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'capacity'})
    conditions: Optional[Sequence[Union[kdsl.core.v1.NodeCondition,
        kdsl.core.v1.NodeConditionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'conditions'})
    config: Optional[Union[kdsl.core.v1.NodeConfigStatus,
        kdsl.core.v1.NodeConfigStatusTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'config'})
    daemonEndpoints: Optional[Union[kdsl.core.v1.NodeDaemonEndpoints,
        kdsl.core.v1.NodeDaemonEndpointsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'daemonEndpoints'})
    images: Optional[Sequence[Union[kdsl.core.v1.ContainerImage,
        kdsl.core.v1.ContainerImageTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'images'})
    nodeInfo: Optional[Union[kdsl.core.v1.NodeSystemInfo,
        kdsl.core.v1.NodeSystemInfoTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeInfo'})
    phase: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'phase'})
    volumesAttached: Optional[Sequence[Union[kdsl.core.v1.AttachedVolume,
        kdsl.core.v1.AttachedVolumeTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumesAttached'})
    volumesInUse: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'volumesInUse'})


@attr.s(kw_only=True)
class NodeSpec(K8sObjectBase):
    """
    | NodeSpec describes the attributes that a node is created with.
    
    :param configSource: If specified, the source to get node configuration from The DynamicKubeletConfig feature gate must be enabled for the Kubelet to use this field
    :param externalID: Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966
    :param podCIDR: PodCIDR represents the pod IP range assigned to the node.
    :param podCIDRs: podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.
    :param providerID: ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>
    :param taints: If specified, the node's taints.
    :param unschedulable: Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration
    """
    configSource: Optional[Union[kdsl.core.v1.NodeConfigSource,
        kdsl.core.v1.NodeConfigSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'configSource'})
    externalID: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'externalID'})
    podCIDR: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'podCIDR'})
    podCIDRs: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'podCIDRs'})
    providerID: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'providerID'})
    taints: Optional[Sequence[Union[kdsl.core.v1.Taint,
        kdsl.core.v1.TaintTypedDict]]] = attr.ib(default=None, metadata={
        'yaml_name': 'taints'})
    unschedulable: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'unschedulable'})


@attr.s(kw_only=True)
class NodeSelectorTerm(K8sObjectBase):
    """
    | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.core.v1.NodeSelectorRequirement,
        kdsl.core.v1.NodeSelectorRequirementTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.core.v1.NodeSelectorRequirement,
        kdsl.core.v1.NodeSelectorRequirementTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class NodeSelectorRequirement(K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class NodeSelector(K8sObjectBase):
    """
    | A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.
    
    :param nodeSelectorTerms: Required. A list of node selector terms. The terms are ORed.
    """
    nodeSelectorTerms: Sequence[Union[kdsl.core.v1.NodeSelectorTerm,
        kdsl.core.v1.NodeSelectorTermTypedDict]] = attr.ib(metadata={
        'yaml_name': 'nodeSelectorTerms'})


@attr.s(kw_only=True)
class NodeList(K8sObjectBase):
    """
    | NodeList is the whole list of all Nodes which have been registered with master.
    
    :param items: List of nodes
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.Node, kdsl.core.v1.NodeTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class NodeDaemonEndpoints(K8sObjectBase):
    """
    | NodeDaemonEndpoints lists ports opened by daemons running on the Node.
    
    :param kubeletEndpoint: Endpoint on which Kubelet is listening.
    """
    kubeletEndpoint: Optional[Union[kdsl.core.v1.DaemonEndpoint,
        kdsl.core.v1.DaemonEndpointTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'kubeletEndpoint'})


@attr.s(kw_only=True)
class NodeConfigStatus(K8sObjectBase):
    """
    | NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.
    
    :param active: Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error.
    :param assigned: Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned.
    :param error: Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.
    :param lastKnownGood: LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future.
    """
    active: Optional[Union[kdsl.core.v1.NodeConfigSource,
        kdsl.core.v1.NodeConfigSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'active'})
    assigned: Optional[Union[kdsl.core.v1.NodeConfigSource,
        kdsl.core.v1.NodeConfigSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'assigned'})
    error: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'error'})
    lastKnownGood: Optional[Union[kdsl.core.v1.NodeConfigSource,
        kdsl.core.v1.NodeConfigSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'lastKnownGood'})


@attr.s(kw_only=True)
class NodeConfigSource(K8sObjectBase):
    """
    | NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil.
    
    :param configMap: ConfigMap is a reference to a Node's ConfigMap
    """
    configMap: Optional[Union[kdsl.core.v1.ConfigMapNodeConfigSource,
        kdsl.core.v1.ConfigMapNodeConfigSourceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'configMap'})


@attr.s(kw_only=True)
class NodeCondition(K8sObjectBase):
    """
    | NodeCondition contains condition information for a node.
    
    :param status: Status of the condition, one of True, False, Unknown.
    :param type: Type of node condition.
    :param lastHeartbeatTime: Last time we got an update on a given condition.
    :param lastTransitionTime: Last time the condition transit from one status to another.
    :param message: Human readable message indicating details about last transition.
    :param reason: (brief) reason for the condition's last transition.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastHeartbeatTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastHeartbeatTime'})
    lastTransitionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTransitionTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class NodeAffinity(K8sObjectBase):
    """
    | Node affinity is a group of node affinity scheduling rules.
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[kdsl.core.v1.PreferredSchedulingTerm,
        kdsl.core.v1.PreferredSchedulingTermTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Union[
        kdsl.core.v1.NodeSelector, kdsl.core.v1.NodeSelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class NodeAddress(K8sObjectBase):
    """
    | NodeAddress contains information for the node's address.
    
    :param address: The node address.
    :param type: Node address type, one of Hostname, ExternalIP or InternalIP.
    """
    address: str = attr.ib(metadata={'yaml_name': 'address'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class Node(K8sResourceBase):
    """
    | Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache (i.e. in etcd).
    
    :param name: metadata.name
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the behavior of a node. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'Node'
    name: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.NodeSpec, kdsl.core.v1.NodeSpecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class NamespaceStatus(K8sObjectBase):
    """
    | NamespaceStatus is information about the current status of a Namespace.
    
    :param conditions: Represents the latest available observations of a namespace's current state.
    :param phase: Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
    """
    conditions: Optional[Sequence[Union[kdsl.core.v1.NamespaceCondition,
        kdsl.core.v1.NamespaceConditionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'conditions'})
    phase: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'phase'})


@attr.s(kw_only=True)
class NamespaceSpec(K8sObjectBase):
    """
    | NamespaceSpec describes the attributes on a Namespace.
    
    :param finalizers: Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
    """
    finalizers: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'finalizers'})


@attr.s(kw_only=True)
class NamespaceList(K8sObjectBase):
    """
    | NamespaceList is a list of Namespaces.
    
    :param items: Items is the list of Namespace objects in the list. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.Namespace,
        kdsl.core.v1.NamespaceTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class NamespaceCondition(K8sObjectBase):
    """
    | NamespaceCondition contains details about state of namespace.
    
    :param status: Status of the condition, one of True, False, Unknown.
    :param type: Type of namespace controller condition.
    :param lastTransitionTime: None
    :param message: None
    :param reason: None
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
class Namespace(K8sResourceBase):
    """
    | Namespace provides a scope for Names. Use of multiple namespaces is optional.
    
    :param name: metadata.name
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the behavior of the Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'Namespace'
    name: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.NamespaceSpec,
        kdsl.core.v1.NamespaceSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class NFSVolumeSource(K8sObjectBase):
    """
    | Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.
    
    :param path: Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param server: Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    :param readOnly: ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    server: str = attr.ib(metadata={'yaml_name': 'server'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class LocalVolumeSource(K8sObjectBase):
    """
    | Local represents directly-attached storage with node affinity (Beta feature)
    
    :param path: The full path to the volume on the node. It can be either a directory or block device (disk, partition, ...).
    :param fsType: Filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a fileystem if unspecified.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})


@attr.s(kw_only=True)
class LocalObjectReference(K8sObjectBase):
    """
    | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class LoadBalancerStatus(K8sObjectBase):
    """
    | LoadBalancerStatus represents the status of a load-balancer.
    
    :param ingress: Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.
    """
    ingress: Optional[Sequence[Union[kdsl.core.v1.LoadBalancerIngress,
        kdsl.core.v1.LoadBalancerIngressTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ingress'})


@attr.s(kw_only=True)
class LoadBalancerIngress(K8sObjectBase):
    """
    | LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended for the service should be sent to an ingress point.
    
    :param hostname: Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)
    :param ip: IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)
    """
    hostname: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'hostname'})
    ip: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'ip'})


@attr.s(kw_only=True)
class LimitRangeSpec(K8sObjectBase):
    """
    | LimitRangeSpec defines a min/max usage limit for resources that match on kind.
    
    :param limits: Limits is the list of LimitRangeItem objects that are enforced.
    """
    limits: Sequence[Union[kdsl.core.v1.LimitRangeItem,
        kdsl.core.v1.LimitRangeItemTypedDict]] = attr.ib(metadata={
        'yaml_name': 'limits'})


@attr.s(kw_only=True)
class LimitRangeList(K8sObjectBase):
    """
    | LimitRangeList is a list of LimitRange items.
    
    :param items: Items is a list of LimitRange objects. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.LimitRange,
        kdsl.core.v1.LimitRangeTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class LimitRangeItem(K8sObjectBase):
    """
    | LimitRangeItem defines a min/max usage limit for any resource that matches on kind.
    
    :param default: Default resource requirement limit value by resource name if resource limit is omitted.
    :param defaultRequest: DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.
    :param max: Max usage constraints on this kind by resource name.
    :param maxLimitRequestRatio: MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.
    :param min: Min usage constraints on this kind by resource name.
    :param type: Type of resource that this limit applies to.
    """
    default: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'default'})
    defaultRequest: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'defaultRequest'})
    max: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'max'})
    maxLimitRequestRatio: Optional[Mapping[str, str]] = attr.ib(default=
        None, metadata={'yaml_name': 'maxLimitRequestRatio'})
    min: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'min'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class LimitRange(K8sResourceBase):
    """
    | LimitRange sets resource usage limits for each kind of resource in a Namespace.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the limits enforced. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'LimitRange'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.core.v1.LimitRangeSpec,
        kdsl.core.v1.LimitRangeSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class Lifecycle(K8sObjectBase):
    """
    | Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.
    
    :param postStart: PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    :param preStop: PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    """
    postStart: Optional[Union[kdsl.core.v1.Handler,
        kdsl.core.v1.HandlerTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'postStart'})
    preStop: Optional[Union[kdsl.core.v1.Handler,
        kdsl.core.v1.HandlerTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'preStop'})


@attr.s(kw_only=True)
class KeyToPath(K8sObjectBase):
    """
    | Maps a string key to a path within a volume.
    
    :param key: The key to project.
    :param path: The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})


@attr.s(kw_only=True)
class ISCSIVolumeSource(K8sObjectBase):
    """
    | Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.
    
    :param iqn: Target iSCSI Qualified Name.
    :param lun: iSCSI Target Lun number.
    :param targetPortal: iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param chapAuthDiscovery: whether support iSCSI Discovery CHAP authentication
    :param chapAuthSession: whether support iSCSI Session CHAP authentication
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi
    :param initiatorName: Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    :param iscsiInterface: iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    :param portals: iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    :param secretRef: CHAP Secret for iSCSI target and initiator authentication
    """
    iqn: str = attr.ib(metadata={'yaml_name': 'iqn'})
    lun: int = attr.ib(metadata={'yaml_name': 'lun'})
    targetPortal: str = attr.ib(metadata={'yaml_name': 'targetPortal'})
    chapAuthDiscovery: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthDiscovery'})
    chapAuthSession: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthSession'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    initiatorName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'initiatorName'})
    iscsiInterface: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'iscsiInterface'})
    portals: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'portals'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class ISCSIPersistentVolumeSource(K8sObjectBase):
    """
    | ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.
    
    :param iqn: Target iSCSI Qualified Name.
    :param lun: iSCSI Target Lun number.
    :param targetPortal: iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param chapAuthDiscovery: whether support iSCSI Discovery CHAP authentication
    :param chapAuthSession: whether support iSCSI Session CHAP authentication
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi
    :param initiatorName: Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    :param iscsiInterface: iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    :param portals: iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    :param secretRef: CHAP Secret for iSCSI target and initiator authentication
    """
    iqn: str = attr.ib(metadata={'yaml_name': 'iqn'})
    lun: int = attr.ib(metadata={'yaml_name': 'lun'})
    targetPortal: str = attr.ib(metadata={'yaml_name': 'targetPortal'})
    chapAuthDiscovery: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthDiscovery'})
    chapAuthSession: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'chapAuthSession'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    initiatorName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'initiatorName'})
    iscsiInterface: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'iscsiInterface'})
    portals: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'portals'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class HostPathVolumeSource(K8sObjectBase):
    """
    | Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.
    
    :param path: Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    :param type: Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class HostAlias(K8sObjectBase):
    """
    | HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
    
    :param hostnames: Hostnames for the above IP address.
    :param ip: IP address of the host file entry.
    """
    hostnames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'hostnames'})
    ip: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'ip'})


@attr.s(kw_only=True)
class Handler(K8sObjectBase):
    """
    | Handler defines a specific action that should be taken
    
    :param exec: One and only one of the following should be specified. Exec specifies the action to take.
    :param httpGet: HTTPGet specifies the http request to perform.
    :param tcpSocket: TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported
    """
    exec: Optional[Union[kdsl.core.v1.ExecAction,
        kdsl.core.v1.ExecActionTypedDict]] = attr.ib(default=None, metadata
        ={'yaml_name': 'exec'})
    httpGet: Optional[Union[kdsl.core.v1.HTTPGetAction,
        kdsl.core.v1.HTTPGetActionTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'httpGet'})
    tcpSocket: Optional[Union[kdsl.core.v1.TCPSocketAction,
        kdsl.core.v1.TCPSocketActionTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'tcpSocket'})


@attr.s(kw_only=True)
class HTTPHeader(K8sObjectBase):
    """
    | HTTPHeader describes a custom header to be used in HTTP probes
    
    :param name: The header field name
    :param value: The header field value
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: str = attr.ib(metadata={'yaml_name': 'value'})


@attr.s(kw_only=True)
class HTTPGetAction(K8sObjectBase):
    """
    | HTTPGetAction describes an action based on HTTP Get requests.
    
    :param port: Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    :param host: Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    :param httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
    :param path: Path to access on the HTTP server.
    :param scheme: Scheme to use for connecting to the host. Defaults to HTTP.
    """
    port: Union[int, str] = attr.ib(metadata={'yaml_name': 'port'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})
    httpHeaders: Optional[Sequence[Union[kdsl.core.v1.HTTPHeader,
        kdsl.core.v1.HTTPHeaderTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'httpHeaders'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    scheme: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'scheme'})


@attr.s(kw_only=True)
class GlusterfsVolumeSource(K8sObjectBase):
    """
    | Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.
    
    :param endpoints: EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param path: Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param readOnly: ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    endpoints: str = attr.ib(metadata={'yaml_name': 'endpoints'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class GlusterfsPersistentVolumeSource(K8sObjectBase):
    """
    | Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.
    
    :param endpoints: EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param path: Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param endpointsNamespace: EndpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    :param readOnly: ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    endpoints: str = attr.ib(metadata={'yaml_name': 'endpoints'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    endpointsNamespace: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'endpointsNamespace'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class GitRepoVolumeSource(K8sObjectBase):
    """
    | Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.
    
    DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    
    :param repository: Repository URL
    :param directory: Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.
    :param revision: Commit hash for the specified revision.
    """
    repository: str = attr.ib(metadata={'yaml_name': 'repository'})
    directory: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'directory'})
    revision: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'revision'})


@attr.s(kw_only=True)
class GCEPersistentDiskVolumeSource(K8sObjectBase):
    """
    | Represents a Persistent Disk resource in Google Compute Engine.
    
    A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.
    
    :param pdName: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    :param readOnly: ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    pdName: str = attr.ib(metadata={'yaml_name': 'pdName'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class FlockerVolumeSource(K8sObjectBase):
    """
    | Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.
    
    :param datasetName: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated
    :param datasetUUID: UUID of the dataset. This is unique identifier of a Flocker dataset
    """
    datasetName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'datasetName'})
    datasetUUID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'datasetUUID'})


@attr.s(kw_only=True)
class FlexVolumeSource(K8sObjectBase):
    """
    | FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    
    :param driver: Driver is the name of the driver to use for this volume.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    :param options: Optional: Extra command options if any.
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    options: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'options'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class FlexPersistentVolumeSource(K8sObjectBase):
    """
    | FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin.
    
    :param driver: Driver is the name of the driver to use for this volume.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    :param options: Optional: Extra command options if any.
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretRef: Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    options: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'options'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class FCVolumeSource(K8sObjectBase):
    """
    | Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.
    
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param lun: Optional: FC target lun number
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param targetWWNs: Optional: FC target worldwide names (WWNs)
    :param wwids: Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.
    """
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    lun: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'lun'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    targetWWNs: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'targetWWNs'})
    wwids: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'wwids'})


@attr.s(kw_only=True)
class ExecAction(K8sObjectBase):
    """
    | ExecAction describes a "run in container" action.
    
    :param command: Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})


@attr.s(kw_only=True)
class EventSource(K8sObjectBase):
    """
    | EventSource contains information for an event.
    
    :param component: Component from which the event is generated.
    :param host: Node name on which the event is generated.
    """
    component: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'component'})
    host: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class EventSeries(K8sObjectBase):
    """
    | EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.
    
    :param count: Number of occurrences in this series up to the last heartbeat time
    :param lastObservedTime: Time of the last occurrence observed
    :param state: State of this Series: Ongoing or Finished Deprecated. Planned removal for 1.18
    """
    count: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'count'})
    lastObservedTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastObservedTime'})
    state: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'state'})


@attr.s(kw_only=True)
class EventList(K8sObjectBase):
    """
    | EventList is a list of events.
    
    :param items: List of events
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.Event, kdsl.core.v1.EventTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class Event(K8sResourceBase):
    """
    | Event is a report of an event somewhere in the cluster.
    
    :param involvedObject: The object that this event is about.
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param action: What action was taken/failed regarding to the Regarding object.
    :param annotations: metadata.annotations
    :param count: The number of times this event has occurred.
    :param eventTime: Time when this Event was first observed.
    :param firstTimestamp: The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)
    :param labels: metadata.labels
    :param lastTimestamp: The time at which the most recent occurrence of this event was recorded.
    :param message: A human-readable description of the status of this operation.
    :param reason: This should be a short, machine understandable string that gives the reason for the transition into the object's current status.
    :param related: Optional secondary object for more complex actions.
    :param reportingComponent: Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.
    :param reportingInstance: ID of the controller instance, e.g. `kubelet-xyzf`.
    :param series: Data about the Event series this event represents or nil if it's a singleton Event.
    :param source: The component reporting this event. Should be a short machine understandable string.
    :param type: Type of this event (Normal, Warning), new types could be added in the future
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'Event'
    involvedObject: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict] = attr.ib(metadata={
        'yaml_name': 'involvedObject'})
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    action: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'action'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    count: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'count'})
    eventTime: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'eventTime'})
    firstTimestamp: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'firstTimestamp'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    lastTimestamp: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTimestamp'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})
    related: Optional[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'related'})
    reportingComponent: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'reportingComponent'})
    reportingInstance: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'reportingInstance'})
    series: Optional[Union[kdsl.core.v1.EventSeries,
        kdsl.core.v1.EventSeriesTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'series'})
    source: Optional[Union[kdsl.core.v1.EventSource,
        kdsl.core.v1.EventSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'source'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class EphemeralContainer(K8sObjectBase):
    """
    | An EphemeralContainer is a container that may be added temporarily to an existing pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a pod is removed or restarted. If an ephemeral container causes a pod to exceed its resource allocation, the pod may be evicted. Ephemeral containers may not be added by directly updating the pod spec. They must be added via the pod's ephemeralcontainers subresource, and they will appear in the pod spec once added. This is an alpha feature enabled by the EphemeralContainers feature flag.
    
    :param name: Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.
    :param args: Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    :param env: List of environment variables to set in the container. Cannot be updated.
    :param envFrom: List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.
    :param image: Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images
    :param imagePullPolicy: Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images
    :param lifecycle: Lifecycle is not allowed for ephemeral containers.
    :param livenessProbe: Probes are not allowed for ephemeral containers.
    :param ports: Ports are not allowed for ephemeral containers.
    :param readinessProbe: Probes are not allowed for ephemeral containers.
    :param resources: Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.
    :param securityContext: SecurityContext is not allowed for ephemeral containers.
    :param startupProbe: Probes are not allowed for ephemeral containers.
    :param stdin: Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.
    :param stdinOnce: Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false
    :param targetContainerName: If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container is run in whatever namespaces are shared for the pod. Note that the container runtime must support this feature.
    :param terminationMessagePath: Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.
    :param terminationMessagePolicy: Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.
    :param tty: Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.
    :param volumeDevices: volumeDevices is the list of block devices to be used by the container. This is a beta feature.
    :param volumeMounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
    :param workingDir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    args: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'args'})
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})
    env: Optional[Sequence[Union[kdsl.core.v1.EnvVar,
        kdsl.core.v1.EnvVarTypedDict]]] = attr.ib(default=None, metadata={
        'yaml_name': 'env'})
    envFrom: Optional[Sequence[Union[kdsl.core.v1.EnvFromSource,
        kdsl.core.v1.EnvFromSourceTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'envFrom'})
    image: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'image'})
    imagePullPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'imagePullPolicy'})
    lifecycle: Optional[Union[kdsl.core.v1.Lifecycle,
        kdsl.core.v1.LifecycleTypedDict]] = attr.ib(default=None, metadata=
        {'yaml_name': 'lifecycle'})
    livenessProbe: Optional[Union[kdsl.core.v1.Probe,
        kdsl.core.v1.ProbeTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'livenessProbe'})
    ports: Optional[Sequence[Union[kdsl.core.v1.ContainerPort,
        kdsl.core.v1.ContainerPortTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ports'})
    readinessProbe: Optional[Union[kdsl.core.v1.Probe,
        kdsl.core.v1.ProbeTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'readinessProbe'})
    resources: Optional[Union[kdsl.core.v1.ResourceRequirements,
        kdsl.core.v1.ResourceRequirementsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'resources'})
    securityContext: Optional[Union[kdsl.core.v1.SecurityContext,
        kdsl.core.v1.SecurityContextTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'securityContext'})
    startupProbe: Optional[Union[kdsl.core.v1.Probe,
        kdsl.core.v1.ProbeTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'startupProbe'})
    stdin: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'stdin'})
    stdinOnce: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'stdinOnce'})
    targetContainerName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'targetContainerName'})
    terminationMessagePath: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'terminationMessagePath'})
    terminationMessagePolicy: Optional[str] = attr.ib(default=None,
        metadata={'yaml_name': 'terminationMessagePolicy'})
    tty: Optional[bool] = attr.ib(default=None, metadata={'yaml_name': 'tty'})
    volumeDevices: Optional[Sequence[Union[kdsl.core.v1.VolumeDevice,
        kdsl.core.v1.VolumeDeviceTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeDevices'})
    volumeMounts: Optional[Sequence[Union[kdsl.core.v1.VolumeMount,
        kdsl.core.v1.VolumeMountTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeMounts'})
    workingDir: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'workingDir'})


@attr.s(kw_only=True)
class EnvVarSource(K8sObjectBase):
    """
    | EnvVarSource represents a source for the value of an EnvVar.
    
    :param configMapKeyRef: Selects a key of a ConfigMap.
    :param fieldRef: Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    :param secretKeyRef: Selects a key of a secret in the pod's namespace
    """
    configMapKeyRef: Optional[Union[kdsl.core.v1.ConfigMapKeySelector,
        kdsl.core.v1.ConfigMapKeySelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'configMapKeyRef'})
    fieldRef: Optional[Union[kdsl.core.v1.ObjectFieldSelector,
        kdsl.core.v1.ObjectFieldSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'fieldRef'})
    resourceFieldRef: Optional[Union[kdsl.core.v1.ResourceFieldSelector,
        kdsl.core.v1.ResourceFieldSelectorTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'resourceFieldRef'})
    secretKeyRef: Optional[Union[kdsl.core.v1.SecretKeySelector,
        kdsl.core.v1.SecretKeySelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretKeyRef'})


@attr.s(kw_only=True)
class EnvVar(K8sObjectBase):
    """
    | EnvVar represents an environment variable present in a Container.
    
    :param name: Name of the environment variable. Must be a C_IDENTIFIER.
    :param value: Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".
    :param valueFrom: Source for the environment variable's value. Cannot be used if value is not empty.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    value: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'value'})
    valueFrom: Optional[Union[kdsl.core.v1.EnvVarSource,
        kdsl.core.v1.EnvVarSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'valueFrom'})


@attr.s(kw_only=True)
class EnvFromSource(K8sObjectBase):
    """
    | EnvFromSource represents the source of a set of ConfigMaps
    
    :param configMapRef: The ConfigMap to select from
    :param prefix: An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.
    :param secretRef: The Secret to select from
    """
    configMapRef: Optional[Union[kdsl.core.v1.ConfigMapEnvSource,
        kdsl.core.v1.ConfigMapEnvSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'configMapRef'})
    prefix: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'prefix'})
    secretRef: Optional[Union[kdsl.core.v1.SecretEnvSource,
        kdsl.core.v1.SecretEnvSourceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class EndpointsList(K8sObjectBase):
    """
    | EndpointsList is a list of endpoints.
    
    :param items: List of endpoints.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.Endpoints,
        kdsl.core.v1.EndpointsTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class Endpoints(K8sResourceBase):
    """
    | Endpoints is a collection of endpoints that implement the actual service. Example:
      Name: "mysvc",
      Subsets: [
        {
          Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
          Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
        },
        {
          Addresses: [{"ip": "10.10.3.3"}],
          Ports: [{"name": "a", "port": 93}, {"name": "b", "port": 76}]
        },
     ]
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param subsets: The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service.
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'Endpoints'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    subsets: Optional[Sequence[Union[kdsl.core.v1.EndpointSubset,
        kdsl.core.v1.EndpointSubsetTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'subsets'})


@attr.s(kw_only=True)
class EndpointSubset(K8sObjectBase):
    """
    | EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:
      {
        Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
        Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
      }
    The resulting set of endpoints can be viewed as:
        a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
        b: [ 10.10.1.1:309, 10.10.2.2:309 ]
    
    :param addresses: IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.
    :param notReadyAddresses: IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.
    :param ports: Port numbers available on the related IP addresses.
    """
    addresses: Optional[Sequence[Union[kdsl.core.v1.EndpointAddress,
        kdsl.core.v1.EndpointAddressTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'addresses'})
    notReadyAddresses: Optional[Sequence[Union[kdsl.core.v1.EndpointAddress,
        kdsl.core.v1.EndpointAddressTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'notReadyAddresses'})
    ports: Optional[Sequence[Union[kdsl.core.v1.EndpointPort,
        kdsl.core.v1.EndpointPortTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ports'})


@attr.s(kw_only=True)
class EndpointPort(K8sObjectBase):
    """
    | EndpointPort is a tuple that describes a single port.
    
    :param port: The port number of the endpoint.
    :param name: The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined.
    :param protocol: The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
    """
    port: int = attr.ib(metadata={'yaml_name': 'port'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    protocol: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'protocol'})


@attr.s(kw_only=True)
class EndpointAddress(K8sObjectBase):
    """
    | EndpointAddress is a tuple that describes single IP address.
    
    :param ip: The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.
    :param hostname: The Hostname of this endpoint
    :param nodeName: Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.
    :param targetRef: Reference to object providing the endpoint.
    """
    ip: str = attr.ib(metadata={'yaml_name': 'ip'})
    hostname: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'hostname'})
    nodeName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'nodeName'})
    targetRef: Optional[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'targetRef'})


@attr.s(kw_only=True)
class EmptyDirVolumeSource(K8sObjectBase):
    """
    | Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.
    
    :param medium: What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    :param sizeLimit: Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir
    """
    medium: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'medium'})
    sizeLimit: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'sizeLimit'})


@attr.s(kw_only=True)
class DownwardAPIVolumeSource(K8sObjectBase):
    """
    | DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling.
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: Items is a list of downward API volume file
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[kdsl.core.v1.DownwardAPIVolumeFile,
        kdsl.core.v1.DownwardAPIVolumeFileTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'items'})


@attr.s(kw_only=True)
class DownwardAPIVolumeFile(K8sObjectBase):
    """
    | DownwardAPIVolumeFile represents information to create the file containing the pod field
    
    :param path: Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    :param fieldRef: Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.
    :param mode: Optional: mode bits to use on this file, must be a value between 0 and 0777. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    fieldRef: Optional[Union[kdsl.core.v1.ObjectFieldSelector,
        kdsl.core.v1.ObjectFieldSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'fieldRef'})
    mode: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'mode'})
    resourceFieldRef: Optional[Union[kdsl.core.v1.ResourceFieldSelector,
        kdsl.core.v1.ResourceFieldSelectorTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'resourceFieldRef'})


@attr.s(kw_only=True)
class DownwardAPIProjection(K8sObjectBase):
    """
    | Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode.
    
    :param items: Items is a list of DownwardAPIVolume file
    """
    items: Optional[Sequence[Union[kdsl.core.v1.DownwardAPIVolumeFile,
        kdsl.core.v1.DownwardAPIVolumeFileTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'items'})


@attr.s(kw_only=True)
class DaemonEndpoint(K8sObjectBase):
    """
    | DaemonEndpoint contains information about a single Daemon endpoint.
    
    :param Port: Port number of the given endpoint.
    """
    Port: int = attr.ib(metadata={'yaml_name': 'Port'})


@attr.s(kw_only=True)
class ContainerStatus(K8sObjectBase):
    """
    | ContainerStatus contains details for the current status of this container.
    
    :param image: The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images
    :param imageID: ImageID of the container's image.
    :param name: This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.
    :param ready: Specifies whether the container has passed its readiness probe.
    :param restartCount: The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.
    :param containerID: Container's ID in the format 'docker://<container_id>'.
    :param lastState: Details about the container's last termination condition.
    :param started: Specifies whether the container has passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. Is always true when no startupProbe is defined.
    :param state: Details about the container's current condition.
    """
    image: str = attr.ib(metadata={'yaml_name': 'image'})
    imageID: str = attr.ib(metadata={'yaml_name': 'imageID'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    ready: bool = attr.ib(metadata={'yaml_name': 'ready'})
    restartCount: int = attr.ib(metadata={'yaml_name': 'restartCount'})
    containerID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerID'})
    lastState: Optional[Union[kdsl.core.v1.ContainerState,
        kdsl.core.v1.ContainerStateTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'lastState'})
    started: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'started'})
    state: Optional[Union[kdsl.core.v1.ContainerState,
        kdsl.core.v1.ContainerStateTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'state'})


@attr.s(kw_only=True)
class ContainerStateWaiting(K8sObjectBase):
    """
    | ContainerStateWaiting is a waiting state of a container.
    
    :param message: Message regarding why the container is not yet running.
    :param reason: (brief) reason the container is not yet running.
    """
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class ContainerStateTerminated(K8sObjectBase):
    """
    | ContainerStateTerminated is a terminated state of a container.
    
    :param exitCode: Exit status from the last termination of the container
    :param containerID: Container's ID in the format 'docker://<container_id>'
    :param finishedAt: Time at which the container last terminated
    :param message: Message regarding the last termination of the container
    :param reason: (brief) reason from the last termination of the container
    :param signal: Signal from the last termination of the container
    :param startedAt: Time at which previous execution of the container started
    """
    exitCode: int = attr.ib(metadata={'yaml_name': 'exitCode'})
    containerID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'containerID'})
    finishedAt: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'finishedAt'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})
    signal: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'signal'})
    startedAt: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'startedAt'})


@attr.s(kw_only=True)
class ContainerStateRunning(K8sObjectBase):
    """
    | ContainerStateRunning is a running state of a container.
    
    :param startedAt: Time at which the container was last (re-)started
    """
    startedAt: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'startedAt'})


@attr.s(kw_only=True)
class ContainerState(K8sObjectBase):
    """
    | ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.
    
    :param running: Details about a running container
    :param terminated: Details about a terminated container
    :param waiting: Details about a waiting container
    """
    running: Optional[Union[kdsl.core.v1.ContainerStateRunning,
        kdsl.core.v1.ContainerStateRunningTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'running'})
    terminated: Optional[Union[kdsl.core.v1.ContainerStateTerminated,
        kdsl.core.v1.ContainerStateTerminatedTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'terminated'})
    waiting: Optional[Union[kdsl.core.v1.ContainerStateWaiting,
        kdsl.core.v1.ContainerStateWaitingTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'waiting'})


@attr.s(kw_only=True)
class ContainerPort(K8sObjectBase):
    """
    | ContainerPort represents a network port in a single container.
    
    :param containerPort: Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.
    :param hostIP: What host IP to bind the external port to.
    :param hostPort: Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.
    :param name: If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.
    :param protocol: Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".
    """
    containerPort: int = attr.ib(metadata={'yaml_name': 'containerPort'})
    hostIP: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'hostIP'})
    hostPort: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'hostPort'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    protocol: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'protocol'})


@attr.s(kw_only=True)
class ContainerImage(K8sObjectBase):
    """
    | Describe a container image
    
    :param names: Names by which this image is known. e.g. ["k8s.gcr.io/hyperkube:v1.0.7", "dockerhub.io/google_containers/hyperkube:v1.0.7"]
    :param sizeBytes: The size of the image in bytes.
    """
    names: Sequence[str] = attr.ib(metadata={'yaml_name': 'names'})
    sizeBytes: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'sizeBytes'})


@attr.s(kw_only=True)
class Container(K8sObjectBase):
    """
    | A single application container that you want to run within a pod.
    
    :param name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.
    :param args: Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    :param command: Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    :param env: List of environment variables to set in the container. Cannot be updated.
    :param envFrom: List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.
    :param image: Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.
    :param imagePullPolicy: Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images
    :param lifecycle: Actions that the management system should take in response to container lifecycle events. Cannot be updated.
    :param livenessProbe: Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param ports: List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Cannot be updated.
    :param readinessProbe: Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param resources: Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
    :param securityContext: Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    :param startupProbe: StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. This is an alpha feature enabled by the StartupProbe feature flag. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    :param stdin: Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.
    :param stdinOnce: Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false
    :param terminationMessagePath: Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.
    :param terminationMessagePolicy: Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.
    :param tty: Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.
    :param volumeDevices: volumeDevices is the list of block devices to be used by the container. This is a beta feature.
    :param volumeMounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
    :param workingDir: Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    args: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'args'})
    command: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'command'})
    env: Optional[Sequence[Union[kdsl.core.v1.EnvVar,
        kdsl.core.v1.EnvVarTypedDict]]] = attr.ib(default=None, metadata={
        'yaml_name': 'env'})
    envFrom: Optional[Sequence[Union[kdsl.core.v1.EnvFromSource,
        kdsl.core.v1.EnvFromSourceTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'envFrom'})
    image: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'image'})
    imagePullPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'imagePullPolicy'})
    lifecycle: Optional[Union[kdsl.core.v1.Lifecycle,
        kdsl.core.v1.LifecycleTypedDict]] = attr.ib(default=None, metadata=
        {'yaml_name': 'lifecycle'})
    livenessProbe: Optional[Union[kdsl.core.v1.Probe,
        kdsl.core.v1.ProbeTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'livenessProbe'})
    ports: Optional[Sequence[Union[kdsl.core.v1.ContainerPort,
        kdsl.core.v1.ContainerPortTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ports'})
    readinessProbe: Optional[Union[kdsl.core.v1.Probe,
        kdsl.core.v1.ProbeTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'readinessProbe'})
    resources: Optional[Union[kdsl.core.v1.ResourceRequirements,
        kdsl.core.v1.ResourceRequirementsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'resources'})
    securityContext: Optional[Union[kdsl.core.v1.SecurityContext,
        kdsl.core.v1.SecurityContextTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'securityContext'})
    startupProbe: Optional[Union[kdsl.core.v1.Probe,
        kdsl.core.v1.ProbeTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'startupProbe'})
    stdin: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'stdin'})
    stdinOnce: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'stdinOnce'})
    terminationMessagePath: Optional[str] = attr.ib(default=None, metadata=
        {'yaml_name': 'terminationMessagePath'})
    terminationMessagePolicy: Optional[str] = attr.ib(default=None,
        metadata={'yaml_name': 'terminationMessagePolicy'})
    tty: Optional[bool] = attr.ib(default=None, metadata={'yaml_name': 'tty'})
    volumeDevices: Optional[Sequence[Union[kdsl.core.v1.VolumeDevice,
        kdsl.core.v1.VolumeDeviceTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeDevices'})
    volumeMounts: Optional[Sequence[Union[kdsl.core.v1.VolumeMount,
        kdsl.core.v1.VolumeMountTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeMounts'})
    workingDir: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'workingDir'})


@attr.s(kw_only=True)
class ConfigMapVolumeSource(K8sObjectBase):
    """
    | Adapts a ConfigMap into a volume.
    
    The contents of the target ConfigMap's Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.
    
    :param defaultMode: Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param optional: Specify whether the ConfigMap or its keys must be defined
    """
    defaultMode: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'defaultMode'})
    items: Optional[Sequence[Union[kdsl.core.v1.KeyToPath,
        kdsl.core.v1.KeyToPathTypedDict]]] = attr.ib(default=None, metadata
        ={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ConfigMapProjection(K8sObjectBase):
    """
    | Adapts a ConfigMap into a projected volume.
    
    The contents of the target ConfigMap's Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode.
    
    :param items: If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param optional: Specify whether the ConfigMap or its keys must be defined
    """
    items: Optional[Sequence[Union[kdsl.core.v1.KeyToPath,
        kdsl.core.v1.KeyToPathTypedDict]]] = attr.ib(default=None, metadata
        ={'yaml_name': 'items'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ConfigMapNodeConfigSource(K8sObjectBase):
    """
    | ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node.
    
    :param kubeletConfigKey: KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.
    :param name: Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.
    :param namespace: Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.
    :param resourceVersion: ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
    :param uid: UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
    """
    kubeletConfigKey: str = attr.ib(metadata={'yaml_name': 'kubeletConfigKey'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    namespace: str = attr.ib(metadata={'yaml_name': 'namespace'})
    resourceVersion: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'resourceVersion'})
    uid: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'uid'})


@attr.s(kw_only=True)
class ConfigMapList(K8sObjectBase):
    """
    | ConfigMapList is a resource containing a list of ConfigMap objects.
    
    :param items: Items is the list of ConfigMaps.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.core.v1.ConfigMap,
        kdsl.core.v1.ConfigMapTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ConfigMapKeySelector(K8sObjectBase):
    """
    | Selects a key from a ConfigMap.
    
    :param key: The key to select.
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param optional: Specify whether the ConfigMap or its key must be defined
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ConfigMapEnvSource(K8sObjectBase):
    """
    | ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.
    
    The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    :param optional: Specify whether the ConfigMap must be defined
    """
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    optional: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'optional'})


@attr.s(kw_only=True)
class ConfigMap(K8sResourceBase):
    """
    | ConfigMap holds configuration data for pods to consume.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param binaryData: BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet.
    :param data: Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process.
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'ConfigMap'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    binaryData: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'binaryData'})
    data: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'data'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class ComponentStatusList(K8sObjectBase):
    """
    | Status of all the conditions for the component as a list of ComponentStatus objects.
    
    :param items: List of ComponentStatus objects.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.core.v1.ComponentStatus,
        kdsl.core.v1.ComponentStatusTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ComponentStatus(K8sObjectBase):
    """
    | ComponentStatus (and ComponentStatusList) holds the cluster validation info.
    
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param conditions: List of component conditions observed
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    conditions: Optional[Sequence[Union[kdsl.core.v1.ComponentCondition,
        kdsl.core.v1.ComponentConditionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'conditions'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ObjectMeta,
        kdsl.meta.v1.ObjectMetaTypedDict]] = attr.ib(default=None, metadata
        ={'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ComponentCondition(K8sObjectBase):
    """
    | Information about the condition of a component.
    
    :param status: Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown".
    :param type: Type of condition for a component. Valid value: "Healthy"
    :param error: Condition error code for a component. For example, a health check error code.
    :param message: Message about the condition for a component. For example, information about a health check.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    error: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'error'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})


@attr.s(kw_only=True)
class ClientIPConfig(K8sObjectBase):
    """
    | ClientIPConfig represents the configurations of Client IP based session affinity.
    
    :param timeoutSeconds: timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours).
    """
    timeoutSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'timeoutSeconds'})


@attr.s(kw_only=True)
class CinderVolumeSource(K8sObjectBase):
    """
    | Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.
    
    :param volumeID: volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param secretRef: Optional: points to a secret object containing parameters used to connect to OpenStack.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class CinderPersistentVolumeSource(K8sObjectBase):
    """
    | Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.
    
    :param volumeID: volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    :param secretRef: Optional: points to a secret object containing parameters used to connect to OpenStack.
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class CephFSVolumeSource(K8sObjectBase):
    """
    | Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.
    
    :param monitors: Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param path: Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretFile: Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretRef: Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param user: Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretFile'})
    secretRef: Optional[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class CephFSPersistentVolumeSource(K8sObjectBase):
    """
    | Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.
    
    :param monitors: Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param path: Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    :param readOnly: Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretFile: Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param secretRef: Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    :param user: Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    monitors: Sequence[str] = attr.ib(metadata={'yaml_name': 'monitors'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretFile: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'secretFile'})
    secretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'secretRef'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class Capabilities(K8sObjectBase):
    """
    | Adds and removes POSIX capabilities from running containers.
    
    :param add: Added capabilities
    :param drop: Removed capabilities
    """
    add: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'add'})
    drop: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'drop'})


@attr.s(kw_only=True)
class CSIVolumeSource(K8sObjectBase):
    """
    | Represents a source location of a volume to mount, managed by an external CSI driver
    
    :param driver: Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.
    :param fsType: Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.
    :param nodePublishSecretRef: NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    :param readOnly: Specifies a read-only configuration for the volume. Defaults to false (read/write).
    :param volumeAttributes: VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    nodePublishSecretRef: Optional[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodePublishSecretRef'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    volumeAttributes: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeAttributes'})


@attr.s(kw_only=True)
class CSIPersistentVolumeSource(K8sObjectBase):
    """
    | Represents storage that is managed by an external CSI volume driver (Beta feature)
    
    :param driver: Driver is the name of the driver to use for this volume. Required.
    :param volumeHandle: VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.
    :param controllerExpandSecretRef: ControllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This is an alpha field and requires enabling ExpandCSIVolumes feature gate. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    :param controllerPublishSecretRef: ControllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".
    :param nodePublishSecretRef: NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    :param nodeStageSecretRef: NodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    :param readOnly: Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).
    :param volumeAttributes: Attributes of the volume to publish.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})
    volumeHandle: str = attr.ib(metadata={'yaml_name': 'volumeHandle'})
    controllerExpandSecretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'controllerExpandSecretRef'})
    controllerPublishSecretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'controllerPublishSecretRef'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    nodePublishSecretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodePublishSecretRef'})
    nodeStageSecretRef: Optional[Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeStageSecretRef'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    volumeAttributes: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'volumeAttributes'})


@attr.s(kw_only=True)
class Binding(K8sResourceBase):
    """
    | Binding ties one object to another; for example, a pod is bound to a node by a scheduler. Deprecated in 1.7, please use the bindings subresource of pods instead.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param target: The target object that you want to bind to the standard object.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'v1'
    kind: ClassVar[str] = 'Binding'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    target: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict] = attr.ib(metadata={
        'yaml_name': 'target'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class AzureFileVolumeSource(K8sObjectBase):
    """
    | AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    
    :param secretName: the name of secret that contains Azure Storage Account Name and Key
    :param shareName: Share Name
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secretName: str = attr.ib(metadata={'yaml_name': 'secretName'})
    shareName: str = attr.ib(metadata={'yaml_name': 'shareName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AzureFilePersistentVolumeSource(K8sObjectBase):
    """
    | AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    
    :param secretName: the name of secret that contains Azure Storage Account Name and Key
    :param shareName: Share Name
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    :param secretNamespace: the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod
    """
    secretName: str = attr.ib(metadata={'yaml_name': 'secretName'})
    shareName: str = attr.ib(metadata={'yaml_name': 'shareName'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})
    secretNamespace: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'secretNamespace'})


@attr.s(kw_only=True)
class AzureDiskVolumeSource(K8sObjectBase):
    """
    | AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    
    :param diskName: The Name of the data disk in the blob storage
    :param diskURI: The URI the data disk in the blob storage
    :param cachingMode: Host Caching mode: None, Read Only, Read Write.
    :param fsType: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    :param kind: Expected values Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared
    :param readOnly: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    diskName: str = attr.ib(metadata={'yaml_name': 'diskName'})
    diskURI: str = attr.ib(metadata={'yaml_name': 'diskURI'})
    cachingMode: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'cachingMode'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AttachedVolume(K8sObjectBase):
    """
    | AttachedVolume describes a volume attached to a node
    
    :param devicePath: DevicePath represents the device path where the volume should be available
    :param name: Name of the attached volume
    """
    devicePath: str = attr.ib(metadata={'yaml_name': 'devicePath'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class Affinity(K8sObjectBase):
    """
    | Affinity is a group of affinity scheduling rules.
    
    :param nodeAffinity: Describes node affinity scheduling rules for the pod.
    :param podAffinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    :param podAntiAffinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    """
    nodeAffinity: Optional[Union[kdsl.core.v1.NodeAffinity,
        kdsl.core.v1.NodeAffinityTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeAffinity'})
    podAffinity: Optional[Union[kdsl.core.v1.PodAffinity,
        kdsl.core.v1.PodAffinityTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'podAffinity'})
    podAntiAffinity: Optional[Union[kdsl.core.v1.PodAntiAffinity,
        kdsl.core.v1.PodAntiAffinityTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'podAntiAffinity'})


@attr.s(kw_only=True)
class AWSElasticBlockStoreVolumeSource(K8sObjectBase):
    """
    | Represents a Persistent Disk resource in AWS.
    
    An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.
    
    :param volumeID: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param fsType: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).
    :param readOnly: Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    volumeID: str = attr.ib(metadata={'yaml_name': 'volumeID'})
    fsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fsType'})
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


class WindowsSecurityContextOptionsTypedDict(TypedDict, total=(False)):
    gmsaCredentialSpec: str
    gmsaCredentialSpecName: str
    runAsUserName: str


class WeightedPodAffinityTermTypedDict(TypedDict, total=(True)):
    podAffinityTerm: Union[kdsl.core.v1.PodAffinityTerm,
        kdsl.core.v1.PodAffinityTermTypedDict]
    weight: int


class VsphereVirtualDiskVolumeSourceOptionalTypedDict(TypedDict, total=(False)
    ):
    fsType: str
    storagePolicyID: str
    storagePolicyName: str


class VsphereVirtualDiskVolumeSourceTypedDict(
    VsphereVirtualDiskVolumeSourceOptionalTypedDict, total=(True)):
    volumePath: str


class VolumeProjectionTypedDict(TypedDict, total=(False)):
    configMap: Union[kdsl.core.v1.ConfigMapProjection,
        kdsl.core.v1.ConfigMapProjectionTypedDict]
    downwardAPI: Union[kdsl.core.v1.DownwardAPIProjection,
        kdsl.core.v1.DownwardAPIProjectionTypedDict]
    secret: Union[kdsl.core.v1.SecretProjection,
        kdsl.core.v1.SecretProjectionTypedDict]
    serviceAccountToken: Union[kdsl.core.v1.ServiceAccountTokenProjection,
        kdsl.core.v1.ServiceAccountTokenProjectionTypedDict]


class VolumeNodeAffinityTypedDict(TypedDict, total=(False)):
    required: Union[kdsl.core.v1.NodeSelector,
        kdsl.core.v1.NodeSelectorTypedDict]


class VolumeMountOptionalTypedDict(TypedDict, total=(False)):
    mountPropagation: str
    readOnly: bool
    subPath: str
    subPathExpr: str


class VolumeMountTypedDict(VolumeMountOptionalTypedDict, total=(True)):
    mountPath: str
    name: str


class VolumeDeviceTypedDict(TypedDict, total=(True)):
    devicePath: str
    name: str


class VolumeOptionalTypedDict(TypedDict, total=(False)):
    awsElasticBlockStore: Union[
        kdsl.core.v1.AWSElasticBlockStoreVolumeSource,
        kdsl.core.v1.AWSElasticBlockStoreVolumeSourceTypedDict]
    azureDisk: Union[kdsl.core.v1.AzureDiskVolumeSource,
        kdsl.core.v1.AzureDiskVolumeSourceTypedDict]
    azureFile: Union[kdsl.core.v1.AzureFileVolumeSource,
        kdsl.core.v1.AzureFileVolumeSourceTypedDict]
    cephfs: Union[kdsl.core.v1.CephFSVolumeSource,
        kdsl.core.v1.CephFSVolumeSourceTypedDict]
    cinder: Union[kdsl.core.v1.CinderVolumeSource,
        kdsl.core.v1.CinderVolumeSourceTypedDict]
    configMap: Union[kdsl.core.v1.ConfigMapVolumeSource,
        kdsl.core.v1.ConfigMapVolumeSourceTypedDict]
    csi: Union[kdsl.core.v1.CSIVolumeSource,
        kdsl.core.v1.CSIVolumeSourceTypedDict]
    downwardAPI: Union[kdsl.core.v1.DownwardAPIVolumeSource,
        kdsl.core.v1.DownwardAPIVolumeSourceTypedDict]
    emptyDir: Union[kdsl.core.v1.EmptyDirVolumeSource,
        kdsl.core.v1.EmptyDirVolumeSourceTypedDict]
    fc: Union[kdsl.core.v1.FCVolumeSource, kdsl.core.v1.FCVolumeSourceTypedDict
        ]
    flexVolume: Union[kdsl.core.v1.FlexVolumeSource,
        kdsl.core.v1.FlexVolumeSourceTypedDict]
    flocker: Union[kdsl.core.v1.FlockerVolumeSource,
        kdsl.core.v1.FlockerVolumeSourceTypedDict]
    gcePersistentDisk: Union[kdsl.core.v1.GCEPersistentDiskVolumeSource,
        kdsl.core.v1.GCEPersistentDiskVolumeSourceTypedDict]
    gitRepo: Union[kdsl.core.v1.GitRepoVolumeSource,
        kdsl.core.v1.GitRepoVolumeSourceTypedDict]
    glusterfs: Union[kdsl.core.v1.GlusterfsVolumeSource,
        kdsl.core.v1.GlusterfsVolumeSourceTypedDict]
    hostPath: Union[kdsl.core.v1.HostPathVolumeSource,
        kdsl.core.v1.HostPathVolumeSourceTypedDict]
    iscsi: Union[kdsl.core.v1.ISCSIVolumeSource,
        kdsl.core.v1.ISCSIVolumeSourceTypedDict]
    nfs: Union[kdsl.core.v1.NFSVolumeSource,
        kdsl.core.v1.NFSVolumeSourceTypedDict]
    persistentVolumeClaim: Union[
        kdsl.core.v1.PersistentVolumeClaimVolumeSource,
        kdsl.core.v1.PersistentVolumeClaimVolumeSourceTypedDict]
    photonPersistentDisk: Union[
        kdsl.core.v1.PhotonPersistentDiskVolumeSource,
        kdsl.core.v1.PhotonPersistentDiskVolumeSourceTypedDict]
    portworxVolume: Union[kdsl.core.v1.PortworxVolumeSource,
        kdsl.core.v1.PortworxVolumeSourceTypedDict]
    projected: Union[kdsl.core.v1.ProjectedVolumeSource,
        kdsl.core.v1.ProjectedVolumeSourceTypedDict]
    quobyte: Union[kdsl.core.v1.QuobyteVolumeSource,
        kdsl.core.v1.QuobyteVolumeSourceTypedDict]
    rbd: Union[kdsl.core.v1.RBDVolumeSource,
        kdsl.core.v1.RBDVolumeSourceTypedDict]
    scaleIO: Union[kdsl.core.v1.ScaleIOVolumeSource,
        kdsl.core.v1.ScaleIOVolumeSourceTypedDict]
    secret: Union[kdsl.core.v1.SecretVolumeSource,
        kdsl.core.v1.SecretVolumeSourceTypedDict]
    storageos: Union[kdsl.core.v1.StorageOSVolumeSource,
        kdsl.core.v1.StorageOSVolumeSourceTypedDict]
    vsphereVolume: Union[kdsl.core.v1.VsphereVirtualDiskVolumeSource,
        kdsl.core.v1.VsphereVirtualDiskVolumeSourceTypedDict]


class VolumeTypedDict(VolumeOptionalTypedDict, total=(True)):
    name: str


class TypedLocalObjectReferenceOptionalTypedDict(TypedDict, total=(False)):
    apiGroup: str


class TypedLocalObjectReferenceTypedDict(
    TypedLocalObjectReferenceOptionalTypedDict, total=(True)):
    kind: str
    name: str


class TopologySpreadConstraintOptionalTypedDict(TypedDict, total=(False)):
    labelSelector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]


class TopologySpreadConstraintTypedDict(
    TopologySpreadConstraintOptionalTypedDict, total=(True)):
    maxSkew: int
    topologyKey: str
    whenUnsatisfiable: str


class TopologySelectorTermTypedDict(TypedDict, total=(False)):
    matchLabelExpressions: Sequence[Union[
        kdsl.core.v1.TopologySelectorLabelRequirement,
        kdsl.core.v1.TopologySelectorLabelRequirementTypedDict]]


class TopologySelectorLabelRequirementTypedDict(TypedDict, total=(True)):
    key: str
    values: Sequence[str]


class TolerationTypedDict(TypedDict, total=(False)):
    effect: str
    key: str
    operator: str
    tolerationSeconds: int
    value: str


class TaintOptionalTypedDict(TypedDict, total=(False)):
    timeAdded: str
    value: str


class TaintTypedDict(TaintOptionalTypedDict, total=(True)):
    effect: str
    key: str


class TCPSocketActionOptionalTypedDict(TypedDict, total=(False)):
    host: str


class TCPSocketActionTypedDict(TCPSocketActionOptionalTypedDict, total=(True)):
    port: Union[int, str]


class SysctlTypedDict(TypedDict, total=(True)):
    name: str
    value: str


class StorageOSVolumeSourceTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]
    volumeName: str
    volumeNamespace: str


class StorageOSPersistentVolumeSourceTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]
    volumeName: str
    volumeNamespace: str


class SessionAffinityConfigTypedDict(TypedDict, total=(False)):
    clientIP: Union[kdsl.core.v1.ClientIPConfig,
        kdsl.core.v1.ClientIPConfigTypedDict]


class ServiceStatusTypedDict(TypedDict, total=(False)):
    loadBalancer: Union[kdsl.core.v1.LoadBalancerStatus,
        kdsl.core.v1.LoadBalancerStatusTypedDict]


class ServiceSpecTypedDict(TypedDict, total=(False)):
    clusterIP: str
    externalIPs: Sequence[str]
    externalName: str
    externalTrafficPolicy: str
    healthCheckNodePort: int
    ipFamily: str
    loadBalancerIP: str
    loadBalancerSourceRanges: Sequence[str]
    ports: Sequence[Union[kdsl.core.v1.ServicePort,
        kdsl.core.v1.ServicePortTypedDict]]
    publishNotReadyAddresses: bool
    selector: Mapping[str, str]
    sessionAffinity: str
    sessionAffinityConfig: Union[kdsl.core.v1.SessionAffinityConfig,
        kdsl.core.v1.SessionAffinityConfigTypedDict]
    topologyKeys: Sequence[str]
    type: str


class ServicePortOptionalTypedDict(TypedDict, total=(False)):
    name: str
    nodePort: int
    protocol: str
    targetPort: Union[int, str]


class ServicePortTypedDict(ServicePortOptionalTypedDict, total=(True)):
    port: int


class ServiceListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ServiceListTypedDict(ServiceListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.Service, kdsl.core.v1.ServiceTypedDict]]


class ServiceAccountTokenProjectionOptionalTypedDict(TypedDict, total=(False)):
    audience: str
    expirationSeconds: int


class ServiceAccountTokenProjectionTypedDict(
    ServiceAccountTokenProjectionOptionalTypedDict, total=(True)):
    path: str


class ServiceAccountListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ServiceAccountListTypedDict(ServiceAccountListOptionalTypedDict,
    total=(True)):
    items: Sequence[Union[kdsl.core.v1.ServiceAccount,
        kdsl.core.v1.ServiceAccountTypedDict]]


class ServiceAccountOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    automountServiceAccountToken: bool
    imagePullSecrets: Sequence[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]]
    labels: Mapping[str, str]
    secrets: Sequence[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]]


class ServiceAccountTypedDict(ServiceAccountOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class ServiceOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.ServiceSpec, kdsl.core.v1.ServiceSpecTypedDict]


class ServiceTypedDict(ServiceOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class SecurityContextTypedDict(TypedDict, total=(False)):
    allowPrivilegeEscalation: bool
    capabilities: Union[kdsl.core.v1.Capabilities,
        kdsl.core.v1.CapabilitiesTypedDict]
    privileged: bool
    procMount: str
    readOnlyRootFilesystem: bool
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: Union[kdsl.core.v1.SELinuxOptions,
        kdsl.core.v1.SELinuxOptionsTypedDict]
    windowsOptions: Union[kdsl.core.v1.WindowsSecurityContextOptions,
        kdsl.core.v1.WindowsSecurityContextOptionsTypedDict]


class SecretVolumeSourceTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[kdsl.core.v1.KeyToPath,
        kdsl.core.v1.KeyToPathTypedDict]]
    optional: bool
    secretName: str


class SecretReferenceTypedDict(TypedDict, total=(False)):
    name: str
    namespace: str


class SecretProjectionTypedDict(TypedDict, total=(False)):
    items: Sequence[Union[kdsl.core.v1.KeyToPath,
        kdsl.core.v1.KeyToPathTypedDict]]
    name: str
    optional: bool


class SecretListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class SecretListTypedDict(SecretListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.Secret, kdsl.core.v1.SecretTypedDict]]


class SecretKeySelectorOptionalTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class SecretKeySelectorTypedDict(SecretKeySelectorOptionalTypedDict, total=
    (True)):
    key: str


class SecretEnvSourceTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class SecretOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    data: Mapping[str, str]
    labels: Mapping[str, str]
    stringData: Mapping[str, str]
    type: str


class SecretTypedDict(SecretOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class ScopedResourceSelectorRequirementOptionalTypedDict(TypedDict, total=(
    False)):
    values: Sequence[str]


class ScopedResourceSelectorRequirementTypedDict(
    ScopedResourceSelectorRequirementOptionalTypedDict, total=(True)):
    operator: str
    scopeName: str


class ScopeSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.core.v1.ScopedResourceSelectorRequirement,
        kdsl.core.v1.ScopedResourceSelectorRequirementTypedDict]]


class ScaleIOVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    protectionDomain: str
    readOnly: bool
    sslEnabled: bool
    storageMode: str
    storagePool: str
    volumeName: str


class ScaleIOVolumeSourceTypedDict(ScaleIOVolumeSourceOptionalTypedDict,
    total=(True)):
    gateway: str
    secretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]
    system: str


class ScaleIOPersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    protectionDomain: str
    readOnly: bool
    sslEnabled: bool
    storageMode: str
    storagePool: str
    volumeName: str


class ScaleIOPersistentVolumeSourceTypedDict(
    ScaleIOPersistentVolumeSourceOptionalTypedDict, total=(True)):
    gateway: str
    secretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]
    system: str


class SELinuxOptionsTypedDict(TypedDict, total=(False)):
    level: str
    role: str
    type: str
    user: str


class ResourceRequirementsTypedDict(TypedDict, total=(False)):
    limits: Mapping[str, str]
    requests: Mapping[str, str]


class ResourceQuotaStatusTypedDict(TypedDict, total=(False)):
    hard: Mapping[str, str]
    used: Mapping[str, str]


class ResourceQuotaSpecTypedDict(TypedDict, total=(False)):
    hard: Mapping[str, str]
    scopeSelector: Union[kdsl.core.v1.ScopeSelector,
        kdsl.core.v1.ScopeSelectorTypedDict]
    scopes: Sequence[str]


class ResourceQuotaListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ResourceQuotaListTypedDict(ResourceQuotaListOptionalTypedDict, total=
    (True)):
    items: Sequence[Union[kdsl.core.v1.ResourceQuota,
        kdsl.core.v1.ResourceQuotaTypedDict]]


class ResourceQuotaOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.ResourceQuotaSpec,
        kdsl.core.v1.ResourceQuotaSpecTypedDict]


class ResourceQuotaTypedDict(ResourceQuotaOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class ResourceFieldSelectorOptionalTypedDict(TypedDict, total=(False)):
    containerName: str
    divisor: str


class ResourceFieldSelectorTypedDict(ResourceFieldSelectorOptionalTypedDict,
    total=(True)):
    resource: str


class ReplicationControllerStatusOptionalTypedDict(TypedDict, total=(False)):
    availableReplicas: int
    conditions: Sequence[Union[kdsl.core.v1.ReplicationControllerCondition,
        kdsl.core.v1.ReplicationControllerConditionTypedDict]]
    fullyLabeledReplicas: int
    observedGeneration: int
    readyReplicas: int


class ReplicationControllerStatusTypedDict(
    ReplicationControllerStatusOptionalTypedDict, total=(True)):
    replicas: int


class ReplicationControllerSpecTypedDict(TypedDict, total=(False)):
    minReadySeconds: int
    replicas: int
    selector: Mapping[str, str]
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]


class ReplicationControllerListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ReplicationControllerListTypedDict(
    ReplicationControllerListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.ReplicationController,
        kdsl.core.v1.ReplicationControllerTypedDict]]


class ReplicationControllerConditionOptionalTypedDict(TypedDict, total=(False)
    ):
    lastTransitionTime: str
    message: str
    reason: str


class ReplicationControllerConditionTypedDict(
    ReplicationControllerConditionOptionalTypedDict, total=(True)):
    status: str
    type: str


class ReplicationControllerOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.ReplicationControllerSpec,
        kdsl.core.v1.ReplicationControllerSpecTypedDict]


class ReplicationControllerTypedDict(ReplicationControllerOptionalTypedDict,
    total=(True)):
    name: str
    namespace: str


class RBDVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    keyring: str
    pool: str
    readOnly: bool
    secretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]
    user: str


class RBDVolumeSourceTypedDict(RBDVolumeSourceOptionalTypedDict, total=(True)):
    image: str
    monitors: Sequence[str]


class RBDPersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    keyring: str
    pool: str
    readOnly: bool
    secretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]
    user: str


class RBDPersistentVolumeSourceTypedDict(
    RBDPersistentVolumeSourceOptionalTypedDict, total=(True)):
    image: str
    monitors: Sequence[str]


class QuobyteVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    group: str
    readOnly: bool
    tenant: str
    user: str


class QuobyteVolumeSourceTypedDict(QuobyteVolumeSourceOptionalTypedDict,
    total=(True)):
    registry: str
    volume: str


class ProjectedVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    defaultMode: int


class ProjectedVolumeSourceTypedDict(ProjectedVolumeSourceOptionalTypedDict,
    total=(True)):
    sources: Sequence[Union[kdsl.core.v1.VolumeProjection,
        kdsl.core.v1.VolumeProjectionTypedDict]]


class ProbeTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.core.v1.ExecAction, kdsl.core.v1.ExecActionTypedDict]
    failureThreshold: int
    httpGet: Union[kdsl.core.v1.HTTPGetAction,
        kdsl.core.v1.HTTPGetActionTypedDict]
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: Union[kdsl.core.v1.TCPSocketAction,
        kdsl.core.v1.TCPSocketActionTypedDict]
    timeoutSeconds: int


class PreferredSchedulingTermTypedDict(TypedDict, total=(True)):
    preference: Union[kdsl.core.v1.NodeSelectorTerm,
        kdsl.core.v1.NodeSelectorTermTypedDict]
    weight: int


class PortworxVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool


class PortworxVolumeSourceTypedDict(PortworxVolumeSourceOptionalTypedDict,
    total=(True)):
    volumeID: str


class PodTemplateSpecTypedDict(TypedDict, total=(False)):
    metadata: Union[kdsl.meta.v1.ObjectMeta, kdsl.meta.v1.ObjectMetaTypedDict]
    spec: Union[kdsl.core.v1.PodSpec, kdsl.core.v1.PodSpecTypedDict]


class PodTemplateListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class PodTemplateListTypedDict(PodTemplateListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.PodTemplate,
        kdsl.core.v1.PodTemplateTypedDict]]


class PodTemplateOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]


class PodTemplateTypedDict(PodTemplateOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class PodStatusTypedDict(TypedDict, total=(False)):
    conditions: Sequence[Union[kdsl.core.v1.PodCondition,
        kdsl.core.v1.PodConditionTypedDict]]
    containerStatuses: Sequence[Union[kdsl.core.v1.ContainerStatus,
        kdsl.core.v1.ContainerStatusTypedDict]]
    ephemeralContainerStatuses: Sequence[Union[kdsl.core.v1.ContainerStatus,
        kdsl.core.v1.ContainerStatusTypedDict]]
    hostIP: str
    initContainerStatuses: Sequence[Union[kdsl.core.v1.ContainerStatus,
        kdsl.core.v1.ContainerStatusTypedDict]]
    message: str
    nominatedNodeName: str
    phase: str
    podIP: str
    podIPs: Sequence[Union[kdsl.core.v1.PodIP, kdsl.core.v1.PodIPTypedDict]]
    qosClass: str
    reason: str
    startTime: str


class PodSpecOptionalTypedDict(TypedDict, total=(False)):
    activeDeadlineSeconds: int
    affinity: Union[kdsl.core.v1.Affinity, kdsl.core.v1.AffinityTypedDict]
    automountServiceAccountToken: bool
    dnsConfig: Union[kdsl.core.v1.PodDNSConfig,
        kdsl.core.v1.PodDNSConfigTypedDict]
    dnsPolicy: str
    enableServiceLinks: bool
    ephemeralContainers: Sequence[Union[kdsl.core.v1.EphemeralContainer,
        kdsl.core.v1.EphemeralContainerTypedDict]]
    hostAliases: Sequence[Union[kdsl.core.v1.HostAlias,
        kdsl.core.v1.HostAliasTypedDict]]
    hostIPC: bool
    hostNetwork: bool
    hostPID: bool
    hostname: str
    imagePullSecrets: Sequence[Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]]
    initContainers: Sequence[Union[kdsl.core.v1.Container,
        kdsl.core.v1.ContainerTypedDict]]
    nodeName: str
    nodeSelector: Mapping[str, str]
    overhead: Mapping[str, str]
    preemptionPolicy: str
    priority: int
    priorityClassName: str
    readinessGates: Sequence[Union[kdsl.core.v1.PodReadinessGate,
        kdsl.core.v1.PodReadinessGateTypedDict]]
    restartPolicy: str
    runtimeClassName: str
    schedulerName: str
    securityContext: Union[kdsl.core.v1.PodSecurityContext,
        kdsl.core.v1.PodSecurityContextTypedDict]
    serviceAccount: str
    serviceAccountName: str
    shareProcessNamespace: bool
    subdomain: str
    terminationGracePeriodSeconds: int
    tolerations: Sequence[Union[kdsl.core.v1.Toleration,
        kdsl.core.v1.TolerationTypedDict]]
    topologySpreadConstraints: Sequence[Union[
        kdsl.core.v1.TopologySpreadConstraint,
        kdsl.core.v1.TopologySpreadConstraintTypedDict]]
    volumes: Sequence[Union[kdsl.core.v1.Volume, kdsl.core.v1.VolumeTypedDict]]


class PodSpecTypedDict(PodSpecOptionalTypedDict, total=(True)):
    containers: Sequence[Union[kdsl.core.v1.Container,
        kdsl.core.v1.ContainerTypedDict]]


class PodSecurityContextTypedDict(TypedDict, total=(False)):
    fsGroup: int
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: Union[kdsl.core.v1.SELinuxOptions,
        kdsl.core.v1.SELinuxOptionsTypedDict]
    supplementalGroups: Sequence[int]
    sysctls: Sequence[Union[kdsl.core.v1.Sysctl, kdsl.core.v1.SysctlTypedDict]]
    windowsOptions: Union[kdsl.core.v1.WindowsSecurityContextOptions,
        kdsl.core.v1.WindowsSecurityContextOptionsTypedDict]


class PodReadinessGateTypedDict(TypedDict, total=(True)):
    conditionType: str


class PodListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class PodListTypedDict(PodListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.Pod, kdsl.core.v1.PodTypedDict]]


class PodIPTypedDict(TypedDict, total=(False)):
    ip: str


class PodDNSConfigOptionTypedDict(TypedDict, total=(False)):
    name: str
    value: str


class PodDNSConfigTypedDict(TypedDict, total=(False)):
    nameservers: Sequence[str]
    options: Sequence[Union[kdsl.core.v1.PodDNSConfigOption,
        kdsl.core.v1.PodDNSConfigOptionTypedDict]]
    searches: Sequence[str]


class PodConditionOptionalTypedDict(TypedDict, total=(False)):
    lastProbeTime: str
    lastTransitionTime: str
    message: str
    reason: str


class PodConditionTypedDict(PodConditionOptionalTypedDict, total=(True)):
    status: str
    type: str


class PodAntiAffinityTypedDict(TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.core.v1.WeightedPodAffinityTerm,
        kdsl.core.v1.WeightedPodAffinityTermTypedDict]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.core.v1.PodAffinityTerm, kdsl.core.v1.PodAffinityTermTypedDict]]


class PodAffinityTermOptionalTypedDict(TypedDict, total=(False)):
    labelSelector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]
    namespaces: Sequence[str]


class PodAffinityTermTypedDict(PodAffinityTermOptionalTypedDict, total=(True)):
    topologyKey: str


class PodAffinityTypedDict(TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.core.v1.WeightedPodAffinityTerm,
        kdsl.core.v1.WeightedPodAffinityTermTypedDict]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.core.v1.PodAffinityTerm, kdsl.core.v1.PodAffinityTermTypedDict]]


class PodOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.PodSpec, kdsl.core.v1.PodSpecTypedDict]


class PodTypedDict(PodOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class PhotonPersistentDiskVolumeSourceOptionalTypedDict(TypedDict, total=(
    False)):
    fsType: str


class PhotonPersistentDiskVolumeSourceTypedDict(
    PhotonPersistentDiskVolumeSourceOptionalTypedDict, total=(True)):
    pdID: str


class PersistentVolumeStatusTypedDict(TypedDict, total=(False)):
    message: str
    phase: str
    reason: str


class PersistentVolumeSpecTypedDict(TypedDict, total=(False)):
    accessModes: Sequence[str]
    awsElasticBlockStore: Union[
        kdsl.core.v1.AWSElasticBlockStoreVolumeSource,
        kdsl.core.v1.AWSElasticBlockStoreVolumeSourceTypedDict]
    azureDisk: Union[kdsl.core.v1.AzureDiskVolumeSource,
        kdsl.core.v1.AzureDiskVolumeSourceTypedDict]
    azureFile: Union[kdsl.core.v1.AzureFilePersistentVolumeSource,
        kdsl.core.v1.AzureFilePersistentVolumeSourceTypedDict]
    capacity: Mapping[str, str]
    cephfs: Union[kdsl.core.v1.CephFSPersistentVolumeSource,
        kdsl.core.v1.CephFSPersistentVolumeSourceTypedDict]
    cinder: Union[kdsl.core.v1.CinderPersistentVolumeSource,
        kdsl.core.v1.CinderPersistentVolumeSourceTypedDict]
    claimRef: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]
    csi: Union[kdsl.core.v1.CSIPersistentVolumeSource,
        kdsl.core.v1.CSIPersistentVolumeSourceTypedDict]
    fc: Union[kdsl.core.v1.FCVolumeSource, kdsl.core.v1.FCVolumeSourceTypedDict
        ]
    flexVolume: Union[kdsl.core.v1.FlexPersistentVolumeSource,
        kdsl.core.v1.FlexPersistentVolumeSourceTypedDict]
    flocker: Union[kdsl.core.v1.FlockerVolumeSource,
        kdsl.core.v1.FlockerVolumeSourceTypedDict]
    gcePersistentDisk: Union[kdsl.core.v1.GCEPersistentDiskVolumeSource,
        kdsl.core.v1.GCEPersistentDiskVolumeSourceTypedDict]
    glusterfs: Union[kdsl.core.v1.GlusterfsPersistentVolumeSource,
        kdsl.core.v1.GlusterfsPersistentVolumeSourceTypedDict]
    hostPath: Union[kdsl.core.v1.HostPathVolumeSource,
        kdsl.core.v1.HostPathVolumeSourceTypedDict]
    iscsi: Union[kdsl.core.v1.ISCSIPersistentVolumeSource,
        kdsl.core.v1.ISCSIPersistentVolumeSourceTypedDict]
    local: Union[kdsl.core.v1.LocalVolumeSource,
        kdsl.core.v1.LocalVolumeSourceTypedDict]
    mountOptions: Sequence[str]
    nfs: Union[kdsl.core.v1.NFSVolumeSource,
        kdsl.core.v1.NFSVolumeSourceTypedDict]
    nodeAffinity: Union[kdsl.core.v1.VolumeNodeAffinity,
        kdsl.core.v1.VolumeNodeAffinityTypedDict]
    persistentVolumeReclaimPolicy: str
    photonPersistentDisk: Union[
        kdsl.core.v1.PhotonPersistentDiskVolumeSource,
        kdsl.core.v1.PhotonPersistentDiskVolumeSourceTypedDict]
    portworxVolume: Union[kdsl.core.v1.PortworxVolumeSource,
        kdsl.core.v1.PortworxVolumeSourceTypedDict]
    quobyte: Union[kdsl.core.v1.QuobyteVolumeSource,
        kdsl.core.v1.QuobyteVolumeSourceTypedDict]
    rbd: Union[kdsl.core.v1.RBDPersistentVolumeSource,
        kdsl.core.v1.RBDPersistentVolumeSourceTypedDict]
    scaleIO: Union[kdsl.core.v1.ScaleIOPersistentVolumeSource,
        kdsl.core.v1.ScaleIOPersistentVolumeSourceTypedDict]
    storageClassName: str
    storageos: Union[kdsl.core.v1.StorageOSPersistentVolumeSource,
        kdsl.core.v1.StorageOSPersistentVolumeSourceTypedDict]
    volumeMode: str
    vsphereVolume: Union[kdsl.core.v1.VsphereVirtualDiskVolumeSource,
        kdsl.core.v1.VsphereVirtualDiskVolumeSourceTypedDict]


class PersistentVolumeListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class PersistentVolumeListTypedDict(PersistentVolumeListOptionalTypedDict,
    total=(True)):
    items: Sequence[Union[kdsl.core.v1.PersistentVolume,
        kdsl.core.v1.PersistentVolumeTypedDict]]


class PersistentVolumeClaimVolumeSourceOptionalTypedDict(TypedDict, total=(
    False)):
    readOnly: bool


class PersistentVolumeClaimVolumeSourceTypedDict(
    PersistentVolumeClaimVolumeSourceOptionalTypedDict, total=(True)):
    claimName: str


class PersistentVolumeClaimStatusTypedDict(TypedDict, total=(False)):
    accessModes: Sequence[str]
    capacity: Mapping[str, str]
    conditions: Sequence[Union[kdsl.core.v1.PersistentVolumeClaimCondition,
        kdsl.core.v1.PersistentVolumeClaimConditionTypedDict]]
    phase: str


class PersistentVolumeClaimSpecTypedDict(TypedDict, total=(False)):
    accessModes: Sequence[str]
    dataSource: Union[kdsl.core.v1.TypedLocalObjectReference,
        kdsl.core.v1.TypedLocalObjectReferenceTypedDict]
    resources: Union[kdsl.core.v1.ResourceRequirements,
        kdsl.core.v1.ResourceRequirementsTypedDict]
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]
    storageClassName: str
    volumeMode: str
    volumeName: str


class PersistentVolumeClaimListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class PersistentVolumeClaimListTypedDict(
    PersistentVolumeClaimListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.PersistentVolumeClaim,
        kdsl.core.v1.PersistentVolumeClaimTypedDict]]


class PersistentVolumeClaimConditionOptionalTypedDict(TypedDict, total=(False)
    ):
    lastProbeTime: str
    lastTransitionTime: str
    message: str
    reason: str


class PersistentVolumeClaimConditionTypedDict(
    PersistentVolumeClaimConditionOptionalTypedDict, total=(True)):
    status: str
    type: str


class PersistentVolumeClaimOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.PersistentVolumeClaimSpec,
        kdsl.core.v1.PersistentVolumeClaimSpecTypedDict]


class PersistentVolumeClaimTypedDict(PersistentVolumeClaimOptionalTypedDict,
    total=(True)):
    name: str
    namespace: str


class PersistentVolumeOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.PersistentVolumeSpec,
        kdsl.core.v1.PersistentVolumeSpecTypedDict]


class PersistentVolumeTypedDict(PersistentVolumeOptionalTypedDict, total=(True)
    ):
    name: str


class ObjectReferenceTypedDict(TypedDict, total=(False)):
    apiVersion: str
    fieldPath: str
    kind: str
    name: str
    namespace: str
    resourceVersion: str
    uid: str


class ObjectFieldSelectorOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str


class ObjectFieldSelectorTypedDict(ObjectFieldSelectorOptionalTypedDict,
    total=(True)):
    fieldPath: str


class NodeSystemInfoTypedDict(TypedDict, total=(True)):
    architecture: str
    bootID: str
    containerRuntimeVersion: str
    kernelVersion: str
    kubeProxyVersion: str
    kubeletVersion: str
    machineID: str
    operatingSystem: str
    osImage: str
    systemUUID: str


class NodeStatusTypedDict(TypedDict, total=(False)):
    addresses: Sequence[Union[kdsl.core.v1.NodeAddress,
        kdsl.core.v1.NodeAddressTypedDict]]
    allocatable: Mapping[str, str]
    capacity: Mapping[str, str]
    conditions: Sequence[Union[kdsl.core.v1.NodeCondition,
        kdsl.core.v1.NodeConditionTypedDict]]
    config: Union[kdsl.core.v1.NodeConfigStatus,
        kdsl.core.v1.NodeConfigStatusTypedDict]
    daemonEndpoints: Union[kdsl.core.v1.NodeDaemonEndpoints,
        kdsl.core.v1.NodeDaemonEndpointsTypedDict]
    images: Sequence[Union[kdsl.core.v1.ContainerImage,
        kdsl.core.v1.ContainerImageTypedDict]]
    nodeInfo: Union[kdsl.core.v1.NodeSystemInfo,
        kdsl.core.v1.NodeSystemInfoTypedDict]
    phase: str
    volumesAttached: Sequence[Union[kdsl.core.v1.AttachedVolume,
        kdsl.core.v1.AttachedVolumeTypedDict]]
    volumesInUse: Sequence[str]


class NodeSpecTypedDict(TypedDict, total=(False)):
    configSource: Union[kdsl.core.v1.NodeConfigSource,
        kdsl.core.v1.NodeConfigSourceTypedDict]
    externalID: str
    podCIDR: str
    podCIDRs: Sequence[str]
    providerID: str
    taints: Sequence[Union[kdsl.core.v1.Taint, kdsl.core.v1.TaintTypedDict]]
    unschedulable: bool


class NodeSelectorTermTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[kdsl.core.v1.NodeSelectorRequirement,
        kdsl.core.v1.NodeSelectorRequirementTypedDict]]
    matchFields: Sequence[Union[kdsl.core.v1.NodeSelectorRequirement,
        kdsl.core.v1.NodeSelectorRequirementTypedDict]]


class NodeSelectorRequirementOptionalTypedDict(TypedDict, total=(False)):
    values: Sequence[str]


class NodeSelectorRequirementTypedDict(NodeSelectorRequirementOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class NodeSelectorTypedDict(TypedDict, total=(True)):
    nodeSelectorTerms: Sequence[Union[kdsl.core.v1.NodeSelectorTerm,
        kdsl.core.v1.NodeSelectorTermTypedDict]]


class NodeListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class NodeListTypedDict(NodeListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.Node, kdsl.core.v1.NodeTypedDict]]


class NodeDaemonEndpointsTypedDict(TypedDict, total=(False)):
    kubeletEndpoint: Union[kdsl.core.v1.DaemonEndpoint,
        kdsl.core.v1.DaemonEndpointTypedDict]


class NodeConfigStatusTypedDict(TypedDict, total=(False)):
    active: Union[kdsl.core.v1.NodeConfigSource,
        kdsl.core.v1.NodeConfigSourceTypedDict]
    assigned: Union[kdsl.core.v1.NodeConfigSource,
        kdsl.core.v1.NodeConfigSourceTypedDict]
    error: str
    lastKnownGood: Union[kdsl.core.v1.NodeConfigSource,
        kdsl.core.v1.NodeConfigSourceTypedDict]


class NodeConfigSourceTypedDict(TypedDict, total=(False)):
    configMap: Union[kdsl.core.v1.ConfigMapNodeConfigSource,
        kdsl.core.v1.ConfigMapNodeConfigSourceTypedDict]


class NodeConditionOptionalTypedDict(TypedDict, total=(False)):
    lastHeartbeatTime: str
    lastTransitionTime: str
    message: str
    reason: str


class NodeConditionTypedDict(NodeConditionOptionalTypedDict, total=(True)):
    status: str
    type: str


class NodeAffinityTypedDict(TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.core.v1.PreferredSchedulingTerm,
        kdsl.core.v1.PreferredSchedulingTermTypedDict]]
    requiredDuringSchedulingIgnoredDuringExecution: Union[
        kdsl.core.v1.NodeSelector, kdsl.core.v1.NodeSelectorTypedDict]


class NodeAddressTypedDict(TypedDict, total=(True)):
    address: str
    type: str


class NodeOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.NodeSpec, kdsl.core.v1.NodeSpecTypedDict]


class NodeTypedDict(NodeOptionalTypedDict, total=(True)):
    name: str


class NamespaceStatusTypedDict(TypedDict, total=(False)):
    conditions: Sequence[Union[kdsl.core.v1.NamespaceCondition,
        kdsl.core.v1.NamespaceConditionTypedDict]]
    phase: str


class NamespaceSpecTypedDict(TypedDict, total=(False)):
    finalizers: Sequence[str]


class NamespaceListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class NamespaceListTypedDict(NamespaceListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.Namespace,
        kdsl.core.v1.NamespaceTypedDict]]


class NamespaceConditionOptionalTypedDict(TypedDict, total=(False)):
    lastTransitionTime: str
    message: str
    reason: str


class NamespaceConditionTypedDict(NamespaceConditionOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class NamespaceOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.NamespaceSpec, kdsl.core.v1.NamespaceSpecTypedDict
        ]


class NamespaceTypedDict(NamespaceOptionalTypedDict, total=(True)):
    name: str


class NFSVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class NFSVolumeSourceTypedDict(NFSVolumeSourceOptionalTypedDict, total=(True)):
    path: str
    server: str


class LocalVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str


class LocalVolumeSourceTypedDict(LocalVolumeSourceOptionalTypedDict, total=
    (True)):
    path: str


class LocalObjectReferenceTypedDict(TypedDict, total=(False)):
    name: str


class LoadBalancerStatusTypedDict(TypedDict, total=(False)):
    ingress: Sequence[Union[kdsl.core.v1.LoadBalancerIngress,
        kdsl.core.v1.LoadBalancerIngressTypedDict]]


class LoadBalancerIngressTypedDict(TypedDict, total=(False)):
    hostname: str
    ip: str


class LimitRangeSpecTypedDict(TypedDict, total=(True)):
    limits: Sequence[Union[kdsl.core.v1.LimitRangeItem,
        kdsl.core.v1.LimitRangeItemTypedDict]]


class LimitRangeListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class LimitRangeListTypedDict(LimitRangeListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.LimitRange,
        kdsl.core.v1.LimitRangeTypedDict]]


class LimitRangeItemTypedDict(TypedDict, total=(False)):
    default: Mapping[str, str]
    defaultRequest: Mapping[str, str]
    max: Mapping[str, str]
    maxLimitRequestRatio: Mapping[str, str]
    min: Mapping[str, str]
    type: str


class LimitRangeOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.core.v1.LimitRangeSpec,
        kdsl.core.v1.LimitRangeSpecTypedDict]


class LimitRangeTypedDict(LimitRangeOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class LifecycleTypedDict(TypedDict, total=(False)):
    postStart: Union[kdsl.core.v1.Handler, kdsl.core.v1.HandlerTypedDict]
    preStop: Union[kdsl.core.v1.Handler, kdsl.core.v1.HandlerTypedDict]


class KeyToPathOptionalTypedDict(TypedDict, total=(False)):
    mode: int


class KeyToPathTypedDict(KeyToPathOptionalTypedDict, total=(True)):
    key: str
    path: str


class ISCSIVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    chapAuthDiscovery: bool
    chapAuthSession: bool
    fsType: str
    initiatorName: str
    iscsiInterface: str
    portals: Sequence[str]
    readOnly: bool
    secretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]


class ISCSIVolumeSourceTypedDict(ISCSIVolumeSourceOptionalTypedDict, total=
    (True)):
    iqn: str
    lun: int
    targetPortal: str


class ISCSIPersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    chapAuthDiscovery: bool
    chapAuthSession: bool
    fsType: str
    initiatorName: str
    iscsiInterface: str
    portals: Sequence[str]
    readOnly: bool
    secretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]


class ISCSIPersistentVolumeSourceTypedDict(
    ISCSIPersistentVolumeSourceOptionalTypedDict, total=(True)):
    iqn: str
    lun: int
    targetPortal: str


class HostPathVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    type: str


class HostPathVolumeSourceTypedDict(HostPathVolumeSourceOptionalTypedDict,
    total=(True)):
    path: str


class HostAliasTypedDict(TypedDict, total=(False)):
    hostnames: Sequence[str]
    ip: str


class HandlerTypedDict(TypedDict, total=(False)):
    exec: Union[kdsl.core.v1.ExecAction, kdsl.core.v1.ExecActionTypedDict]
    httpGet: Union[kdsl.core.v1.HTTPGetAction,
        kdsl.core.v1.HTTPGetActionTypedDict]
    tcpSocket: Union[kdsl.core.v1.TCPSocketAction,
        kdsl.core.v1.TCPSocketActionTypedDict]


class HTTPHeaderTypedDict(TypedDict, total=(True)):
    name: str
    value: str


class HTTPGetActionOptionalTypedDict(TypedDict, total=(False)):
    host: str
    httpHeaders: Sequence[Union[kdsl.core.v1.HTTPHeader,
        kdsl.core.v1.HTTPHeaderTypedDict]]
    path: str
    scheme: str


class HTTPGetActionTypedDict(HTTPGetActionOptionalTypedDict, total=(True)):
    port: Union[int, str]


class GlusterfsVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class GlusterfsVolumeSourceTypedDict(GlusterfsVolumeSourceOptionalTypedDict,
    total=(True)):
    endpoints: str
    path: str


class GlusterfsPersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)
    ):
    endpointsNamespace: str
    readOnly: bool


class GlusterfsPersistentVolumeSourceTypedDict(
    GlusterfsPersistentVolumeSourceOptionalTypedDict, total=(True)):
    endpoints: str
    path: str


class GitRepoVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    directory: str
    revision: str


class GitRepoVolumeSourceTypedDict(GitRepoVolumeSourceOptionalTypedDict,
    total=(True)):
    repository: str


class GCEPersistentDiskVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    partition: int
    readOnly: bool


class GCEPersistentDiskVolumeSourceTypedDict(
    GCEPersistentDiskVolumeSourceOptionalTypedDict, total=(True)):
    pdName: str


class FlockerVolumeSourceTypedDict(TypedDict, total=(False)):
    datasetName: str
    datasetUUID: str


class FlexVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    options: Mapping[str, str]
    readOnly: bool
    secretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]


class FlexVolumeSourceTypedDict(FlexVolumeSourceOptionalTypedDict, total=(True)
    ):
    driver: str


class FlexPersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    options: Mapping[str, str]
    readOnly: bool
    secretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]


class FlexPersistentVolumeSourceTypedDict(
    FlexPersistentVolumeSourceOptionalTypedDict, total=(True)):
    driver: str


class FCVolumeSourceTypedDict(TypedDict, total=(False)):
    fsType: str
    lun: int
    readOnly: bool
    targetWWNs: Sequence[str]
    wwids: Sequence[str]


class ExecActionTypedDict(TypedDict, total=(False)):
    command: Sequence[str]


class EventSourceTypedDict(TypedDict, total=(False)):
    component: str
    host: str


class EventSeriesTypedDict(TypedDict, total=(False)):
    count: int
    lastObservedTime: str
    state: str


class EventListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class EventListTypedDict(EventListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.Event, kdsl.core.v1.EventTypedDict]]


class EventOptionalTypedDict(TypedDict, total=(False)):
    action: str
    annotations: Mapping[str, str]
    count: int
    eventTime: str
    firstTimestamp: str
    labels: Mapping[str, str]
    lastTimestamp: str
    message: str
    reason: str
    related: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]
    reportingComponent: str
    reportingInstance: str
    series: Union[kdsl.core.v1.EventSeries, kdsl.core.v1.EventSeriesTypedDict]
    source: Union[kdsl.core.v1.EventSource, kdsl.core.v1.EventSourceTypedDict]
    type: str


class EventTypedDict(EventOptionalTypedDict, total=(True)):
    involvedObject: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]
    name: str
    namespace: str


class EphemeralContainerOptionalTypedDict(TypedDict, total=(False)):
    args: Sequence[str]
    command: Sequence[str]
    env: Sequence[Union[kdsl.core.v1.EnvVar, kdsl.core.v1.EnvVarTypedDict]]
    envFrom: Sequence[Union[kdsl.core.v1.EnvFromSource,
        kdsl.core.v1.EnvFromSourceTypedDict]]
    image: str
    imagePullPolicy: str
    lifecycle: Union[kdsl.core.v1.Lifecycle, kdsl.core.v1.LifecycleTypedDict]
    livenessProbe: Union[kdsl.core.v1.Probe, kdsl.core.v1.ProbeTypedDict]
    ports: Sequence[Union[kdsl.core.v1.ContainerPort,
        kdsl.core.v1.ContainerPortTypedDict]]
    readinessProbe: Union[kdsl.core.v1.Probe, kdsl.core.v1.ProbeTypedDict]
    resources: Union[kdsl.core.v1.ResourceRequirements,
        kdsl.core.v1.ResourceRequirementsTypedDict]
    securityContext: Union[kdsl.core.v1.SecurityContext,
        kdsl.core.v1.SecurityContextTypedDict]
    startupProbe: Union[kdsl.core.v1.Probe, kdsl.core.v1.ProbeTypedDict]
    stdin: bool
    stdinOnce: bool
    targetContainerName: str
    terminationMessagePath: str
    terminationMessagePolicy: str
    tty: bool
    volumeDevices: Sequence[Union[kdsl.core.v1.VolumeDevice,
        kdsl.core.v1.VolumeDeviceTypedDict]]
    volumeMounts: Sequence[Union[kdsl.core.v1.VolumeMount,
        kdsl.core.v1.VolumeMountTypedDict]]
    workingDir: str


class EphemeralContainerTypedDict(EphemeralContainerOptionalTypedDict,
    total=(True)):
    name: str


class EnvVarSourceTypedDict(TypedDict, total=(False)):
    configMapKeyRef: Union[kdsl.core.v1.ConfigMapKeySelector,
        kdsl.core.v1.ConfigMapKeySelectorTypedDict]
    fieldRef: Union[kdsl.core.v1.ObjectFieldSelector,
        kdsl.core.v1.ObjectFieldSelectorTypedDict]
    resourceFieldRef: Union[kdsl.core.v1.ResourceFieldSelector,
        kdsl.core.v1.ResourceFieldSelectorTypedDict]
    secretKeyRef: Union[kdsl.core.v1.SecretKeySelector,
        kdsl.core.v1.SecretKeySelectorTypedDict]


class EnvVarOptionalTypedDict(TypedDict, total=(False)):
    value: str
    valueFrom: Union[kdsl.core.v1.EnvVarSource,
        kdsl.core.v1.EnvVarSourceTypedDict]


class EnvVarTypedDict(EnvVarOptionalTypedDict, total=(True)):
    name: str


class EnvFromSourceTypedDict(TypedDict, total=(False)):
    configMapRef: Union[kdsl.core.v1.ConfigMapEnvSource,
        kdsl.core.v1.ConfigMapEnvSourceTypedDict]
    prefix: str
    secretRef: Union[kdsl.core.v1.SecretEnvSource,
        kdsl.core.v1.SecretEnvSourceTypedDict]


class EndpointsListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class EndpointsListTypedDict(EndpointsListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.Endpoints,
        kdsl.core.v1.EndpointsTypedDict]]


class EndpointsOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    subsets: Sequence[Union[kdsl.core.v1.EndpointSubset,
        kdsl.core.v1.EndpointSubsetTypedDict]]


class EndpointsTypedDict(EndpointsOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class EndpointSubsetTypedDict(TypedDict, total=(False)):
    addresses: Sequence[Union[kdsl.core.v1.EndpointAddress,
        kdsl.core.v1.EndpointAddressTypedDict]]
    notReadyAddresses: Sequence[Union[kdsl.core.v1.EndpointAddress,
        kdsl.core.v1.EndpointAddressTypedDict]]
    ports: Sequence[Union[kdsl.core.v1.EndpointPort,
        kdsl.core.v1.EndpointPortTypedDict]]


class EndpointPortOptionalTypedDict(TypedDict, total=(False)):
    name: str
    protocol: str


class EndpointPortTypedDict(EndpointPortOptionalTypedDict, total=(True)):
    port: int


class EndpointAddressOptionalTypedDict(TypedDict, total=(False)):
    hostname: str
    nodeName: str
    targetRef: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]


class EndpointAddressTypedDict(EndpointAddressOptionalTypedDict, total=(True)):
    ip: str


class EmptyDirVolumeSourceTypedDict(TypedDict, total=(False)):
    medium: str
    sizeLimit: str


class DownwardAPIVolumeSourceTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[kdsl.core.v1.DownwardAPIVolumeFile,
        kdsl.core.v1.DownwardAPIVolumeFileTypedDict]]


class DownwardAPIVolumeFileOptionalTypedDict(TypedDict, total=(False)):
    fieldRef: Union[kdsl.core.v1.ObjectFieldSelector,
        kdsl.core.v1.ObjectFieldSelectorTypedDict]
    mode: int
    resourceFieldRef: Union[kdsl.core.v1.ResourceFieldSelector,
        kdsl.core.v1.ResourceFieldSelectorTypedDict]


class DownwardAPIVolumeFileTypedDict(DownwardAPIVolumeFileOptionalTypedDict,
    total=(True)):
    path: str


class DownwardAPIProjectionTypedDict(TypedDict, total=(False)):
    items: Sequence[Union[kdsl.core.v1.DownwardAPIVolumeFile,
        kdsl.core.v1.DownwardAPIVolumeFileTypedDict]]


class DaemonEndpointTypedDict(TypedDict, total=(True)):
    Port: int


class ContainerStatusOptionalTypedDict(TypedDict, total=(False)):
    containerID: str
    lastState: Union[kdsl.core.v1.ContainerState,
        kdsl.core.v1.ContainerStateTypedDict]
    started: bool
    state: Union[kdsl.core.v1.ContainerState,
        kdsl.core.v1.ContainerStateTypedDict]


class ContainerStatusTypedDict(ContainerStatusOptionalTypedDict, total=(True)):
    image: str
    imageID: str
    name: str
    ready: bool
    restartCount: int


class ContainerStateWaitingTypedDict(TypedDict, total=(False)):
    message: str
    reason: str


class ContainerStateTerminatedOptionalTypedDict(TypedDict, total=(False)):
    containerID: str
    finishedAt: str
    message: str
    reason: str
    signal: int
    startedAt: str


class ContainerStateTerminatedTypedDict(
    ContainerStateTerminatedOptionalTypedDict, total=(True)):
    exitCode: int


class ContainerStateRunningTypedDict(TypedDict, total=(False)):
    startedAt: str


class ContainerStateTypedDict(TypedDict, total=(False)):
    running: Union[kdsl.core.v1.ContainerStateRunning,
        kdsl.core.v1.ContainerStateRunningTypedDict]
    terminated: Union[kdsl.core.v1.ContainerStateTerminated,
        kdsl.core.v1.ContainerStateTerminatedTypedDict]
    waiting: Union[kdsl.core.v1.ContainerStateWaiting,
        kdsl.core.v1.ContainerStateWaitingTypedDict]


class ContainerPortOptionalTypedDict(TypedDict, total=(False)):
    hostIP: str
    hostPort: int
    name: str
    protocol: str


class ContainerPortTypedDict(ContainerPortOptionalTypedDict, total=(True)):
    containerPort: int


class ContainerImageOptionalTypedDict(TypedDict, total=(False)):
    sizeBytes: int


class ContainerImageTypedDict(ContainerImageOptionalTypedDict, total=(True)):
    names: Sequence[str]


class ContainerOptionalTypedDict(TypedDict, total=(False)):
    args: Sequence[str]
    command: Sequence[str]
    env: Sequence[Union[kdsl.core.v1.EnvVar, kdsl.core.v1.EnvVarTypedDict]]
    envFrom: Sequence[Union[kdsl.core.v1.EnvFromSource,
        kdsl.core.v1.EnvFromSourceTypedDict]]
    image: str
    imagePullPolicy: str
    lifecycle: Union[kdsl.core.v1.Lifecycle, kdsl.core.v1.LifecycleTypedDict]
    livenessProbe: Union[kdsl.core.v1.Probe, kdsl.core.v1.ProbeTypedDict]
    ports: Sequence[Union[kdsl.core.v1.ContainerPort,
        kdsl.core.v1.ContainerPortTypedDict]]
    readinessProbe: Union[kdsl.core.v1.Probe, kdsl.core.v1.ProbeTypedDict]
    resources: Union[kdsl.core.v1.ResourceRequirements,
        kdsl.core.v1.ResourceRequirementsTypedDict]
    securityContext: Union[kdsl.core.v1.SecurityContext,
        kdsl.core.v1.SecurityContextTypedDict]
    startupProbe: Union[kdsl.core.v1.Probe, kdsl.core.v1.ProbeTypedDict]
    stdin: bool
    stdinOnce: bool
    terminationMessagePath: str
    terminationMessagePolicy: str
    tty: bool
    volumeDevices: Sequence[Union[kdsl.core.v1.VolumeDevice,
        kdsl.core.v1.VolumeDeviceTypedDict]]
    volumeMounts: Sequence[Union[kdsl.core.v1.VolumeMount,
        kdsl.core.v1.VolumeMountTypedDict]]
    workingDir: str


class ContainerTypedDict(ContainerOptionalTypedDict, total=(True)):
    name: str


class ConfigMapVolumeSourceTypedDict(TypedDict, total=(False)):
    defaultMode: int
    items: Sequence[Union[kdsl.core.v1.KeyToPath,
        kdsl.core.v1.KeyToPathTypedDict]]
    name: str
    optional: bool


class ConfigMapProjectionTypedDict(TypedDict, total=(False)):
    items: Sequence[Union[kdsl.core.v1.KeyToPath,
        kdsl.core.v1.KeyToPathTypedDict]]
    name: str
    optional: bool


class ConfigMapNodeConfigSourceOptionalTypedDict(TypedDict, total=(False)):
    resourceVersion: str
    uid: str


class ConfigMapNodeConfigSourceTypedDict(
    ConfigMapNodeConfigSourceOptionalTypedDict, total=(True)):
    kubeletConfigKey: str
    name: str
    namespace: str


class ConfigMapListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ConfigMapListTypedDict(ConfigMapListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.core.v1.ConfigMap,
        kdsl.core.v1.ConfigMapTypedDict]]


class ConfigMapKeySelectorOptionalTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class ConfigMapKeySelectorTypedDict(ConfigMapKeySelectorOptionalTypedDict,
    total=(True)):
    key: str


class ConfigMapEnvSourceTypedDict(TypedDict, total=(False)):
    name: str
    optional: bool


class ConfigMapOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    binaryData: Mapping[str, str]
    data: Mapping[str, str]
    labels: Mapping[str, str]


class ConfigMapTypedDict(ConfigMapOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class ComponentStatusListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ComponentStatusListTypedDict(ComponentStatusListOptionalTypedDict,
    total=(True)):
    items: Sequence[Union[kdsl.core.v1.ComponentStatus,
        kdsl.core.v1.ComponentStatusTypedDict]]


class ComponentStatusTypedDict(TypedDict, total=(False)):
    apiVersion: str
    conditions: Sequence[Union[kdsl.core.v1.ComponentCondition,
        kdsl.core.v1.ComponentConditionTypedDict]]
    kind: str
    metadata: Union[kdsl.meta.v1.ObjectMeta, kdsl.meta.v1.ObjectMetaTypedDict]


class ComponentConditionOptionalTypedDict(TypedDict, total=(False)):
    error: str
    message: str


class ComponentConditionTypedDict(ComponentConditionOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class ClientIPConfigTypedDict(TypedDict, total=(False)):
    timeoutSeconds: int


class CinderVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]


class CinderVolumeSourceTypedDict(CinderVolumeSourceOptionalTypedDict,
    total=(True)):
    volumeID: str


class CinderPersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    readOnly: bool
    secretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]


class CinderPersistentVolumeSourceTypedDict(
    CinderPersistentVolumeSourceOptionalTypedDict, total=(True)):
    volumeID: str


class CephFSVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    path: str
    readOnly: bool
    secretFile: str
    secretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]
    user: str


class CephFSVolumeSourceTypedDict(CephFSVolumeSourceOptionalTypedDict,
    total=(True)):
    monitors: Sequence[str]


class CephFSPersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    path: str
    readOnly: bool
    secretFile: str
    secretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]
    user: str


class CephFSPersistentVolumeSourceTypedDict(
    CephFSPersistentVolumeSourceOptionalTypedDict, total=(True)):
    monitors: Sequence[str]


class CapabilitiesTypedDict(TypedDict, total=(False)):
    add: Sequence[str]
    drop: Sequence[str]


class CSIVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    fsType: str
    nodePublishSecretRef: Union[kdsl.core.v1.LocalObjectReference,
        kdsl.core.v1.LocalObjectReferenceTypedDict]
    readOnly: bool
    volumeAttributes: Mapping[str, str]


class CSIVolumeSourceTypedDict(CSIVolumeSourceOptionalTypedDict, total=(True)):
    driver: str


class CSIPersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    controllerExpandSecretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]
    controllerPublishSecretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]
    fsType: str
    nodePublishSecretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]
    nodeStageSecretRef: Union[kdsl.core.v1.SecretReference,
        kdsl.core.v1.SecretReferenceTypedDict]
    readOnly: bool
    volumeAttributes: Mapping[str, str]


class CSIPersistentVolumeSourceTypedDict(
    CSIPersistentVolumeSourceOptionalTypedDict, total=(True)):
    driver: str
    volumeHandle: str


class BindingOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class BindingTypedDict(BindingOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    target: Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]


class AzureFileVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    readOnly: bool


class AzureFileVolumeSourceTypedDict(AzureFileVolumeSourceOptionalTypedDict,
    total=(True)):
    secretName: str
    shareName: str


class AzureFilePersistentVolumeSourceOptionalTypedDict(TypedDict, total=(False)
    ):
    readOnly: bool
    secretNamespace: str


class AzureFilePersistentVolumeSourceTypedDict(
    AzureFilePersistentVolumeSourceOptionalTypedDict, total=(True)):
    secretName: str
    shareName: str


class AzureDiskVolumeSourceOptionalTypedDict(TypedDict, total=(False)):
    cachingMode: str
    fsType: str
    kind: str
    readOnly: bool


class AzureDiskVolumeSourceTypedDict(AzureDiskVolumeSourceOptionalTypedDict,
    total=(True)):
    diskName: str
    diskURI: str


class AttachedVolumeTypedDict(TypedDict, total=(True)):
    devicePath: str
    name: str


class AffinityTypedDict(TypedDict, total=(False)):
    nodeAffinity: Union[kdsl.core.v1.NodeAffinity,
        kdsl.core.v1.NodeAffinityTypedDict]
    podAffinity: Union[kdsl.core.v1.PodAffinity,
        kdsl.core.v1.PodAffinityTypedDict]
    podAntiAffinity: Union[kdsl.core.v1.PodAntiAffinity,
        kdsl.core.v1.PodAntiAffinityTypedDict]


class AWSElasticBlockStoreVolumeSourceOptionalTypedDict(TypedDict, total=(
    False)):
    fsType: str
    partition: int
    readOnly: bool


class AWSElasticBlockStoreVolumeSourceTypedDict(
    AWSElasticBlockStoreVolumeSourceOptionalTypedDict, total=(True)):
    volumeID: str
