from __future__ import annotations
import attr
import kdsl.meta.v1
import kdsl.apiextensions.v1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import Any, ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class WebhookConversion(K8sObjectBase):
    """
    | WebhookConversion describes how to call a conversion webhook
    
    :param conversionReviewVersions: conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail.
    :param clientConfig: clientConfig is the instructions for how to call the webhook if strategy is `Webhook`.
    """
    conversionReviewVersions: Sequence[str] = attr.ib(metadata={'yaml_name':
        'conversionReviewVersions'})
    clientConfig: Optional[Union[kdsl.apiextensions.v1.WebhookClientConfig,
        kdsl.apiextensions.v1.WebhookClientConfigTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'clientConfig'})


@attr.s(kw_only=True)
class WebhookClientConfig(K8sObjectBase):
    """
    | WebhookClientConfig contains the information to make a TLS connection with the webhook.
    
    :param caBundle: caBundle is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used.
    :param service: service is a reference to the service for this webhook. Either service or url must be specified.
    
    If the webhook is running within the cluster, then you should use `service`.
    :param url: url gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.
    
    The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.
    
    Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.
    
    The scheme must be "https"; the URL must begin with "https://".
    
    A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.
    
    Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either.
    """
    caBundle: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caBundle'})
    service: Optional[Union[kdsl.apiextensions.v1.ServiceReference,
        kdsl.apiextensions.v1.ServiceReferenceTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'service'})
    url: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'url'})


