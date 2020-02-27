# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetKubernetesClusterResult:
    """
    A collection of values returned by getKubernetesCluster.
    """
    def __init__(__self__, addon_profiles=None, agent_pool_profiles=None, api_server_authorized_ip_ranges=None, dns_prefix=None, fqdn=None, kube_admin_configs=None, kube_admin_config_raw=None, kube_configs=None, kube_config_raw=None, kubernetes_version=None, linux_profiles=None, location=None, name=None, network_profiles=None, node_resource_group=None, private_fqdn=None, private_link_enabled=None, resource_group_name=None, role_based_access_controls=None, service_principals=None, tags=None, windows_profiles=None, id=None):
        if addon_profiles and not isinstance(addon_profiles, list):
            raise TypeError("Expected argument 'addon_profiles' to be a list")
        __self__.addon_profiles = addon_profiles
        """
        A `addon_profile` block as documented below.
        """
        if agent_pool_profiles and not isinstance(agent_pool_profiles, list):
            raise TypeError("Expected argument 'agent_pool_profiles' to be a list")
        __self__.agent_pool_profiles = agent_pool_profiles
        """
        An `agent_pool_profile` block as documented below.
        """
        if api_server_authorized_ip_ranges and not isinstance(api_server_authorized_ip_ranges, list):
            raise TypeError("Expected argument 'api_server_authorized_ip_ranges' to be a list")
        __self__.api_server_authorized_ip_ranges = api_server_authorized_ip_ranges
        """
        The IP ranges to whitelist for incoming traffic to the masters.
        """
        if dns_prefix and not isinstance(dns_prefix, str):
            raise TypeError("Expected argument 'dns_prefix' to be a str")
        __self__.dns_prefix = dns_prefix
        """
        The DNS Prefix of the managed Kubernetes cluster.
        """
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        __self__.fqdn = fqdn
        """
        The FQDN of the Azure Kubernetes Managed Cluster.
        """
        if kube_admin_configs and not isinstance(kube_admin_configs, list):
            raise TypeError("Expected argument 'kube_admin_configs' to be a list")
        __self__.kube_admin_configs = kube_admin_configs
        """
        A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
        """
        if kube_admin_config_raw and not isinstance(kube_admin_config_raw, str):
            raise TypeError("Expected argument 'kube_admin_config_raw' to be a str")
        __self__.kube_admin_config_raw = kube_admin_config_raw
        """
        Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
        """
        if kube_configs and not isinstance(kube_configs, list):
            raise TypeError("Expected argument 'kube_configs' to be a list")
        __self__.kube_configs = kube_configs
        """
        A `kube_config` block as defined below.
        """
        if kube_config_raw and not isinstance(kube_config_raw, str):
            raise TypeError("Expected argument 'kube_config_raw' to be a str")
        __self__.kube_config_raw = kube_config_raw
        """
        Base64 encoded Kubernetes configuration.
        """
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        __self__.kubernetes_version = kubernetes_version
        """
        The version of Kubernetes used on the managed Kubernetes Cluster.
        """
        if linux_profiles and not isinstance(linux_profiles, list):
            raise TypeError("Expected argument 'linux_profiles' to be a list")
        __self__.linux_profiles = linux_profiles
        """
        A `linux_profile` block as documented below.
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The Azure Region in which the managed Kubernetes Cluster exists.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name assigned to this pool of agents.
        """
        if network_profiles and not isinstance(network_profiles, list):
            raise TypeError("Expected argument 'network_profiles' to be a list")
        __self__.network_profiles = network_profiles
        """
        A `network_profile` block as documented below.
        """
        if node_resource_group and not isinstance(node_resource_group, str):
            raise TypeError("Expected argument 'node_resource_group' to be a str")
        __self__.node_resource_group = node_resource_group
        """
        Auto-generated Resource Group containing AKS Cluster resources.
        """
        if private_fqdn and not isinstance(private_fqdn, str):
            raise TypeError("Expected argument 'private_fqdn' to be a str")
        __self__.private_fqdn = private_fqdn
        """
        The FQDN of this Kubernetes Cluster when private link has been enabled. This name is only resolvable inside the Virtual Network where the Azure Kubernetes Service is located                   
        """
        if private_link_enabled and not isinstance(private_link_enabled, bool):
            raise TypeError("Expected argument 'private_link_enabled' to be a bool")
        __self__.private_link_enabled = private_link_enabled
        """
        Does this Kubernetes Cluster have the Kubernetes API exposed via Private Link?                           
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if role_based_access_controls and not isinstance(role_based_access_controls, list):
            raise TypeError("Expected argument 'role_based_access_controls' to be a list")
        __self__.role_based_access_controls = role_based_access_controls
        """
        A `role_based_access_control` block as documented below.
        """
        if service_principals and not isinstance(service_principals, list):
            raise TypeError("Expected argument 'service_principals' to be a list")
        __self__.service_principals = service_principals
        """
        A `service_principal` block as documented below.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to this resource.
        """
        if windows_profiles and not isinstance(windows_profiles, list):
            raise TypeError("Expected argument 'windows_profiles' to be a list")
        __self__.windows_profiles = windows_profiles
        """
        A `windows_profile` block as documented below.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetKubernetesClusterResult(GetKubernetesClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubernetesClusterResult(
            addon_profiles=self.addon_profiles,
            agent_pool_profiles=self.agent_pool_profiles,
            api_server_authorized_ip_ranges=self.api_server_authorized_ip_ranges,
            dns_prefix=self.dns_prefix,
            fqdn=self.fqdn,
            kube_admin_configs=self.kube_admin_configs,
            kube_admin_config_raw=self.kube_admin_config_raw,
            kube_configs=self.kube_configs,
            kube_config_raw=self.kube_config_raw,
            kubernetes_version=self.kubernetes_version,
            linux_profiles=self.linux_profiles,
            location=self.location,
            name=self.name,
            network_profiles=self.network_profiles,
            node_resource_group=self.node_resource_group,
            private_fqdn=self.private_fqdn,
            private_link_enabled=self.private_link_enabled,
            resource_group_name=self.resource_group_name,
            role_based_access_controls=self.role_based_access_controls,
            service_principals=self.service_principals,
            tags=self.tags,
            windows_profiles=self.windows_profiles,
            id=self.id)

def get_kubernetes_cluster(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Managed Kubernetes Cluster (AKS).
    
    > **Note:** All arguments including the client secret will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    
    :param str name: The name of the managed Kubernetes Cluster.
    :param str resource_group_name: The name of the Resource Group in which the managed Kubernetes Cluster exists.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_cluster.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:containerservice/getKubernetesCluster:getKubernetesCluster', __args__, opts=opts).value

    return AwaitableGetKubernetesClusterResult(
        addon_profiles=__ret__.get('addonProfiles'),
        agent_pool_profiles=__ret__.get('agentPoolProfiles'),
        api_server_authorized_ip_ranges=__ret__.get('apiServerAuthorizedIpRanges'),
        dns_prefix=__ret__.get('dnsPrefix'),
        fqdn=__ret__.get('fqdn'),
        kube_admin_configs=__ret__.get('kubeAdminConfigs'),
        kube_admin_config_raw=__ret__.get('kubeAdminConfigRaw'),
        kube_configs=__ret__.get('kubeConfigs'),
        kube_config_raw=__ret__.get('kubeConfigRaw'),
        kubernetes_version=__ret__.get('kubernetesVersion'),
        linux_profiles=__ret__.get('linuxProfiles'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        network_profiles=__ret__.get('networkProfiles'),
        node_resource_group=__ret__.get('nodeResourceGroup'),
        private_fqdn=__ret__.get('privateFqdn'),
        private_link_enabled=__ret__.get('privateLinkEnabled'),
        resource_group_name=__ret__.get('resourceGroupName'),
        role_based_access_controls=__ret__.get('roleBasedAccessControls'),
        service_principals=__ret__.get('servicePrincipals'),
        tags=__ret__.get('tags'),
        windows_profiles=__ret__.get('windowsProfiles'),
        id=__ret__.get('id'))
