from __future__ import annotations
import attr
import kdsl.certmanager.v1alpha2
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import Literal, Any, ClassVar, Mapping, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class IssuerSpecAcmeExternalAccountBindingKeySecretRef(K8sObjectBase):
    """
    | keySecretRef is a Secret Key Selector referencing a data item in a Kubernetes Secret which holds the symmetric MAC key of the External Account Binding. The `key` is the index string that is paired with the key data in the Secret and should not be confused with the key data itself, or indeed with the External Account Binding keyID above. The secret key stored in the Secret **must** be un-padded, base64 URL encoded data.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeExternalAccountBinding(K8sObjectBase):
    """
    | ExternalAcccountBinding is a reference to a CA external account of the ACME server.
    
    :param keyAlgorithm: keyAlgorithm is the MAC key algorithm that the key is used for. Valid values are "HS256", "HS384" and "HS512".
    :param keyID: keyID is the ID of the CA key that the External Account is bound to.
    :param keySecretRef: keySecretRef is a Secret Key Selector referencing a data item in a Kubernetes Secret which holds the symmetric MAC key of the External Account Binding. The `key` is the index string that is paired with the key data in the Secret and should not be confused with the key data itself, or indeed with the External Account Binding keyID above. The secret key stored in the Secret **must** be un-padded, base64 URL encoded data.
    """
    keyAlgorithm: Literal['HS256', 'HS384', 'HS512'] = attr.ib(metadata={
        'yaml_name': 'keyAlgorithm'})
    keyID: str = attr.ib(metadata={'yaml_name': 'keyID'})
    keySecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeExternalAccountBindingKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeExternalAccountBindingKeySecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'keySecretRef'})


@attr.s(kw_only=True)
class IssuerSpecAcmePrivateKeySecretRef(K8sObjectBase):
    """
    | PrivateKey is the name of a secret containing the private key for this user account.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01AcmednsAccountSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01AcmednsAccountSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Acmedns(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderAcmeDNS is a structure containing the configuration for ACME-DNS servers
    
    :param accountSecretRef: None
    :param host: None
    """
    accountSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AcmednsAccountSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AcmednsAccountSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'accountSecretRef'})
    host: str = attr.ib(metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Akamai(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderAkamai is a structure containing the DNS configuration for Akamai DNS—Zone Record Management API
    
    :param accessTokenSecretRef: None
    :param clientSecretSecretRef: None
    :param clientTokenSecretRef: None
    :param serviceConsumerDomain: None
    """
    accessTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'accessTokenSecretRef'})
    clientSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'clientSecretSecretRef'})
    clientTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'clientTokenSecretRef'})
    serviceConsumerDomain: str = attr.ib(metadata={'yaml_name':
        'serviceConsumerDomain'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Azuredns(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderAzureDNS is a structure containing the configuration for Azure DNS
    
    :param clientID: None
    :param clientSecretSecretRef: None
    :param resourceGroupName: None
    :param subscriptionID: None
    :param tenantID: None
    :param environment: None
    :param hostedZoneName: None
    """
    clientID: str = attr.ib(metadata={'yaml_name': 'clientID'})
    clientSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'clientSecretSecretRef'})
    resourceGroupName: str = attr.ib(metadata={'yaml_name':
        'resourceGroupName'})
    subscriptionID: str = attr.ib(metadata={'yaml_name': 'subscriptionID'})
    tenantID: str = attr.ib(metadata={'yaml_name': 'tenantID'})
    environment: Optional[Literal['AzurePublicCloud', 'AzureChinaCloud',
        'AzureGermanCloud', 'AzureUSGovernmentCloud']] = attr.ib(default=
        None, metadata={'yaml_name': 'environment'})
    hostedZoneName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'hostedZoneName'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Clouddns(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderCloudDNS is a structure containing the DNS configuration for Google Cloud DNS
    
    :param project: None
    :param serviceAccountSecretRef: None
    """
    project: str = attr.ib(metadata={'yaml_name': 'project'})
    serviceAccountSecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'serviceAccountSecretRef'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Cloudflare(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderCloudflare is a structure containing the DNS configuration for Cloudflare
    
    :param email: None
    :param apiKeySecretRef: None
    :param apiTokenSecretRef: None
    """
    email: str = attr.ib(metadata={'yaml_name': 'email'})
    apiKeySecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'apiKeySecretRef'})
    apiTokenSecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'apiTokenSecretRef'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Digitalocean(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderDigitalOcean is a structure containing the DNS configuration for DigitalOcean Domains
    
    :param tokenSecretRef: None
    """
    tokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'tokenSecretRef'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRef(K8sObjectBase):
    """
    | The name of the secret containing the TSIG value. If ``tsigKeyName`` is defined, this field is required.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Rfc2136(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderRFC2136 is a structure containing the configuration for RFC2136 DNS
    
    :param nameserver: The IP address of the DNS supporting RFC2136. Required. Note: FQDN is not a valid value, only IP.
    :param tsigAlgorithm: The TSIG Algorithm configured in the DNS supporting RFC2136. Used only when ``tsigSecretSecretRef`` and ``tsigKeyName`` are defined. Supported values are (case-insensitive): ``HMACMD5`` (default), ``HMACSHA1``, ``HMACSHA256`` or ``HMACSHA512``.
    :param tsigKeyName: The TSIG Key name configured in the DNS. If ``tsigSecretSecretRef`` is defined, this field is required.
    :param tsigSecretSecretRef: The name of the secret containing the TSIG value. If ``tsigKeyName`` is defined, this field is required.
    """
    nameserver: str = attr.ib(metadata={'yaml_name': 'nameserver'})
    tsigAlgorithm: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'tsigAlgorithm'})
    tsigKeyName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'tsigKeyName'})
    tsigSecretSecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'tsigSecretSecretRef'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRef(K8sObjectBase):
    """
    | The SecretAccessKey is used for authentication. If not set we fall-back to using env vars, shared credentials file or AWS Instance metadata https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Route53(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderRoute53 is a structure containing the Route 53 configuration for AWS
    
    :param region: Always set the region when using AccessKeyID and SecretAccessKey
    :param accessKeyID: The AccessKeyID is used for authentication. If not set we fall-back to using env vars, shared credentials file or AWS Instance metadata see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
    :param hostedZoneID: If set, the provider will manage only this zone in Route53 and will not do an lookup using the route53:ListHostedZonesByName api call.
    :param role: Role is a Role ARN which the Route53 provider will assume using either the explicit credentials AccessKeyID/SecretAccessKey or the inferred credentials from environment variables, shared credentials file or AWS Instance metadata
    :param secretAccessKeySecretRef: The SecretAccessKey is used for authentication. If not set we fall-back to using env vars, shared credentials file or AWS Instance metadata https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
    """
    region: str = attr.ib(metadata={'yaml_name': 'region'})
    accessKeyID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'accessKeyID'})
    hostedZoneID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'hostedZoneID'})
    role: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'role'})
    secretAccessKeySecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'secretAccessKeySecretRef'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01Webhook(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderWebhook specifies configuration for a webhook DNS01 provider, including where to POST ChallengePayload resources.
    
    :param groupName: The API group name that should be used when POSTing ChallengePayload resources to the webhook apiserver. This should be the same as the GroupName specified in the webhook provider implementation.
    :param solverName: The name of the solver to use, as defined in the webhook provider implementation. This will typically be the name of the provider, e.g. 'cloudflare'.
    :param config: Additional configuration that should be passed to the webhook apiserver when challenges are processed. This can contain arbitrary JSON data. Secret values should not be specified in this stanza. If secret values are needed (e.g. credentials for a DNS service), you should use a SecretKeySelector to reference a Secret resource. For details on the schema of this field, consult the webhook provider implementation's documentation.
    """
    groupName: str = attr.ib(metadata={'yaml_name': 'groupName'})
    solverName: str = attr.ib(metadata={'yaml_name': 'solverName'})
    config: Optional[Any] = attr.ib(default=None, metadata={'yaml_name':
        'config'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayDns01(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArrayDns01
    
    :param acmedns: ACMEIssuerDNS01ProviderAcmeDNS is a structure containing the configuration for ACME-DNS servers
    :param akamai: ACMEIssuerDNS01ProviderAkamai is a structure containing the DNS configuration for Akamai DNS—Zone Record Management API
    :param azuredns: ACMEIssuerDNS01ProviderAzureDNS is a structure containing the configuration for Azure DNS
    :param clouddns: ACMEIssuerDNS01ProviderCloudDNS is a structure containing the DNS configuration for Google Cloud DNS
    :param cloudflare: ACMEIssuerDNS01ProviderCloudflare is a structure containing the DNS configuration for Cloudflare
    :param cnameStrategy: CNAMEStrategy configures how the DNS01 provider should handle CNAME records when found in DNS zones.
    :param digitalocean: ACMEIssuerDNS01ProviderDigitalOcean is a structure containing the DNS configuration for DigitalOcean Domains
    :param rfc2136: ACMEIssuerDNS01ProviderRFC2136 is a structure containing the configuration for RFC2136 DNS
    :param route53: ACMEIssuerDNS01ProviderRoute53 is a structure containing the Route 53 configuration for AWS
    :param webhook: ACMEIssuerDNS01ProviderWebhook specifies configuration for a webhook DNS01 provider, including where to POST ChallengePayload resources.
    """
    acmedns: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Acmedns,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AcmednsTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'acmedns'})
    akamai: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Akamai,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'akamai'})
    azuredns: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Azuredns,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AzurednsTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'azuredns'})
    clouddns: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Clouddns,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01ClouddnsTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'clouddns'})
    cloudflare: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Cloudflare,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'cloudflare'})
    cnameStrategy: Optional[Literal['None', 'Follow']] = attr.ib(default=
        None, metadata={'yaml_name': 'cnameStrategy'})
    digitalocean: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Digitalocean,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01DigitaloceanTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'digitalocean'})
    rfc2136: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Rfc2136,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Rfc2136TypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'rfc2136'})
    route53: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Route53,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Route53TypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'route53'})
    webhook: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Webhook,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01WebhookTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'webhook'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateMetadata(K8sObjectBase):
    """
    | ObjectMeta overrides for the pod used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.
    
    :param annotations: Annotations that should be added to the create ACME HTTP01 solver pods.
    :param labels: Labels that should be added to the created ACME HTTP01 solver pods.
    """
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'annotations'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'labels'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray(
    K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference(
    K8sObjectBase):
    """
    | A node selector term, associated with the corresponding weight.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArray(
    K8sObjectBase):
    """
    | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
    
    :param preference: A node selector term, associated with the corresponding weight.
    :param weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.
    """
    preference: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ] = attr.ib(metadata={'yaml_name': 'preference'})
    weight: int = attr.ib(metadata={'yaml_name': 'weight'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray(
    K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray(
    K8sObjectBase):
    """
    | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(
    K8sObjectBase):
    """
    | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    
    :param nodeSelectorTerms: Required. A list of node selector terms. The terms are ORed.
    """
    nodeSelectorTerms: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]] = attr.ib(metadata={'yaml_name': 'nodeSelectorTerms'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinity(
    K8sObjectBase):
    """
    | Describes node affinity scheduling rules for the pod.
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray(
    K8sObjectBase):
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
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTerm(
    K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray(
    K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray(
    K8sObjectBase):
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
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinity(
    K8sObjectBase):
    """
    | Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray(
    K8sObjectBase):
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
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTerm(
    K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray(
    K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray(
    K8sObjectBase):
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
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinity(
    K8sObjectBase):
    """
    | Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinity(K8sObjectBase):
    """
    | If specified, the pod's scheduling constraints
    
    :param nodeAffinity: Describes node affinity scheduling rules for the pod.
    :param podAffinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    :param podAntiAffinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    """
    nodeAffinity: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinity
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'nodeAffinity'})
    podAffinity: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinity
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podAffinity'})
    podAntiAffinity: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinity
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podAntiAffinity'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArray(K8sObjectBase):
    """
    | The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.
    
    :param effect: Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.
    :param key: Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.
    :param operator: Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.
    :param tolerationSeconds: TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.
    :param value: Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.
    """
    effect: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'effect'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})
    operator: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'operator'})
    tolerationSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'tolerationSeconds'})
    value: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'value'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpec(K8sObjectBase):
    """
    | PodSpec defines overrides for the HTTP01 challenge solver pod. Only the 'nodeSelector', 'affinity' and 'tolerations' fields are supported currently. All other fields will be ignored.
    
    :param affinity: If specified, the pod's scheduling constraints
    :param nodeSelector: NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
    :param tolerations: If specified, the pod's tolerations.
    """
    affinity: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinity
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'affinity'})
    nodeSelector: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeSelector'})
    tolerations: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'tolerations'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01IngressPodTemplate(K8sObjectBase):
    """
    | Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges
    
    :param metadata: ObjectMeta overrides for the pod used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.
    :param spec: PodSpec defines overrides for the HTTP01 challenge solver pod. Only the 'nodeSelector', 'affinity' and 'tolerations' fields are supported currently. All other fields will be ignored.
    """
    metadata: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateMetadata
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateMetadataTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'metadata'})
    spec: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpec
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01Ingress(K8sObjectBase):
    """
    | The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.
    
    :param class_: The ingress class to use when creating Ingress resources to solve ACME challenges that use this challenge solver. Only one of 'class' or 'name' may be specified.
    :param name: The name of the ingress resource that should have ACME challenge solving routes inserted into it in order to solve HTTP01 challenges. This is typically used in conjunction with ingress controllers like ingress-gce, which maintains a 1:1 mapping between external IPs and ingress resources.
    :param podTemplate: Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges
    :param serviceType: Optional service type for Kubernetes solver service
    """
    class_: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'class'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    podTemplate: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplate,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podTemplate'})
    serviceType: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'serviceType'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArrayHttp01(K8sObjectBase):
    """
    | ACMEChallengeSolverHTTP01 contains configuration detailing how to solve HTTP01 challenges within a Kubernetes cluster. Typically this is accomplished through creating 'routes' of some description that configure ingress controllers to direct traffic to 'solver pods', which are responsible for responding to the ACME server's HTTP requests.
    
    :param ingress: The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.
    """
    ingress: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01Ingress,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'ingress'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArraySelector(K8sObjectBase):
    """
    | Selector selects a set of DNSNames on the Certificate resource that should be solved using this challenge solver.
    
    :param dnsNames: List of DNSNames that this solver will be used to solve. If specified and a match is found, a dnsNames selector will take precedence over a dnsZones selector. If multiple solvers match with the same dnsNames value, the solver with the most matching labels in matchLabels will be selected. If neither has more matches, the solver defined earlier in the list will be selected.
    :param dnsZones: List of DNSZones that this solver will be used to solve. The most specific DNS zone match specified here will take precedence over other DNS zone matches, so a solver specifying sys.example.com will be selected over one specifying example.com for the domain www.sys.example.com. If multiple solvers match with the same dnsZones value, the solver with the most matching labels in matchLabels will be selected. If neither has more matches, the solver defined earlier in the list will be selected.
    :param matchLabels: A label selector that is used to refine the set of certificate's that this challenge solver will apply to.
    """
    dnsNames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'dnsNames'})
    dnsZones: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'dnsZones'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class IssuerSpecAcmeArray(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecAcmeArray
    
    :param dns01: None
    :param http01: ACMEChallengeSolverHTTP01 contains configuration detailing how to solve HTTP01 challenges within a Kubernetes cluster. Typically this is accomplished through creating 'routes' of some description that configure ingress controllers to direct traffic to 'solver pods', which are responsible for responding to the ACME server's HTTP requests.
    :param selector: Selector selects a set of DNSNames on the Certificate resource that should be solved using this challenge solver.
    """
    dns01: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01TypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'dns01'})
    http01: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01TypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'http01'})
    selector: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArraySelector,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArraySelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'selector'})


