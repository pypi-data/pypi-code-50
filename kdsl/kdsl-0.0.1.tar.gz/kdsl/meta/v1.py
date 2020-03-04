from __future__ import annotations
import attr
import kdsl.meta.v1
from kdsl.bases import K8sObjectBase
from typing import ClassVar, Any, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class WatchEvent(K8sObjectBase):
    """
    | Event represents a single event to a watched resource.
    
    :param object: Object is:
     * If Type is Added or Modified: the new state of the object.
     * If Type is Deleted: the state of the object immediately before deletion.
     * If Type is Error: *Status is recommended; other types may make sense
       depending on context.
    :param type: None
    """
    object: Mapping[str, Any] = attr.ib(metadata={'yaml_name': 'object'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})


@attr.s(kw_only=True)
class StatusDetails(K8sObjectBase):
    """
    | StatusDetails is a set of additional properties that MAY be set by the server to provide additional information about a response. The Reason field of a Status object defines what attributes will be set. Clients must ignore fields that do not match the defined type of each attribute, and should assume that any attribute may be empty, invalid, or under defined.
    
    :param causes: The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.
    :param group: The group attribute of the resource associated with the status StatusReason.
    :param kind: The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param name: The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).
    :param retryAfterSeconds: If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.
    :param uid: UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids
    """
    causes: Optional[Sequence[Union[kdsl.meta.v1.StatusCause,
        kdsl.meta.v1.StatusCauseTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'causes'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    retryAfterSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'retryAfterSeconds'})
    uid: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'uid'})


@attr.s(kw_only=True)
class StatusCause(K8sObjectBase):
    """
    | StatusCause provides more information about an api.Status failure, including cases when multiple errors are encountered.
    
    :param field: The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.
    
    Examples:
      "name" - the field "name" on the current resource
      "items[0].name" - the field "name" on the first array entry in "items"
    :param message: A human-readable description of the cause of the error.  This field may be presented as-is to a reader.
    :param reason: A machine-readable description of the cause of the error. If this value is empty there is no information available.
    """
    field: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'field'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class Status(K8sObjectBase):
    """
    | Status is a return value for calls that don't return other objects.
    
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param code: Suggested HTTP return code for this status, 0 if not set.
    :param details: Extended data associated with the reason.  Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type.
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param message: A human-readable description of the status of this operation.
    :param metadata: Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param reason: A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it.
    :param status: Status of the operation. One of: "Success" or "Failure". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    code: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'code'})
    details: Optional[Union[kdsl.meta.v1.StatusDetails,
        kdsl.meta.v1.StatusDetailsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'details'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})
    status: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'status'})


@attr.s(kw_only=True)
class ServerAddressByClientCIDR(K8sObjectBase):
    """
    | ServerAddressByClientCIDR helps the client to determine the server address that they should use, depending on the clientCIDR that they match.
    
    :param clientCIDR: The CIDR with which clients can match their IP to figure out the server address that they should use.
    :param serverAddress: Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port.
    """
    clientCIDR: str = attr.ib(metadata={'yaml_name': 'clientCIDR'})
    serverAddress: str = attr.ib(metadata={'yaml_name': 'serverAddress'})


@attr.s(kw_only=True)
class Preconditions(K8sObjectBase):
    """
    | Preconditions must be fulfilled before an operation (update, delete, etc.) is carried out.
    
    :param resourceVersion: Specifies the target ResourceVersion
    :param uid: Specifies the target UID.
    """
    resourceVersion: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'resourceVersion'})
    uid: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'uid'})


@attr.s(kw_only=True)
class OwnerReference(K8sObjectBase):
    """
    | OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.
    
    :param apiVersion: API version of the referent.
    :param kind: Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names
    :param uid: UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids
    :param blockOwnerDeletion: If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.
    :param controller: If true, this reference points to the managing controller.
    """
    apiVersion: str = attr.ib(metadata={'yaml_name': 'apiVersion'})
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    uid: str = attr.ib(metadata={'yaml_name': 'uid'})
    blockOwnerDeletion: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'blockOwnerDeletion'})
    controller: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'controller'})


@attr.s(kw_only=True)
class ObjectMeta(K8sObjectBase):
    """
    | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.
    
    :param annotations: Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations
    :param clusterName: The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.
    :param creationTimestamp: CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.
    
    Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    :param deletionGracePeriodSeconds: Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.
    :param deletionTimestamp: DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.
    
    Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    :param finalizers: Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.
    :param generateName: GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.
    
    If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).
    
    Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency
    :param generation: A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.
    :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels
    :param managedFields: ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.
    :param name: Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names
    :param namespace: Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.
    
    Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces
    :param ownerReferences: List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.
    :param resourceVersion: An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.
    
    Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    :param selfLink: SelfLink is a URL representing this object. Populated by the system. Read-only.
    
    DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.
    :param uid: UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.
    
    Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids
    """
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'annotations'})
    clusterName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'clusterName'})
    creationTimestamp: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'creationTimestamp'})
    deletionGracePeriodSeconds: Optional[int] = attr.ib(default=None,
        metadata={'yaml_name': 'deletionGracePeriodSeconds'})
    deletionTimestamp: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'deletionTimestamp'})
    finalizers: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'finalizers'})
    generateName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'generateName'})
    generation: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'generation'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'labels'})
    managedFields: Optional[Sequence[Union[kdsl.meta.v1.ManagedFieldsEntry,
        kdsl.meta.v1.ManagedFieldsEntryTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'managedFields'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    namespace: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'namespace'})
    ownerReferences: Optional[Sequence[Union[kdsl.meta.v1.OwnerReference,
        kdsl.meta.v1.OwnerReferenceTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'ownerReferences'})
    resourceVersion: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'resourceVersion'})
    selfLink: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'selfLink'})
    uid: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'uid'})


@attr.s(kw_only=True)
class ManagedFieldsEntry(K8sObjectBase):
    """
    | ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to.
    
    :param apiVersion: APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.
    :param fieldsType: FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"
    :param fieldsV1: FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.
    :param manager: Manager is an identifier of the workflow managing these fields.
    :param operation: Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.
    :param time: Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    fieldsType: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'fieldsType'})
    fieldsV1: Optional[Mapping[str, Any]] = attr.ib(default=None, metadata=
        {'yaml_name': 'fieldsV1'})
    manager: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'manager'})
    operation: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'operation'})
    time: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'time'})


