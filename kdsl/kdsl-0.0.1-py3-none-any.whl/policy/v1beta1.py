from __future__ import annotations
import kdsl.meta.v1
import attr
import kdsl.core.v1
import kdsl.policy.v1beta1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import Optional, Sequence, Union, TypedDict, ClassVar, Mapping


@attr.s(kw_only=True)
class SupplementalGroupsStrategyOptions(K8sObjectBase):
    """
    | SupplementalGroupsStrategyOptions defines the strategy type and options used to create the strategy.
    
    :param ranges: ranges are the allowed ranges of supplemental groups.  If you would like to force a single supplemental group then supply a single range with the same start and end. Required for MustRunAs.
    :param rule: rule is the strategy that will dictate what supplemental groups is used in the SecurityContext.
    """
    ranges: Optional[Sequence[Union[kdsl.policy.v1beta1.IDRange,
        kdsl.policy.v1beta1.IDRangeTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ranges'})
    rule: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'rule'})


@attr.s(kw_only=True)
class SELinuxStrategyOptions(K8sObjectBase):
    """
    | SELinuxStrategyOptions defines the strategy type and any options used to create the strategy.
    
    :param rule: rule is the strategy that will dictate the allowable labels that may be set.
    :param seLinuxOptions: seLinuxOptions required to run as; required for MustRunAs More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    """
    rule: str = attr.ib(metadata={'yaml_name': 'rule'})
    seLinuxOptions: Optional[Union[kdsl.core.v1.SELinuxOptions,
        kdsl.core.v1.SELinuxOptionsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'seLinuxOptions'})


@attr.s(kw_only=True)
class RuntimeClassStrategyOptions(K8sObjectBase):
    """
    | RuntimeClassStrategyOptions define the strategy that will dictate the allowable RuntimeClasses for a pod.
    
    :param allowedRuntimeClassNames: allowedRuntimeClassNames is a whitelist of RuntimeClass names that may be specified on a pod. A value of "*" means that any RuntimeClass name is allowed, and must be the only item in the list. An empty list requires the RuntimeClassName field to be unset.
    :param defaultRuntimeClassName: defaultRuntimeClassName is the default RuntimeClassName to set on the pod. The default MUST be allowed by the allowedRuntimeClassNames list. A value of nil does not mutate the Pod.
    """
    allowedRuntimeClassNames: Sequence[str] = attr.ib(metadata={'yaml_name':
        'allowedRuntimeClassNames'})
    defaultRuntimeClassName: Optional[str] = attr.ib(default=None, metadata
        ={'yaml_name': 'defaultRuntimeClassName'})


@attr.s(kw_only=True)
class RunAsUserStrategyOptions(K8sObjectBase):
    """
    | RunAsUserStrategyOptions defines the strategy type and any options used to create the strategy.
    
    :param rule: rule is the strategy that will dictate the allowable RunAsUser values that may be set.
    :param ranges: ranges are the allowed ranges of uids that may be used. If you would like to force a single uid then supply a single range with the same start and end. Required for MustRunAs.
    """
    rule: str = attr.ib(metadata={'yaml_name': 'rule'})
    ranges: Optional[Sequence[Union[kdsl.policy.v1beta1.IDRange,
        kdsl.policy.v1beta1.IDRangeTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ranges'})


@attr.s(kw_only=True)
class RunAsGroupStrategyOptions(K8sObjectBase):
    """
    | RunAsGroupStrategyOptions defines the strategy type and any options used to create the strategy.
    
    :param rule: rule is the strategy that will dictate the allowable RunAsGroup values that may be set.
    :param ranges: ranges are the allowed ranges of gids that may be used. If you would like to force a single gid then supply a single range with the same start and end. Required for MustRunAs.
    """
    rule: str = attr.ib(metadata={'yaml_name': 'rule'})
    ranges: Optional[Sequence[Union[kdsl.policy.v1beta1.IDRange,
        kdsl.policy.v1beta1.IDRangeTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ranges'})


@attr.s(kw_only=True)
class PodSecurityPolicySpec(K8sObjectBase):
    """
    | PodSecurityPolicySpec defines the policy enforced.
    
    :param fsGroup: fsGroup is the strategy that will dictate what fs group is used by the SecurityContext.
    :param runAsUser: runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.
    :param seLinux: seLinux is the strategy that will dictate the allowable labels that may be set.
    :param supplementalGroups: supplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.
    :param allowPrivilegeEscalation: allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.
    :param allowedCSIDrivers: AllowedCSIDrivers is a whitelist of inline CSI drivers that must be explicitly set to be embedded within a pod spec. An empty value indicates that any CSI driver can be used for inline ephemeral volumes. This is an alpha field, and is only honored if the API server enables the CSIInlineVolume feature gate.
    :param allowedCapabilities: allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.
    :param allowedFlexVolumes: allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the "volumes" field.
    :param allowedHostPaths: allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths may be used.
    :param allowedProcMountTypes: AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.
    :param allowedUnsafeSysctls: allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.
    
    Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc.
    :param defaultAddCapabilities: defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.
    :param defaultAllowPrivilegeEscalation: defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.
    :param forbiddenSysctls: forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.
    
    Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.
    :param hostIPC: hostIPC determines if the policy allows the use of HostIPC in the pod spec.
    :param hostNetwork: hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.
    :param hostPID: hostPID determines if the policy allows the use of HostPID in the pod spec.
    :param hostPorts: hostPorts determines which host port ranges are allowed to be exposed.
    :param privileged: privileged determines if a pod can request to be run as privileged.
    :param readOnlyRootFilesystem: readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.
    :param requiredDropCapabilities: requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.
    :param runAsGroup: RunAsGroup is the strategy that will dictate the allowable RunAsGroup values that may be set. If this field is omitted, the pod's RunAsGroup can take any value. This field requires the RunAsGroup feature gate to be enabled.
    :param runtimeClass: runtimeClass is the strategy that will dictate the allowable RuntimeClasses for a pod. If this field is omitted, the pod's runtimeClassName field is unrestricted. Enforcement of this field depends on the RuntimeClass feature gate being enabled.
    :param volumes: volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'.
    """
    fsGroup: Union[kdsl.policy.v1beta1.FSGroupStrategyOptions,
        kdsl.policy.v1beta1.FSGroupStrategyOptionsTypedDict] = attr.ib(metadata
        ={'yaml_name': 'fsGroup'})
    runAsUser: Union[kdsl.policy.v1beta1.RunAsUserStrategyOptions,
        kdsl.policy.v1beta1.RunAsUserStrategyOptionsTypedDict] = attr.ib(
        metadata={'yaml_name': 'runAsUser'})
    seLinux: Union[kdsl.policy.v1beta1.SELinuxStrategyOptions,
        kdsl.policy.v1beta1.SELinuxStrategyOptionsTypedDict] = attr.ib(metadata
        ={'yaml_name': 'seLinux'})
    supplementalGroups: Union[
        kdsl.policy.v1beta1.SupplementalGroupsStrategyOptions,
        kdsl.policy.v1beta1.SupplementalGroupsStrategyOptionsTypedDict
        ] = attr.ib(metadata={'yaml_name': 'supplementalGroups'})
    allowPrivilegeEscalation: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'allowPrivilegeEscalation'})
    allowedCSIDrivers: Optional[Sequence[Union[
        kdsl.policy.v1beta1.AllowedCSIDriver,
        kdsl.policy.v1beta1.AllowedCSIDriverTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'allowedCSIDrivers'})
    allowedCapabilities: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'allowedCapabilities'})
    allowedFlexVolumes: Optional[Sequence[Union[
        kdsl.policy.v1beta1.AllowedFlexVolume,
        kdsl.policy.v1beta1.AllowedFlexVolumeTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'allowedFlexVolumes'})
    allowedHostPaths: Optional[Sequence[Union[
        kdsl.policy.v1beta1.AllowedHostPath,
        kdsl.policy.v1beta1.AllowedHostPathTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'allowedHostPaths'})
    allowedProcMountTypes: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'allowedProcMountTypes'})
    allowedUnsafeSysctls: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'allowedUnsafeSysctls'})
    defaultAddCapabilities: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'defaultAddCapabilities'})
    defaultAllowPrivilegeEscalation: Optional[bool] = attr.ib(default=None,
        metadata={'yaml_name': 'defaultAllowPrivilegeEscalation'})
    forbiddenSysctls: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'forbiddenSysctls'})
    hostIPC: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'hostIPC'})
    hostNetwork: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'hostNetwork'})
    hostPID: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'hostPID'})
    hostPorts: Optional[Sequence[Union[kdsl.policy.v1beta1.HostPortRange,
        kdsl.policy.v1beta1.HostPortRangeTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'hostPorts'})
    privileged: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'privileged'})
    readOnlyRootFilesystem: Optional[bool] = attr.ib(default=None, metadata
        ={'yaml_name': 'readOnlyRootFilesystem'})
    requiredDropCapabilities: Optional[Sequence[str]] = attr.ib(default=
        None, metadata={'yaml_name': 'requiredDropCapabilities'})
    runAsGroup: Optional[Union[
        kdsl.policy.v1beta1.RunAsGroupStrategyOptions,
        kdsl.policy.v1beta1.RunAsGroupStrategyOptionsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'runAsGroup'})
    runtimeClass: Optional[Union[
        kdsl.policy.v1beta1.RuntimeClassStrategyOptions,
        kdsl.policy.v1beta1.RuntimeClassStrategyOptionsTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'runtimeClass'})
    volumes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'volumes'})


