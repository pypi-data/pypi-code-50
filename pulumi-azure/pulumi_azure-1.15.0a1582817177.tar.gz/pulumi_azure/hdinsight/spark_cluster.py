# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class SparkCluster(pulumi.CustomResource):
    cluster_version: pulumi.Output[str]
    """
    Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
    """
    component_version: pulumi.Output[dict]
    """
    A `component_version` block as defined below.
    
      * `spark` (`str`)
    """
    gateway: pulumi.Output[dict]
    """
    A `gateway` block as defined below.
    
      * `enabled` (`bool`)
      * `password` (`str`)
      * `username` (`str`)
    """
    https_endpoint: pulumi.Output[str]
    """
    The HTTPS Connectivity Endpoint for this HDInsight Spark Cluster.
    """
    location: pulumi.Output[str]
    """
    Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
    """
    roles: pulumi.Output[dict]
    """
    A `roles` block as defined below.
    
      * `headNode` (`dict`)
    
        * `password` (`str`)
        * `sshKeys` (`list`)
        * `subnet_id` (`str`)
        * `username` (`str`)
        * `virtualNetworkId` (`str`)
        * `vm_size` (`str`)
    
      * `workerNode` (`dict`)
    
        * `minInstanceCount` (`float`)
        * `password` (`str`)
        * `sshKeys` (`list`)
        * `subnet_id` (`str`)
        * `targetInstanceCount` (`float`)
        * `username` (`str`)
        * `virtualNetworkId` (`str`)
        * `vm_size` (`str`)
    
      * `zookeeperNode` (`dict`)
    
        * `password` (`str`)
        * `sshKeys` (`list`)
        * `subnet_id` (`str`)
        * `username` (`str`)
        * `virtualNetworkId` (`str`)
        * `vm_size` (`str`)
    """
    ssh_endpoint: pulumi.Output[str]
    """
    The SSH Connectivity Endpoint for this HDInsight Spark Cluster.
    """
    storage_accounts: pulumi.Output[list]
    """
    One or more `storage_account` block as defined below.
    
      * `isDefault` (`bool`)
      * `storageAccountKey` (`str`)
      * `storageContainerId` (`str`)
    """
    storage_account_gen2: pulumi.Output[dict]
    """
    A `storage_account_gen2` block as defined below.
    
      * `filesystemId` (`str`)
      * `isDefault` (`bool`)
      * `managedIdentityResourceId` (`str`)
      * `storageResourceId` (`str`)
    """
    tags: pulumi.Output[dict]
    """
    A map of Tags which should be assigned to this HDInsight Spark Cluster.
    """
    tier: pulumi.Output[str]
    """
    Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, cluster_version=None, component_version=None, gateway=None, location=None, name=None, resource_group_name=None, roles=None, storage_accounts=None, storage_account_gen2=None, tags=None, tier=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a HDInsight Spark Cluster.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] component_version: A `component_version` block as defined below.
        :param pulumi.Input[dict] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] roles: A `roles` block as defined below.
        :param pulumi.Input[list] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[dict] storage_account_gen2: A `storage_account_gen2` block as defined below.
        :param pulumi.Input[dict] tags: A map of Tags which should be assigned to this HDInsight Spark Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        
        The **component_version** object supports the following:
        
          * `spark` (`pulumi.Input[str]`)
        
        The **gateway** object supports the following:
        
          * `enabled` (`pulumi.Input[bool]`)
          * `password` (`pulumi.Input[str]`)
          * `username` (`pulumi.Input[str]`)
        
        The **roles** object supports the following:
        
          * `headNode` (`pulumi.Input[dict]`)
        
            * `password` (`pulumi.Input[str]`)
            * `sshKeys` (`pulumi.Input[list]`)
            * `subnet_id` (`pulumi.Input[str]`)
            * `username` (`pulumi.Input[str]`)
            * `virtualNetworkId` (`pulumi.Input[str]`)
            * `vm_size` (`pulumi.Input[str]`)
        
          * `workerNode` (`pulumi.Input[dict]`)
        
            * `minInstanceCount` (`pulumi.Input[float]`)
            * `password` (`pulumi.Input[str]`)
            * `sshKeys` (`pulumi.Input[list]`)
            * `subnet_id` (`pulumi.Input[str]`)
            * `targetInstanceCount` (`pulumi.Input[float]`)
            * `username` (`pulumi.Input[str]`)
            * `virtualNetworkId` (`pulumi.Input[str]`)
            * `vm_size` (`pulumi.Input[str]`)
        
          * `zookeeperNode` (`pulumi.Input[dict]`)
        
            * `password` (`pulumi.Input[str]`)
            * `sshKeys` (`pulumi.Input[list]`)
            * `subnet_id` (`pulumi.Input[str]`)
            * `username` (`pulumi.Input[str]`)
            * `virtualNetworkId` (`pulumi.Input[str]`)
            * `vm_size` (`pulumi.Input[str]`)
        
        The **storage_account_gen2** object supports the following:
        
          * `filesystemId` (`pulumi.Input[str]`)
          * `isDefault` (`pulumi.Input[bool]`)
          * `managedIdentityResourceId` (`pulumi.Input[str]`)
          * `storageResourceId` (`pulumi.Input[str]`)
        
        The **storage_accounts** object supports the following:
        
          * `isDefault` (`pulumi.Input[bool]`)
          * `storageAccountKey` (`pulumi.Input[str]`)
          * `storageContainerId` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_spark_cluster.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if cluster_version is None:
                raise TypeError("Missing required property 'cluster_version'")
            __props__['cluster_version'] = cluster_version
            if component_version is None:
                raise TypeError("Missing required property 'component_version'")
            __props__['component_version'] = component_version
            if gateway is None:
                raise TypeError("Missing required property 'gateway'")
            __props__['gateway'] = gateway
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if roles is None:
                raise TypeError("Missing required property 'roles'")
            __props__['roles'] = roles
            __props__['storage_accounts'] = storage_accounts
            __props__['storage_account_gen2'] = storage_account_gen2
            __props__['tags'] = tags
            if tier is None:
                raise TypeError("Missing required property 'tier'")
            __props__['tier'] = tier
            __props__['https_endpoint'] = None
            __props__['ssh_endpoint'] = None
        super(SparkCluster, __self__).__init__(
            'azure:hdinsight/sparkCluster:SparkCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cluster_version=None, component_version=None, gateway=None, https_endpoint=None, location=None, name=None, resource_group_name=None, roles=None, ssh_endpoint=None, storage_accounts=None, storage_account_gen2=None, tags=None, tier=None):
        """
        Get an existing SparkCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] component_version: A `component_version` block as defined below.
        :param pulumi.Input[dict] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] https_endpoint: The HTTPS Connectivity Endpoint for this HDInsight Spark Cluster.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] roles: A `roles` block as defined below.
        :param pulumi.Input[str] ssh_endpoint: The SSH Connectivity Endpoint for this HDInsight Spark Cluster.
        :param pulumi.Input[list] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[dict] storage_account_gen2: A `storage_account_gen2` block as defined below.
        :param pulumi.Input[dict] tags: A map of Tags which should be assigned to this HDInsight Spark Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        
        The **component_version** object supports the following:
        
          * `spark` (`pulumi.Input[str]`)
        
        The **gateway** object supports the following:
        
          * `enabled` (`pulumi.Input[bool]`)
          * `password` (`pulumi.Input[str]`)
          * `username` (`pulumi.Input[str]`)
        
        The **roles** object supports the following:
        
          * `headNode` (`pulumi.Input[dict]`)
        
            * `password` (`pulumi.Input[str]`)
            * `sshKeys` (`pulumi.Input[list]`)
            * `subnet_id` (`pulumi.Input[str]`)
            * `username` (`pulumi.Input[str]`)
            * `virtualNetworkId` (`pulumi.Input[str]`)
            * `vm_size` (`pulumi.Input[str]`)
        
          * `workerNode` (`pulumi.Input[dict]`)
        
            * `minInstanceCount` (`pulumi.Input[float]`)
            * `password` (`pulumi.Input[str]`)
            * `sshKeys` (`pulumi.Input[list]`)
            * `subnet_id` (`pulumi.Input[str]`)
            * `targetInstanceCount` (`pulumi.Input[float]`)
            * `username` (`pulumi.Input[str]`)
            * `virtualNetworkId` (`pulumi.Input[str]`)
            * `vm_size` (`pulumi.Input[str]`)
        
          * `zookeeperNode` (`pulumi.Input[dict]`)
        
            * `password` (`pulumi.Input[str]`)
            * `sshKeys` (`pulumi.Input[list]`)
            * `subnet_id` (`pulumi.Input[str]`)
            * `username` (`pulumi.Input[str]`)
            * `virtualNetworkId` (`pulumi.Input[str]`)
            * `vm_size` (`pulumi.Input[str]`)
        
        The **storage_account_gen2** object supports the following:
        
          * `filesystemId` (`pulumi.Input[str]`)
          * `isDefault` (`pulumi.Input[bool]`)
          * `managedIdentityResourceId` (`pulumi.Input[str]`)
          * `storageResourceId` (`pulumi.Input[str]`)
        
        The **storage_accounts** object supports the following:
        
          * `isDefault` (`pulumi.Input[bool]`)
          * `storageAccountKey` (`pulumi.Input[str]`)
          * `storageContainerId` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_spark_cluster.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["cluster_version"] = cluster_version
        __props__["component_version"] = component_version
        __props__["gateway"] = gateway
        __props__["https_endpoint"] = https_endpoint
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["roles"] = roles
        __props__["ssh_endpoint"] = ssh_endpoint
        __props__["storage_accounts"] = storage_accounts
        __props__["storage_account_gen2"] = storage_account_gen2
        __props__["tags"] = tags
        __props__["tier"] = tier
        return SparkCluster(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