@attr.s(kw_only=True)
class IssuerSpecAcme(K8sObjectBase):
    """
    | ACMEIssuer contains the specification for an ACME issuer
    
    :param privateKeySecretRef: PrivateKey is the name of a secret containing the private key for this user account.
    :param server: Server is the ACME server URL
    :param email: Email is the email for this account
    :param externalAccountBinding: ExternalAcccountBinding is a reference to a CA external account of the ACME server.
    :param skipTLSVerify: If true, skip verifying the ACME server TLS certificate
    :param solvers: Solvers is a list of challenge solvers that will be used to solve ACME challenges for the matching domains.
    """
    privateKeySecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmePrivateKeySecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmePrivateKeySecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'privateKeySecretRef'})
    server: str = attr.ib(metadata={'yaml_name': 'server'})
    email: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'email'})
    externalAccountBinding: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeExternalAccountBinding,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeExternalAccountBindingTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'externalAccountBinding'})
    skipTLSVerify: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'skipTLSVerify'})
    solvers: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArray,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayTypedDict]]] = attr.ib(
        default=None, metadata={'yaml_name': 'solvers'})


@attr.s(kw_only=True)
class IssuerSpecCa(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecCa
    
    :param secretName: SecretName is the name of the secret used to sign Certificates issued by this Issuer.
    """
    secretName: str = attr.ib(metadata={'yaml_name': 'secretName'})


@attr.s(kw_only=True)
class IssuerSpecVaultAuthAppRoleSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecVaultAuthAppRoleSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecVaultAuthAppRole(K8sObjectBase):
    """
    | This Secret contains a AppRole and Secret
    
    :param path: Where the authentication path is mounted in Vault.
    :param roleId: None
    :param secretRef: None
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    roleId: str = attr.ib(metadata={'yaml_name': 'roleId'})
    secretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthAppRoleSecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthAppRoleSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class IssuerSpecVaultAuthKubernetesSecretRef(K8sObjectBase):
    """
    | The required Secret field containing a Kubernetes ServiceAccount JWT used for authenticating with Vault. Use of 'ambient credentials' is not supported.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecVaultAuthKubernetes(K8sObjectBase):
    """
    | This contains a Role and Secret with a ServiceAccount token to authenticate with vault.
    
    :param role: A required field containing the Vault Role to assume. A Role binds a Kubernetes ServiceAccount with a set of Vault policies.
    :param secretRef: The required Secret field containing a Kubernetes ServiceAccount JWT used for authenticating with Vault. Use of 'ambient credentials' is not supported.
    :param mountPath: The Vault mountPath here is the mount path to use when authenticating with Vault. For example, setting a value to `/v1/auth/foo`, will use the path `/v1/auth/foo/login` to authenticate with Vault. If unspecified, the default value "/v1/auth/kubernetes" will be used.
    """
    role: str = attr.ib(metadata={'yaml_name': 'role'})
    secretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthKubernetesSecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthKubernetesSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'secretRef'})
    mountPath: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'mountPath'})


@attr.s(kw_only=True)
class IssuerSpecVaultAuthTokenSecretRef(K8sObjectBase):
    """
    | This Secret contains the Vault token key
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecVaultAuth(K8sObjectBase):
    """
    | Vault authentication
    
    :param appRole: This Secret contains a AppRole and Secret
    :param kubernetes: This contains a Role and Secret with a ServiceAccount token to authenticate with vault.
    :param tokenSecretRef: This Secret contains the Vault token key
    """
    appRole: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthAppRole,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthAppRoleTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'appRole'})
    kubernetes: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthKubernetes,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthKubernetesTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'kubernetes'})
    tokenSecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthTokenSecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthTokenSecretRefTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tokenSecretRef'})


@attr.s(kw_only=True)
class IssuerSpecVault(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.IssuerSpecVault
    
    :param auth: Vault authentication
    :param path: Vault URL path to the certificate role
    :param server: Server is the vault connection address
    :param caBundle: Base64 encoded CA bundle to validate Vault server certificate. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. If not set the system root certificates are used to validate the TLS connection.
    """
    auth: Union[kdsl.certmanager.v1alpha2.IssuerSpecVaultAuth,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthTypedDict] = attr.ib(
        metadata={'yaml_name': 'auth'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    server: str = attr.ib(metadata={'yaml_name': 'server'})
    caBundle: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caBundle'})


@attr.s(kw_only=True)
class IssuerSpecVenafiCloudApiTokenSecretRef(K8sObjectBase):
    """
    | APITokenSecretRef is a secret key selector for the Venafi Cloud API token.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class IssuerSpecVenafiCloud(K8sObjectBase):
    """
    | Cloud specifies the Venafi cloud configuration settings. Only one of TPP or Cloud may be specified.
    
    :param apiTokenSecretRef: APITokenSecretRef is a secret key selector for the Venafi Cloud API token.
    :param url: URL is the base URL for Venafi Cloud
    """
    apiTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiCloudApiTokenSecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiCloudApiTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'apiTokenSecretRef'})
    url: str = attr.ib(metadata={'yaml_name': 'url'})


