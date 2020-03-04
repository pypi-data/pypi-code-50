from __future__ import annotations
import kdsl.meta.v1
import attr
import kdsl.core.v1
import kdsl.batch.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class JobStatus(K8sObjectBase):
    """
    | JobStatus represents the current state of a Job.
    
    :param active: The number of actively running pods.
    :param completionTime: Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.
    :param conditions: The latest available observations of an object's current state. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/
    :param failed: The number of pods which reached phase Failed.
    :param startTime: Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.
    :param succeeded: The number of pods which reached phase Succeeded.
    """
    active: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'active'})
    completionTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'completionTime'})
    conditions: Optional[Sequence[Union[kdsl.batch.v1.JobCondition,
        kdsl.batch.v1.JobConditionTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'conditions'})
    failed: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'failed'})
    startTime: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'startTime'})
    succeeded: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'succeeded'})


@attr.s(kw_only=True)
class JobSpec(K8sObjectBase):
    """
    | JobSpec describes how the job execution will look like.
    
    :param template: Describes the pod that will be created when executing a job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/
    :param activeDeadlineSeconds: Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer
    :param backoffLimit: Specifies the number of retries before marking this job failed. Defaults to 6
    :param completions: Specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/
    :param manualSelector: manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector
    :param parallelism: Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/
    :param selector: A label query over pods that should match the pod count. Normally, the system sets this field for you. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    :param ttlSecondsAfterFinished: ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the TTLAfterFinished feature.
    """
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'template'})
    activeDeadlineSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'activeDeadlineSeconds'})
    backoffLimit: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'backoffLimit'})
    completions: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'completions'})
    manualSelector: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'manualSelector'})
    parallelism: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'parallelism'})
    selector: Optional[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'selector'})
    ttlSecondsAfterFinished: Optional[int] = attr.ib(default=None, metadata
        ={'yaml_name': 'ttlSecondsAfterFinished'})


@attr.s(kw_only=True)
class JobList(K8sObjectBase):
    """
    | JobList is a collection of jobs.
    
    :param items: items is the list of Jobs.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.batch.v1.Job, kdsl.batch.v1.JobTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class JobCondition(K8sObjectBase):
    """
    | JobCondition describes current state of a job.
    
    :param status: Status of the condition, one of True, False, Unknown.
    :param type: Type of job condition, Complete or Failed.
    :param lastProbeTime: Last time the condition was checked.
    :param lastTransitionTime: Last time the condition transit from one status to another.
    :param message: Human readable message indicating details about last transition.
    :param reason: (brief) reason for the condition's last transition.
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
class Job(K8sResourceBase):
    """
    | Job represents the configuration of a single job.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Specification of the desired behavior of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'batch/v1'
    kind: ClassVar[str] = 'Job'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.batch.v1.JobSpec, kdsl.batch.v1.JobSpecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


class JobStatusTypedDict(TypedDict, total=(False)):
    active: int
    completionTime: str
    conditions: Sequence[Union[kdsl.batch.v1.JobCondition,
        kdsl.batch.v1.JobConditionTypedDict]]
    failed: int
    startTime: str
    succeeded: int


class JobSpecOptionalTypedDict(TypedDict, total=(False)):
    activeDeadlineSeconds: int
    backoffLimit: int
    completions: int
    manualSelector: bool
    parallelism: int
    selector: Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]
    ttlSecondsAfterFinished: int


class JobSpecTypedDict(JobSpecOptionalTypedDict, total=(True)):
    template: Union[kdsl.core.v1.PodTemplateSpec,
        kdsl.core.v1.PodTemplateSpecTypedDict]


class JobListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class JobListTypedDict(JobListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.batch.v1.Job, kdsl.batch.v1.JobTypedDict]]


class JobConditionOptionalTypedDict(TypedDict, total=(False)):
    lastProbeTime: str
    lastTransitionTime: str
    message: str
    reason: str


class JobConditionTypedDict(JobConditionOptionalTypedDict, total=(True)):
    status: str
    type: str


class JobOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.batch.v1.JobSpec, kdsl.batch.v1.JobSpecTypedDict]


class JobTypedDict(JobOptionalTypedDict, total=(True)):
    name: str
    namespace: str
