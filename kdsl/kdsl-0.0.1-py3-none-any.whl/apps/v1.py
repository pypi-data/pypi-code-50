from __future__ import annotations
import kdsl.meta.v1
import kdsl.core.v1
import attr
import kdsl.apps.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Any, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class StatefulSetUpdateStrategy(K8sObjectBase):
    """
    | StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy.
    
    :param rollingUpdate: RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType.
    :param type: Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.
    """
    rollingUpdate: Optional[Union[
        kdsl.apps.v1.RollingUpdateStatefulSetStrategy,
        kdsl.apps.v1.RollingUpdateStatefulSetStrategyTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'rollingUpdate'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class StatefulSetStatus(K8sObjectBase):
    """
    | StatefulSetStatus represents the current state of a StatefulSet.
    
    :param replicas: replicas is the number of Pods created by the StatefulSet controller.
    :param collisionCount: collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.
    :param conditions: Represents the latest available observations of a statefulset's current state.
    :param currentReplicas: currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.
    :param currentRevision: currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).
    :param observedGeneration: observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.
    :param readyReplicas: readyReplicas is the number of Pods created by the StatefulSet controller that have a Ready Condition.
    :param updateRevision: updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)
    :param updatedReplicas: updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.
    """
    replicas: int = attr.ib(metadata={'yaml_name': 'replicas'})
    collisionCount: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'collisionCount'})
    conditions: Optional[Sequence[Union[kdsl.apps.v1.StatefulSetCondition,
        kdsl.apps.v1.StatefulSetConditionTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'conditions'})
    currentReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'currentReplicas'})
    currentRevision: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'currentRevision'})
    observedGeneration: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'observedGeneration'})
    readyReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'readyReplicas'})
    updateRevision: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'updateRevision'})
    updatedReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'updatedReplicas'})


@attr.s(kw_only=True)
class StatefulSetSpec(K8sObjectBase):
    """
    | A StatefulSetSpec is the specification of a StatefulSet.
    
    :param selector: selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    :param serviceName: serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller.
    :param template: template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet.
    :param podManagementPolicy: podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.
    :param replicas: replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.
    :param revisionHistoryLimit: revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.
    :param updateStrategy: updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.
    :param volumeClaimTemplates: volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.
    """
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict] = attr.ib(metadata={
        'yaml_name': 'selector'})
    serviceName: str = attr.ib(metadata={'yaml_name': 'serviceName'})
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'template'})
    podManagementPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'podManagementPolicy'})
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})
    revisionHistoryLimit: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'revisionHistoryLimit'})
    updateStrategy: Optional[Union[kdsl.apps.v1.StatefulSetUpdateStrategy,
        kdsl.apps.v1.StatefulSetUpdateStrategyTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'updateStrategy'})
    volumeClaimTemplates: Optional[Sequence[Union[
        kdsl.core.v1.PersistentVolumeClaim,
        kdsl.core.v1.PersistentVolumeClaimTypedDict]]] = attr.ib(default=
        None, metadata={'yaml_name': 'volumeClaimTemplates'})