@attr.s(kw_only=True)
class ListMeta(K8sObjectBase):
    """
    | ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}.
    
    :param continue_: continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.
    :param remainingItemCount: remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.
    :param resourceVersion: String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    :param selfLink: selfLink is a URL representing this object. Populated by the system. Read-only.
    
    DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.
    """
    continue_: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'continue'})
    remainingItemCount: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'remainingItemCount'})
    resourceVersion: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'resourceVersion'})
    selfLink: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'selfLink'})


@attr.s(kw_only=True)
class LabelSelectorRequirement(K8sObjectBase):
    """
    | A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: key is the label key that the selector applies to.
    :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class LabelSelector(K8sObjectBase):
    """
    | A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.meta.v1.LabelSelectorRequirement,
        kdsl.meta.v1.LabelSelectorRequirementTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class GroupVersionForDiscovery(K8sObjectBase):
    """
    | GroupVersion contains the "group/version" and "version" string of a version. It is made a struct to keep extensibility.
    
    :param groupVersion: groupVersion specifies the API group and version in the form "group/version"
    :param version: version specifies the version in the form of "version". This is to save the clients the trouble of splitting the GroupVersion.
    """
    groupVersion: str = attr.ib(metadata={'yaml_name': 'groupVersion'})
    version: str = attr.ib(metadata={'yaml_name': 'version'})


@attr.s(kw_only=True)
class DeleteOptions(K8sObjectBase):
    """
    | DeleteOptions may be provided when deleting an API object.
    
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :param gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the "orphan" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.
    :param preconditions: Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned.
    :param propagationPolicy: Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground.
    """
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    dryRun: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'dryRun'})
    gracePeriodSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'gracePeriodSeconds'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    orphanDependents: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'orphanDependents'})
    preconditions: Optional[Union[kdsl.meta.v1.Preconditions,
        kdsl.meta.v1.PreconditionsTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'preconditions'})
    propagationPolicy: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'propagationPolicy'})


