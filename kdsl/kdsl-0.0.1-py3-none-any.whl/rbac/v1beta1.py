from __future__ import annotations
import kdsl.meta.v1
import attr
import kdsl.rbac.v1beta1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class Subject(K8sObjectBase):
    """
    | Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names.
    
    :param kind: Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error.
    :param name: Name of the object being referenced.
    :param apiGroup: APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects.
    :param namespace: Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error.
    """
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    apiGroup: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiGroup'})
    namespace: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'namespace'})


@attr.s(kw_only=True)
class RoleRef(K8sObjectBase):
    """
    | RoleRef contains information that points to the role being used
    
    :param apiGroup: APIGroup is the group for the resource being referenced
    :param kind: Kind is the type of resource being referenced
    :param name: Name is the name of resource being referenced
    """
    apiGroup: str = attr.ib(metadata={'yaml_name': 'apiGroup'})
    kind: str = attr.ib(metadata={'yaml_name': 'kind'})
    name: str = attr.ib(metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class RoleList(K8sObjectBase):
    """
    | RoleList is a collection of Roles Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 RoleList, and will no longer be served in v1.20.
    
    :param items: Items is a list of Roles
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata.
    """
    items: Sequence[Union[kdsl.rbac.v1beta1.Role,
        kdsl.rbac.v1beta1.RoleTypedDict]] = attr.ib(metadata={'yaml_name':
        'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class RoleBindingList(K8sObjectBase):
    """
    | RoleBindingList is a collection of RoleBindings Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 RoleBindingList, and will no longer be served in v1.20.
    
    :param items: Items is a list of RoleBindings
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata.
    """
    items: Sequence[Union[kdsl.rbac.v1beta1.RoleBinding,
        kdsl.rbac.v1beta1.RoleBindingTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class RoleBinding(K8sResourceBase):
    """
    | RoleBinding references a role, but does not contain it.  It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in.  RoleBindings in a given namespace only have effect in that namespace. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 RoleBinding, and will no longer be served in v1.20.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param roleRef: RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param subjects: Subjects holds references to the objects the role applies to.
    """
    apiVersion: ClassVar[str] = 'rbac.authorization.k8s.io/v1beta1'
    kind: ClassVar[str] = 'RoleBinding'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    roleRef: Union[kdsl.rbac.v1beta1.RoleRef,
        kdsl.rbac.v1beta1.RoleRefTypedDict] = attr.ib(metadata={'yaml_name':
        'roleRef'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    subjects: Optional[Sequence[Union[kdsl.rbac.v1beta1.Subject,
        kdsl.rbac.v1beta1.SubjectTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'subjects'})


@attr.s(kw_only=True)
class Role(K8sResourceBase):
    """
    | Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 Role, and will no longer be served in v1.20.
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param rules: Rules holds all the PolicyRules for this Role
    """
    apiVersion: ClassVar[str] = 'rbac.authorization.k8s.io/v1beta1'
    kind: ClassVar[str] = 'Role'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    rules: Optional[Sequence[Union[kdsl.rbac.v1beta1.PolicyRule,
        kdsl.rbac.v1beta1.PolicyRuleTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'rules'})


@attr.s(kw_only=True)
class PolicyRule(K8sObjectBase):
    """
    | PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.
    
    :param verbs: Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.
    :param apiGroups: APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.
    :param nonResourceURLs: NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both.
    :param resourceNames: ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.
    :param resources: Resources is a list of resources this rule applies to.  '*' represents all resources in the specified apiGroups. '*/foo' represents the subresource 'foo' for all resources in the specified apiGroups.
    """
    verbs: Sequence[str] = attr.ib(metadata={'yaml_name': 'verbs'})
    apiGroups: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'apiGroups'})
    nonResourceURLs: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nonResourceURLs'})
    resourceNames: Optional[Sequence[str]] = attr.ib(default=None, metadata
        ={'yaml_name': 'resourceNames'})
    resources: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'resources'})


@attr.s(kw_only=True)
class ClusterRoleList(K8sObjectBase):
    """
    | ClusterRoleList is a collection of ClusterRoles. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRoles, and will no longer be served in v1.20.
    
    :param items: Items is a list of ClusterRoles
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata.
    """
    items: Sequence[Union[kdsl.rbac.v1beta1.ClusterRole,
        kdsl.rbac.v1beta1.ClusterRoleTypedDict]] = attr.ib(metadata={
        'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ClusterRoleBindingList(K8sObjectBase):
    """
    | ClusterRoleBindingList is a collection of ClusterRoleBindings. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRoleBindingList, and will no longer be served in v1.20.
    
    :param items: Items is a list of ClusterRoleBindings
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: Standard object's metadata.
    """
    items: Sequence[Union[kdsl.rbac.v1beta1.ClusterRoleBinding,
        kdsl.rbac.v1beta1.ClusterRoleBindingTypedDict]] = attr.ib(metadata=
        {'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class ClusterRoleBinding(K8sResourceBase):
    """
    | ClusterRoleBinding references a ClusterRole, but not contain it.  It can reference a ClusterRole in the global namespace, and adds who information via Subject. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRoleBinding, and will no longer be served in v1.20.
    
    :param name: metadata.name
    :param roleRef: RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param subjects: Subjects holds references to the objects the role applies to.
    """
    apiVersion: ClassVar[str] = 'rbac.authorization.k8s.io/v1beta1'
    kind: ClassVar[str] = 'ClusterRoleBinding'
    name: str = attr.ib(metadata={'yaml_name': None})
    roleRef: Union[kdsl.rbac.v1beta1.RoleRef,
        kdsl.rbac.v1beta1.RoleRefTypedDict] = attr.ib(metadata={'yaml_name':
        'roleRef'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    subjects: Optional[Sequence[Union[kdsl.rbac.v1beta1.Subject,
        kdsl.rbac.v1beta1.SubjectTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'subjects'})


@attr.s(kw_only=True)
class ClusterRole(K8sResourceBase):
    """
    | ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRole, and will no longer be served in v1.20.
    
    :param name: metadata.name
    :param aggregationRule: AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param rules: Rules holds all the PolicyRules for this ClusterRole
    """
    apiVersion: ClassVar[str] = 'rbac.authorization.k8s.io/v1beta1'
    kind: ClassVar[str] = 'ClusterRole'
    name: str = attr.ib(metadata={'yaml_name': None})
    aggregationRule: Optional[Union[kdsl.rbac.v1beta1.AggregationRule,
        kdsl.rbac.v1beta1.AggregationRuleTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'aggregationRule'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    rules: Optional[Sequence[Union[kdsl.rbac.v1beta1.PolicyRule,
        kdsl.rbac.v1beta1.PolicyRuleTypedDict]]] = attr.ib(default=None,
        metadata={'yaml_name': 'rules'})


@attr.s(kw_only=True)
class AggregationRule(K8sObjectBase):
    """
    | AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole
    
    :param clusterRoleSelectors: ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added
    """
    clusterRoleSelectors: Optional[Sequence[Union[
        kdsl.meta.v1.LabelSelector, kdsl.meta.v1.LabelSelectorTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name':
        'clusterRoleSelectors'})


class SubjectOptionalTypedDict(TypedDict, total=(False)):
    apiGroup: str
    namespace: str


class SubjectTypedDict(SubjectOptionalTypedDict, total=(True)):
    kind: str
    name: str


class RoleRefTypedDict(TypedDict, total=(True)):
    apiGroup: str
    kind: str
    name: str


class RoleListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class RoleListTypedDict(RoleListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.rbac.v1beta1.Role,
        kdsl.rbac.v1beta1.RoleTypedDict]]


class RoleBindingListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class RoleBindingListTypedDict(RoleBindingListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.rbac.v1beta1.RoleBinding,
        kdsl.rbac.v1beta1.RoleBindingTypedDict]]


class RoleBindingOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    subjects: Sequence[Union[kdsl.rbac.v1beta1.Subject,
        kdsl.rbac.v1beta1.SubjectTypedDict]]


class RoleBindingTypedDict(RoleBindingOptionalTypedDict, total=(True)):
    name: str
    namespace: str
    roleRef: Union[kdsl.rbac.v1beta1.RoleRef,
        kdsl.rbac.v1beta1.RoleRefTypedDict]


class RoleOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    rules: Sequence[Union[kdsl.rbac.v1beta1.PolicyRule,
        kdsl.rbac.v1beta1.PolicyRuleTypedDict]]


class RoleTypedDict(RoleOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class PolicyRuleOptionalTypedDict(TypedDict, total=(False)):
    apiGroups: Sequence[str]
    nonResourceURLs: Sequence[str]
    resourceNames: Sequence[str]
    resources: Sequence[str]


class PolicyRuleTypedDict(PolicyRuleOptionalTypedDict, total=(True)):
    verbs: Sequence[str]


class ClusterRoleListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ClusterRoleListTypedDict(ClusterRoleListOptionalTypedDict, total=(True)):
    items: Sequence[Union[kdsl.rbac.v1beta1.ClusterRole,
        kdsl.rbac.v1beta1.ClusterRoleTypedDict]]


class ClusterRoleBindingListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class ClusterRoleBindingListTypedDict(ClusterRoleBindingListOptionalTypedDict,
    total=(True)):
    items: Sequence[Union[kdsl.rbac.v1beta1.ClusterRoleBinding,
        kdsl.rbac.v1beta1.ClusterRoleBindingTypedDict]]


class ClusterRoleBindingOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    subjects: Sequence[Union[kdsl.rbac.v1beta1.Subject,
        kdsl.rbac.v1beta1.SubjectTypedDict]]


class ClusterRoleBindingTypedDict(ClusterRoleBindingOptionalTypedDict,
    total=(True)):
    name: str
    roleRef: Union[kdsl.rbac.v1beta1.RoleRef,
        kdsl.rbac.v1beta1.RoleRefTypedDict]


class ClusterRoleOptionalTypedDict(TypedDict, total=(False)):
    aggregationRule: Union[kdsl.rbac.v1beta1.AggregationRule,
        kdsl.rbac.v1beta1.AggregationRuleTypedDict]
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    rules: Sequence[Union[kdsl.rbac.v1beta1.PolicyRule,
        kdsl.rbac.v1beta1.PolicyRuleTypedDict]]


class ClusterRoleTypedDict(ClusterRoleOptionalTypedDict, total=(True)):
    name: str


class AggregationRuleTypedDict(TypedDict, total=(False)):
    clusterRoleSelectors: Sequence[Union[kdsl.meta.v1.LabelSelector,
        kdsl.meta.v1.LabelSelectorTypedDict]]