@attr.s(kw_only=True)
class IssuerSpecVenafiTppCredentialsRef(K8sObjectBase):
    """
    | CredentialsRef is a reference to a Secret containing the username and password for the TPP server. The secret must contain two keys, 'username' and 'password'.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class IssuerSpecVenafiTpp(K8sObjectBase):
    """
    | TPP specifies Trust Protection Platform configuration settings. Only one of TPP or Cloud may be specified.
    
    :param credentialsRef: CredentialsRef is a reference to a Secret containing the username and password for the TPP server. The secret must contain two keys, 'username' and 'password'.
    :param url: URL is the base URL for the Venafi TPP instance
    :param caBundle: CABundle is a PEM encoded TLS certifiate to use to verify connections to the TPP instance. If specified, system roots will not be used and the issuing CA for the TPP instance must be verifiable using the provided root. If not specified, the connection will be verified using the cert-manager system root certificates.
    """
    credentialsRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiTppCredentialsRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiTppCredentialsRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'credentialsRef'})
    url: str = attr.ib(metadata={'yaml_name': 'url'})
    caBundle: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caBundle'})


@attr.s(kw_only=True)
class IssuerSpecVenafi(K8sObjectBase):
    """
    | VenafiIssuer describes issuer configuration details for Venafi Cloud.
    
    :param zone: Zone is the Venafi Policy Zone to use for this issuer. All requests made to the Venafi platform will be restricted by the named zone policy. This field is required.
    :param cloud: Cloud specifies the Venafi cloud configuration settings. Only one of TPP or Cloud may be specified.
    :param tpp: TPP specifies Trust Protection Platform configuration settings. Only one of TPP or Cloud may be specified.
    """
    zone: str = attr.ib(metadata={'yaml_name': 'zone'})
    cloud: Optional[Union[kdsl.certmanager.v1alpha2.IssuerSpecVenafiCloud,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiCloudTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'cloud'})
    tpp: Optional[Union[kdsl.certmanager.v1alpha2.IssuerSpecVenafiTpp,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiTppTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'tpp'})


@attr.s(kw_only=True)
class IssuerSpec(K8sObjectBase):
    """
    | IssuerSpec is the specification of an Issuer. This includes any configuration required for the issuer.
    
    :param acme: ACMEIssuer contains the specification for an ACME issuer
    :param ca: None
    :param selfSigned: None
    :param vault: None
    :param venafi: VenafiIssuer describes issuer configuration details for Venafi Cloud.
    """
    acme: Optional[Union[kdsl.certmanager.v1alpha2.IssuerSpecAcme,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'acme'})
    ca: Optional[Union[kdsl.certmanager.v1alpha2.IssuerSpecCa,
        kdsl.certmanager.v1alpha2.IssuerSpecCaTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'ca'})
    selfSigned: Optional[Mapping[str, Any]] = attr.ib(default=None,
        metadata={'yaml_name': 'selfSigned'})
    vault: Optional[Union[kdsl.certmanager.v1alpha2.IssuerSpecVault,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'vault'})
    venafi: Optional[Union[kdsl.certmanager.v1alpha2.IssuerSpecVenafi,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'venafi'})


@attr.s(kw_only=True)
class Issuer(K8sResourceBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.Issuer
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: IssuerSpec is the specification of an Issuer. This includes any configuration required for the issuer.
    """
    apiVersion: ClassVar[str] = 'cert-manager.io/v1alpha2'
    kind: ClassVar[str] = 'Issuer'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.certmanager.v1alpha2.IssuerSpec,
        kdsl.certmanager.v1alpha2.IssuerSpecTypedDict]] = attr.ib(default=
        None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRef(K8sObjectBase):
    """
    | keySecretRef is a Secret Key Selector referencing a data item in a Kubernetes Secret which holds the symmetric MAC key of the External Account Binding. The `key` is the index string that is paired with the key data in the Secret and should not be confused with the key data itself, or indeed with the External Account Binding keyID above. The secret key stored in the Secret **must** be un-padded, base64 URL encoded data.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeExternalAccountBinding(K8sObjectBase):
    """
    | ExternalAcccountBinding is a reference to a CA external account of the ACME server.
    
    :param keyAlgorithm: keyAlgorithm is the MAC key algorithm that the key is used for. Valid values are "HS256", "HS384" and "HS512".
    :param keyID: keyID is the ID of the CA key that the External Account is bound to.
    :param keySecretRef: keySecretRef is a Secret Key Selector referencing a data item in a Kubernetes Secret which holds the symmetric MAC key of the External Account Binding. The `key` is the index string that is paired with the key data in the Secret and should not be confused with the key data itself, or indeed with the External Account Binding keyID above. The secret key stored in the Secret **must** be un-padded, base64 URL encoded data.
    """
    keyAlgorithm: Literal['HS256', 'HS384', 'HS512'] = attr.ib(metadata={
        'yaml_name': 'keyAlgorithm'})
    keyID: str = attr.ib(metadata={'yaml_name': 'keyID'})
    keySecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'keySecretRef'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmePrivateKeySecretRef(K8sObjectBase):
    """
    | PrivateKey is the name of a secret containing the private key for this user account.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Acmedns(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderAcmeDNS is a structure containing the configuration for ACME-DNS servers
    
    :param accountSecretRef: None
    :param host: None
    """
    accountSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'accountSecretRef'})
    host: str = attr.ib(metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRef(K8sObjectBase
    ):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Akamai(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderAkamai is a structure containing the DNS configuration for Akamai DNS—Zone Record Management API
    
    :param accessTokenSecretRef: None
    :param clientSecretSecretRef: None
    :param clientTokenSecretRef: None
    :param serviceConsumerDomain: None
    """
    accessTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'accessTokenSecretRef'})
    clientSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'clientSecretSecretRef'})
    clientTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'clientTokenSecretRef'})
    serviceConsumerDomain: str = attr.ib(metadata={'yaml_name':
        'serviceConsumerDomain'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRef(
    K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Azuredns(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderAzureDNS is a structure containing the configuration for Azure DNS
    
    :param clientID: None
    :param clientSecretSecretRef: None
    :param resourceGroupName: None
    :param subscriptionID: None
    :param tenantID: None
    :param environment: None
    :param hostedZoneName: None
    """
    clientID: str = attr.ib(metadata={'yaml_name': 'clientID'})
    clientSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'clientSecretSecretRef'})
    resourceGroupName: str = attr.ib(metadata={'yaml_name':
        'resourceGroupName'})
    subscriptionID: str = attr.ib(metadata={'yaml_name': 'subscriptionID'})
    tenantID: str = attr.ib(metadata={'yaml_name': 'tenantID'})
    environment: Optional[Literal['AzurePublicCloud', 'AzureChinaCloud',
        'AzureGermanCloud', 'AzureUSGovernmentCloud']] = attr.ib(default=
        None, metadata={'yaml_name': 'environment'})
    hostedZoneName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'hostedZoneName'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRef(
    K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Clouddns(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderCloudDNS is a structure containing the DNS configuration for Google Cloud DNS
    
    :param project: None
    :param serviceAccountSecretRef: None
    """
    project: str = attr.ib(metadata={'yaml_name': 'project'})
    serviceAccountSecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'serviceAccountSecretRef'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRef(K8sObjectBase
    ):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Cloudflare(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderCloudflare is a structure containing the DNS configuration for Cloudflare
    
    :param email: None
    :param apiKeySecretRef: None
    :param apiTokenSecretRef: None
    """
    email: str = attr.ib(metadata={'yaml_name': 'email'})
    apiKeySecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'apiKeySecretRef'})
    apiTokenSecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'apiTokenSecretRef'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Digitalocean(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderDigitalOcean is a structure containing the DNS configuration for DigitalOcean Domains
    
    :param tokenSecretRef: None
    """
    tokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'tokenSecretRef'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRef(K8sObjectBase):
    """
    | The name of the secret containing the TSIG value. If ``tsigKeyName`` is defined, this field is required.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Rfc2136(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderRFC2136 is a structure containing the configuration for RFC2136 DNS
    
    :param nameserver: The IP address of the DNS supporting RFC2136. Required. Note: FQDN is not a valid value, only IP.
    :param tsigAlgorithm: The TSIG Algorithm configured in the DNS supporting RFC2136. Used only when ``tsigSecretSecretRef`` and ``tsigKeyName`` are defined. Supported values are (case-insensitive): ``HMACMD5`` (default), ``HMACSHA1``, ``HMACSHA256`` or ``HMACSHA512``.
    :param tsigKeyName: The TSIG Key name configured in the DNS. If ``tsigSecretSecretRef`` is defined, this field is required.
    :param tsigSecretSecretRef: The name of the secret containing the TSIG value. If ``tsigKeyName`` is defined, this field is required.
    """
    nameserver: str = attr.ib(metadata={'yaml_name': 'nameserver'})
    tsigAlgorithm: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'tsigAlgorithm'})
    tsigKeyName: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'tsigKeyName'})
    tsigSecretSecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'tsigSecretSecretRef'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRef(
    K8sObjectBase):
    """
    | The SecretAccessKey is used for authentication. If not set we fall-back to using env vars, shared credentials file or AWS Instance metadata https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Route53(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderRoute53 is a structure containing the Route 53 configuration for AWS
    
    :param region: Always set the region when using AccessKeyID and SecretAccessKey
    :param accessKeyID: The AccessKeyID is used for authentication. If not set we fall-back to using env vars, shared credentials file or AWS Instance metadata see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
    :param hostedZoneID: If set, the provider will manage only this zone in Route53 and will not do an lookup using the route53:ListHostedZonesByName api call.
    :param role: Role is a Role ARN which the Route53 provider will assume using either the explicit credentials AccessKeyID/SecretAccessKey or the inferred credentials from environment variables, shared credentials file or AWS Instance metadata
    :param secretAccessKeySecretRef: The SecretAccessKey is used for authentication. If not set we fall-back to using env vars, shared credentials file or AWS Instance metadata https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
    """
    region: str = attr.ib(metadata={'yaml_name': 'region'})
    accessKeyID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'accessKeyID'})
    hostedZoneID: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'hostedZoneID'})
    role: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'role'})
    secretAccessKeySecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'secretAccessKeySecretRef'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01Webhook(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderWebhook specifies configuration for a webhook DNS01 provider, including where to POST ChallengePayload resources.
    
    :param groupName: The API group name that should be used when POSTing ChallengePayload resources to the webhook apiserver. This should be the same as the GroupName specified in the webhook provider implementation.
    :param solverName: The name of the solver to use, as defined in the webhook provider implementation. This will typically be the name of the provider, e.g. 'cloudflare'.
    :param config: Additional configuration that should be passed to the webhook apiserver when challenges are processed. This can contain arbitrary JSON data. Secret values should not be specified in this stanza. If secret values are needed (e.g. credentials for a DNS service), you should use a SecretKeySelector to reference a Secret resource. For details on the schema of this field, consult the webhook provider implementation's documentation.
    """
    groupName: str = attr.ib(metadata={'yaml_name': 'groupName'})
    solverName: str = attr.ib(metadata={'yaml_name': 'solverName'})
    config: Optional[Any] = attr.ib(default=None, metadata={'yaml_name':
        'config'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayDns01(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01
    
    :param acmedns: ACMEIssuerDNS01ProviderAcmeDNS is a structure containing the configuration for ACME-DNS servers
    :param akamai: ACMEIssuerDNS01ProviderAkamai is a structure containing the DNS configuration for Akamai DNS—Zone Record Management API
    :param azuredns: ACMEIssuerDNS01ProviderAzureDNS is a structure containing the configuration for Azure DNS
    :param clouddns: ACMEIssuerDNS01ProviderCloudDNS is a structure containing the DNS configuration for Google Cloud DNS
    :param cloudflare: ACMEIssuerDNS01ProviderCloudflare is a structure containing the DNS configuration for Cloudflare
    :param cnameStrategy: CNAMEStrategy configures how the DNS01 provider should handle CNAME records when found in DNS zones.
    :param digitalocean: ACMEIssuerDNS01ProviderDigitalOcean is a structure containing the DNS configuration for DigitalOcean Domains
    :param rfc2136: ACMEIssuerDNS01ProviderRFC2136 is a structure containing the configuration for RFC2136 DNS
    :param route53: ACMEIssuerDNS01ProviderRoute53 is a structure containing the Route 53 configuration for AWS
    :param webhook: ACMEIssuerDNS01ProviderWebhook specifies configuration for a webhook DNS01 provider, including where to POST ChallengePayload resources.
    """
    acmedns: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Acmedns,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AcmednsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'acmedns'})
    akamai: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Akamai,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'akamai'})
    azuredns: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Azuredns,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AzurednsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'azuredns'})
    clouddns: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Clouddns,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01ClouddnsTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'clouddns'})
    cloudflare: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Cloudflare,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'cloudflare'})
    cnameStrategy: Optional[Literal['None', 'Follow']] = attr.ib(default=
        None, metadata={'yaml_name': 'cnameStrategy'})
    digitalocean: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Digitalocean,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01DigitaloceanTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'digitalocean'})
    rfc2136: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Rfc2136,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Rfc2136TypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'rfc2136'})
    route53: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Route53,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Route53TypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'route53'})
    webhook: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Webhook,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01WebhookTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'webhook'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateMetadata(K8sObjectBase
    ):
    """
    | ObjectMeta overrides for the pod used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.
    
    :param annotations: Annotations that should be added to the create ACME HTTP01 solver pods.
    :param labels: Labels that should be added to the created ACME HTTP01 solver pods.
    """
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'annotations'})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': 'labels'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray(
    K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference(
    K8sObjectBase):
    """
    | A node selector term, associated with the corresponding weight.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArray(
    K8sObjectBase):
    """
    | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
    
    :param preference: A node selector term, associated with the corresponding weight.
    :param weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.
    """
    preference: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ] = attr.ib(metadata={'yaml_name': 'preference'})
    weight: int = attr.ib(metadata={'yaml_name': 'weight'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray(
    K8sObjectBase):
    """
    | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    
    :param key: The label key that the selector applies to.
    :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    operator: str = attr.ib(metadata={'yaml_name': 'operator'})
    values: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'values'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray(
    K8sObjectBase):
    """
    | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(
    K8sObjectBase):
    """
    | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    
    :param nodeSelectorTerms: Required. A list of node selector terms. The terms are ORed.
    """
    nodeSelectorTerms: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]] = attr.ib(metadata={'yaml_name': 'nodeSelectorTerms'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinity(
    K8sObjectBase):
    """
    | Describes node affinity scheduling rules for the pod.
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray(
    K8sObjectBase):
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
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTerm(
    K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray(
    K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray(
    K8sObjectBase):
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
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinity(
    K8sObjectBase):
    """
    | Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray(
    K8sObjectBase):
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
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTerm(
    K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray(
    K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray(
    K8sObjectBase):
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
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinity(
    K8sObjectBase):
    """
    | Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinity(
    K8sObjectBase):
    """
    | If specified, the pod's scheduling constraints
    
    :param nodeAffinity: Describes node affinity scheduling rules for the pod.
    :param podAffinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    :param podAntiAffinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    """
    nodeAffinity: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinity
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'nodeAffinity'})
    podAffinity: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinity
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podAffinity'})
    podAntiAffinity: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinity
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podAntiAffinity'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArray(K8sObjectBase
    ):
    """
    | The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.
    
    :param effect: Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.
    :param key: Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.
    :param operator: Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.
    :param tolerationSeconds: TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.
    :param value: Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.
    """
    effect: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'effect'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})
    operator: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'operator'})
    tolerationSeconds: Optional[int] = attr.ib(default=None, metadata={
        'yaml_name': 'tolerationSeconds'})
    value: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'value'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpec(K8sObjectBase):
    """
    | PodSpec defines overrides for the HTTP01 challenge solver pod. Only the 'nodeSelector', 'affinity' and 'tolerations' fields are supported currently. All other fields will be ignored.
    
    :param affinity: If specified, the pod's scheduling constraints
    :param nodeSelector: NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
    :param tolerations: If specified, the pod's tolerations.
    """
    affinity: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinity
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'affinity'})
    nodeSelector: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeSelector'})
    tolerations: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'tolerations'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplate(K8sObjectBase):
    """
    | Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges
    
    :param metadata: ObjectMeta overrides for the pod used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.
    :param spec: PodSpec defines overrides for the HTTP01 challenge solver pod. Only the 'nodeSelector', 'affinity' and 'tolerations' fields are supported currently. All other fields will be ignored.
    """
    metadata: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateMetadata
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateMetadataTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'metadata'})
    spec: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpec
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01Ingress(K8sObjectBase):
    """
    | The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.
    
    :param class_: The ingress class to use when creating Ingress resources to solve ACME challenges that use this challenge solver. Only one of 'class' or 'name' may be specified.
    :param name: The name of the ingress resource that should have ACME challenge solving routes inserted into it in order to solve HTTP01 challenges. This is typically used in conjunction with ingress controllers like ingress-gce, which maintains a 1:1 mapping between external IPs and ingress resources.
    :param podTemplate: Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges
    :param serviceType: Optional service type for Kubernetes solver service
    """
    class_: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'class'})
    name: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'name'})
    podTemplate: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplate
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podTemplate'})
    serviceType: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'serviceType'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArrayHttp01(K8sObjectBase):
    """
    | ACMEChallengeSolverHTTP01 contains configuration detailing how to solve HTTP01 challenges within a Kubernetes cluster. Typically this is accomplished through creating 'routes' of some description that configure ingress controllers to direct traffic to 'solver pods', which are responsible for responding to the ACME server's HTTP requests.
    
    :param ingress: The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.
    """
    ingress: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01Ingress,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'ingress'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArraySelector(K8sObjectBase):
    """
    | Selector selects a set of DNSNames on the Certificate resource that should be solved using this challenge solver.
    
    :param dnsNames: List of DNSNames that this solver will be used to solve. If specified and a match is found, a dnsNames selector will take precedence over a dnsZones selector. If multiple solvers match with the same dnsNames value, the solver with the most matching labels in matchLabels will be selected. If neither has more matches, the solver defined earlier in the list will be selected.
    :param dnsZones: List of DNSZones that this solver will be used to solve. The most specific DNS zone match specified here will take precedence over other DNS zone matches, so a solver specifying sys.example.com will be selected over one specifying example.com for the domain www.sys.example.com. If multiple solvers match with the same dnsZones value, the solver with the most matching labels in matchLabels will be selected. If neither has more matches, the solver defined earlier in the list will be selected.
    :param matchLabels: A label selector that is used to refine the set of certificate's that this challenge solver will apply to.
    """
    dnsNames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'dnsNames'})
    dnsZones: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'dnsZones'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcmeArray(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecAcmeArray
    
    :param dns01: None
    :param http01: ACMEChallengeSolverHTTP01 contains configuration detailing how to solve HTTP01 challenges within a Kubernetes cluster. Typically this is accomplished through creating 'routes' of some description that configure ingress controllers to direct traffic to 'solver pods', which are responsible for responding to the ACME server's HTTP requests.
    :param selector: Selector selects a set of DNSNames on the Certificate resource that should be solved using this challenge solver.
    """
    dns01: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01TypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'dns01'})
    http01: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01TypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'http01'})
    selector: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArraySelector,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArraySelectorTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'selector'})


@attr.s(kw_only=True)
class ClusterIssuerSpecAcme(K8sObjectBase):
    """
    | ACMEIssuer contains the specification for an ACME issuer
    
    :param privateKeySecretRef: PrivateKey is the name of a secret containing the private key for this user account.
    :param server: Server is the ACME server URL
    :param email: Email is the email for this account
    :param externalAccountBinding: ExternalAcccountBinding is a reference to a CA external account of the ACME server.
    :param skipTLSVerify: If true, skip verifying the ACME server TLS certificate
    :param solvers: Solvers is a list of challenge solvers that will be used to solve ACME challenges for the matching domains.
    """
    privateKeySecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmePrivateKeySecretRef,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmePrivateKeySecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'privateKeySecretRef'})
    server: str = attr.ib(metadata={'yaml_name': 'server'})
    email: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'email'})
    externalAccountBinding: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeExternalAccountBinding,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeExternalAccountBindingTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'externalAccountBinding'})
    skipTLSVerify: Optional[bool] = attr.ib(default=None, metadata={
        'yaml_name': 'skipTLSVerify'})
    solvers: Optional[Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArray,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayTypedDict]]
        ] = attr.ib(default=None, metadata={'yaml_name': 'solvers'})


@attr.s(kw_only=True)
class ClusterIssuerSpecCa(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecCa
    
    :param secretName: SecretName is the name of the secret used to sign Certificates issued by this Issuer.
    """
    secretName: str = attr.ib(metadata={'yaml_name': 'secretName'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVaultAuthAppRoleSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecVaultAuthAppRoleSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVaultAuthAppRole(K8sObjectBase):
    """
    | This Secret contains a AppRole and Secret
    
    :param path: Where the authentication path is mounted in Vault.
    :param roleId: None
    :param secretRef: None
    """
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    roleId: str = attr.ib(metadata={'yaml_name': 'roleId'})
    secretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthAppRoleSecretRef,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthAppRoleSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'secretRef'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVaultAuthKubernetesSecretRef(K8sObjectBase):
    """
    | The required Secret field containing a Kubernetes ServiceAccount JWT used for authenticating with Vault. Use of 'ambient credentials' is not supported.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVaultAuthKubernetes(K8sObjectBase):
    """
    | This contains a Role and Secret with a ServiceAccount token to authenticate with vault.
    
    :param role: A required field containing the Vault Role to assume. A Role binds a Kubernetes ServiceAccount with a set of Vault policies.
    :param secretRef: The required Secret field containing a Kubernetes ServiceAccount JWT used for authenticating with Vault. Use of 'ambient credentials' is not supported.
    :param mountPath: The Vault mountPath here is the mount path to use when authenticating with Vault. For example, setting a value to `/v1/auth/foo`, will use the path `/v1/auth/foo/login` to authenticate with Vault. If unspecified, the default value "/v1/auth/kubernetes" will be used.
    """
    role: str = attr.ib(metadata={'yaml_name': 'role'})
    secretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthKubernetesSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthKubernetesSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'secretRef'})
    mountPath: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'mountPath'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVaultAuthTokenSecretRef(K8sObjectBase):
    """
    | This Secret contains the Vault token key
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVaultAuth(K8sObjectBase):
    """
    | Vault authentication
    
    :param appRole: This Secret contains a AppRole and Secret
    :param kubernetes: This contains a Role and Secret with a ServiceAccount token to authenticate with vault.
    :param tokenSecretRef: This Secret contains the Vault token key
    """
    appRole: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthAppRole,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthAppRoleTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'appRole'})
    kubernetes: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthKubernetes,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthKubernetesTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'kubernetes'})
    tokenSecretRef: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthTokenSecretRef,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthTokenSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'tokenSecretRef'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVault(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuerSpecVault
    
    :param auth: Vault authentication
    :param path: Vault URL path to the certificate role
    :param server: Server is the vault connection address
    :param caBundle: Base64 encoded CA bundle to validate Vault server certificate. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. If not set the system root certificates are used to validate the TLS connection.
    """
    auth: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuth,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthTypedDict
        ] = attr.ib(metadata={'yaml_name': 'auth'})
    path: str = attr.ib(metadata={'yaml_name': 'path'})
    server: str = attr.ib(metadata={'yaml_name': 'server'})
    caBundle: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caBundle'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVenafiCloudApiTokenSecretRef(K8sObjectBase):
    """
    | APITokenSecretRef is a secret key selector for the Venafi Cloud API token.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVenafiCloud(K8sObjectBase):
    """
    | Cloud specifies the Venafi cloud configuration settings. Only one of TPP or Cloud may be specified.
    
    :param apiTokenSecretRef: APITokenSecretRef is a secret key selector for the Venafi Cloud API token.
    :param url: URL is the base URL for Venafi Cloud
    """
    apiTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiCloudApiTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiCloudApiTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'apiTokenSecretRef'})
    url: str = attr.ib(metadata={'yaml_name': 'url'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVenafiTppCredentialsRef(K8sObjectBase):
    """
    | CredentialsRef is a reference to a Secret containing the username and password for the TPP server. The secret must contain two keys, 'username' and 'password'.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVenafiTpp(K8sObjectBase):
    """
    | TPP specifies Trust Protection Platform configuration settings. Only one of TPP or Cloud may be specified.
    
    :param credentialsRef: CredentialsRef is a reference to a Secret containing the username and password for the TPP server. The secret must contain two keys, 'username' and 'password'.
    :param url: URL is the base URL for the Venafi TPP instance
    :param caBundle: CABundle is a PEM encoded TLS certifiate to use to verify connections to the TPP instance. If specified, system roots will not be used and the issuing CA for the TPP instance must be verifiable using the provided root. If not specified, the connection will be verified using the cert-manager system root certificates.
    """
    credentialsRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTppCredentialsRef,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTppCredentialsRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'credentialsRef'})
    url: str = attr.ib(metadata={'yaml_name': 'url'})
    caBundle: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'caBundle'})


@attr.s(kw_only=True)
class ClusterIssuerSpecVenafi(K8sObjectBase):
    """
    | VenafiIssuer describes issuer configuration details for Venafi Cloud.
    
    :param zone: Zone is the Venafi Policy Zone to use for this issuer. All requests made to the Venafi platform will be restricted by the named zone policy. This field is required.
    :param cloud: Cloud specifies the Venafi cloud configuration settings. Only one of TPP or Cloud may be specified.
    :param tpp: TPP specifies Trust Protection Platform configuration settings. Only one of TPP or Cloud may be specified.
    """
    zone: str = attr.ib(metadata={'yaml_name': 'zone'})
    cloud: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiCloud,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiCloudTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'cloud'})
    tpp: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTpp,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTppTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'tpp'})


@attr.s(kw_only=True)
class ClusterIssuerSpec(K8sObjectBase):
    """
    | IssuerSpec is the specification of an Issuer. This includes any configuration required for the issuer.
    
    :param acme: ACMEIssuer contains the specification for an ACME issuer
    :param ca: None
    :param selfSigned: None
    :param vault: None
    :param venafi: VenafiIssuer describes issuer configuration details for Venafi Cloud.
    """
    acme: Optional[Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcme,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'acme'})
    ca: Optional[Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecCa,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecCaTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'ca'})
    selfSigned: Optional[Mapping[str, Any]] = attr.ib(default=None,
        metadata={'yaml_name': 'selfSigned'})
    vault: Optional[Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecVault,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'vault'})
    venafi: Optional[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafi,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'venafi'})


@attr.s(kw_only=True)
class ClusterIssuer(K8sResourceBase):
    """
    | Kubernates API object: io.cert-manager.v1alpha2.ClusterIssuer
    
    :param name: metadata.name
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: IssuerSpec is the specification of an Issuer. This includes any configuration required for the issuer.
    """
    apiVersion: ClassVar[str] = 'cert-manager.io/v1alpha2'
    kind: ClassVar[str] = 'ClusterIssuer'
    name: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpec,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class CertificateRequestSpecIssuerRef(K8sObjectBase):
    """
    | IssuerRef is a reference to the issuer for this CertificateRequest.  If the 'kind' field is not set, or set to 'Issuer', an Issuer resource with the given name in the same namespace as the CertificateRequest will be used.  If the 'kind' field is set to 'ClusterIssuer', a ClusterIssuer with the provided name will be used. The 'name' field in this stanza is required at all times. The group field refers to the API group of the issuer which defaults to 'cert-manager.io' if empty.
    
    :param name: None
    :param group: None
    :param kind: None
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})


