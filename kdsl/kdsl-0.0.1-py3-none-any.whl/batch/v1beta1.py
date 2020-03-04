from __future__ import annotations
import kdsl.batch.v1beta1
import kdsl.meta.v1
import attr
import kdsl.core.v1
import kdsl.batch.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class JobTemplateSpec(K8sObjectBase):
    """
    | JobTemplateSpec describes the data a Job should have when created from a template
    
    :param metadata: Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    :param spec: Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    metadata: Optional[Union[kdsl.meta.v1.ObjectMeta,
        kdsl.meta.v1.ObjectMetaTypedDict]] = attr.ib(default=None, metadata
        ={'yaml_name': 'metadata'})
    spec: Optional[Union[kdsl.batch.v1.JobSpec, kdsl.batch.v1.JobSpecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class CronJobStatus(K8sObjectBase):
    """
    | CronJobStatus represents the current state of a cron job.
    
    :param active: A list of pointers to currently running jobs.
    :param lastScheduleTime: Information when was the last time the job was successfully scheduled.
    """
    active: Optional[Sequence[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'active'})
    lastScheduleTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastScheduleTime'})


@attr.s(kw_only=True)
class CronJobSpec(K8sObjectBase):
    """
    | CronJobSpec describes how the job execution will look like and when it will actually run.
    
    :param jobTemplate: Specifies the job that will be created when executing a CronJob.
    :param schedule: The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.
    :param concurrencyPolicy: Specifies how to treat concurrent executions of a Job. Valid values are: - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - "Replace": cancels currently running job and replaces it with a new one
    :param failedJobsHistoryLimit: The number of failed finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.
    :param startingDeadlineSeconds: Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.
    :param successfulJobsHistoryLimit: The number of successful finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified. Defaults to 3.
    :param suspend: This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.
    """
    jobTemplate: Union[kdsl.batch.v1beta1.JobTemplateSpec,
        kdsl.batch.v1beta1.JobTemplateSpecTypedDict] = attr.ib(metadata={
        'yaml_name': 'jobTemplate'})
    schedule: str = attr.ib(metadata={'yaml_name': 'schedule'})
    concurrencyPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'concurrencyPolicy'})
    failedJobsHistoryLimit: Optional[int] = attr.ib(default=None, metadata=
        {'yaml_name': 'failedJobsHistoryLimit'})
    startingDeadlineSeconds: Optional[int] = attr.ib(default=None, metadata
        ={'yaml_name': 'startingDeadlineSeconds'})
    successfulJobsHistoryLimit: Optional[int] = attr.ib(default=None,
        metadata={'yaml_name': 'successfulJobsHistoryLimit'})
    suspend: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'suspend'})


@attr.s(kw_only=True)
class CronJobList(K8sObjectBase):
    """
    | CronJobList is a collection of cron jobs.
    
    :param items: items is the list of CronJobs.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: Sequence[Union[kdsl.batch.v1beta1.CronJob,
        kdsl.batch.v1beta1.CronJobTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class CronJob(K8sResourceBase):
    """
    | CronJob represents the configuration of a single cron job.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: ClassVar[str] = 'batch/v1beta1'
    kind: ClassVar[str] = 'CronJob'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.batch.v1beta1.CronJobSpec,
        kdsl.batch.v1beta1.CronJobSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


class JobTemplateSpecTypedDict(TypedDict, total=(False)):
    metadata: Union[kdsl.meta.v1.ObjectMeta, kdsl.meta.v1.ObjectMetaTypedDict]
    spec: Union[kdsl.batch.v1.JobSpec, kdsl.batch.v1.JobSpecTypedDict]


class CronJobStatusTypedDict(TypedDict, total=(False)):
    active: Sequence[Union[kdsl.core.v1.ObjectReference,
        kdsl.core.v1.ObjectReferenceTypedDict]]
    lastScheduleTime: str


class CronJobSpecOptionalTypedDict(TypedDict, total=(False)):
    concurrencyPolicy: str
    failedJobsHistoryLimit: int
    startingDeadlineSeconds: int
    successfulJobsHistoryLimit: int
    suspend: bool


class CronJobSpecTypedDict(CronJobSpecOptionalTypedDict, total=(True)):
    jobTemplate: Union[kdsl.batch.v1beta1.JobTemplateSpec,
        kdsl.batch.v1beta1.JobTemplateSpecTypedDict]
    schedule: str


class CronJobListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class CronJobListTypedDict(CronJobListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.batch.v1beta1.CronJob,
        kdsl.batch.v1beta1.CronJobTypedDict]]


class CronJobOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.batch.v1beta1.CronJobSpec,
        kdsl.batch.v1beta1.CronJobSpecTypedDict]


class CronJobTypedDict(CronJobOptionalTypedDict, total=(True)):
    name: str
    namespace: str
