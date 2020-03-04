from __future__ import annotations
import attr
import kdsl.acme.v1alpha2
from kdsl.bases import K8sObjectBase, K8sResourceBase
from typing import Literal, ClassVar, Mapping, Any, Optional, Sequence, Union, TypedDict


@attr.s(kw_only=True)
class OrderSpecIssuerRef(K8sObjectBase):
    """
    | IssuerRef references a properly configured ACME-type Issuer which should be used to create this Order. If the Issuer does not exist, processing will be retried. If the Issuer is not an 'ACME' Issuer, an error will be returned and the Order will be marked as failed.
    
    :param name: None
    :param group: None
    :param kind: None
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})


@attr.s(kw_only=True)
class OrderSpec(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.OrderSpec
    
    :param csr: Certificate signing request bytes in DER encoding. This will be used when finalizing the order. This field must be set on the order.
    :param issuerRef: IssuerRef references a properly configured ACME-type Issuer which should be used to create this Order. If the Issuer does not exist, processing will be retried. If the Issuer is not an 'ACME' Issuer, an error will be returned and the Order will be marked as failed.
    :param commonName: CommonName is the common name as specified on the DER encoded CSR. If CommonName is not specified, the first DNSName specified will be used as the CommonName. At least one of CommonName or a DNSNames must be set. This field must match the corresponding field on the DER encoded CSR.
    :param dnsNames: DNSNames is a list of DNS names that should be included as part of the Order validation process. If CommonName is not specified, the first DNSName specified will be used as the CommonName. At least one of CommonName or a DNSNames must be set. This field must match the corresponding field on the DER encoded CSR.
    """
    csr: str = attr.ib(metadata={'yaml_name': 'csr'})
    issuerRef: Union[kdsl.acme.v1alpha2.OrderSpecIssuerRef,
        kdsl.acme.v1alpha2.OrderSpecIssuerRefTypedDict] = attr.ib(metadata=
        {'yaml_name': 'issuerRef'})
    commonName: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'commonName'})
    dnsNames: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'dnsNames'})