@attr.s(kw_only=True)
class CertificateRequestSpec(K8sObjectBase):
    """
    | CertificateRequestSpec defines the desired state of CertificateRequest
    
    :param csr: Byte slice containing the PEM encoded CertificateSigningRequest
    :param issuerRef: IssuerRef is a reference to the issuer for this CertificateRequest.  If the 'kind' field is not set, or set to 'Issuer', an Issuer resource with the given name in the same namespace as the CertificateRequest will be used.  If the 'kind' field is set to 'ClusterIssuer', a ClusterIssuer with the provided name will be used. The 'name' field in this stanza is required at all times. The group field refers to the API group of the issuer which defaults to 'cert-manager.io' if empty.
    :param duration: Requested certificate default Duration
    :param isCA: IsCA will mark the resulting certificate as valid for signing. This implies that the 'cert sign' usage is set
    :param usages: Usages is the set of x509 actions that are enabled for a given key. Defaults are ('digital signature', 'key encipherment') if empty
    """
    csr: str = attr.ib(metadata={'yaml_name': 'csr'})
    issuerRef: Union[
        kdsl.certmanager.v1alpha2.CertificateRequestSpecIssuerRef,
        kdsl.certmanager.v1alpha2.CertificateRequestSpecIssuerRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'issuerRef'})
    duration: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'duration'})
    isCA: Optional[bool] = attr.ib(default=None, metadata={'yaml_name': 'isCA'}
        )
    usages: Optional[Sequence[Literal['signing', 'digital signature',
        'content commitment', 'key encipherment', 'key agreement',
        'data encipherment', 'cert sign', 'crl sign', 'encipher only',
        'decipher only', 'any', 'server auth', 'client auth',
        'code signing', 'email protection', 's/mime', 'ipsec end system',
        'ipsec tunnel', 'ipsec user', 'timestamping', 'ocsp signing',
        'microsoft sgc', 'netscape sgc']]] = attr.ib(default=None, metadata
        ={'yaml_name': 'usages'})


