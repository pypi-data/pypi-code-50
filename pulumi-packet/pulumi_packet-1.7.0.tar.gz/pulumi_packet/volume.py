# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Volume(pulumi.CustomResource):
    attachments: pulumi.Output[list]
    """
    A list of attachments, each with it's own `href` attribute
    
      * `href` (`str`)
    """
    billing_cycle: pulumi.Output[str]
    """
    The billing cycle, defaults to "hourly"
    """
    created: pulumi.Output[str]
    """
    The timestamp for when the volume was created
    """
    description: pulumi.Output[str]
    """
    Optional description for the volume
    """
    facility: pulumi.Output[str]
    """
    The facility to create the volume in
    """
    locked: pulumi.Output[bool]
    """
    Lock or unlock the volume
    """
    name: pulumi.Output[str]
    """
    The name of the volume
    """
    plan: pulumi.Output[str]
    """
    The service plan slug of the volume
    """
    project_id: pulumi.Output[str]
    """
    The packet project ID to deploy the volume in
    """
    size: pulumi.Output[float]
    """
    The size in GB to make the volume
    """
    snapshot_policies: pulumi.Output[list]
    """
    Optional list of snapshot policies
    
      * `snapshotCount` (`float`)
      * `snapshotFrequency` (`str`)
    """
    state: pulumi.Output[str]
    """
    The state of the volume
    """
    updated: pulumi.Output[str]
    """
    The timestamp for the last time the volume was updated
    """
    def __init__(__self__, resource_name, opts=None, billing_cycle=None, description=None, facility=None, locked=None, plan=None, project_id=None, size=None, snapshot_policies=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a Volume resource with the given unique name, props, and options.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_cycle: The billing cycle, defaults to "hourly"
        :param pulumi.Input[str] description: Optional description for the volume
        :param pulumi.Input[str] facility: The facility to create the volume in
        :param pulumi.Input[bool] locked: Lock or unlock the volume
        :param pulumi.Input[str] plan: The service plan slug of the volume
        :param pulumi.Input[str] project_id: The packet project ID to deploy the volume in
        :param pulumi.Input[float] size: The size in GB to make the volume
        :param pulumi.Input[list] snapshot_policies: Optional list of snapshot policies
        
        The **snapshot_policies** object supports the following:
        
          * `snapshotCount` (`pulumi.Input[float]`)
          * `snapshotFrequency` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/volume.html.markdown.
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

            __props__['billing_cycle'] = billing_cycle
            __props__['description'] = description
            if facility is None:
                raise TypeError("Missing required property 'facility'")
            __props__['facility'] = facility
            __props__['locked'] = locked
            if plan is None:
                raise TypeError("Missing required property 'plan'")
            __props__['plan'] = plan
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            if size is None:
                raise TypeError("Missing required property 'size'")
            __props__['size'] = size
            __props__['snapshot_policies'] = snapshot_policies
            __props__['attachments'] = None
            __props__['created'] = None
            __props__['name'] = None
            __props__['state'] = None
            __props__['updated'] = None
        super(Volume, __self__).__init__(
            'packet:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, attachments=None, billing_cycle=None, created=None, description=None, facility=None, locked=None, name=None, plan=None, project_id=None, size=None, snapshot_policies=None, state=None, updated=None):
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] attachments: A list of attachments, each with it's own `href` attribute
        :param pulumi.Input[str] billing_cycle: The billing cycle, defaults to "hourly"
        :param pulumi.Input[str] created: The timestamp for when the volume was created
        :param pulumi.Input[str] description: Optional description for the volume
        :param pulumi.Input[str] facility: The facility to create the volume in
        :param pulumi.Input[bool] locked: Lock or unlock the volume
        :param pulumi.Input[str] name: The name of the volume
        :param pulumi.Input[str] plan: The service plan slug of the volume
        :param pulumi.Input[str] project_id: The packet project ID to deploy the volume in
        :param pulumi.Input[float] size: The size in GB to make the volume
        :param pulumi.Input[list] snapshot_policies: Optional list of snapshot policies
        :param pulumi.Input[str] state: The state of the volume
        :param pulumi.Input[str] updated: The timestamp for the last time the volume was updated
        
        The **attachments** object supports the following:
        
          * `href` (`pulumi.Input[str]`)
        
        The **snapshot_policies** object supports the following:
        
          * `snapshotCount` (`pulumi.Input[float]`)
          * `snapshotFrequency` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/volume.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["attachments"] = attachments
        __props__["billing_cycle"] = billing_cycle
        __props__["created"] = created
        __props__["description"] = description
        __props__["facility"] = facility
        __props__["locked"] = locked
        __props__["name"] = name
        __props__["plan"] = plan
        __props__["project_id"] = project_id
        __props__["size"] = size
        __props__["snapshot_policies"] = snapshot_policies
        __props__["state"] = state
        __props__["updated"] = updated
        return Volume(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

