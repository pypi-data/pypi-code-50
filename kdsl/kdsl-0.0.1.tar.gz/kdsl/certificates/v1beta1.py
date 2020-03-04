from __future__ import annotations
import kdsl.meta.v1
import attr
import kdsl.certificates.v1beta1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class CertificateSigningRequestStatus(K8sObjectBase):
    """
    | Kubernates API object: io.k8s.api.certificates.v1beta1.CertificateSigningRequestStatus
    
    :param certificate: If request was approved, the controller will place the issued certificate here.
    :param conditions: Conditions applied to the request, such as approval or denial.
    """
    certificate: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'certificate'})
    conditions: Optional[Sequence[Union[
        kdsl.certificates.v1beta1.CertificateSigningRequestCondition,
        kdsl.certificates.v1beta1.CertificateSigningRequestConditionTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'conditions'})


@attr.s(kw_only=True)
class CertificateSigningRequestSpec(K8sObjectBase):
    """
    | This information is immutable after the request is created. Only the Request and Usages fields can be set on creation, other fields are derived by Kubernetes and cannot be modified by users.
    
    :param request: Base64-encoded PKCS#10 CSR data
    :param extra: Extra information about the requesting user. See user.Info interface for details.
    :param groups: Group information about the requesting user. See user.Info interface for details.
    :param uid: UID information about the requesting user. See user.Info interface for details.
    :param usages: allowedUsages specifies a set of usage contexts the key will be valid for. See: https://tools.ietf.org/html/rfc5280#section-4.2.1.3
         https://tools.ietf.org/html/rfc5280#section-4.2.1.12
    :param username: Information about the requesting user. See user.Info interface for details.
    """
    request: str = attr.ib(metadata={'yaml_name': 'request'})
    extra: Optional[Mapping[str, Sequence[str]]] = attr.ib(default=None,
        metadata={'yaml_name': 'extra'})
    groups: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'groups'})
    uid: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'uid'})
    usages: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'usages'})
    username: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'username'})


@attr.s(kw_only=True)
class CertificateSigningRequestList(K8sObjectBase):
    """
    | Kubernates API object: io.k8s.api.certificates.v1beta1.CertificateSigningRequestList
    
    :param items: None
    :param apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    :param kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    :param metadata: None
    """
    items: Sequence[Union[
        kdsl.certificates.v1beta1.CertificateSigningRequest,
        kdsl.certificates.v1beta1.CertificateSigningRequestTypedDict]
        ] = attr.ib(metadata={'yaml_name': 'items'})
    apiVersion: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'apiVersion'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})
    metadata: Optional[Union[kdsl.meta.v1.ListMeta,
        kdsl.meta.v1.ListMetaTypedDict]] = attr.ib(default=None, metadata={
        'yaml_name': 'metadata'})


@attr.s(kw_only=True)
class CertificateSigningRequestCondition(K8sObjectBase):
    """
    | Kubernates API object: io.k8s.api.certificates.v1beta1.CertificateSigningRequestCondition
    
    :param type: request approval state, currently Approved or Denied.
    :param lastUpdateTime: timestamp for the last update to this condition
    :param message: human readable message with details about the request state
    :param reason: brief reason for the request state
    """
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    lastUpdateTime: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'lastUpdateTime'})
    message: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'message'})
    reason: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'reason'})


@attr.s(kw_only=True)
class CertificateSigningRequest(K8sResourceBase):
    """
    | Describes a certificate signing request
    
    :param name: metadata.name
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: The certificate request itself and any additional information.
    """
    apiVersion: ClassVar[str] = 'certificates.k8s.io/v1beta1'
    kind: ClassVar[str] = 'CertificateSigningRequest'
    name: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[
        kdsl.certificates.v1beta1.CertificateSigningRequestSpec,
        kdsl.certificates.v1beta1.CertificateSigningRequestSpecTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


class CertificateSigningRequestStatusTypedDict(TypedDict, total=(False)):
    certificate: str
    conditions: Sequence[Union[
        kdsl.certificates.v1beta1.CertificateSigningRequestCondition,
        kdsl.certificates.v1beta1.CertificateSigningRequestConditionTypedDict]]


class CertificateSigningRequestSpecOptionalTypedDict(TypedDict, total=(False)):
    extra: Mapping[str, Sequence[str]]
    groups: Sequence[str]
    uid: str
    usages: Sequence[str]
    username: str


class CertificateSigningRequestSpecTypedDict(
    CertificateSigningRequestSpecOptionalTypedDict, total=(True)):
    request: str


class CertificateSigningRequestListOptionalTypedDict(TypedDict, total=(False)):
    apiVersion: str
    kind: str
    metadata: Union[kdsl.meta.v1.ListMeta, kdsl.meta.v1.ListMetaTypedDict]


class CertificateSigningRequestListTypedDict(
    CertificateSigningRequestListOptionalTypedDict, total=(True)):
    items: Sequence[Union[
        kdsl.certificates.v1beta1.CertificateSigningRequest,
        kdsl.certificates.v1beta1.CertificateSigningRequestTypedDict]]


class CertificateSigningRequestConditionOptionalTypedDict(TypedDict, total=
    (False)):
    lastUpdateTime: str
    message: str
    reason: str


class CertificateSigningRequestConditionTypedDict(
    CertificateSigningRequestConditionOptionalTypedDict, total=(True)):
    type: str


class CertificateSigningRequestOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.certificates.v1beta1.CertificateSigningRequestSpec,
        kdsl.certificates.v1beta1.CertificateSigningRequestSpecTypedDict]


class CertificateSigningRequestTypedDict(
    CertificateSigningRequestOptionalTypedDict, total=(True)):
    name: str