@attr.s(kw_only=True)
class CertificateRequest(K8sResourceBase):
    """
    | CertificateRequest is a type to represent a Certificate Signing Request
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: CertificateRequestSpec defines the desired state of CertificateRequest
    """
    apiVersion: ClassVar[str] = 'cert-manager.io/v1alpha2'
    kind: ClassVar[str] = 'CertificateRequest'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.certmanager.v1alpha2.CertificateRequestSpec,
        kdsl.certmanager.v1alpha2.CertificateRequestSpecTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class CertificateSpecIssuerRef(K8sObjectBase):
    """
    | IssuerRef is a reference to the issuer for this certificate. If the 'kind' field is not set, or set to 'Issuer', an Issuer resource with the given name in the same namespace as the Certificate will be used. If the 'kind' field is set to 'ClusterIssuer', a ClusterIssuer with the provided name will be used. The 'name' field in this stanza is required at all times.
    
    :param name: None
    :param group: None
    :param kind: None
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})


@attr.s(kw_only=True)
class CertificateSpecSubject(K8sObjectBase):
    """
    | Full X509 name specification (https://golang.org/pkg/crypto/x509/pkix/#Name).
    
    :param countries: Countries to be used on the Certificate.
    :param localities: Cities to be used on the Certificate.
    :param organizationalUnits: Organizational Units to be used on the Certificate.
    :param postalCodes: Postal codes to be used on the Certificate.
    :param provinces: State/Provinces to be used on the Certificate.
    :param serialNumber: Serial number to be used on the Certificate.
    :param streetAddresses: Street addresses to be used on the Certificate.
    """
    countries: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'countries'})
    localities: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'localities'})
    organizationalUnits: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'organizationalUnits'})
    postalCodes: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'postalCodes'})
    provinces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'provinces'})
    serialNumber: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'serialNumber'})
    streetAddresses: Optional[Sequence[str]] = attr.ib(default=None,
        metadata={'yaml_name': 'streetAddresses'})


@attr.s(kw_only=True)
class CertificateSpec(K8sObjectBase):
    """
    | CertificateSpec defines the desired state of Certificate. A valid Certificate requires at least one of a CommonName, DNSName, or URISAN to be valid.
    
    :param issuerRef: IssuerRef is a reference to the issuer for this certificate. If the 'kind' field is not set, or set to 'Issuer', an Issuer resource with the given name in the same namespace as the Certificate will be used. If the 'kind' field is set to 'ClusterIssuer', a ClusterIssuer with the provided name will be used. The 'name' field in this stanza is required at all times.
    :param secretName: SecretName is the name of the secret resource to store this secret in
    :param commonName: CommonName is a common name to be used on the Certificate. The CommonName should have a length of 64 characters or fewer to avoid generating invalid CSRs.
    :param dnsNames: DNSNames is a list of subject alt names to be used on the Certificate.
    :param duration: Certificate default Duration
    :param ipAddresses: IPAddresses is a list of IP addresses to be used on the Certificate
    :param isCA: IsCA will mark this Certificate as valid for signing. This implies that the 'cert sign' usage is set
    :param keyAlgorithm: KeyAlgorithm is the private key algorithm of the corresponding private key for this certificate. If provided, allowed values are either "rsa" or "ecdsa" If KeyAlgorithm is specified and KeySize is not provided, key size of 256 will be used for "ecdsa" key algorithm and key size of 2048 will be used for "rsa" key algorithm.
    :param keyEncoding: KeyEncoding is the private key cryptography standards (PKCS) for this certificate's private key to be encoded in. If provided, allowed values are "pkcs1" and "pkcs8" standing for PKCS#1 and PKCS#8, respectively. If KeyEncoding is not specified, then PKCS#1 will be used by default.
    :param keySize: KeySize is the key bit size of the corresponding private key for this certificate. If provided, value must be between 2048 and 8192 inclusive when KeyAlgorithm is empty or is set to "rsa", and value must be one of (256, 384, 521) when KeyAlgorithm is set to "ecdsa".
    :param organization: Organization is the organization to be used on the Certificate
    :param renewBefore: Certificate renew before expiration duration
    :param subject: Full X509 name specification (https://golang.org/pkg/crypto/x509/pkix/#Name).
    :param uriSANs: URISANs is a list of URI Subject Alternative Names to be set on this Certificate.
    :param usages: Usages is the set of x509 actions that are enabled for a given key. Defaults are ('digital signature', 'key encipherment') if empty
    """
    issuerRef: Union[kdsl.certmanager.v1alpha2.CertificateSpecIssuerRef,
        kdsl.certmanager.v1alpha2.CertificateSpecIssuerRefTypedDict] = attr.ib(
        metadata={'yaml_name': 'issuerRef'})
    secretName: str = attr.ib(metadata={'yaml_name': 'secretName'})
    commonName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'commonName'})
    dnsNames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'dnsNames'})
    duration: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'duration'})
    ipAddresses: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'ipAddresses'})
    isCA: Optional[bool] = attr.ib(default=None, metadata={'yaml_name': 'isCA'}
        )
    keyAlgorithm: Optional[Literal['rsa', 'ecdsa']] = attr.ib(default=None,
        metadata={'yaml_name': 'keyAlgorithm'})
    keyEncoding: Optional[Literal['pkcs1', 'pkcs8']] = attr.ib(default=None,
        metadata={'yaml_name': 'keyEncoding'})
    keySize: Optional[int] = attr.ib(default=None, metadata={'yaml_name':
        'keySize'})
    organization: Optional[Sequence[str]] = attr.ib(default=None, metadata=
        {'yaml_name': 'organization'})
    renewBefore: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'renewBefore'})
    subject: Optional[Union[
        kdsl.certmanager.v1alpha2.CertificateSpecSubject,
        kdsl.certmanager.v1alpha2.CertificateSpecSubjectTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'subject'})
    uriSANs: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'uriSANs'})
    usages: Optional[Sequence[Literal['signing', 'digital signature',
        'content commitment', 'key encipherment', 'key agreement',
        'data encipherment', 'cert sign', 'crl sign', 'encipher only',
        'decipher only', 'any', 'server auth', 'client auth',
        'code signing', 'email protection', 's/mime', 'ipsec end system',
        'ipsec tunnel', 'ipsec user', 'timestamping', 'ocsp signing',
        'microsoft sgc', 'netscape sgc']]] = attr.ib(default=None, metadata
        ={'yaml_name': 'usages'})


@attr.s(kw_only=True)
class Certificate(K8sResourceBase):
    """
    | Certificate is a type to represent a Certificate from ACME
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: CertificateSpec defines the desired state of Certificate. A valid Certificate requires at least one of a CommonName, DNSName, or URISAN to be valid.
    """
    apiVersion: ClassVar[str] = 'cert-manager.io/v1alpha2'
    kind: ClassVar[str] = 'Certificate'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.certmanager.v1alpha2.CertificateSpec,
        kdsl.certmanager.v1alpha2.CertificateSpecTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'spec'})


class IssuerSpecAcmeExternalAccountBindingKeySecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeExternalAccountBindingKeySecretRefTypedDict(
    IssuerSpecAcmeExternalAccountBindingKeySecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeExternalAccountBindingTypedDict(TypedDict, total=(True)):
    keyAlgorithm: Literal['HS256', 'HS384', 'HS512']
    keyID: str
    keySecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeExternalAccountBindingKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeExternalAccountBindingKeySecretRefTypedDict
        ]


class IssuerSpecAcmePrivateKeySecretRefOptionalTypedDict(TypedDict, total=(
    False)):
    key: str


class IssuerSpecAcmePrivateKeySecretRefTypedDict(
    IssuerSpecAcmePrivateKeySecretRefOptionalTypedDict, total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01AcmednsAccountSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01AcmednsAccountSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01AcmednsAccountSecretRefOptionalTypedDict, total
    =(True)):
    name: str


class IssuerSpecAcmeArrayDns01AcmednsTypedDict(TypedDict, total=(True)):
    accountSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AcmednsAccountSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AcmednsAccountSecretRefTypedDict
        ]
    host: str


class IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01AkamaiTypedDict(TypedDict, total=(True)):
    accessTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefTypedDict
        ]
    clientSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefTypedDict
        ]
    clientTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefTypedDict
        ]
    serviceConsumerDomain: str


class IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01AzurednsOptionalTypedDict(TypedDict, total=(
    False)):
    environment: Literal['AzurePublicCloud', 'AzureChinaCloud',
        'AzureGermanCloud', 'AzureUSGovernmentCloud']
    hostedZoneName: str


class IssuerSpecAcmeArrayDns01AzurednsTypedDict(
    IssuerSpecAcmeArrayDns01AzurednsOptionalTypedDict, total=(True)):
    clientID: str
    clientSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefTypedDict
        ]
    resourceGroupName: str
    subscriptionID: str
    tenantID: str


class IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01ClouddnsOptionalTypedDict(TypedDict, total=(
    False)):
    serviceAccountSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefTypedDict
        ]


class IssuerSpecAcmeArrayDns01ClouddnsTypedDict(
    IssuerSpecAcmeArrayDns01ClouddnsOptionalTypedDict, total=(True)):
    project: str


class IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefTypedDict(
    IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01CloudflareOptionalTypedDict(TypedDict, total=
    (False)):
    apiKeySecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefTypedDict
        ]
    apiTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefTypedDict
        ]


class IssuerSpecAcmeArrayDns01CloudflareTypedDict(
    IssuerSpecAcmeArrayDns01CloudflareOptionalTypedDict, total=(True)):
    email: str


class IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01DigitaloceanTypedDict(TypedDict, total=(True)):
    tokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefTypedDict
        ]


class IssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefTypedDict(
    IssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01Rfc2136OptionalTypedDict(TypedDict, total=(False)
    ):
    tsigAlgorithm: str
    tsigKeyName: str
    tsigSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefTypedDict
        ]


class IssuerSpecAcmeArrayDns01Rfc2136TypedDict(
    IssuerSpecAcmeArrayDns01Rfc2136OptionalTypedDict, total=(True)):
    nameserver: str


class IssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class IssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefTypedDict(
    IssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefOptionalTypedDict,
    total=(True)):
    name: str


class IssuerSpecAcmeArrayDns01Route53OptionalTypedDict(TypedDict, total=(False)
    ):
    accessKeyID: str
    hostedZoneID: str
    role: str
    secretAccessKeySecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefTypedDict
        ]


class IssuerSpecAcmeArrayDns01Route53TypedDict(
    IssuerSpecAcmeArrayDns01Route53OptionalTypedDict, total=(True)):
    region: str


class IssuerSpecAcmeArrayDns01WebhookOptionalTypedDict(TypedDict, total=(False)
    ):
    config: Any


class IssuerSpecAcmeArrayDns01WebhookTypedDict(
    IssuerSpecAcmeArrayDns01WebhookOptionalTypedDict, total=(True)):
    groupName: str
    solverName: str


class IssuerSpecAcmeArrayDns01TypedDict(TypedDict, total=(False)):
    acmedns: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Acmedns,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AcmednsTypedDict]
    akamai: Union[kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Akamai,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AkamaiTypedDict]
    azuredns: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Azuredns,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01AzurednsTypedDict]
    clouddns: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Clouddns,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01ClouddnsTypedDict]
    cloudflare: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Cloudflare,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01CloudflareTypedDict]
    cnameStrategy: Literal['None', 'Follow']
    digitalocean: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Digitalocean,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01DigitaloceanTypedDict
        ]
    rfc2136: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Rfc2136,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Rfc2136TypedDict]
    route53: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Route53,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Route53TypedDict]
    webhook: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01Webhook,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01WebhookTypedDict]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateMetadataTypedDict(TypedDict,
    total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict(
    TypedDict, total=(True)):
    preference: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ]
    weight: int


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict(
    TypedDict, total=(True)):
    nodeSelectorTerms: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict
    , total=(True)):
    topologyKey: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayOptionalTypedDict
    , total=(True)):
    topologyKey: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict
    , total=(True)):
    topologyKey: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayOptionalTypedDict
    , total=(True)):
    topologyKey: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict(
    IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityTypedDict(
    TypedDict, total=(False)):
    nodeAffinity: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinity
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict
        ]
    podAffinity: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinity
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict
        ]
    podAntiAffinity: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinity
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict
        ]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArrayTypedDict(TypedDict,
    total=(False)):
    effect: str
    key: str
    operator: str
    tolerationSeconds: int
    value: str


class IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecTypedDict(TypedDict,
    total=(False)):
    affinity: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinity
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityTypedDict
        ]
    nodeSelector: Mapping[str, str]
    tolerations: Sequence[Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArray
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArrayTypedDict
        ]]


class IssuerSpecAcmeArrayHttp01IngressPodTemplateTypedDict(TypedDict, total
    =(False)):
    metadata: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateMetadata
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateMetadataTypedDict
        ]
    spec: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpec
        ,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateSpecTypedDict
        ]


class IssuerSpecAcmeArrayHttp01IngressTypedDict(TypedDict, total=(False)):
    class_: str
    name: str
    podTemplate: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplate,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressPodTemplateTypedDict
        ]
    serviceType: str


class IssuerSpecAcmeArrayHttp01TypedDict(TypedDict, total=(False)):
    ingress: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01Ingress,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01IngressTypedDict]


class IssuerSpecAcmeArraySelectorTypedDict(TypedDict, total=(False)):
    dnsNames: Sequence[str]
    dnsZones: Sequence[str]
    matchLabels: Mapping[str, str]


class IssuerSpecAcmeArrayTypedDict(TypedDict, total=(False)):
    dns01: Union[kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayDns01TypedDict]
    http01: Union[kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayHttp01TypedDict]
    selector: Union[kdsl.certmanager.v1alpha2.IssuerSpecAcmeArraySelector,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArraySelectorTypedDict]


class IssuerSpecAcmeOptionalTypedDict(TypedDict, total=(False)):
    email: str
    externalAccountBinding: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeExternalAccountBinding,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeExternalAccountBindingTypedDict
        ]
    skipTLSVerify: bool
    solvers: Sequence[Union[kdsl.certmanager.v1alpha2.IssuerSpecAcmeArray,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeArrayTypedDict]]


class IssuerSpecAcmeTypedDict(IssuerSpecAcmeOptionalTypedDict, total=(True)):
    privateKeySecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecAcmePrivateKeySecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmePrivateKeySecretRefTypedDict]
    server: str


class IssuerSpecCaTypedDict(TypedDict, total=(True)):
    secretName: str


class IssuerSpecVaultAuthAppRoleSecretRefOptionalTypedDict(TypedDict, total
    =(False)):
    key: str


class IssuerSpecVaultAuthAppRoleSecretRefTypedDict(
    IssuerSpecVaultAuthAppRoleSecretRefOptionalTypedDict, total=(True)):
    name: str


class IssuerSpecVaultAuthAppRoleTypedDict(TypedDict, total=(True)):
    path: str
    roleId: str
    secretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthAppRoleSecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthAppRoleSecretRefTypedDict]


class IssuerSpecVaultAuthKubernetesSecretRefOptionalTypedDict(TypedDict,
    total=(False)):
    key: str


class IssuerSpecVaultAuthKubernetesSecretRefTypedDict(
    IssuerSpecVaultAuthKubernetesSecretRefOptionalTypedDict, total=(True)):
    name: str


class IssuerSpecVaultAuthKubernetesOptionalTypedDict(TypedDict, total=(False)):
    mountPath: str


class IssuerSpecVaultAuthKubernetesTypedDict(
    IssuerSpecVaultAuthKubernetesOptionalTypedDict, total=(True)):
    role: str
    secretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthKubernetesSecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthKubernetesSecretRefTypedDict
        ]


class IssuerSpecVaultAuthTokenSecretRefOptionalTypedDict(TypedDict, total=(
    False)):
    key: str


class IssuerSpecVaultAuthTokenSecretRefTypedDict(
    IssuerSpecVaultAuthTokenSecretRefOptionalTypedDict, total=(True)):
    name: str


class IssuerSpecVaultAuthTypedDict(TypedDict, total=(False)):
    appRole: Union[kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthAppRole,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthAppRoleTypedDict]
    kubernetes: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthKubernetes,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthKubernetesTypedDict]
    tokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthTokenSecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthTokenSecretRefTypedDict]


class IssuerSpecVaultOptionalTypedDict(TypedDict, total=(False)):
    caBundle: str


class IssuerSpecVaultTypedDict(IssuerSpecVaultOptionalTypedDict, total=(True)):
    auth: Union[kdsl.certmanager.v1alpha2.IssuerSpecVaultAuth,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultAuthTypedDict]
    path: str
    server: str


class IssuerSpecVenafiCloudApiTokenSecretRefOptionalTypedDict(TypedDict,
    total=(False)):
    key: str


class IssuerSpecVenafiCloudApiTokenSecretRefTypedDict(
    IssuerSpecVenafiCloudApiTokenSecretRefOptionalTypedDict, total=(True)):
    name: str


class IssuerSpecVenafiCloudTypedDict(TypedDict, total=(True)):
    apiTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiCloudApiTokenSecretRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiCloudApiTokenSecretRefTypedDict
        ]
    url: str


class IssuerSpecVenafiTppCredentialsRefTypedDict(TypedDict, total=(True)):
    name: str


class IssuerSpecVenafiTppOptionalTypedDict(TypedDict, total=(False)):
    caBundle: str


class IssuerSpecVenafiTppTypedDict(IssuerSpecVenafiTppOptionalTypedDict,
    total=(True)):
    credentialsRef: Union[
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiTppCredentialsRef,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiTppCredentialsRefTypedDict]
    url: str


class IssuerSpecVenafiOptionalTypedDict(TypedDict, total=(False)):
    cloud: Union[kdsl.certmanager.v1alpha2.IssuerSpecVenafiCloud,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiCloudTypedDict]
    tpp: Union[kdsl.certmanager.v1alpha2.IssuerSpecVenafiTpp,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiTppTypedDict]


class IssuerSpecVenafiTypedDict(IssuerSpecVenafiOptionalTypedDict, total=(True)
    ):
    zone: str


class IssuerSpecTypedDict(TypedDict, total=(False)):
    acme: Union[kdsl.certmanager.v1alpha2.IssuerSpecAcme,
        kdsl.certmanager.v1alpha2.IssuerSpecAcmeTypedDict]
    ca: Union[kdsl.certmanager.v1alpha2.IssuerSpecCa,
        kdsl.certmanager.v1alpha2.IssuerSpecCaTypedDict]
    selfSigned: Mapping[str, Any]
    vault: Union[kdsl.certmanager.v1alpha2.IssuerSpecVault,
        kdsl.certmanager.v1alpha2.IssuerSpecVaultTypedDict]
    venafi: Union[kdsl.certmanager.v1alpha2.IssuerSpecVenafi,
        kdsl.certmanager.v1alpha2.IssuerSpecVenafiTypedDict]


class IssuerOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.certmanager.v1alpha2.IssuerSpec,
        kdsl.certmanager.v1alpha2.IssuerSpecTypedDict]


class IssuerTypedDict(IssuerOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRefTypedDict(
    ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ClusterIssuerSpecAcmeExternalAccountBindingTypedDict(TypedDict, total
    =(True)):
    keyAlgorithm: Literal['HS256', 'HS384', 'HS512']
    keyID: str
    keySecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeExternalAccountBindingKeySecretRefTypedDict
        ]


class ClusterIssuerSpecAcmePrivateKeySecretRefOptionalTypedDict(TypedDict,
    total=(False)):
    key: str


class ClusterIssuerSpecAcmePrivateKeySecretRefTypedDict(
    ClusterIssuerSpecAcmePrivateKeySecretRefOptionalTypedDict, total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01AcmednsTypedDict(TypedDict, total=(True)):
    accountSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AcmednsAccountSecretRefTypedDict
        ]
    host: str


class ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefOptionalTypedDict
    , total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01AkamaiTypedDict(TypedDict, total=(True)):
    accessTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiAccessTokenSecretRefTypedDict
        ]
    clientSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientSecretSecretRefTypedDict
        ]
    clientTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiClientTokenSecretRefTypedDict
        ]
    serviceConsumerDomain: str


class ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefOptionalTypedDict
    , total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01AzurednsOptionalTypedDict(TypedDict,
    total=(False)):
    environment: Literal['AzurePublicCloud', 'AzureChinaCloud',
        'AzureGermanCloud', 'AzureUSGovernmentCloud']
    hostedZoneName: str


class ClusterIssuerSpecAcmeArrayDns01AzurednsTypedDict(
    ClusterIssuerSpecAcmeArrayDns01AzurednsOptionalTypedDict, total=(True)):
    clientID: str
    clientSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AzurednsClientSecretSecretRefTypedDict
        ]
    resourceGroupName: str
    subscriptionID: str
    tenantID: str


class ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefOptionalTypedDict
    , total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01ClouddnsOptionalTypedDict(TypedDict,
    total=(False)):
    serviceAccountSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01ClouddnsServiceAccountSecretRefTypedDict
        ]


class ClusterIssuerSpecAcmeArrayDns01ClouddnsTypedDict(
    ClusterIssuerSpecAcmeArrayDns01ClouddnsOptionalTypedDict, total=(True)):
    project: str


class ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefOptionalTypedDict
    , total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01CloudflareOptionalTypedDict(TypedDict,
    total=(False)):
    apiKeySecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiKeySecretRefTypedDict
        ]
    apiTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareApiTokenSecretRefTypedDict
        ]


class ClusterIssuerSpecAcmeArrayDns01CloudflareTypedDict(
    ClusterIssuerSpecAcmeArrayDns01CloudflareOptionalTypedDict, total=(True)):
    email: str


class ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01DigitaloceanTypedDict(TypedDict, total
    =(True)):
    tokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01DigitaloceanTokenSecretRefTypedDict
        ]


class ClusterIssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01Rfc2136OptionalTypedDict(TypedDict,
    total=(False)):
    tsigAlgorithm: str
    tsigKeyName: str
    tsigSecretSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Rfc2136TsigSecretSecretRefTypedDict
        ]


class ClusterIssuerSpecAcmeArrayDns01Rfc2136TypedDict(
    ClusterIssuerSpecAcmeArrayDns01Rfc2136OptionalTypedDict, total=(True)):
    nameserver: str


class ClusterIssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ClusterIssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefTypedDict(
    ClusterIssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefOptionalTypedDict
    , total=(True)):
    name: str


class ClusterIssuerSpecAcmeArrayDns01Route53OptionalTypedDict(TypedDict,
    total=(False)):
    accessKeyID: str
    hostedZoneID: str
    role: str
    secretAccessKeySecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Route53SecretAccessKeySecretRefTypedDict
        ]


class ClusterIssuerSpecAcmeArrayDns01Route53TypedDict(
    ClusterIssuerSpecAcmeArrayDns01Route53OptionalTypedDict, total=(True)):
    region: str


class ClusterIssuerSpecAcmeArrayDns01WebhookOptionalTypedDict(TypedDict,
    total=(False)):
    config: Any


class ClusterIssuerSpecAcmeArrayDns01WebhookTypedDict(
    ClusterIssuerSpecAcmeArrayDns01WebhookOptionalTypedDict, total=(True)):
    groupName: str
    solverName: str


class ClusterIssuerSpecAcmeArrayDns01TypedDict(TypedDict, total=(False)):
    acmedns: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Acmedns,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AcmednsTypedDict
        ]
    akamai: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Akamai,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AkamaiTypedDict
        ]
    azuredns: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Azuredns,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01AzurednsTypedDict
        ]
    clouddns: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Clouddns,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01ClouddnsTypedDict
        ]
    cloudflare: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Cloudflare,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01CloudflareTypedDict
        ]
    cnameStrategy: Literal['None', 'Follow']
    digitalocean: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Digitalocean,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01DigitaloceanTypedDict
        ]
    rfc2136: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Rfc2136,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Rfc2136TypedDict
        ]
    route53: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Route53,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Route53TypedDict
        ]
    webhook: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01Webhook,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01WebhookTypedDict
        ]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateMetadataTypedDict(
    TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict(
    TypedDict, total=(True)):
    preference: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ]
    weight: int


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict(
    TypedDict, total=(True)):
    nodeSelectorTerms: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict
    , total=(True)):
    topologyKey: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayOptionalTypedDict
    , total=(True)):
    topologyKey: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict
    , total=(True)):
    topologyKey: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayOptionalTypedDict
    , total=(True)):
    topologyKey: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict(
    ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityTypedDict(
    TypedDict, total=(False)):
    nodeAffinity: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinity
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict
        ]
    podAffinity: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinity
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict
        ]
    podAntiAffinity: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinity
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict
        ]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArrayTypedDict(
    TypedDict, total=(False)):
    effect: str
    key: str
    operator: str
    tolerationSeconds: int
    value: str


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecTypedDict(TypedDict
    , total=(False)):
    affinity: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinity
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecAffinityTypedDict
        ]
    nodeSelector: Mapping[str, str]
    tolerations: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArray
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecArrayTypedDict
        ]]


class ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateTypedDict(TypedDict,
    total=(False)):
    metadata: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateMetadata
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateMetadataTypedDict
        ]
    spec: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpec
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateSpecTypedDict
        ]


class ClusterIssuerSpecAcmeArrayHttp01IngressTypedDict(TypedDict, total=(False)
    ):
    class_: str
    name: str
    podTemplate: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplate
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressPodTemplateTypedDict
        ]
    serviceType: str


class ClusterIssuerSpecAcmeArrayHttp01TypedDict(TypedDict, total=(False)):
    ingress: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01Ingress,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01IngressTypedDict
        ]


class ClusterIssuerSpecAcmeArraySelectorTypedDict(TypedDict, total=(False)):
    dnsNames: Sequence[str]
    dnsZones: Sequence[str]
    matchLabels: Mapping[str, str]


class ClusterIssuerSpecAcmeArrayTypedDict(TypedDict, total=(False)):
    dns01: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayDns01TypedDict]
    http01: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayHttp01TypedDict]
    selector: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArraySelector,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArraySelectorTypedDict]


class ClusterIssuerSpecAcmeOptionalTypedDict(TypedDict, total=(False)):
    email: str
    externalAccountBinding: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeExternalAccountBinding,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeExternalAccountBindingTypedDict
        ]
    skipTLSVerify: bool
    solvers: Sequence[Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArray,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeArrayTypedDict]]


class ClusterIssuerSpecAcmeTypedDict(ClusterIssuerSpecAcmeOptionalTypedDict,
    total=(True)):
    privateKeySecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmePrivateKeySecretRef,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmePrivateKeySecretRefTypedDict
        ]
    server: str


class ClusterIssuerSpecCaTypedDict(TypedDict, total=(True)):
    secretName: str


class ClusterIssuerSpecVaultAuthAppRoleSecretRefOptionalTypedDict(TypedDict,
    total=(False)):
    key: str


class ClusterIssuerSpecVaultAuthAppRoleSecretRefTypedDict(
    ClusterIssuerSpecVaultAuthAppRoleSecretRefOptionalTypedDict, total=(True)):
    name: str


class ClusterIssuerSpecVaultAuthAppRoleTypedDict(TypedDict, total=(True)):
    path: str
    roleId: str
    secretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthAppRoleSecretRef,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthAppRoleSecretRefTypedDict
        ]


class ClusterIssuerSpecVaultAuthKubernetesSecretRefOptionalTypedDict(TypedDict,
    total=(False)):
    key: str


class ClusterIssuerSpecVaultAuthKubernetesSecretRefTypedDict(
    ClusterIssuerSpecVaultAuthKubernetesSecretRefOptionalTypedDict, total=(
    True)):
    name: str


class ClusterIssuerSpecVaultAuthKubernetesOptionalTypedDict(TypedDict,
    total=(False)):
    mountPath: str


class ClusterIssuerSpecVaultAuthKubernetesTypedDict(
    ClusterIssuerSpecVaultAuthKubernetesOptionalTypedDict, total=(True)):
    role: str
    secretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthKubernetesSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthKubernetesSecretRefTypedDict
        ]


class ClusterIssuerSpecVaultAuthTokenSecretRefOptionalTypedDict(TypedDict,
    total=(False)):
    key: str


class ClusterIssuerSpecVaultAuthTokenSecretRefTypedDict(
    ClusterIssuerSpecVaultAuthTokenSecretRefOptionalTypedDict, total=(True)):
    name: str


class ClusterIssuerSpecVaultAuthTypedDict(TypedDict, total=(False)):
    appRole: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthAppRole,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthAppRoleTypedDict]
    kubernetes: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthKubernetes,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthKubernetesTypedDict
        ]
    tokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthTokenSecretRef,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthTokenSecretRefTypedDict
        ]


class ClusterIssuerSpecVaultOptionalTypedDict(TypedDict, total=(False)):
    caBundle: str


class ClusterIssuerSpecVaultTypedDict(ClusterIssuerSpecVaultOptionalTypedDict,
    total=(True)):
    auth: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuth,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultAuthTypedDict]
    path: str
    server: str


class ClusterIssuerSpecVenafiCloudApiTokenSecretRefOptionalTypedDict(TypedDict,
    total=(False)):
    key: str


class ClusterIssuerSpecVenafiCloudApiTokenSecretRefTypedDict(
    ClusterIssuerSpecVenafiCloudApiTokenSecretRefOptionalTypedDict, total=(
    True)):
    name: str


class ClusterIssuerSpecVenafiCloudTypedDict(TypedDict, total=(True)):
    apiTokenSecretRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiCloudApiTokenSecretRef
        ,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiCloudApiTokenSecretRefTypedDict
        ]
    url: str


class ClusterIssuerSpecVenafiTppCredentialsRefTypedDict(TypedDict, total=(True)
    ):
    name: str


class ClusterIssuerSpecVenafiTppOptionalTypedDict(TypedDict, total=(False)):
    caBundle: str


class ClusterIssuerSpecVenafiTppTypedDict(
    ClusterIssuerSpecVenafiTppOptionalTypedDict, total=(True)):
    credentialsRef: Union[
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTppCredentialsRef,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTppCredentialsRefTypedDict
        ]
    url: str


class ClusterIssuerSpecVenafiOptionalTypedDict(TypedDict, total=(False)):
    cloud: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiCloud,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiCloudTypedDict]
    tpp: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTpp,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTppTypedDict]


class ClusterIssuerSpecVenafiTypedDict(ClusterIssuerSpecVenafiOptionalTypedDict
    , total=(True)):
    zone: str


class ClusterIssuerSpecTypedDict(TypedDict, total=(False)):
    acme: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcme,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecAcmeTypedDict]
    ca: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecCa,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecCaTypedDict]
    selfSigned: Mapping[str, Any]
    vault: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecVault,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVaultTypedDict]
    venafi: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafi,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecVenafiTypedDict]


class ClusterIssuerOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.certmanager.v1alpha2.ClusterIssuerSpec,
        kdsl.certmanager.v1alpha2.ClusterIssuerSpecTypedDict]


class ClusterIssuerTypedDict(ClusterIssuerOptionalTypedDict, total=(True)):
    name: str


class CertificateRequestSpecIssuerRefOptionalTypedDict(TypedDict, total=(False)
    ):
    group: str
    kind: str


class CertificateRequestSpecIssuerRefTypedDict(
    CertificateRequestSpecIssuerRefOptionalTypedDict, total=(True)):
    name: str


class CertificateRequestSpecOptionalTypedDict(TypedDict, total=(False)):
    duration: str
    isCA: bool
    usages: Sequence[Literal['signing', 'digital signature',
        'content commitment', 'key encipherment', 'key agreement',
        'data encipherment', 'cert sign', 'crl sign', 'encipher only',
        'decipher only', 'any', 'server auth', 'client auth',
        'code signing', 'email protection', 's/mime', 'ipsec end system',
        'ipsec tunnel', 'ipsec user', 'timestamping', 'ocsp signing',
        'microsoft sgc', 'netscape sgc']]


class CertificateRequestSpecTypedDict(CertificateRequestSpecOptionalTypedDict,
    total=(True)):
    csr: str
    issuerRef: Union[
        kdsl.certmanager.v1alpha2.CertificateRequestSpecIssuerRef,
        kdsl.certmanager.v1alpha2.CertificateRequestSpecIssuerRefTypedDict]


class CertificateRequestOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.certmanager.v1alpha2.CertificateRequestSpec,
        kdsl.certmanager.v1alpha2.CertificateRequestSpecTypedDict]


class CertificateRequestTypedDict(CertificateRequestOptionalTypedDict,
    total=(True)):
    name: str
    namespace: str


class CertificateSpecIssuerRefOptionalTypedDict(TypedDict, total=(False)):
    group: str
    kind: str


class CertificateSpecIssuerRefTypedDict(
    CertificateSpecIssuerRefOptionalTypedDict, total=(True)):
    name: str


class CertificateSpecSubjectTypedDict(TypedDict, total=(False)):
    countries: Sequence[str]
    localities: Sequence[str]
    organizationalUnits: Sequence[str]
    postalCodes: Sequence[str]
    provinces: Sequence[str]
    serialNumber: str
    streetAddresses: Sequence[str]


class CertificateSpecOptionalTypedDict(TypedDict, total=(False)):
    commonName: str
    dnsNames: Sequence[str]
    duration: str
    ipAddresses: Sequence[str]
    isCA: bool
    keyAlgorithm: Literal['rsa', 'ecdsa']
    keyEncoding: Literal['pkcs1', 'pkcs8']
    keySize: int
    organization: Sequence[str]
    renewBefore: str
    subject: Union[kdsl.certmanager.v1alpha2.CertificateSpecSubject,
        kdsl.certmanager.v1alpha2.CertificateSpecSubjectTypedDict]
    uriSANs: Sequence[str]
    usages: Sequence[Literal['signing', 'digital signature',
        'content commitment', 'key encipherment', 'key agreement',
        'data encipherment', 'cert sign', 'crl sign', 'encipher only',
        'decipher only', 'any', 'server auth', 'client auth',
        'code signing', 'email protection', 's/mime', 'ipsec end system',
        'ipsec tunnel', 'ipsec user', 'timestamping', 'ocsp signing',
        'microsoft sgc', 'netscape sgc']]


class CertificateSpecTypedDict(CertificateSpecOptionalTypedDict, total=(True)):
    issuerRef: Union[kdsl.certmanager.v1alpha2.CertificateSpecIssuerRef,
        kdsl.certmanager.v1alpha2.CertificateSpecIssuerRefTypedDict]
    secretName: str


class CertificateOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.certmanager.v1alpha2.CertificateSpec,
        kdsl.certmanager.v1alpha2.CertificateSpecTypedDict]


class CertificateTypedDict(CertificateOptionalTypedDict, total=(True)):
    name: str
    namespace: str
