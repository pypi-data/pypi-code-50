from __future__ import annotations
import attr
import kdsl.authentication.v1beta1
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class UserInfo(K8sObjectBase):
    """
    | UserInfo holds the information about the user needed to implement the user.Info interface.
    
    :param extra: Any additional information provided by the authenticator.
    :param groups: The names of groups this user is a part of.
    :param uid: A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.
    :param username: The name that uniquely identifies this user among all active users.
    """
    extra: Optional[Mapping[str, Sequence[str]]] = attr.ib(default=None,
        metadata={'yaml_name': 'extra'})
    groups: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'groups'})
    uid: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'uid'})
    username: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'username'})


@attr.s(kw_only=True)
class TokenReviewStatus(K8sObjectBase):
    """
    | TokenReviewStatus is the result of the token authentication request.
    
    :param audiences: Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server.
    :param authenticated: Authenticated indicates that the token was associated with a known user.
    :param error: Error indicates that the token couldn't be checked
    :param user: User is the UserInfo associated with the provided token.
    """
    audiences: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'audiences'})
    authenticated: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'authenticated'})
    error: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'error'})
    user: Optional[Union[kdsl.authentication.v1beta1.UserInfo,
        kdsl.authentication.v1beta1.UserInfoTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'user'})


@attr.s(kw_only=True)
class TokenReviewSpec(K8sObjectBase):
    """
    | TokenReviewSpec is a description of the token authentication request.
    
    :param audiences: Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.
    :param token: Token is the opaque bearer token.
    """
    audiences: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'audiences'})
    token: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'token'})


@attr.s(kw_only=True)
class TokenReview(K8sResourceBase):
    """
    | TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached by the webhook token authenticator plugin in the kube-apiserver.
    
    :param name: metadata.name
    :param spec: Spec holds information about the request being evaluated
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    """
    apiVersion: ClassVar[str] = 'authentication.k8s.io/v1beta1'
    kind: ClassVar[str] = 'TokenReview'
    name: str = attr.ib(metadata={'yaml_name': None})
    spec: Union[kdsl.authentication.v1beta1.TokenReviewSpec,
        kdsl.authentication.v1beta1.TokenReviewSpecTypedDict] = attr.ib(
        metadata={'yaml_name': 'spec'})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})


class UserInfoTypedDict(TypedDict, total=(False)):
    extra: Mapping[str, Sequence[str]]
    groups: Sequence[str]
    uid: str
    username: str


class TokenReviewStatusTypedDict(TypedDict, total=(False)):
    audiences: Sequence[str]
    authenticated: bool
    error: str
    user: Union[kdsl.authentication.v1beta1.UserInfo,
        kdsl.authentication.v1beta1.UserInfoTypedDict]


class TokenReviewSpecTypedDict(TypedDict, total=(False)):
    audiences: Sequence[str]
    token: str


class TokenReviewOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class TokenReviewTypedDict(TokenReviewOptionalTypedDict, total=(True)):
    name: str
    spec: Union[kdsl.authentication.v1beta1.TokenReviewSpec,
        kdsl.authentication.v1beta1.TokenReviewSpecTypedDict]