@attr.s(kw_only=True)
class Order(K8sResourceBase):
    """
    | Order is a type to represent an Order with an ACME server
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: None
    """
    apiVersion: ClassVar[str] = 'acme.cert-manager.io/v1alpha2'
    kind: ClassVar[str] = 'Order'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.acme.v1alpha2.OrderSpec,
        kdsl.acme.v1alpha2.OrderSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class ChallengeSpecIssuerRef(K8sObjectBase):
    """
    | IssuerRef references a properly configured ACME-type Issuer which should be used to create this Challenge. If the Issuer does not exist, processing will be retried. If the Issuer is not an 'ACME' Issuer, an error will be returned and the Challenge will be marked as failed.
    
    :param name: None
    :param group: None
    :param kind: None
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    group: Optional[str] = attr.ib(default=None, metadata={'yaml_name':
        'group'})
    kind: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'kind'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01AcmednsAccountSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01AcmednsAccountSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Acmedns(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderAcmeDNS is a structure containing the configuration for ACME-DNS servers
    
    :param accountSecretRef: None
    :param host: None
    """
    accountSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AcmednsAccountSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AcmednsAccountSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'accountSecretRef'})
    host: str = attr.ib(metadata={'yaml_name': 'host'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01AkamaiClientSecretSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientSecretSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01AkamaiClientTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Akamai(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderAkamai is a structure containing the DNS configuration for Akamai DNS—Zone Record Management API
    
    :param accessTokenSecretRef: None
    :param clientSecretSecretRef: None
    :param clientTokenSecretRef: None
    :param serviceConsumerDomain: None
    """
    accessTokenSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiAccessTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'accessTokenSecretRef'})
    clientSecretSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientSecretSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientSecretSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'clientSecretSecretRef'})
    clientTokenSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientTokenSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'clientTokenSecretRef'})
    serviceConsumerDomain: str = attr.ib(metadata={'yaml_name':
        'serviceConsumerDomain'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01AzurednsClientSecretSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01AzurednsClientSecretSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Azuredns(K8sObjectBase):
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
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AzurednsClientSecretSecretRef
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AzurednsClientSecretSecretRefTypedDict
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
class ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Clouddns(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderCloudDNS is a structure containing the DNS configuration for Google Cloud DNS
    
    :param project: None
    :param serviceAccountSecretRef: None
    """
    project: str = attr.ib(metadata={'yaml_name': 'project'})
    serviceAccountSecretRef: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRef
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'serviceAccountSecretRef'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01CloudflareApiKeySecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiKeySecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01CloudflareApiTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Cloudflare(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderCloudflare is a structure containing the DNS configuration for Cloudflare
    
    :param email: None
    :param apiKeySecretRef: None
    :param apiTokenSecretRef: None
    """
    email: str = attr.ib(metadata={'yaml_name': 'email'})
    apiKeySecretRef: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiKeySecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiKeySecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'apiKeySecretRef'})
    apiTokenSecretRef: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiTokenSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiTokenSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'apiTokenSecretRef'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01DigitaloceanTokenSecretRef(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01DigitaloceanTokenSecretRef
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Digitalocean(K8sObjectBase):
    """
    | ACMEIssuerDNS01ProviderDigitalOcean is a structure containing the DNS configuration for DigitalOcean Domains
    
    :param tokenSecretRef: None
    """
    tokenSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01DigitaloceanTokenSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01DigitaloceanTokenSecretRefTypedDict
        ] = attr.ib(metadata={'yaml_name': 'tokenSecretRef'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef(K8sObjectBase):
    """
    | The name of the secret containing the TSIG value. If ``tsigKeyName`` is defined, this field is required.
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Rfc2136(K8sObjectBase):
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
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'tsigSecretSecretRef'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef(K8sObjectBase):
    """
    | The SecretAccessKey is used for authentication. If not set we fall-back to using env vars, shared credentials file or AWS Instance metadata https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
    
    :param name: Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?
    :param key: The key of the secret to select from. Must be a valid secret key.
    """
    name: str = attr.ib(metadata={'yaml_name': 'name'})
    key: Optional[str] = attr.ib(default=None, metadata={'yaml_name': 'key'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Route53(K8sObjectBase):
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
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Route53SecretAccessKeySecretRefTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'secretAccessKeySecretRef'})


@attr.s(kw_only=True)
class ChallengeSpecSolverDns01Webhook(K8sObjectBase):
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
class ChallengeSpecSolverDns01(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpecSolverDns01
    
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
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Acmedns,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AcmednsTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'acmedns'})
    akamai: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Akamai,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'akamai'})
    azuredns: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Azuredns,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AzurednsTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'azuredns'})
    clouddns: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Clouddns,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01ClouddnsTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'clouddns'})
    cloudflare: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Cloudflare,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'cloudflare'})
    cnameStrategy: Optional[Literal['None', 'Follow']] = attr.ib(default=
        None, metadata={'yaml_name': 'cnameStrategy'})
    digitalocean: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Digitalocean,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01DigitaloceanTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'digitalocean'})
    rfc2136: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Rfc2136,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Rfc2136TypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'rfc2136'})
    route53: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Route53,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Route53TypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'route53'})
    webhook: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Webhook,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01WebhookTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'webhook'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateMetadata(K8sObjectBase):
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
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray(
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
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference(
    K8sObjectBase):
    """
    | A node selector term, associated with the corresponding weight.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArray(
    K8sObjectBase):
    """
    | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
    
    :param preference: A node selector term, associated with the corresponding weight.
    :param weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.
    """
    preference: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ] = attr.ib(metadata={'yaml_name': 'preference'})
    weight: int = attr.ib(metadata={'yaml_name': 'weight'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray(
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
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray(
    K8sObjectBase):
    """
    | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    
    :param matchExpressions: A list of node selector requirements by node's labels.
    :param matchFields: A list of node selector requirements by node's fields.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchFields: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchFields'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(
    K8sObjectBase):
    """
    | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    
    :param nodeSelectorTerms: Required. A list of node selector terms. The terms are ORed.
    """
    nodeSelectorTerms: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]] = attr.ib(metadata={'yaml_name': 'nodeSelectorTerms'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity(
    K8sObjectBase):
    """
    | Describes node affinity scheduling rules for the pod.
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray(
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
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTerm(
    K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArray(
    K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray(
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
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity(
    K8sObjectBase):
    """
    | Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray(
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
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTerm(
    K8sObjectBase):
    """
    | Required. A pod affinity term, associated with the corresponding weight.
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray(
    K8sObjectBase):
    """
    | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    
    :param topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    :param labelSelector: A label query over a set of resources, in this case pods.
    :param namespaces: namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means "this pod's namespace"
    """
    topologyKey: str = attr.ib(metadata={'yaml_name': 'topologyKey'})
    labelSelector: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'labelSelector'})
    namespaces: Optional[Sequence[str]] = attr.ib(default=None, metadata={
        'yaml_name': 'namespaces'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray(
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
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector(
    K8sObjectBase):
    """
    | A label query over a set of resources, in this case pods.
    
    :param matchExpressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
    :param matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """
    matchExpressions: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'matchExpressions'})
    matchLabels: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'matchLabels'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity(
    K8sObjectBase):
    """
    | Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    
    :param preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    :param requiredDuringSchedulingIgnoredDuringExecution: If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """
    preferredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[
        Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'preferredDuringSchedulingIgnoredDuringExecution'})
    requiredDuringSchedulingIgnoredDuringExecution: Optional[Sequence[Union
        [
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name':
        'requiredDuringSchedulingIgnoredDuringExecution'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity(K8sObjectBase):
    """
    | If specified, the pod's scheduling constraints
    
    :param nodeAffinity: Describes node affinity scheduling rules for the pod.
    :param podAffinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    :param podAntiAffinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    """
    nodeAffinity: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'nodeAffinity'})
    podAffinity: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podAffinity'})
    podAntiAffinity: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podAntiAffinity'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecArray(K8sObjectBase):
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
class ChallengeSpecSolverHttp01IngressPodTemplateSpec(K8sObjectBase):
    """
    | PodSpec defines overrides for the HTTP01 challenge solver pod. Only the 'nodeSelector', 'affinity' and 'tolerations' fields are supported currently. All other fields will be ignored.
    
    :param affinity: If specified, the pod's scheduling constraints
    :param nodeSelector: NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
    :param tolerations: If specified, the pod's tolerations.
    """
    affinity: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'affinity'})
    nodeSelector: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': 'nodeSelector'})
    tolerations: Optional[Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecArrayTypedDict
        ]]] = attr.ib(default=None, metadata={'yaml_name': 'tolerations'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01IngressPodTemplate(K8sObjectBase):
    """
    | Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges
    
    :param metadata: ObjectMeta overrides for the pod used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.
    :param spec: PodSpec defines overrides for the HTTP01 challenge solver pod. Only the 'nodeSelector', 'affinity' and 'tolerations' fields are supported currently. All other fields will be ignored.
    """
    metadata: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateMetadata,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateMetadataTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'metadata'})
    spec: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpec,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'spec'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01Ingress(K8sObjectBase):
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
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplate,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateTypedDict
        ]] = attr.ib(default=None, metadata={'yaml_name': 'podTemplate'})
    serviceType: Optional[str] = attr.ib(default=None, metadata={
        'yaml_name': 'serviceType'})


@attr.s(kw_only=True)
class ChallengeSpecSolverHttp01(K8sObjectBase):
    """
    | ACMEChallengeSolverHTTP01 contains configuration detailing how to solve HTTP01 challenges within a Kubernetes cluster. Typically this is accomplished through creating 'routes' of some description that configure ingress controllers to direct traffic to 'solver pods', which are responsible for responding to the ACME server's HTTP requests.
    
    :param ingress: The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.
    """
    ingress: Optional[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01Ingress,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressTypedDict]
        ] = attr.ib(default=None, metadata={'yaml_name': 'ingress'})


@attr.s(kw_only=True)
class ChallengeSpecSolverSelector(K8sObjectBase):
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
class ChallengeSpecSolver(K8sObjectBase):
    """
    | Solver contains the domain solving configuration that should be used to solve this challenge resource.
    
    :param dns01: None
    :param http01: ACMEChallengeSolverHTTP01 contains configuration detailing how to solve HTTP01 challenges within a Kubernetes cluster. Typically this is accomplished through creating 'routes' of some description that configure ingress controllers to direct traffic to 'solver pods', which are responsible for responding to the ACME server's HTTP requests.
    :param selector: Selector selects a set of DNSNames on the Certificate resource that should be solved using this challenge solver.
    """
    dns01: Optional[Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01TypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'dns01'})
    http01: Optional[Union[kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01TypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'http01'})
    selector: Optional[Union[kdsl.acme.v1alpha2.ChallengeSpecSolverSelector,
        kdsl.acme.v1alpha2.ChallengeSpecSolverSelectorTypedDict]] = attr.ib(
        default=None, metadata={'yaml_name': 'selector'})


@attr.s(kw_only=True)
class ChallengeSpec(K8sObjectBase):
    """
    | Kubernates API object: io.cert-manager.acme.v1alpha2.ChallengeSpec
    
    :param authzURL: AuthzURL is the URL to the ACME Authorization resource that this challenge is a part of.
    :param dnsName: DNSName is the identifier that this challenge is for, e.g. example.com.
    :param issuerRef: IssuerRef references a properly configured ACME-type Issuer which should be used to create this Challenge. If the Issuer does not exist, processing will be retried. If the Issuer is not an 'ACME' Issuer, an error will be returned and the Challenge will be marked as failed.
    :param key: Key is the ACME challenge key for this challenge
    :param token: Token is the ACME challenge token for this challenge.
    :param type: Type is the type of ACME challenge this resource represents, e.g. "dns01" or "http01"
    :param url: URL is the URL of the ACME Challenge resource for this challenge. This can be used to lookup details about the status of this challenge.
    :param solver: Solver contains the domain solving configuration that should be used to solve this challenge resource.
    :param wildcard: Wildcard will be true if this challenge is for a wildcard identifier, for example '*.example.com'
    """
    authzURL: str = attr.ib(metadata={'yaml_name': 'authzURL'})
    dnsName: str = attr.ib(metadata={'yaml_name': 'dnsName'})
    issuerRef: Union[kdsl.acme.v1alpha2.ChallengeSpecIssuerRef,
        kdsl.acme.v1alpha2.ChallengeSpecIssuerRefTypedDict] = attr.ib(metadata
        ={'yaml_name': 'issuerRef'})
    key: str = attr.ib(metadata={'yaml_name': 'key'})
    token: str = attr.ib(metadata={'yaml_name': 'token'})
    type: str = attr.ib(metadata={'yaml_name': 'type'})
    url: str = attr.ib(metadata={'yaml_name': 'url'})
    solver: Optional[Union[kdsl.acme.v1alpha2.ChallengeSpecSolver,
        kdsl.acme.v1alpha2.ChallengeSpecSolverTypedDict]] = attr.ib(default
        =None, metadata={'yaml_name': 'solver'})
    wildcard: Optional[bool] = attr.ib(default=None, metadata={'yaml_name':
        'wildcard'})


@attr.s(kw_only=True)
class Challenge(K8sResourceBase):
    """
    | Challenge is a type to represent a Challenge request with an ACME server
    
    :param name: metadata.name
    :param namespace: metadata.namespace
    :param annotations: metadata.annotations
    :param labels: metadata.labels
    :param spec: None
    """
    apiVersion: ClassVar[str] = 'acme.cert-manager.io/v1alpha2'
    kind: ClassVar[str] = 'Challenge'
    name: str = attr.ib(metadata={'yaml_name': None})
    namespace: str = attr.ib(metadata={'yaml_name': None})
    annotations: Optional[Mapping[str, str]] = attr.ib(default=None,
        metadata={'yaml_name': None})
    labels: Optional[Mapping[str, str]] = attr.ib(default=None, metadata={
        'yaml_name': None})
    spec: Optional[Union[kdsl.acme.v1alpha2.ChallengeSpec,
        kdsl.acme.v1alpha2.ChallengeSpecTypedDict]] = attr.ib(default=None,
        metadata={'yaml_name': 'spec'})


class OrderSpecIssuerRefOptionalTypedDict(TypedDict, total=(False)):
    group: str
    kind: str


class OrderSpecIssuerRefTypedDict(OrderSpecIssuerRefOptionalTypedDict,
    total=(True)):
    name: str


class OrderSpecOptionalTypedDict(TypedDict, total=(False)):
    commonName: str
    dnsNames: Sequence[str]


class OrderSpecTypedDict(OrderSpecOptionalTypedDict, total=(True)):
    csr: str
    issuerRef: Union[kdsl.acme.v1alpha2.OrderSpecIssuerRef,
        kdsl.acme.v1alpha2.OrderSpecIssuerRefTypedDict]


class OrderOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.acme.v1alpha2.OrderSpec,
        kdsl.acme.v1alpha2.OrderSpecTypedDict]


class OrderTypedDict(OrderOptionalTypedDict, total=(True)):
    name: str
    namespace: str


class ChallengeSpecIssuerRefOptionalTypedDict(TypedDict, total=(False)):
    group: str
    kind: str


class ChallengeSpecIssuerRefTypedDict(ChallengeSpecIssuerRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01AcmednsAccountSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01AcmednsAccountSecretRefTypedDict(
    ChallengeSpecSolverDns01AcmednsAccountSecretRefOptionalTypedDict, total
    =(True)):
    name: str


class ChallengeSpecSolverDns01AcmednsTypedDict(TypedDict, total=(True)):
    accountSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AcmednsAccountSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AcmednsAccountSecretRefTypedDict
        ]
    host: str


class ChallengeSpecSolverDns01AkamaiAccessTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01AkamaiAccessTokenSecretRefTypedDict(
    ChallengeSpecSolverDns01AkamaiAccessTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01AkamaiClientSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01AkamaiClientSecretSecretRefTypedDict(
    ChallengeSpecSolverDns01AkamaiClientSecretSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01AkamaiClientTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01AkamaiClientTokenSecretRefTypedDict(
    ChallengeSpecSolverDns01AkamaiClientTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01AkamaiTypedDict(TypedDict, total=(True)):
    accessTokenSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiAccessTokenSecretRefTypedDict
        ]
    clientSecretSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientSecretSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientSecretSecretRefTypedDict
        ]
    clientTokenSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientTokenSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiClientTokenSecretRefTypedDict
        ]
    serviceConsumerDomain: str


class ChallengeSpecSolverDns01AzurednsClientSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01AzurednsClientSecretSecretRefTypedDict(
    ChallengeSpecSolverDns01AzurednsClientSecretSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01AzurednsOptionalTypedDict(TypedDict, total=(
    False)):
    environment: Literal['AzurePublicCloud', 'AzureChinaCloud',
        'AzureGermanCloud', 'AzureUSGovernmentCloud']
    hostedZoneName: str


class ChallengeSpecSolverDns01AzurednsTypedDict(
    ChallengeSpecSolverDns01AzurednsOptionalTypedDict, total=(True)):
    clientID: str
    clientSecretSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AzurednsClientSecretSecretRef
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AzurednsClientSecretSecretRefTypedDict
        ]
    resourceGroupName: str
    subscriptionID: str
    tenantID: str


class ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRefTypedDict(
    ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01ClouddnsOptionalTypedDict(TypedDict, total=(
    False)):
    serviceAccountSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRef
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01ClouddnsServiceAccountSecretRefTypedDict
        ]


class ChallengeSpecSolverDns01ClouddnsTypedDict(
    ChallengeSpecSolverDns01ClouddnsOptionalTypedDict, total=(True)):
    project: str


class ChallengeSpecSolverDns01CloudflareApiKeySecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01CloudflareApiKeySecretRefTypedDict(
    ChallengeSpecSolverDns01CloudflareApiKeySecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01CloudflareApiTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01CloudflareApiTokenSecretRefTypedDict(
    ChallengeSpecSolverDns01CloudflareApiTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01CloudflareOptionalTypedDict(TypedDict, total=
    (False)):
    apiKeySecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiKeySecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiKeySecretRefTypedDict
        ]
    apiTokenSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiTokenSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareApiTokenSecretRefTypedDict
        ]


class ChallengeSpecSolverDns01CloudflareTypedDict(
    ChallengeSpecSolverDns01CloudflareOptionalTypedDict, total=(True)):
    email: str


class ChallengeSpecSolverDns01DigitaloceanTokenSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01DigitaloceanTokenSecretRefTypedDict(
    ChallengeSpecSolverDns01DigitaloceanTokenSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01DigitaloceanTypedDict(TypedDict, total=(True)):
    tokenSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01DigitaloceanTokenSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01DigitaloceanTokenSecretRefTypedDict
        ]


class ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRefTypedDict(
    ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01Rfc2136OptionalTypedDict(TypedDict, total=(False)
    ):
    tsigAlgorithm: str
    tsigKeyName: str
    tsigSecretSecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRefTypedDict
        ]


class ChallengeSpecSolverDns01Rfc2136TypedDict(
    ChallengeSpecSolverDns01Rfc2136OptionalTypedDict, total=(True)):
    nameserver: str


class ChallengeSpecSolverDns01Route53SecretAccessKeySecretRefOptionalTypedDict(
    TypedDict, total=(False)):
    key: str


class ChallengeSpecSolverDns01Route53SecretAccessKeySecretRefTypedDict(
    ChallengeSpecSolverDns01Route53SecretAccessKeySecretRefOptionalTypedDict,
    total=(True)):
    name: str


class ChallengeSpecSolverDns01Route53OptionalTypedDict(TypedDict, total=(False)
    ):
    accessKeyID: str
    hostedZoneID: str
    role: str
    secretAccessKeySecretRef: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Route53SecretAccessKeySecretRefTypedDict
        ]


class ChallengeSpecSolverDns01Route53TypedDict(
    ChallengeSpecSolverDns01Route53OptionalTypedDict, total=(True)):
    region: str


class ChallengeSpecSolverDns01WebhookOptionalTypedDict(TypedDict, total=(False)
    ):
    config: Any


class ChallengeSpecSolverDns01WebhookTypedDict(
    ChallengeSpecSolverDns01WebhookOptionalTypedDict, total=(True)):
    groupName: str
    solverName: str


class ChallengeSpecSolverDns01TypedDict(TypedDict, total=(False)):
    acmedns: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Acmedns,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AcmednsTypedDict]
    akamai: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Akamai,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AkamaiTypedDict]
    azuredns: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Azuredns,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01AzurednsTypedDict]
    clouddns: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Clouddns,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01ClouddnsTypedDict]
    cloudflare: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Cloudflare,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01CloudflareTypedDict]
    cnameStrategy: Literal['None', 'Follow']
    digitalocean: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Digitalocean,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01DigitaloceanTypedDict]
    rfc2136: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Rfc2136,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Rfc2136TypedDict]
    route53: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Route53,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Route53TypedDict]
    webhook: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01Webhook,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01WebhookTypedDict]


class ChallengeSpecSolverHttp01IngressPodTemplateMetadataTypedDict(TypedDict,
    total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceArrayTypedDict
        ]]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict(
    TypedDict, total=(True)):
    preference: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreference
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayPreferenceTypedDict
        ]
    weight: int


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]
    matchFields: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayArrayTypedDict
        ]]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict(
    TypedDict, total=(True)):
    nodeSelectorTerms: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionArrayTypedDict
        ]]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionTypedDict
        ]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayPodAffinityTermOptionalTypedDict
    , total=(True)):
    topologyKey: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelector
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayOptionalTypedDict
    , total=(True)):
    topologyKey: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityArrayTypedDict
        ]]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelector
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayPodAffinityTermOptionalTypedDict
    , total=(True)):
    topologyKey: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayOptionalTypedDict(
    TypedDict, total=(False)):
    labelSelector: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelector
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict
        ]
    namespaces: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayOptionalTypedDict
    , total=(True)):
    topologyKey: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict(
    TypedDict, total=(False)):
    values: Sequence[str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict(
    ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayOptionalTypedDict
    , total=(True)):
    key: str
    operator: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorTypedDict(
    TypedDict, total=(False)):
    matchExpressions: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayLabelSelectorArrayTypedDict
        ]]
    matchLabels: Mapping[str, str]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict(
    TypedDict, total=(False)):
    preferredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]
    requiredDuringSchedulingIgnoredDuringExecution: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityArrayTypedDict
        ]]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityTypedDict(
    TypedDict, total=(False)):
    nodeAffinity: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityTypedDict
        ]
    podAffinity: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityTypedDict
        ]
    podAntiAffinity: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityTypedDict
        ]


class ChallengeSpecSolverHttp01IngressPodTemplateSpecArrayTypedDict(TypedDict,
    total=(False)):
    effect: str
    key: str
    operator: str
    tolerationSeconds: int
    value: str


class ChallengeSpecSolverHttp01IngressPodTemplateSpecTypedDict(TypedDict,
    total=(False)):
    affinity: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityTypedDict
        ]
    nodeSelector: Mapping[str, str]
    tolerations: Sequence[Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecArray
        ,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecArrayTypedDict
        ]]


class ChallengeSpecSolverHttp01IngressPodTemplateTypedDict(TypedDict, total
    =(False)):
    metadata: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateMetadata,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateMetadataTypedDict
        ]
    spec: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpec,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateSpecTypedDict
        ]


class ChallengeSpecSolverHttp01IngressTypedDict(TypedDict, total=(False)):
    class_: str
    name: str
    podTemplate: Union[
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplate,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressPodTemplateTypedDict
        ]
    serviceType: str


class ChallengeSpecSolverHttp01TypedDict(TypedDict, total=(False)):
    ingress: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01Ingress,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01IngressTypedDict]


class ChallengeSpecSolverSelectorTypedDict(TypedDict, total=(False)):
    dnsNames: Sequence[str]
    dnsZones: Sequence[str]
    matchLabels: Mapping[str, str]


class ChallengeSpecSolverTypedDict(TypedDict, total=(False)):
    dns01: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverDns01,
        kdsl.acme.v1alpha2.ChallengeSpecSolverDns01TypedDict]
    http01: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01,
        kdsl.acme.v1alpha2.ChallengeSpecSolverHttp01TypedDict]
    selector: Union[kdsl.acme.v1alpha2.ChallengeSpecSolverSelector,
        kdsl.acme.v1alpha2.ChallengeSpecSolverSelectorTypedDict]


class ChallengeSpecOptionalTypedDict(TypedDict, total=(False)):
    solver: Union[kdsl.acme.v1alpha2.ChallengeSpecSolver,
        kdsl.acme.v1alpha2.ChallengeSpecSolverTypedDict]
    wildcard: bool


class ChallengeSpecTypedDict(ChallengeSpecOptionalTypedDict, total=(True)):
    authzURL: str
    dnsName: str
    issuerRef: Union[kdsl.acme.v1alpha2.ChallengeSpecIssuerRef,
        kdsl.acme.v1alpha2.ChallengeSpecIssuerRefTypedDict]
    key: str
    token: str
    type: str
    url: str


class ChallengeOptionalTypedDict(TypedDict, total=(False)):
    annotations: Mapping[str, str]
    labels: Mapping[str, str]
    spec: Union[kdsl.acme.v1alpha2.ChallengeSpec,
        kdsl.acme.v1alpha2.ChallengeSpecTypedDict]


class ChallengeTypedDict(ChallengeOptionalTypedDict, total=(True)):
    name: str
    namespace: str
