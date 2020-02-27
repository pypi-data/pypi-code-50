# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Job(pulumi.CustomResource):
    compatibility_level: pulumi.Output[str]
    """
    Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are `1.0` and `1.1`.
    """
    data_locale: pulumi.Output[str]
    """
    Specifies the Data Locale of the Job, which [should be a supported .NET Culture](https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx).
    """
    events_late_arrival_max_delay_in_seconds: pulumi.Output[float]
    """
    Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is `-1` (indefinite) to `1814399` (20d 23h 59m 59s).  Default is `0`.
    """
    events_out_of_order_max_delay_in_seconds: pulumi.Output[float]
    """
    Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is `0` to `599` (9m 59s). Default is `5`.
    """
    events_out_of_order_policy: pulumi.Output[str]
    """
    Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are `Adjust` and `Drop`.  Default is `Adjust`.
    """
    job_id: pulumi.Output[str]
    """
    The Job ID assigned by the Stream Analytics Job.
    """
    location: pulumi.Output[str]
    """
    The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    The name of the Stream Analytics Job. Changing this forces a new resource to be created.
    """
    output_error_policy: pulumi.Output[str]
    """
    Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are `Drop` and `Stop`.  Default is `Drop`.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.
    """
    streaming_units: pulumi.Output[float]
    """
    Specifies the number of streaming units that the streaming job uses. Supported values are `1`, `3`, `6` and multiples of `6` up to `120`.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags assigned to the resource.
    """
    transformation_query: pulumi.Output[str]
    """
    Specifies the query that will be run in the streaming job, [written in Stream Analytics Query Language (SAQL)](https://msdn.microsoft.com/library/azure/dn834998).
    """
    def __init__(__self__, resource_name, opts=None, compatibility_level=None, data_locale=None, events_late_arrival_max_delay_in_seconds=None, events_out_of_order_max_delay_in_seconds=None, events_out_of_order_policy=None, location=None, name=None, output_error_policy=None, resource_group_name=None, streaming_units=None, tags=None, transformation_query=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Stream Analytics Job.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compatibility_level: Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are `1.0` and `1.1`.
        :param pulumi.Input[str] data_locale: Specifies the Data Locale of the Job, which [should be a supported .NET Culture](https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx).
        :param pulumi.Input[float] events_late_arrival_max_delay_in_seconds: Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is `-1` (indefinite) to `1814399` (20d 23h 59m 59s).  Default is `0`.
        :param pulumi.Input[float] events_out_of_order_max_delay_in_seconds: Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is `0` to `599` (9m 59s). Default is `5`.
        :param pulumi.Input[str] events_out_of_order_policy: Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are `Adjust` and `Drop`.  Default is `Adjust`.
        :param pulumi.Input[str] location: The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        :param pulumi.Input[str] output_error_policy: Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are `Drop` and `Stop`.  Default is `Drop`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[float] streaming_units: Specifies the number of streaming units that the streaming job uses. Supported values are `1`, `3`, `6` and multiples of `6` up to `120`.
        :param pulumi.Input[dict] tags: A mapping of tags assigned to the resource.
        :param pulumi.Input[str] transformation_query: Specifies the query that will be run in the streaming job, [written in Stream Analytics Query Language (SAQL)](https://msdn.microsoft.com/library/azure/dn834998).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_job.html.markdown.
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

            __props__['compatibility_level'] = compatibility_level
            __props__['data_locale'] = data_locale
            __props__['events_late_arrival_max_delay_in_seconds'] = events_late_arrival_max_delay_in_seconds
            __props__['events_out_of_order_max_delay_in_seconds'] = events_out_of_order_max_delay_in_seconds
            __props__['events_out_of_order_policy'] = events_out_of_order_policy
            __props__['location'] = location
            __props__['name'] = name
            __props__['output_error_policy'] = output_error_policy
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if streaming_units is None:
                raise TypeError("Missing required property 'streaming_units'")
            __props__['streaming_units'] = streaming_units
            __props__['tags'] = tags
            if transformation_query is None:
                raise TypeError("Missing required property 'transformation_query'")
            __props__['transformation_query'] = transformation_query
            __props__['job_id'] = None
        super(Job, __self__).__init__(
            'azure:streamanalytics/job:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, compatibility_level=None, data_locale=None, events_late_arrival_max_delay_in_seconds=None, events_out_of_order_max_delay_in_seconds=None, events_out_of_order_policy=None, job_id=None, location=None, name=None, output_error_policy=None, resource_group_name=None, streaming_units=None, tags=None, transformation_query=None):
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compatibility_level: Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are `1.0` and `1.1`.
        :param pulumi.Input[str] data_locale: Specifies the Data Locale of the Job, which [should be a supported .NET Culture](https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx).
        :param pulumi.Input[float] events_late_arrival_max_delay_in_seconds: Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is `-1` (indefinite) to `1814399` (20d 23h 59m 59s).  Default is `0`.
        :param pulumi.Input[float] events_out_of_order_max_delay_in_seconds: Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is `0` to `599` (9m 59s). Default is `5`.
        :param pulumi.Input[str] events_out_of_order_policy: Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are `Adjust` and `Drop`.  Default is `Adjust`.
        :param pulumi.Input[str] job_id: The Job ID assigned by the Stream Analytics Job.
        :param pulumi.Input[str] location: The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Stream Analytics Job. Changing this forces a new resource to be created.
        :param pulumi.Input[str] output_error_policy: Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are `Drop` and `Stop`.  Default is `Drop`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[float] streaming_units: Specifies the number of streaming units that the streaming job uses. Supported values are `1`, `3`, `6` and multiples of `6` up to `120`.
        :param pulumi.Input[dict] tags: A mapping of tags assigned to the resource.
        :param pulumi.Input[str] transformation_query: Specifies the query that will be run in the streaming job, [written in Stream Analytics Query Language (SAQL)](https://msdn.microsoft.com/library/azure/dn834998).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/stream_analytics_job.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["compatibility_level"] = compatibility_level
        __props__["data_locale"] = data_locale
        __props__["events_late_arrival_max_delay_in_seconds"] = events_late_arrival_max_delay_in_seconds
        __props__["events_out_of_order_max_delay_in_seconds"] = events_out_of_order_max_delay_in_seconds
        __props__["events_out_of_order_policy"] = events_out_of_order_policy
        __props__["job_id"] = job_id
        __props__["location"] = location
        __props__["name"] = name
        __props__["output_error_policy"] = output_error_policy
        __props__["resource_group_name"] = resource_group_name
        __props__["streaming_units"] = streaming_units
        __props__["tags"] = tags
        __props__["transformation_query"] = transformation_query
        return Job(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

