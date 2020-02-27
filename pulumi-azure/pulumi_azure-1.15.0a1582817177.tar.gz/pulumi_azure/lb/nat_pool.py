# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class NatPool(pulumi.CustomResource):
    backend_port: pulumi.Output[float]
    """
    The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.
    """
    frontend_ip_configuration_id: pulumi.Output[str]
    frontend_ip_configuration_name: pulumi.Output[str]
    """
    The name of the frontend IP configuration exposing this rule.
    """
    frontend_port_end: pulumi.Output[float]
    """
    The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.
    """
    frontend_port_start: pulumi.Output[float]
    """
    The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.
    """
    loadbalancer_id: pulumi.Output[str]
    """
    The ID of the Load Balancer in which to create the NAT pool.
    """
    location: pulumi.Output[str]
    name: pulumi.Output[str]
    """
    Specifies the name of the NAT pool.
    """
    protocol: pulumi.Output[str]
    """
    The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the resource.
    """
    def __init__(__self__, resource_name, opts=None, backend_port=None, frontend_ip_configuration_name=None, frontend_port_end=None, frontend_port_start=None, loadbalancer_id=None, location=None, name=None, protocol=None, resource_group_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Load Balancer NAT pool.
        
        > **NOTE:** This resource cannot be used with with virtual machines, instead use the `lb.NatRule` resource.
        
        > **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] backend_port: The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.
        :param pulumi.Input[str] frontend_ip_configuration_name: The name of the frontend IP configuration exposing this rule.
        :param pulumi.Input[float] frontend_port_end: The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.
        :param pulumi.Input[float] frontend_port_start: The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.
        :param pulumi.Input[str] loadbalancer_id: The ID of the Load Balancer in which to create the NAT pool.
        :param pulumi.Input[str] name: Specifies the name of the NAT pool.
        :param pulumi.Input[str] protocol: The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_pool.html.markdown.
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

            if backend_port is None:
                raise TypeError("Missing required property 'backend_port'")
            __props__['backend_port'] = backend_port
            if frontend_ip_configuration_name is None:
                raise TypeError("Missing required property 'frontend_ip_configuration_name'")
            __props__['frontend_ip_configuration_name'] = frontend_ip_configuration_name
            if frontend_port_end is None:
                raise TypeError("Missing required property 'frontend_port_end'")
            __props__['frontend_port_end'] = frontend_port_end
            if frontend_port_start is None:
                raise TypeError("Missing required property 'frontend_port_start'")
            __props__['frontend_port_start'] = frontend_port_start
            if loadbalancer_id is None:
                raise TypeError("Missing required property 'loadbalancer_id'")
            __props__['loadbalancer_id'] = loadbalancer_id
            __props__['location'] = location
            __props__['name'] = name
            if protocol is None:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['frontend_ip_configuration_id'] = None
        super(NatPool, __self__).__init__(
            'azure:lb/natPool:NatPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, backend_port=None, frontend_ip_configuration_id=None, frontend_ip_configuration_name=None, frontend_port_end=None, frontend_port_start=None, loadbalancer_id=None, location=None, name=None, protocol=None, resource_group_name=None):
        """
        Get an existing NatPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] backend_port: The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.
        :param pulumi.Input[str] frontend_ip_configuration_name: The name of the frontend IP configuration exposing this rule.
        :param pulumi.Input[float] frontend_port_end: The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.
        :param pulumi.Input[float] frontend_port_start: The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.
        :param pulumi.Input[str] loadbalancer_id: The ID of the Load Balancer in which to create the NAT pool.
        :param pulumi.Input[str] name: Specifies the name of the NAT pool.
        :param pulumi.Input[str] protocol: The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_pool.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["backend_port"] = backend_port
        __props__["frontend_ip_configuration_id"] = frontend_ip_configuration_id
        __props__["frontend_ip_configuration_name"] = frontend_ip_configuration_name
        __props__["frontend_port_end"] = frontend_port_end
        __props__["frontend_port_start"] = frontend_port_start
        __props__["loadbalancer_id"] = loadbalancer_id
        __props__["location"] = location
        __props__["name"] = name
        __props__["protocol"] = protocol
        __props__["resource_group_name"] = resource_group_name
        return NatPool(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