@attr.s(kw_only=True)
class APIVersions(K8sObjectBase):
    """
    | APIVersions lists the versions that are available, to allow clients to discover the API at /api, which is the root path of the legacy v1 API.
    
    :param serverAddressByClientCIDRs: a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.
    :param versions: versions are the api versions that are available.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    serverAddressByClientCIDRs: Sequence[Union[
        kdsl.meta.v1.ServerAddressByClientCIDR,
        kdsl.meta.v1.ServerAddressByClientCIDRTypedDict]] = attr.ib(metadata
        ={'yaml_name': 'serverAddressByClientCIDRs'})
    versions: Sequence[str] = attr.ib(metadata={'yaml_name': 'versions'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})


@attr.s(kw_only=True)
class APIResourceList(K8sObjectBase):
    """
    | APIResourceList is a list of APIResource, it is used to expose the name of the resources supported in a specific group and version, and if the resource is namespaced.
    
    :param groupVersion: groupVersion is the group and version this APIResourceList is for.
    :param resources: resources contains the name of the resources and if they are namespaced.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    groupVersion: str = attr.ib(metadata={'yaml_name': 'groupVersion'})
    resources: Sequence[Union[kdsl.meta.v1.APIResource,
        kdsl.meta.v1.APIResourceTypedDict]] = attr.ib(metadata={'yaml_name':
        'resources'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})


@attr.s(kw_only=True)
class APIResource(K8sObjectBase):
    """
    | APIResource specifies the name of a resource and whether it is namespaced.
    
    :param kind: kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')
    :param name: name is the plural name of the resource.
    :param namespaced: namespaced indicates if a resource is namespaced or not.
    :param singularName: singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.
    :param verbs: verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)
    :param categories: categories is a list of the grouped resources this resource belongs to (e.g. 'all')
    :param group: group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale".
    :param shortNames: shortNames is a list of suggested short names of the resource.
    :param storageVersionHash: The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates.
    :param version: version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)".
    """
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    namespaced: bool = attr.ib(metadata={'yaml_name': 'namespaced'})
    singularName: str = attr.ib(metadata={'yaml_name': 'singularName'})
    verbs: Sequence[str] = attr.ib(metadata={'yaml_name': 'verbs'})
    categories: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'categories'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    shortNames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'shortNames'})
    storageVersionHash: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'storageVersionHash'})
    version: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'version'})


