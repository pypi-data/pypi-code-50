from __future__ import annotations
import attr
import kdsl.authorization.v1beta1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class SubjectRulesReviewStatus(K8sObjectBase):
    """
    | SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete.
    
    :param incomplete: Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation.
    :param nonResourceRules: NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.
    :param resourceRules: ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.
    :param evaluationError: EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.
    """
    incomplete: bool = attr.ib(metadata={'yaml_name': 'incomplete'})
    nonResourceRules: Sequence[Union[
        kdsl.authorization.v1beta1.NonResourceRule,
        kdsl.authorization.v1beta1.NonResourceRuleTypedDict]] = attr.ib(
        metadata={'yaml_name': 'nonResourceRules'})
    resourceRules: Sequence[Union[kdsl.authorization.v1beta1.ResourceRule,
        kdsl.authorization.v1beta1.ResourceRuleTypedDict]] = attr.ib(metadata
        ={'yaml_name': 'resourceRules'})
    evaluationError: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'evaluationError'})


@attr.s(kw_only=True)
class SubjectAccessReviewStatus(K8sObjectBase):
    """
    | SubjectAccessReviewStatus
    
    :param allowed: Allowed is required. True if the action would be allowed, false otherwise.
    :param denied: Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true.
    :param evaluationError: EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.
    :param reason: Reason is optional.  It indicates why a request was allowed or denied.
    """
    allowed: bool = attr.ib(metadata={'yaml_name': 'allowed'})
    denied: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'denied'})
    evaluationError: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'evaluationError'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class SubjectAccessReviewSpec(K8sObjectBase):
    """
    | SubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set
    
    :param extra: Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here.
    :param group: Groups is the groups you're testing for.
    :param nonResourceAttributes: NonResourceAttributes describes information for a non-resource access request
    :param resourceAttributes: ResourceAuthorizationAttributes describes information for a resource access request
    :param uid: UID information about the requesting user.
    :param user: User is the user you're testing for. If you specify "User" but not "Group", then is it interpreted as "What if User were not a member of any groups
    """
    extra: Optional[Mapping[str, Sequence[str]]] = attr.ib(default=None,
        metadata={'yaml_name': 'extra'})
    group: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'group'})
    nonResourceAttributes: Optional[Union[
        kdsl.authorization.v1beta1.NonResourceAttributes,
        kdsl.authorization.v1beta1.NonResourceAttributesTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'nonResourceAttributes'})
    resourceAttributes: Optional[Union[
        kdsl.authorization.v1beta1.ResourceAttributes,
        kdsl.authorization.v1beta1.ResourceAttributesTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'resourceAttributes'})
    uid: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'uid'})
    user: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class SubjectAccessReview(K8sResourceBase):
    """
    | SubjectAccessReview checks whether or not a user or group can perform an action.
    
    :param name: metadata.name
    :param spec: Spec holds information about the request being evaluated
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'authorization.k8s.io/v1beta1'
    kind: ClassVar[str] = 'SubjectAccessReview'
    name: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.authorization.v1beta1.SubjectAccessReviewSpec,
        kdsl.authorization.v1beta1.SubjectAccessReviewSpecTypedDict] = attr.ib(
        metadata={'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class SelfSubjectRulesReviewSpec(K8sObjectBase):
    """
    | Kubernates API object: io.k8s.api.authorization.v1beta1.SelfSubjectRulesReviewSpec
    
    :param namespace: Namespace to evaluate rules for. Required.
    """
    namespace: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'namespace'})


@attr.s(kw_only=True)
class SelfSubjectRulesReview(K8sResourceBase):
    """
    | SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace. The returned list of actions may be incomplete depending on the server's authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide actions, or to quickly let an end user reason about their permissions. It should NOT Be used by external systems to drive authorization decisions as this raises confused deputy, cache lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions to the API server.
    
    :param name: metadata.name
    :param spec: Spec holds information about the request being evaluated.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'authorization.k8s.io/v1beta1'
    kind: ClassVar[str] = 'SelfSubjectRulesReview'
    name: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.authorization.v1beta1.SelfSubjectRulesReviewSpec,
        kdsl.authorization.v1beta1.SelfSubjectRulesReviewSpecTypedDict
        ] = attr.ib(metadata={'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class SelfSubjectAccessReviewSpec(K8sObjectBase):
    """
    | SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set
    
    :param nonResourceAttributes: NonResourceAttributes describes information for a non-resource access request
    :param resourceAttributes: ResourceAuthorizationAttributes describes information for a resource access request
    """
    nonResourceAttributes: Optional[Union[
        kdsl.authorization.v1beta1.NonResourceAttributes,
        kdsl.authorization.v1beta1.NonResourceAttributesTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'nonResourceAttributes'})
    resourceAttributes: Optional[Union[
        kdsl.authorization.v1beta1.ResourceAttributes,
        kdsl.authorization.v1beta1.ResourceAttributesTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'resourceAttributes'})


@attr.s(kw_only=True)
class SelfSubjectAccessReview(K8sResourceBase):
    """
    | SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling in a spec.namespace means "in all namespaces".  Self is a special case, because users should always be able to check whether they can perform an action
    
    :param name: metadata.name
    :param spec: Spec holds information about the request being evaluated.  user and groups must be empty
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'authorization.k8s.io/v1beta1'
    kind: ClassVar[str] = 'SelfSubjectAccessReview'
    name: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.authorization.v1beta1.SelfSubjectAccessReviewSpec,
        kdsl.authorization.v1beta1.SelfSubjectAccessReviewSpecTypedDict
        ] = attr.ib(metadata={'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


@attr.s(kw_only=True)
class ResourceRule(K8sObjectBase):
    """
    | ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.
    
    :param verbs: Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  "*" means all.
    :param apiGroups: APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  "*" means all.
    :param resourceNames: ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  "*" means all.
    :param resources: Resources is a list of resources this rule applies to.  "*" means all in the specified apiGroups.
     "*/foo" represents the subresource 'foo' for all resources in the specified apiGroups.
    """
    verbs: Sequence[str] = attr.ib(metadata={'yaml_name': 'verbs'})
    apiGroups: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'apiGroups'})
    resourceNames: Optional[Sequence[str]] = attr.ib(default=None, metadata
        ={'yaml_name': 'resourceNames'})
    resources: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'resources'})


@attr.s(kw_only=True)
class ResourceAttributes(K8sObjectBase):
    """
    | ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface
    
    :param group: Group is the API Group of the Resource.  "*" means all.
    :param name: Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.
    :param namespace: Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview
    :param resource: Resource is one of the existing resource types.  "*" means all.
    :param subresource: Subresource is one of the existing resource types.  "" means none.
    :param verb: Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all.
    :param version: Version is the API Version of the Resource.  "*" means all.
    """
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    namespace: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'namespace'})
    resource: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'resource'})
    subresource: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'subresource'})
    verb: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'verb'})
    version: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'version'})


@attr.s(kw_only=True)
class NonResourceRule(K8sObjectBase):
    """
    | NonResourceRule holds information that describes a rule for the non-resource
    
    :param verbs: Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all.
    :param nonResourceURLs: NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all.
    """
    verbs: Sequence[str] = attr.ib(metadata={'yaml_name': 'verbs'})
    nonResourceURLs: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nonResourceURLs'})


@attr.s(kw_only=True)
class NonResourceAttributes(K8sObjectBase):
    """
    | NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface
    
    :param path: Path is the URL path of the request
    :param verb: Verb is the standard HTTP verb
    """
    path: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'path'})
    verb: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'verb'})


@attr.s(kw_only=True)
class LocalSubjectAccessReview(K8sResourceBase):
    """
    | LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped policy that includes permissions checking.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param spec: Spec holds information about the request being evaluated.  spec.namespace must be equal to the namespace you made the request against.  If empty, it is defaulted.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'authorization.k8s.io/v1beta1'
    kind: ClassVar[str] = 'LocalSubjectAccessReview'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.authorization.v1beta1.SubjectAccessReviewSpec,
        kdsl.authorization.v1beta1.SubjectAccessReviewSpecTypedDict] = attr.ib(
        metadata={'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


class SubjectRulesReviewStatusOptionalTypedDict(TypedDict, total=(False)):
    evaluationError: str


class SubjectRulesReviewStatusTypedDict(
    SubjectRulesReviewStatusOptionalTypedDict, total=(True)):
    incomplete: bool
    nonResourceRules: Sequence[Union[
        kdsl.authorization.v1beta1.NonResourceRule,
        kdsl.authorization.v1beta1.NonResourceRuleTypedDict]]
    resourceRules: Sequence[Union[kdsl.authorization.v1beta1.ResourceRule,
        kdsl.authorization.v1beta1.ResourceRuleTypedDict]]


class SubjectAccessReviewStatusOptionalTypedDict(TypedDict, total=(False)):
    denied: bool
    evaluationError: str
    reason: str


class SubjectAccessReviewStatusTypedDict(
    SubjectAccessReviewStatusOptionalTypedDict, total=(True)):
    allowed: bool


class SubjectAccessReviewSpecTypedDict(TypedDict, total=(False)):
    extra: Mapping[str, Sequence[str]]
    group: Sequence[str]
    nonResourceAttributes: Union[
        kdsl.authorization.v1beta1.NonResourceAttributes,
        kdsl.authorization.v1beta1.NonResourceAttributesTypedDict]
    resourceAttributes: Union[kdsl.authorization.v1beta1.ResourceAttributes,
        kdsl.authorization.v1beta1.ResourceAttributesTypedDict]
    uid: str
    user: str


class SubjectAccessReviewOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class SubjectAccessReviewTypedDict(SubjectAccessReviewOptionalTypedDict,
    total=(True)):
    name: str
    spec: Union[kdsl.authorization.v1beta1.SubjectAccessReviewSpec,
        kdsl.authorization.v1beta1.SubjectAccessReviewSpecTypedDict]


class SelfSubjectRulesReviewSpecTypedDict(TypedDict, total=(False)):
    namespace: str


class SelfSubjectRulesReviewOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class SelfSubjectRulesReviewTypedDict(SelfSubjectRulesReviewOptionalTypedDict,
    total=(True)):
    name: str
    spec: Union[kdsl.authorization.v1beta1.SelfSubjectRulesReviewSpec,
        kdsl.authorization.v1beta1.SelfSubjectRulesReviewSpecTypedDict]


class SelfSubjectAccessReviewSpecTypedDict(TypedDict, total=(False)):
    nonResourceAttributes: Union[
        kdsl.authorization.v1beta1.NonResourceAttributes,
        kdsl.authorization.v1beta1.NonResourceAttributesTypedDict]
    resourceAttributes: Union[kdsl.authorization.v1beta1.ResourceAttributes,
        kdsl.authorization.v1beta1.ResourceAttributesTypedDict]


class SelfSubjectAccessReviewOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class SelfSubjectAccessReviewTypedDict(SelfSubjectAccessReviewOptionalTypedDict
    , total=(True)):
    name: str
    spec: Union[kdsl.authorization.v1beta1.SelfSubjectAccessReviewSpec,
        kdsl.authorization.v1beta1.SelfSubjectAccessReviewSpecTypedDict]


class ResourceRuleOptionalTypedDict(TypedDict, total=(False)):
    apiGroups: Sequence[str]
    resourceNames: Sequence[str]
    resources: Sequence[str]


class ResourceRuleTypedDict(ResourceRuleOptionalTypedDict, total=(True)):
    verbs: Sequence[str]


class ResourceAttributesTypedDict(TypedDict, total=(False)):
    group: str
    name: str
    namespace: str
    resource: str
    subresource: str
    verb: str
    version: str


class NonResourceRuleOptionalTypedDict(TypedDict, total=(False)):
    nonResourceURLs: Sequence[str]


class NonResourceRuleTypedDict(NonResourceRuleOptionalTypedDict, total=(True)):
    verbs: Sequence[str]


class NonResourceAttributesTypedDict(TypedDict, total=(False)):
    path: str
    verb: str


class LocalSubjectAccessReviewOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class LocalSubjectAccessReviewTypedDict(
    LocalSubjectAccessReviewOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    spec: Union[kdsl.authorization.v1beta1.SubjectAccessReviewSpec,
        kdsl.authorization.v1beta1.SubjectAccessReviewSpecTypedDict]