@attr.s(kw_only=True)
class StatefulSetList(K8sObjectBase):
    """
    | StatefulSetList is a collection of StatefulSets.
    
    :param items: None
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: None
    """
    items: Sequence[Union[kdsl.apps.v1.StatefulSet,
        kdsl.apps.v1.StatefulSetTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class StatefulSetCondition(K8sObjectBase):
    """
    | StatefulSetCondition describes the state of a statefulset at a certain point.
    
    :param status: Status of the condition, one of True, False, Unknown.
    :param type: Type of statefulset condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
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
class StatefulSet(K8sResourceBase):
    """
    | StatefulSet represents a set of pods with consistent identities. Identities are defined as:
     - Network: A single stable DNS and hostname.
     - Storage: As many VolumeClaims as requested.
    The StatefulSet guarantees that a given network identity will always map to the same storage identity.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the desired identities of pods in this set.
    """
    apiVersion: ClassVar[str] = 'apps/v1'
    kind: ClassVar[str] = 'StatefulSet'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.apps.v1.StatefulSetSpec,
        kdsl.apps.v1.StatefulSetSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class RollingUpdateStatefulSetStrategy(K8sObjectBase):
    """
    | RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType.
    
    :param partition: Partition indicates the ordinal at which the StatefulSet should be partitioned. Default value is 0.
    """
    partition: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'partition'})


@attr.s(kw_only=True)
class RollingUpdateDeployment(K8sObjectBase):
    """
    | Spec to control the desired behavior of rolling update.
    
    :param maxSurge: The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.
    :param maxUnavailable: The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.
    """
    maxSurge: Optional[Union[int, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'maxSurge'})
    maxUnavailable: Optional[Union[int, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'maxUnavailable'})


@attr.s(kw_only=True)
class RollingUpdateDaemonSet(K8sObjectBase):
    """
    | Spec to control the desired behavior of daemon set rolling update.
    
    :param maxUnavailable: The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0. Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update.
    """
    maxUnavailable: Optional[Union[int, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'maxUnavailable'})


@attr.s(kw_only=True)
class ReplicaSetStatus(K8sObjectBase):
    """
    | ReplicaSetStatus represents the current status of a ReplicaSet.
    
    :param replicas: Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller
    :param availableReplicas: The number of available replicas (ready for at least minReadySeconds) for this replica set.
    :param conditions: Represents the latest available observations of a replica set's current state.
    :param fullyLabeledReplicas: The number of pods that have labels matching the labels of the pod template of the replicaset.
    :param observedGeneration: ObservedGeneration reflects the generation of the most recently observed ReplicaSet.
    :param readyReplicas: The number of ready replicas for this replica set.
    """
    replicas: int = attr.ib(metadata={'yaml_name': 'replicas'})
    availableReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'availableReplicas'})
    conditions: Optional[Sequence[Union[kdsl.apps.v1.ReplicaSetCondition,
        kdsl.apps.v1.ReplicaSetConditionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'conditions'})
    fullyLabeledReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'fullyLabeledReplicas'})
    observedGeneration: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'observedGeneration'})
    readyReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'readyReplicas'})


@attr.s(kw_only=True)
class ReplicaSetSpec(K8sObjectBase):
    """
    | ReplicaSetSpec is the specification of a ReplicaSet.
    
    :param selector: Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    :param minReadySeconds: Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    :param replicas: Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller
    :param template: Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    """
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict] = attr.ib(metadata={
        'yaml_name': 'selector'})
    minReadySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'minReadySeconds'})
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})
    template: Optional[Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'template'})


@attr.s(kw_only=True)
class ReplicaSetList(K8sObjectBase):
    """
    | ReplicaSetList is a collection of ReplicaSets.
    
    :param items: List of ReplicaSets. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    items: Sequence[Union[kdsl.apps.v1.ReplicaSet,
        kdsl.apps.v1.ReplicaSetTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ReplicaSetCondition(K8sObjectBase):
    """
    | ReplicaSetCondition describes the state of a replica set at a certain point.
    
    :param status: Status of the condition, one of True, False, Unknown.
    :param type: Type of replica set condition.
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
class ReplicaSet(K8sResourceBase):
    """
    | ReplicaSet ensures that a specified number of pod replicas are running at any given time.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Spec defines the specification of the desired behavior of the ReplicaSet. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'apps/v1'
    kind: ClassVar[str] = 'ReplicaSet'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.apps.v1.ReplicaSetSpec,
        kdsl.apps.v1.ReplicaSetSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class DeploymentStrategy(K8sObjectBase):
    """
    | DeploymentStrategy describes how to replace existing pods with new ones.
    
    :param rollingUpdate: Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.
    :param type: Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.
    """
    rollingUpdate: Optional[Union[kdsl.apps.v1.RollingUpdateDeployment,
        kdsl.apps.v1.RollingUpdateDeploymentTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'rollingUpdate'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class DeploymentStatus(K8sObjectBase):
    """
    | DeploymentStatus is the most recently observed status of the Deployment.
    
    :param availableReplicas: Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.
    :param collisionCount: Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.
    :param conditions: Represents the latest available observations of a deployment's current state.
    :param observedGeneration: The generation observed by the deployment controller.
    :param readyReplicas: Total number of ready pods targeted by this deployment.
    :param replicas: Total number of non-terminated pods targeted by this deployment (their labels match the selector).
    :param unavailableReplicas: Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.
    :param updatedReplicas: Total number of non-terminated pods targeted by this deployment that have the desired template spec.
    """
    availableReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'availableReplicas'})
    collisionCount: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'collisionCount'})
    conditions: Optional[Sequence[Union[kdsl.apps.v1.DeploymentCondition,
        kdsl.apps.v1.DeploymentConditionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'conditions'})
    observedGeneration: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'observedGeneration'})
    readyReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'readyReplicas'})
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})
    unavailableReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'unavailableReplicas'})
    updatedReplicas: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'updatedReplicas'})