@attr.s(kw_only=True)
class PodSecurityPolicyList(K8sObjectBase):
    """
    | PodSecurityPolicyList is a list of PodSecurityPolicy objects.
    
    :param items: items is a list of schema objects.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.policy.v1beta1.PodSecurityPolicy,
        kdsl.policy.v1beta1.PodSecurityPolicyTypedDict]] = attr.ib(metadata
        ={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class PodSecurityPolicy(K8sResourceBase):
    """
    | PodSecurityPolicy governs the ability to make requests that affect the Security Context that will be applied to a pod and container.
    
    :param name: metadata.name
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: spec defines the policy enforced.
    """
    apiVersion: ClassVar[str] = 'policy/v1beta1'
    kind: ClassVar[str] = 'PodSecurityPolicy'
    name: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.policy.v1beta1.PodSecurityPolicySpec,
        kdsl.policy.v1beta1.PodSecurityPolicySpecTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class PodDisruptionBudgetStatus(K8sObjectBase):
    """
    | PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget. Status may trail the actual state of a system.
    
    :param currentHealthy: current number of healthy pods
    :param desiredHealthy: minimum desired number of healthy pods
    :param disruptionsAllowed: Number of pod disruptions that are currently allowed.
    :param expectedPods: total number of pods counted by this disruption budget
    :param disruptedPods: DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.
    :param observedGeneration: Most recent generation observed when updating this PDB status. PodDisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.
    """
    currentHealthy: int = attr.ib(metadata={'yaml_name': 'currentHealthy'})
    desiredHealthy: int = attr.ib(metadata={'yaml_name': 'desiredHealthy'})
    disruptionsAllowed: int = attr.ib(metadata={'yaml_name':
        'disruptionsAllowed'})
    expectedPods: int = attr.ib(metadata={'yaml_name': 'expectedPods'})
    disruptedPods: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'disruptedPods'})
    observedGeneration: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'observedGeneration'})


@attr.s(kw_only=True)
class PodDisruptionBudgetSpec(K8sObjectBase):
    """
    | PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.
    
    :param maxUnavailable: An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".
    :param minAvailable: An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".
    :param selector: Label query over pods whose evictions are managed by the disruption budget.
    """
    maxUnavailable: Optional[Union[int, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'maxUnavailable'})
    minAvailable: Optional[Union[int, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'minAvailable'})
    selector: Optional[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'selector'})


@attr.s(kw_only=True)
class PodDisruptionBudgetList(K8sObjectBase):
    """
    | PodDisruptionBudgetList is a collection of PodDisruptionBudgets.
    
    :param items: None
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: None
    """
    items: Sequence[Union[kdsl.policy.v1beta1.PodDisruptionBudget,
        kdsl.policy.v1beta1.PodDisruptionBudgetTypedDict]] = attr.ib(metadata
        ={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class PodDisruptionBudget(K8sResourceBase):
    """
    | PodDisruptionBudget is an object to define the max disruption that can be caused to a collection of pods
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Specification of the desired behavior of the PodDisruptionBudget.
    """
    apiVersion: ClassVar[str] = 'policy/v1beta1'
    kind: ClassVar[str] = 'PodDisruptionBudget'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.policy.v1beta1.PodDisruptionBudgetSpec,
        kdsl.policy.v1beta1.PodDisruptionBudgetSpecTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class IDRange(K8sObjectBase):
    """
    | IDRange provides a min/max of an allowed range of IDs.
    
    :param max: max is the end of the range, inclusive.
    :param min: min is the start of the range, inclusive.
    """
    max: int = attr.ib(metadata={'yaml_name': 'max'})
    min: int = attr.ib(metadata={'yaml_name': 'min'})


@attr.s(kw_only=True)
class HostPortRange(K8sObjectBase):
    """
    | HostPortRange defines a range of host ports that will be enabled by a policy for pods to use.  It requires both the start and end to be defined.
    
    :param max: max is the end of the range, inclusive.
    :param min: min is the start of the range, inclusive.
    """
    max: int = attr.ib(metadata={'yaml_name': 'max'})
    min: int = attr.ib(metadata={'yaml_name': 'min'})


@attr.s(kw_only=True)
class FSGroupStrategyOptions(K8sObjectBase):
    """
    | FSGroupStrategyOptions defines the strategy type and options used to create the strategy.
    
    :param ranges: ranges are the allowed ranges of fs groups.  If you would like to force a single fs group then supply a single range with the same start and end. Required for MustRunAs.
    :param rule: rule is the strategy that will dictate what FSGroup is used in the SecurityContext.
    """
    ranges: Optional[Sequence[Union[kdsl.policy.v1beta1.IDRange,
        kdsl.policy.v1beta1.IDRangeTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ranges'})
    rule: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'rule'})


@attr.s(kw_only=True)
class Eviction(K8sResourceBase):
    """
    | Eviction evicts a pod from its node subject to certain policies and safety constraints. This is a subresource of Pod.  A request to cause such an eviction is created by POSTing to .../pods/<pod name>/evictions.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param deleteOptions: DeleteOptions may be provided
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'policy/v1beta1'
    kind: ClassVar[str] = 'Eviction'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    deleteOptions: Optional[Union[kdsl.meta.v1.DeleteOptions,
        kdsl.meta.v1.DeleteOptionsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'deleteOptions'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class AllowedHostPath(K8sObjectBase):
    """
    | AllowedHostPath defines the host volume conditions that will be enabled by a policy for pods to use. It requires the path prefix to be defined.
    
    :param pathPrefix: pathPrefix is the path prefix that the host volume must match. It does not support `*`. Trailing slashes are trimmed when validating the path prefix with a host path.
    
    Examples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food` or `/etc/foo`
    :param readOnly: when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.
    """
    pathPrefix: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'pathPrefix'})
    readOnly: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'readOnly'})


