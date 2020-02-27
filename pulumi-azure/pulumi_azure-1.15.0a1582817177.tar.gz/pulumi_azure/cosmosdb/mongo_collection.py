# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class MongoCollection(pulumi.CustomResource):
    account_name: pulumi.Output[str]
    database_name: pulumi.Output[str]
    """
    The name of the Cosmos DB Mongo Database in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.
    """
    default_ttl_seconds: pulumi.Output[float]
    """
    The default Time To Live in seconds. If the value is `-1` items are not automatically expired.
    """
    indexes: pulumi.Output[list]
    """
    One or more `indexes` blocks as defined below.
    
      * `key` (`str`)
      * `unique` (`bool`)
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Cosmos DB Mongo Collection. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.
    """
    shard_key: pulumi.Output[str]
    """
    The name of the key to partition on for sharding. There must not be any other unique index keys.
    """
    throughput: pulumi.Output[float]
    def __init__(__self__, resource_name, opts=None, account_name=None, database_name=None, default_ttl_seconds=None, indexes=None, name=None, resource_group_name=None, shard_key=None, throughput=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Mongo Collection within a Cosmos DB Account.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name of the Cosmos DB Mongo Database in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[float] default_ttl_seconds: The default Time To Live in seconds. If the value is `-1` items are not automatically expired.
        :param pulumi.Input[list] indexes: One or more `indexes` blocks as defined below.
        :param pulumi.Input[str] name: Specifies the name of the Cosmos DB Mongo Collection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] shard_key: The name of the key to partition on for sharding. There must not be any other unique index keys.
        
        The **indexes** object supports the following:
        
          * `key` (`pulumi.Input[str]`)
          * `unique` (`pulumi.Input[bool]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cosmosdb_mongo_collection.html.markdown.
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

            if account_name is None:
                raise TypeError("Missing required property 'account_name'")
            __props__['account_name'] = account_name
            if database_name is None:
                raise TypeError("Missing required property 'database_name'")
            __props__['database_name'] = database_name
            __props__['default_ttl_seconds'] = default_ttl_seconds
            __props__['indexes'] = indexes
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['shard_key'] = shard_key
            __props__['throughput'] = throughput
        super(MongoCollection, __self__).__init__(
            'azure:cosmosdb/mongoCollection:MongoCollection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, account_name=None, database_name=None, default_ttl_seconds=None, indexes=None, name=None, resource_group_name=None, shard_key=None, throughput=None):
        """
        Get an existing MongoCollection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name of the Cosmos DB Mongo Database in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[float] default_ttl_seconds: The default Time To Live in seconds. If the value is `-1` items are not automatically expired.
        :param pulumi.Input[list] indexes: One or more `indexes` blocks as defined below.
        :param pulumi.Input[str] name: Specifies the name of the Cosmos DB Mongo Collection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] shard_key: The name of the key to partition on for sharding. There must not be any other unique index keys.
        
        The **indexes** object supports the following:
        
          * `key` (`pulumi.Input[str]`)
          * `unique` (`pulumi.Input[bool]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cosmosdb_mongo_collection.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["account_name"] = account_name
        __props__["database_name"] = database_name
        __props__["default_ttl_seconds"] = default_ttl_seconds
        __props__["indexes"] = indexes
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["shard_key"] = shard_key
        __props__["throughput"] = throughput
        return MongoCollection(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