@attr.s(kw_only=True)
class DeploymentSpec(K8sObjectBase):
    """
    | DeploymentSpec is the specification of the desired behavior of the Deployment.
    
    :param selector: Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.
    :param template: Template describes the pods that will be created.
    :param minReadySeconds: Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    :param paused: Indicates that the deployment is paused.
    :param progressDeadlineSeconds: The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.
    :param replicas: Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.
    :param revisionHistoryLimit: The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.
    :param strategy: The deployment strategy to use to replace existing pods with new ones.
    """
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict] = attr.ib(metadata={
        'yaml_name': 'selector'})
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'template'})
    minReadySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'minReadySeconds'})
    paused: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'paused'})
    progressDeadlineSeconds: Optional[int] = attr.ib(default=None, metadata
        ={'yaml_name': 'progressDeadlineSeconds'})
    replicas: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'replicas'})
    revisionHistoryLimit: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'revisionHistoryLimit'})
    strategy: Optional[Union[kdsl.apps.v1.DeploymentStrategy,
        kdsl.apps.v1.DeploymentStrategyTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'strategy'})


@attr.s(kw_only=True)
class DeploymentList(K8sObjectBase):
    """
    | DeploymentList is a list of Deployments.
    
    :param items: Items is the list of Deployments.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata.
    """
    items: Sequence[Union[kdsl.apps.v1.Deployment,
        kdsl.apps.v1.DeploymentTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class DeploymentCondition(K8sObjectBase):
    """
    | DeploymentCondition describes the state of a deployment at a certain point.
    
    :param status: Status of the condition, one of True, False, Unknown.
    :param type: Type of deployment condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
    :param lastUpdateTime: The last time this condition was updated.
    :param message: A human readable message indicating details about the transition.
    :param reason: The reason for the condition's last transition.
    """
    status: str = attr.ib(metadata={'yaml_name': 'status'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastTransitionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastTransitionTime'})
    lastUpdateTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastUpdateTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class Deployment(K8sResourceBase):
    """
    | Deployment enables declarative updates for Pods and ReplicaSets.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Specification of the desired behavior of the Deployment.
    """
    apiVersion: ClassVar[str] = 'apps/v1'
    kind: ClassVar[str] = 'Deployment'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.apps.v1.DeploymentSpec,
        kdsl.apps.v1.DeploymentSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class DaemonSetUpdateStrategy(K8sObjectBase):
    """
    | DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.
    
    :param rollingUpdate: Rolling update config params. Present only if type = "RollingUpdate".
    :param type: Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.
    """
    rollingUpdate: Optional[Union[kdsl.apps.v1.RollingUpdateDaemonSet,
        kdsl.apps.v1.RollingUpdateDaemonSetTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'rollingUpdate'})
    type: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class DaemonSetStatus(K8sObjectBase):
    """
    | DaemonSetStatus represents the current status of a daemon set.
    
    :param currentNumberScheduled: The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
    :param desiredNumberScheduled: The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
    :param numberMisscheduled: The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
    :param numberReady: The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.
    :param collisionCount: Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.
    :param conditions: Represents the latest available observations of a DaemonSet's current state.
    :param numberAvailable: The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)
    :param numberUnavailable: The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)
    :param observedGeneration: The most recent generation observed by the daemon set controller.
    :param updatedNumberScheduled: The total number of nodes that are running updated daemon pod
    """
    currentNumberScheduled: int = attr.ib(metadata={'yaml_name':
        'currentNumberScheduled'})
    desiredNumberScheduled: int = attr.ib(metadata={'yaml_name':
        'desiredNumberScheduled'})
    numberMisscheduled: int = attr.ib(metadata={'yaml_name':
        'numberMisscheduled'})
    numberReady: int = attr.ib(metadata={'yaml_name': 'numberReady'})
    collisionCount: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'collisionCount'})
    conditions: Optional[Sequence[Union[kdsl.apps.v1.DaemonSetCondition,
        kdsl.apps.v1.DaemonSetConditionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'conditions'})
    numberAvailable: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'numberAvailable'})
    numberUnavailable: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'numberUnavailable'})
    observedGeneration: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'observedGeneration'})
    updatedNumberScheduled: Optional[int] = attr.ib(default=None, metadata=
        {'yaml_name': 'updatedNumberScheduled'})