@attr.s(kw_only=True)
class AllowedFlexVolume(K8sObjectBase):
    """
    | AllowedFlexVolume represents a single Flexvolume that is allowed to be used.
    
    :param driver: driver is the name of the Flexvolume driver.
    """
    driver: str = attr.ib(metadata={'yaml_name': 'driver'})


@attr.s(kw_only=True)
class AllowedCSIDriver(K8sObjectBase):
    """
    | AllowedCSIDriver represents a single inline CSI Driver that is allowed to be used.
    
    :param name: Name is the registered name of the CSI driver
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})


class SupplementalGroupsStrategyOptionsTypedDict(TypedDict, total=(False)):
    ranges: Sequence[Union[kdsl.policy.v1beta1.IDRange,
        kdsl.policy.v1beta1.IDRangeTypedDict]]
    rule: str


class SELinuxStrategyOptionsOptionalTypedDict(TypedDict, total=(False)):
    seLinuxOptions: Union[kdsl.core.v1.SELinuxOptions,
        kdsl.core.v1.SELinuxOptionsTypedDict]


class SELinuxStrategyOptionsTypedDict(SELinuxStrategyOptionsOptionalTypedDict,
    total=(True)):
    rule: str


class RuntimeClassStrategyOptionsOptionalTypedDict(TypedDict, total=(False)):
    defaultRuntimeClassName: str


class RuntimeClassStrategyOptionsTypedDict(
    RuntimeClassStrategyOptionsOptionalTypedDict, total=(True)):
    allowedRuntimeClassNames: Sequence[str]


class RunAsUserStrategyOptionsOptionalTypedDict(TypedDict, total=(False)):
    ranges: Sequence[Union[kdsl.policy.v1beta1.IDRange,
        kdsl.policy.v1beta1.IDRangeTypedDict]]


class RunAsUserStrategyOptionsTypedDict(
    RunAsUserStrategyOptionsOptionalTypedDict, total=(True)):
    rule: str


class RunAsGroupStrategyOptionsOptionalTypedDict(TypedDict, total=(False)):
    ranges: Sequence[Union[kdsl.policy.v1beta1.IDRange,
        kdsl.policy.v1beta1.IDRangeTypedDict]]


class RunAsGroupStrategyOptionsTypedDict(
    RunAsGroupStrategyOptionsOptionalTypedDict, total=(True)):
    rule: str


class PodSecurityPolicySpecOptionalTypedDict(TypedDict, total=(False)):
    allowPrivilegeEscalation: bool
    allowedCSIDrivers: Sequence[Union[kdsl.policy.v1beta1.AllowedCSIDriver,
        kdsl.policy.v1beta1.AllowedCSIDriverTypedDict]]
    allowedCapabilities: Sequence[str]
    allowedFlexVolumes: Sequence[Union[
        kdsl.policy.v1beta1.AllowedFlexVolume,
        kdsl.policy.v1beta1.AllowedFlexVolumeTypedDict]]
    allowedHostPaths: Sequence[Union[kdsl.policy.v1beta1.AllowedHostPath,
        kdsl.policy.v1beta1.AllowedHostPathTypedDict]]
    allowedProcMountTypes: Sequence[str]
    allowedUnsafeSysctls: Sequence[str]
    defaultAddCapabilities: Sequence[str]
    defaultAllowPrivilegeEscalation: bool
    forbiddenSysctls: Sequence[str]
    hostIPC: bool
    hostNetwork: bool
    hostPID: bool
    hostPorts: Sequence[Union[kdsl.policy.v1beta1.HostPortRange,
        kdsl.policy.v1beta1.HostPortRangeTypedDict]]
    privileged: bool
    readOnlyRootFilesystem: bool
    requiredDropCapabilities: Sequence[str]
    runAsGroup: Union[kdsl.policy.v1beta1.RunAsGroupStrategyOptions,
        kdsl.policy.v1beta1.RunAsGroupStrategyOptionsTypedDict]
    runtimeClass: Union[kdsl.policy.v1beta1.RuntimeClassStrategyOptions,
        kdsl.policy.v1beta1.RuntimeClassStrategyOptionsTypedDict]
    volumes: Sequence[str]


class PodSecurityPolicySpecTypedDict(PodSecurityPolicySpecOptionalTypedDict,
    total=(True)):
    fsGroup: Union[kdsl.policy.v1beta1.FSGroupStrategyOptions,
        kdsl.policy.v1beta1.FSGroupStrategyOptionsTypedDict]
    runAsUser: Union[kdsl.policy.v1beta1.RunAsUserStrategyOptions,
        kdsl.policy.v1beta1.RunAsUserStrategyOptionsTypedDict]
    seLinux: Union[kdsl.policy.v1beta1.SELinuxStrategyOptions,
        kdsl.policy.v1beta1.SELinuxStrategyOptionsTypedDict]
    supplementalGroups: Union[
        kdsl.policy.v1beta1.SupplementalGroupsStrategyOptions,
        kdsl.policy.v1beta1.SupplementalGroupsStrategyOptionsTypedDict]


class PodSecurityPolicyListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class PodSecurityPolicyListTypedDict(PodSecurityPolicyListOptionalTypedDict,
    total=(True)):
    items: Sequence[Union[kdsl.policy.v1beta1.PodSecurityPolicy,
        kdsl.policy.v1beta1.PodSecurityPolicyTypedDict]]


class PodSecurityPolicyOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.policy.v1beta1.PodSecurityPolicySpec,
        kdsl.policy.v1beta1.PodSecurityPolicySpecTypedDict]


class PodSecurityPolicyTypedDict(PodSecurityPolicyOptionalTypedDict, total=
    (True)):
    name: str


class PodDisruptionBudgetStatusOptionalTypedDict(TypedDict, total=(False)):
    disruptedPods: Mapping[str, str]
    observedGeneration: int


class PodDisruptionBudgetStatusTypedDict(
    PodDisruptionBudgetStatusOptionalTypedDict, total=(True)):
    currentHealthy: int
    desiredHealthy: int
    disruptionsAllowed: int
    expectedPods: int


class PodDisruptionBudgetSpecTypedDict(TypedDict, total=(False)):
    maxUnavailable: Union[int, str]
    minAvailable: Union[int, str]
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]


class PodDisruptionBudgetListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class PodDisruptionBudgetListTypedDict(PodDisruptionBudgetListOptionalTypedDict
    , total=(True)):
    items: Sequence[Union[kdsl.policy.v1beta1.PodDisruptionBudget,
        kdsl.policy.v1beta1.PodDisruptionBudgetTypedDict]]


class PodDisruptionBudgetOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.policy.v1beta1.PodDisruptionBudgetSpec,
        kdsl.policy.v1beta1.PodDisruptionBudgetSpecTypedDict]


class PodDisruptionBudgetTypedDict(PodDisruptionBudgetOptionalTypedDict,
    total=(True)):
    name: str
    namespace: str


class IDRangeTypedDict(TypedDict, total=(True)):
    max: int
    min: int


class HostPortRangeTypedDict(TypedDict, total=(True)):
    max: int
    min: int


class FSGroupStrategyOptionsTypedDict(TypedDict, total=(False)):
    ranges: Sequence[Union[kdsl.policy.v1beta1.IDRange,
        kdsl.policy.v1beta1.IDRangeTypedDict]]
    rule: str


class EvictionOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    deleteOptions: Union[kdsl.meta.v1.DeleteOptions,
        kdsl.meta.v1.DeleteOptionsTypedDict]
    labels: Mapping[str, str]


class EvictionTypedDict(EvictionOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class AllowedHostPathTypedDict(TypedDict, total=(False)):
    pathPrefix: str
    readOnly: bool


class AllowedFlexVolumeTypedDict(TypedDict, total=(True)):
    driver: str


class AllowedCSIDriverTypedDict(TypedDict, total=(True)):
    name: str