@attr.s(kw_only=True)
class APIGroupList(K8sObjectBase):
    """
    | APIGroupList is a list of APIGroup, to allow clients to discover the API at /apis.
    
    :param groups: groups is a list of APIGroup.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    groups: Sequence[Union[kdsl.meta.v1.APIGroup,
        kdsl.meta.v1.APIGroupTypedDict]] = attr.ib(metadata={'yaml_name':
        'groups'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})


@attr.s(kw_only=True)
class APIGroup(K8sObjectBase):
    """
    | APIGroup contains the name, the supported versions, and the preferred version of a group.
    
    :param name: name is the name of the group.
    :param versions: versions are the versions supported in this group.
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param preferredVersion: preferredVersion is the version preferred by the API server, which probably is the storage version.
    :param serverAddressByClientCIDRs: a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    versions: Sequence[Union[kdsl.meta.v1.GroupVersionForDiscovery,
        kdsl.meta.v1.GroupVersionForDiscoveryTypedDict]] = attr.ib(metadata
        ={'yaml_name': 'versions'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    preferredVersion: Optional[Union[kdsl.meta.v1.GroupVersionForDiscovery,
        kdsl.meta.v1.GroupVersionForDiscoveryTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'preferredVersion'})
    serverAddressByClientCIDRs: Optional[Sequence[Union[
        kdsl.meta.v1.ServerAddressByClientCIDR,
        kdsl.meta.v1.ServerAddressByClientCIDRTypedDict]]] = attr.ib(default
        =None, metadata={'yaml_name': 'serverAddressByClientCIDRs'})


class WatchEventTypedDict(TypedDict, total=(True)):
    object: Mapping[str, Any]
    type: str


class StatusDetailsTypedDict(TypedDict, total=(False)):
    causes: Sequence[Union[kdsl.meta.v1.StatusCause,
        kdsl.meta.v1.StatusCauseTypedDict]]
    group: str
    kind: str
    name: str
    retryAfterSeconds: int
    uid: str


class StatusCauseTypedDict(TypedDict, total=(False)):
    field: str
    message: str
    reason: str


class StatusTypedDict(TypedDict, total=(False)):
    apiVersion: str
    code: int
    details: Union[kdsl.meta.v1.StatusDetails,
        kdsl.meta.v1.StatusDetailsTypedDict]
    kind: str
    message: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]
    reason: str
    status: str


class ServerAddressByClientCIDRTypedDict(TypedDict, total=(True)):
    clientCIDR: str
    serverAddress: str


class PreconditionsTypedDict(TypedDict, total=(False)):
    resourceVersion: str
    uid: str


class OwnerReferenceOptionalTypedDict(TypedDict, total=(False)):
    blockOwnerDeletion: bool
    controller: bool


class OwnerReferenceTypedDict(OwnerReferenceOptionalTypedDict, total=(True)):
    apiVersion: str
    kind: str
    name: str
    uid: str


class ObjectMetaTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    clusterName: str
    creationTimestamp: str
    deletionGracePeriodSeconds: int
    deletionTimestamp: str
    finalizers: Sequence[str]
    generateName: str
    generation: int
    labels: Mapping[str, str]
    managedFields: Sequence[Union[kdsl.meta.v1.ManagedFieldsEntry,
        kdsl.meta.v1.ManagedFieldsEntryTypedDict]]
    name: str
    namespace: str
    ownerReferences: Sequence[Union[kdsl.meta.v1.OwnerReference,
        kdsl.meta.v1.OwnerReferenceTypedDict]]
    resourceVersion: str
    selfLink: str
    uid: str


class ManagedFieldsEntryTypedDict(TypedDict, total=(False)):
    apiVersion: str
    fieldsType: str
    fieldsV1: Mapping[str, Any]
    manager: str
    operation: str
    time: str


class ListMetaTypedDict(TypedDict, total=(False)):
    continue_: str
    remainingItemCount: int
    resourceVersion: str
    selfLink: str


class LabelSelectorRequirementOptionalTypedDict(TypedDict, total=(False)):
    values: Sequence[str]


class LabelSelectorRequirementTypedDict(
    LabelSelectorRequirementOptionalTypedDict, total=(True)):
    key: str
    operator: str


class LabelSelectorTypedDict(TypedDict, total=(False)):
    matchExpressions: Sequence[Union[kdsl.meta.v1.LabelSelectorRequirement,
        kdsl.meta.v1.LabelSelectorRequirementTypedDict]]
    matchLabels: Mapping[str, str]


class GroupVersionForDiscoveryTypedDict(TypedDict, total=(True)):
    groupVersion: str
    version: str


class DeleteOptionsTypedDict(TypedDict, total=(False)):
    apiVersion: str
    dryRun: Sequence[str]
    gracePeriodSeconds: int
    kind: str
    orphanDependents: bool
    preconditions: Union[kdsl.meta.v1.Preconditions,
        kdsl.meta.v1.PreconditionsTypedDict]
    propagationPolicy: str


class APIVersionsOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str


class APIVersionsTypedDict(APIVersionsOptionalTypedDict, total=(True)):
    serverAddressByClientCIDRs: Sequence[Union[
        kdsl.meta.v1.ServerAddressByClientCIDR,
        kdsl.meta.v1.ServerAddressByClientCIDRTypedDict]]
    versions: Sequence[str]


class APIResourceListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str


class APIResourceListTypedDict(APIResourceListOptionalTypedDict, total=(True)):
    groupVersion: str
    resources: Sequence[Union[kdsl.meta.v1.APIResource,
        kdsl.meta.v1.APIResourceTypedDict]]


class APIResourceOptionalTypedDict(TypedDict, total=(False)):
    categories: Sequence[str]
    group: str
    shortNames: Sequence[str]
    storageVersionHash: str
    version: str


class APIResourceTypedDict(APIResourceOptionalTypedDict, total=(True)):
    kind: str
    name: str
    namespaced: bool
    singularName: str
    verbs: Sequence[str]


class APIGroupListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str


class APIGroupListTypedDict(APIGroupListOptionalTypedDict, total=(True)):
    groups: Sequence[Union[kdsl.meta.v1.APIGroup,
        kdsl.meta.v1.APIGroupTypedDict]]


class APIGroupOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    preferredVersion: Union[kdsl.meta.v1.GroupVersionForDiscovery,
        kdsl.meta.v1.GroupVersionForDiscoveryTypedDict]
    serverAddressByClientCIDRs: Sequence[Union[
        kdsl.meta.v1.ServerAddressByClientCIDR,
        kdsl.meta.v1.ServerAddressByClientCIDRTypedDict]]


class APIGroupTypedDict(APIGroupOptionalTypedDict, total=(True)):
    name: str
    versions: Sequence[Union[kdsl.meta.v1.GroupVersionForDiscovery,
        kdsl.meta.v1.GroupVersionForDiscoveryTypedDict]]