@attr.s(kw_only=True)
class DaemonSetSpec(K8sObjectBase):
    """
    | DaemonSetSpec is the specification of a daemon set.
    
    :param selector: A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    :param template: An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    :param minReadySeconds: The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).
    :param revisionHistoryLimit: The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.
    :param updateStrategy: An update strategy to replace existing DaemonSet pods with new pods.
    """
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict] = attr.ib(metadata={
        'yaml_name': 'selector'})
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'template'})
    minReadySeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'minReadySeconds'})
    revisionHistoryLimit: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'revisionHistoryLimit'})
    updateStrategy: Optional[Union[kdsl.apps.v1.DaemonSetUpdateStrategy,
        kdsl.apps.v1.DaemonSetUpdateStrategyTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'updateStrategy'})


@attr.s(kw_only=True)
class DaemonSetList(K8sObjectBase):
    """
    | DaemonSetList is a collection of daemon sets.
    
    :param items: A list of daemon sets.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.apps.v1.DaemonSet,
        kdsl.apps.v1.DaemonSetTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class DaemonSetCondition(K8sObjectBase):
    """
    | DaemonSetCondition describes the state of a DaemonSet at a certain point.
    
    :param status: Status of the condition, one of True, False, Unknown.
    :param type: Type of DaemonSet condition.
    :param lastTransitionTime: Last time the condition transitioned from one status to another.
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
class DaemonSet(K8sResourceBase):
    """
    | DaemonSet represents the configuration of a daemon set.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: The desired behavior of this daemon set. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'apps/v1'
    kind: ClassVar[str] = 'DaemonSet'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.apps.v1.DaemonSetSpec,
        kdsl.apps.v1.DaemonSetSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class ControllerRevisionList(K8sObjectBase):
    """
    | ControllerRevisionList is a resource containing a list of ControllerRevision objects.
    
    :param items: Items is the list of ControllerRevisions
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.apps.v1.ControllerRevision,
        kdsl.apps.v1.ControllerRevisionTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ControllerRevision(K8sResourceBase):
    """
    | ControllerRevision implements an immutable snapshot of state data. Clients are responsible for serializing and deserializing the objects that contain their internal state. Once a ControllerRevision has been successfully created, it can not be updated. The API Server will fail validation of all requests that attempt to mutate the Data field. ControllerRevisions may, however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet controllers for update and rollback, this object is beta. However, it may be subject to name and representation changes in future releases, and clients should not depend on its stability. It is primarily for internal use by controllers.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param revision: Revision indicates the revision of the state represented by Data.
    :param annotations: metadata.annotations
    :param data: Data is the serialized representation of the state.
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'apps/v1'
    kind: ClassVar[str] = 'ControllerRevision'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    revision: int = attr.ib(metadata={'yaml_name': 'revision'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    data: Optional[Mapping[str, Any]] = attr.ib(default=None, metadata={
        'yaml_name': 'data'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


class StatefulSetUpdateStrategyTypedDict(TypedDict, total=(False)):
    rollingUpdate: Union[kdsl.apps.v1.RollingUpdateStatefulSetStrategy,
        kdsl.apps.v1.RollingUpdateStatefulSetStrategyTypedDict]
    type: str


class StatefulSetStatusOptionalTypedDict(TypedDict, total=(False)):
    collisionCount: int
    conditions: Sequence[Union[kdsl.apps.v1.StatefulSetCondition,
        kdsl.apps.v1.StatefulSetConditionTypedDict]]
    currentReplicas: int
    currentRevision: str
    observedGeneration: int
    readyReplicas: int
    updateRevision: str
    updatedReplicas: int


class StatefulSetStatusTypedDict(StatefulSetStatusOptionalTypedDict, total=
    (True)):
    replicas: int


class StatefulSetSpecOptionalTypedDict(TypedDict, total=(False)):
    podManagementPolicy: str
    replicas: int
    revisionHistoryLimit: int
    updateStrategy: Union[kdsl.apps.v1.StatefulSetUpdateStrategy,
        kdsl.apps.v1.StatefulSetUpdateStrategyTypedDict]
    volumeClaimTemplates: Sequence[Union[kdsl.core.v1.PersistentVolumeClaim,
        kdsl.core.v1.PersistentVolumeClaimTypedDict]]


class StatefulSetSpecTypedDict(StatefulSetSpecOptionalTypedDict, total=(True)):
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]
    serviceName: str
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]


class StatefulSetListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class StatefulSetListTypedDict(StatefulSetListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.apps.v1.StatefulSet,
        kdsl.apps.v1.StatefulSetTypedDict]]


class StatefulSetConditionOptionalTypedDict(TypedDict, total=(False)):
    lastTransitionTime: str
    message: str
    reason: str


class StatefulSetConditionTypedDict(StatefulSetConditionOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class StatefulSetOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.apps.v1.StatefulSetSpec,
        kdsl.apps.v1.StatefulSetSpecTypedDict]


class StatefulSetTypedDict(StatefulSetOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class RollingUpdateStatefulSetStrategyTypedDict(TypedDict, total=(False)):
    partition: int


class RollingUpdateDeploymentTypedDict(TypedDict, total=(False)):
    maxSurge: Union[int, str]
    maxUnavailable: Union[int, str]


class RollingUpdateDaemonSetTypedDict(TypedDict, total=(False)):
    maxUnavailable: Union[int, str]


class ReplicaSetStatusOptionalTypedDict(TypedDict, total=(False)):
    availableReplicas: int
    conditions: Sequence[Union[kdsl.apps.v1.ReplicaSetCondition,
        kdsl.apps.v1.ReplicaSetConditionTypedDict]]
    fullyLabeledReplicas: int
    observedGeneration: int
    readyReplicas: int


class ReplicaSetStatusTypedDict(ReplicaSetStatusOptionalTypedDict, total=(True)
    ):
    replicas: int


class ReplicaSetSpecOptionalTypedDict(TypedDict, total=(False)):
    minReadySeconds: int
    replicas: int
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]


class ReplicaSetSpecTypedDict(ReplicaSetSpecOptionalTypedDict, total=(True)):
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]


class ReplicaSetListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ReplicaSetListTypedDict(ReplicaSetListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.apps.v1.ReplicaSet,
        kdsl.apps.v1.ReplicaSetTypedDict]]


class ReplicaSetConditionOptionalTypedDict(TypedDict, total=(False)):
    lastTransitionTime: str
    message: str
    reason: str


class ReplicaSetConditionTypedDict(ReplicaSetConditionOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class ReplicaSetOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.apps.v1.ReplicaSetSpec,
        kdsl.apps.v1.ReplicaSetSpecTypedDict]


class ReplicaSetTypedDict(ReplicaSetOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class DeploymentStrategyTypedDict(TypedDict, total=(False)):
    rollingUpdate: Union[kdsl.apps.v1.RollingUpdateDeployment,
        kdsl.apps.v1.RollingUpdateDeploymentTypedDict]
    type: str


class DeploymentStatusTypedDict(TypedDict, total=(False)):
    availableReplicas: int
    collisionCount: int
    conditions: Sequence[Union[kdsl.apps.v1.DeploymentCondition,
        kdsl.apps.v1.DeploymentConditionTypedDict]]
    observedGeneration: int
    readyReplicas: int
    replicas: int
    unavailableReplicas: int
    updatedReplicas: int


class DeploymentSpecOptionalTypedDict(TypedDict, total=(False)):
    minReadySeconds: int
    paused: bool
    progressDeadlineSeconds: int
    replicas: int
    revisionHistoryLimit: int
    strategy: Union[kdsl.apps.v1.DeploymentStrategy,
        kdsl.apps.v1.DeploymentStrategyTypedDict]


class DeploymentSpecTypedDict(DeploymentSpecOptionalTypedDict, total=(True)):
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]


class DeploymentListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class DeploymentListTypedDict(DeploymentListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.apps.v1.Deployment,
        kdsl.apps.v1.DeploymentTypedDict]]


class DeploymentConditionOptionalTypedDict(TypedDict, total=(False)):
    lastTransitionTime: str
    lastUpdateTime: str
    message: str
    reason: str


class DeploymentConditionTypedDict(DeploymentConditionOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class DeploymentOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.apps.v1.DeploymentSpec,
        kdsl.apps.v1.DeploymentSpecTypedDict]


class DeploymentTypedDict(DeploymentOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class DaemonSetUpdateStrategyTypedDict(TypedDict, total=(False)):
    rollingUpdate: Union[kdsl.apps.v1.RollingUpdateDaemonSet,
        kdsl.apps.v1.RollingUpdateDaemonSetTypedDict]
    type: str


class DaemonSetStatusOptionalTypedDict(TypedDict, total=(False)):
    collisionCount: int
    conditions: Sequence[Union[kdsl.apps.v1.DaemonSetCondition,
        kdsl.apps.v1.DaemonSetConditionTypedDict]]
    numberAvailable: int
    numberUnavailable: int
    observedGeneration: int
    updatedNumberScheduled: int


class DaemonSetStatusTypedDict(DaemonSetStatusOptionalTypedDict, total=(True)):
    currentNumberScheduled: int
    desiredNumberScheduled: int
    numberMisscheduled: int
    numberReady: int


class DaemonSetSpecOptionalTypedDict(TypedDict, total=(False)):
    minReadySeconds: int
    revisionHistoryLimit: int
    updateStrategy: Union[kdsl.apps.v1.DaemonSetUpdateStrategy,
        kdsl.apps.v1.DaemonSetUpdateStrategyTypedDict]


class DaemonSetSpecTypedDict(DaemonSetSpecOptionalTypedDict, total=(True)):
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]


class DaemonSetListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class DaemonSetListTypedDict(DaemonSetListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.apps.v1.DaemonSet,
        kdsl.apps.v1.DaemonSetTypedDict]]


class DaemonSetConditionOptionalTypedDict(TypedDict, total=(False)):
    lastTransitionTime: str
    message: str
    reason: str


class DaemonSetConditionTypedDict(DaemonSetConditionOptionalTypedDict,
    total=(True)):
    status: str
    type: str


class DaemonSetOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.apps.v1.DaemonSetSpec, kdsl.apps.v1.DaemonSetSpecTypedDict
        ]


class DaemonSetTypedDict(DaemonSetOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class ControllerRevisionListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ControllerRevisionListTypedDict(ControllerRevisionListOptionalTypedDict,
    total=(True)):
    items: Sequence[Union[kdsl.apps.v1.ControllerRevision,
        kdsl.apps.v1.ControllerRevisionTypedDict]]


class ControllerRevisionOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    data: Mapping[str, Any]
    labels: Mapping[str, str]


class ControllerRevisionTypedDict(ControllerRevisionOptionalTypedDict,
    total=(True)):
    name: str
    namespace: str
    revision: int