@attr.s(kw_only=True)
class ServiceReference(K8sObjectBase):
    """
    | ServiceReference holds a reference to Service.legacy.k8s.io
    
    :param name: name is the name of the service. Required
    :param namespace: namespace is the namespace of the service. Required
    :param path: path is an optional URL path at which the webhook will be contacted.
    :param port: port is an optional service port at which the webhook will be contacted. `port` should be a valid port number (1-65535, inclusive). Defaults to 443 for backward compatibility.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    namespace: str = attr.ib(metadata={'yaml_name': 'namespace'})
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    port: Optional[int] = attr.ib(default=None, metadata={'yaml_name': 'port'})


@attr.s(kw_only=True)
class ExternalDocumentation(K8sObjectBase):
    """
    | ExternalDocumentation allows referencing an external resource for extended documentation.
    
    :param description: None
    :param url: None
    """
    description: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'description'})
    url: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'url'})


@attr.s(kw_only=True)
class CustomResourceValidation(K8sObjectBase):
    """
    | CustomResourceValidation is a list of validation methods for CustomResources.
    
    :param openAPIV3Schema: openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning.
    """
    openAPIV3Schema: Optional[Any] = attr.ib(default=None, metadata={
        'yaml_name': 'openAPIV3Schema'})


@attr.s(kw_only=True)
class CustomResourceSubresources(K8sObjectBase):
    """
    | CustomResourceSubresources defines the status and scale subresources for CustomResources.
    
    :param scale: scale indicates the custom resource should serve a `/scale` subresource that returns an `autoscaling/v1` Scale object.
    :param status: status indicates the custom resource should serve a `/status` subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the `status` stanza of the object. 2. requests to the custom resource `/status` subresource ignore changes to anything other than the `status` stanza of the object.
    """
    scale: Optional[Union[
        kdsl.apiextensions.v1.CustomResourceSubresourceScale,
        kdsl.apiextensions.v1.CustomResourceSubresourceScaleTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'scale'})
    status: Optional[Mapping[str, Any]] = attr.ib(default=None, metadata={
        'yaml_name': 'status'})


@attr.s(kw_only=True)
class CustomResourceSubresourceScale(K8sObjectBase):
    """
    | CustomResourceSubresourceScale defines how to serve the scale subresource for CustomResources.
    
    :param specReplicasPath: specReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `spec.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.spec`. If there is no value under the given path in the custom resource, the `/scale` subresource will return an error on GET.
    :param statusReplicasPath: statusReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `status.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status`. If there is no value under the given path in the custom resource, the `status.replicas` value in the `/scale` subresource will default to 0.
    :param labelSelectorPath: labelSelectorPath defines the JSON path inside of a custom resource that corresponds to Scale `status.selector`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status` or `.spec`. Must be set to work with HorizontalPodAutoscaler. The field pointed by this JSON path must be a string field (not a complex selector struct) which contains a serialized label selector in string form. More info: https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions#scale-subresource If there is no value under the given path in the custom resource, the `status.selector` value in the `/scale` subresource will default to the empty string.
    """
    specReplicasPath: str = attr.ib(metadata={'yaml_name': 'specReplicasPath'})
    statusReplicasPath: str = attr.ib(metadata={'yaml_name':
        'statusReplicasPath'})
    labelSelectorPath: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'labelSelectorPath'})


@attr.s(kw_only=True)
class CustomResourceDefinitionVersion(K8sObjectBase):
    """
    | CustomResourceDefinitionVersion describes a version for CRD.
    
    :param name: name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true.
    :param served: served is a flag enabling/disabling this version from being served via REST APIs
    :param storage: storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true.
    :param additionalPrinterColumns: additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used.
    :param schema: schema describes the schema used for validation, pruning, and defaulting of this version of the custom resource.
    :param subresources: subresources specify what subresources this version of the defined custom resource have.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    served: bool = attr.ib(metadata={'yaml_name': 'served'})
    storage: bool = attr.ib(metadata={'yaml_name': 'storage'})
    additionalPrinterColumns: Optional[Sequence[Union[
        kdsl.apiextensions.v1.CustomResourceColumnDefinition,
        kdsl.apiextensions.v1.CustomResourceColumnDefinitionTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'additionalPrinterColumns'})
    schema: Optional[Union[kdsl.apiextensions.v1.CustomResourceValidation,
        kdsl.apiextensions.v1.CustomResourceValidationTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'schema'})
    subresources: Optional[Union[
        kdsl.apiextensions.v1.CustomResourceSubresources,
        kdsl.apiextensions.v1.CustomResourceSubresourcesTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'subresources'})


@attr.s(kw_only=True)
class CustomResourceDefinitionStatus(K8sObjectBase):
    """
    | CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition
    
    :param acceptedNames: acceptedNames are the names that are actually being used to serve discovery. They may be different than the names in spec.
    :param storedVersions: storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list.
    :param conditions: conditions indicate state for particular aspects of a CustomResourceDefinition
    """
    acceptedNames: Union[
        kdsl.apiextensions.v1.CustomResourceDefinitionNames,
        kdsl.apiextensions.v1.CustomResourceDefinitionNamesTypedDict
        ] = attr.ib(metadata={'yaml_name': 'acceptedNames'})
    storedVersions: Sequence[str] = attr.ib(metadata={'yaml_name':
        'storedVersions'})
    conditions: Optional[Sequence[Union[
        kdsl.apiextensions.v1.CustomResourceDefinitionCondition,
        kdsl.apiextensions.v1.CustomResourceDefinitionConditionTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'conditions'})


@attr.s(kw_only=True)
class CustomResourceDefinitionSpec(K8sObjectBase):
    """
    | CustomResourceDefinitionSpec describes how a user wants their resource to appear
    
    :param group: group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`).
    :param names: names specify the resource and kind names for the custom resource.
    :param scope: scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`.
    :param versions: versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.
    :param conversion: conversion defines conversion settings for the CRD.
    :param preserveUnknownFields: preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. This field is deprecated in favor of setting `x-preserve-unknown-fields` to true in `spec.versions[*].schema.openAPIV3Schema`. See https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#pruning-versus-preserving-unknown-fields for details.
    """
    group: str = attr.ib(metadata={'yaml_name': 'group'})
    names: Union[kdsl.apiextensions.v1.CustomResourceDefinitionNames,
        kdsl.apiextensions.v1.CustomResourceDefinitionNamesTypedDict
        ] = attr.ib(metadata={'yaml_name': 'names'})
    scope: str = attr.ib(metadata={'yaml_name': 'scope'})
    versions: Sequence[Union[
        kdsl.apiextensions.v1.CustomResourceDefinitionVersion,
        kdsl.apiextensions.v1.CustomResourceDefinitionVersionTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'versions'})
    conversion: Optional[Union[
        kdsl.apiextensions.v1.CustomResourceConversion,
        kdsl.apiextensions.v1.CustomResourceConversionTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'conversion'})
    preserveUnknownFields: Optional[bool] = attr.ib(default=None, metadata=
        {'yaml_name': 'preserveUnknownFields'})


@attr.s(kw_only=True)
class CustomResourceDefinitionNames(K8sObjectBase):
    """
    | CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition
    
    :param kind: kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls.
    :param plural: plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase.
    :param categories: categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`.
    :param listKind: listKind is the serialized kind of the list for this resource. Defaults to "`kind`List".
    :param shortNames: shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.
    :param singular: singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`.
    """
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    plural: str = attr.ib(metadata={'yaml_name': 'plural'})
    categories: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'categories'})
    listKind: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'listKind'})
    shortNames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'shortNames'})
    singular: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'singular'})


@attr.s(kw_only=True)
class CustomResourceDefinitionList(K8sObjectBase):
    """
    | CustomResourceDefinitionList is a list of CustomResourceDefinition objects.
    
    :param items: items list individual CustomResourceDefinition objects
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: None
    """
    items: Sequence[Union[kdsl.apiextensions.v1.CustomResourceDefinition,
        kdsl.apiextensions.v1.CustomResourceDefinitionTypedDict]] = attr.ib(
        metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class CustomResourceDefinitionCondition(K8sObjectBase):
    """
    | CustomResourceDefinitionCondition contains details for the current condition of this pod.
    
    :param status: status is the status of the condition. Can be True, False, Unknown.
    :param type: type is the type of the condition. Types include Established, NamesAccepted and Terminating.
    :param lastTransitionTime: lastTransitionTime last time the condition transitioned from one status to another.
    :param message: message is a human-readable message indicating details about last transition.
    :param reason: reason is a unique, one-word, CamelCase reason for the condition's last transition.
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
class CustomResourceDefinition(K8sResourceBase):
    """
    | CustomResourceDefinition represents a resource that should be exposed on the API server.  Its name MUST be in the format <.spec.name>.<.spec.group>.
    
    :param name: metadata.name
    :param spec: spec describes how the user wants the resources to appear
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'apiextensions.k8s.io/v1'
    kind: ClassVar[str] = 'CustomResourceDefinition'
    name: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.apiextensions.v1.CustomResourceDefinitionSpec,
        kdsl.apiextensions.v1.CustomResourceDefinitionSpecTypedDict] = attr.ib(
        metadata={'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class CustomResourceConversion(K8sObjectBase):
    """
    | CustomResourceConversion describes how to convert different versions of a CR.
    
    :param strategy: strategy specifies how custom resources are converted between versions. Allowed values are: - `None`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `Webhook`: API Server will call to an external webhook to do the conversion. Additional information
      is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set.
    :param webhook: webhook describes how to call the conversion webhook. Required when `strategy` is set to `Webhook`.
    """
    strategy: str = attr.ib(metadata={'yaml_name': 'strategy'})
    webhook: Optional[Union[kdsl.apiextensions.v1.WebhookConversion,
        kdsl.apiextensions.v1.WebhookConversionTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'webhook'})


@attr.s(kw_only=True)
class CustomResourceColumnDefinition(K8sObjectBase):
    """
    | CustomResourceColumnDefinition specifies a column for server side printing.
    
    :param jsonPath: jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column.
    :param name: name is a human readable name for the column.
    :param type: type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.
    :param description: description is a human readable description of this column.
    :param format: format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.
    :param priority: priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0.
    """
    jsonPath: str = attr.ib(metadata={'yaml_name': 'jsonPath'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    description: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'description'})
    format: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'format'})
    priority: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'priority'})


class WebhookConversionOptionalTypedDict(TypedDict, total=(False)):
    clientConfig: Union[kdsl.apiextensions.v1.WebhookClientConfig,
        kdsl.apiextensions.v1.WebhookClientConfigTypedDict]


class WebhookConversionTypedDict(WebhookConversionOptionalTypedDict, total=
    (True)):
    conversionReviewVersions: Sequence[str]


class WebhookClientConfigTypedDict(TypedDict, total=(False)):
    caBundle: str
    service: Union[kdsl.apiextensions.v1.ServiceReference,
        kdsl.apiextensions.v1.ServiceReferenceTypedDict]
    url: str


class ServiceReferenceOptionalTypedDict(TypedDict, total=(False)):
    path: str
    port: int


class ServiceReferenceTypedDict(ServiceReferenceOptionalTypedDict, total=(True)
    ):
    name: str
    namespace: str


class ExternalDocumentationTypedDict(TypedDict, total=(False)):
    description: str
    url: str


class CustomResourceValidationTypedDict(TypedDict, total=(False)):
    openAPIV3Schema: Any


class CustomResourceSubresourcesTypedDict(TypedDict, total=(False)):
    scale: Union[kdsl.apiextensions.v1.CustomResourceSubresourceScale,
        kdsl.apiextensions.v1.CustomResourceSubresourceScaleTypedDict]
    status: Mapping[str, Any]


class CustomResourceSubresourceScaleOptionalTypedDict(TypedDict, total=(False)
    ):
    labelSelectorPath: str


class CustomResourceSubresourceScaleTypedDict(
    CustomResourceSubresourceScaleOptionalTypedDict, total=(True)):
    specReplicasPath: str
    statusReplicasPath: str


class CustomResourceDefinitionVersionOptionalTypedDict(TypedDict, total=(False)
    ):
    additionalPrinterColumns: Sequence[Union[
        kdsl.apiextensions.v1.CustomResourceColumnDefinition,
        kdsl.apiextensions.v1.CustomResourceColumnDefinitionTypedDict]]
    schema: Union[kdsl.apiextensions.v1.CustomResourceValidation,
        kdsl.apiextensions.v1.CustomResourceValidationTypedDict]
    subresources: Union[kdsl.apiextensions.v1.CustomResourceSubresources,
        kdsl.apiextensions.v1.CustomResourceSubresourcesTypedDict]


class CustomResourceDefinitionVersionTypedDict(
    CustomResourceDefinitionVersionOptionalTypedDict, total=(True)):
    name: str
    served: bool
    storage: bool


class CustomResourceDefinitionStatusOptionalTypedDict(TypedDict, total=(False)
    ):
    conditions: Sequence[Union[
        kdsl.apiextensions.v1.CustomResourceDefinitionCondition,
        kdsl.apiextensions.v1.CustomResourceDefinitionConditionTypedDict]]


class CustomResourceDefinitionStatusTypedDict(
    CustomResourceDefinitionStatusOptionalTypedDict, total=(True)):
    acceptedNames: Union[
        kdsl.apiextensions.v1.CustomResourceDefinitionNames,
        kdsl.apiextensions.v1.CustomResourceDefinitionNamesTypedDict]
    storedVersions: Sequence[str]


class CustomResourceDefinitionSpecOptionalTypedDict(TypedDict, total=(False)):
    conversion: Union[kdsl.apiextensions.v1.CustomResourceConversion,
        kdsl.apiextensions.v1.CustomResourceConversionTypedDict]
    preserveUnknownFields: bool


class CustomResourceDefinitionSpecTypedDict(
    CustomResourceDefinitionSpecOptionalTypedDict, total=(True)):
    group: str
    names: Union[kdsl.apiextensions.v1.CustomResourceDefinitionNames,
        kdsl.apiextensions.v1.CustomResourceDefinitionNamesTypedDict]
    scope: str
    versions: Sequence[Union[
        kdsl.apiextensions.v1.CustomResourceDefinitionVersion,
        kdsl.apiextensions.v1.CustomResourceDefinitionVersionTypedDict]]


class CustomResourceDefinitionNamesOptionalTypedDict(TypedDict, total=(False)):
    categories: Sequence[str]
    listKind: str
    shortNames: Sequence[str]
    singular: str


class CustomResourceDefinitionNamesTypedDict(
    CustomResourceDefinitionNamesOptionalTypedDict, total=(True)):
    kind: str
    plural: str


class CustomResourceDefinitionListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class CustomResourceDefinitionListTypedDict(
    CustomResourceDefinitionListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.apiextensions.v1.CustomResourceDefinition,
        kdsl.apiextensions.v1.CustomResourceDefinitionTypedDict]]


class CustomResourceDefinitionConditionOptionalTypedDict(TypedDict, total=(
    False)):
    lastTransitionTime: str
    message: str
    reason: str


class CustomResourceDefinitionConditionTypedDict(
    CustomResourceDefinitionConditionOptionalTypedDict, total=(True)):
    status: str
    type: str


class CustomResourceDefinitionOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class CustomResourceDefinitionTypedDict(
    CustomResourceDefinitionOptionalTypedDict, total=(True)):
    name: str
    spec: Union[kdsl.apiextensions.v1.CustomResourceDefinitionSpec,
        kdsl.apiextensions.v1.CustomResourceDefinitionSpecTypedDict]


class CustomResourceConversionOptionalTypedDict(TypedDict, total=(False)):
    webhook: Union[kdsl.apiextensions.v1.WebhookConversion,
        kdsl.apiextensions.v1.WebhookConversionTypedDict]


class CustomResourceConversionTypedDict(
    CustomResourceConversionOptionalTypedDict, total=(True)):
    strategy: str


class CustomResourceColumnDefinitionOptionalTypedDict(TypedDict, total=(False)
    ):
    description: str
    format: str
    priority: int


class CustomResourceColumnDefinitionTypedDict(
    CustomResourceColumnDefinitionOptionalTypedDict, total=(True)):
    jsonPath: str
    name: str
    type: str
