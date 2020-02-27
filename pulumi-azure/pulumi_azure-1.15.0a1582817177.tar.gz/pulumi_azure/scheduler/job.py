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
    action_storage_queue: pulumi.Output[dict]
    """
    A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.
    
      * `message` (`str`)
      * `sasToken` (`str`)
      * `storageAccountName` (`str`)
      * `storageQueueName` (`str`)
    """
    action_web: pulumi.Output[dict]
    """
    A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.
    
      * `authenticationActiveDirectory` (`dict`)
    
        * `audience` (`str`)
        * `client_id` (`str`)
        * `secret` (`str`)
        * `tenant_id` (`str`)
    
      * `authenticationBasic` (`dict`)
    
        * `password` (`str`)
        * `username` (`str`)
    
      * `authenticationCertificate` (`dict`)
    
        * `expiration` (`str`) - (Computed)  The certificate expiration date.
        * `password` (`str`)
        * `pfx` (`str`)
        * `subject_name` (`str`) - (Computed) The certificate's certificate subject name.
        * `thumbprint` (`str`) - (Computed) The certificate thumbprint.
    
      * `body` (`str`)
      * `headers` (`dict`)
      * `method` (`str`)
      * `url` (`str`)
    """
    error_action_storage_queue: pulumi.Output[dict]
    """
    A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.
    
      * `message` (`str`)
      * `sasToken` (`str`)
      * `storageAccountName` (`str`)
      * `storageQueueName` (`str`)
    """
    error_action_web: pulumi.Output[dict]
    """
    A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.
    
      * `authenticationActiveDirectory` (`dict`)
    
        * `audience` (`str`)
        * `client_id` (`str`)
        * `secret` (`str`)
        * `tenant_id` (`str`)
    
      * `authenticationBasic` (`dict`)
    
        * `password` (`str`)
        * `username` (`str`)
    
      * `authenticationCertificate` (`dict`)
    
        * `expiration` (`str`) - (Computed)  The certificate expiration date.
        * `password` (`str`)
        * `pfx` (`str`)
        * `subject_name` (`str`) - (Computed) The certificate's certificate subject name.
        * `thumbprint` (`str`) - (Computed) The certificate thumbprint.
    
      * `body` (`str`)
      * `headers` (`dict`)
      * `method` (`str`)
      * `url` (`str`)
    """
    job_collection_name: pulumi.Output[str]
    """
    Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    The name of the Scheduler Job. Changing this forces a new resource to be created.
    """
    recurrence: pulumi.Output[dict]
    """
    A `recurrence` block defining a job occurrence schedule.
    
      * `count` (`float`)
      * `end_time` (`str`)
      * `frequency` (`str`)
      * `hours` (`list`)
      * `interval` (`float`)
      * `minutes` (`list`)
      * `month_days` (`list`)
      * `monthly_occurrences` (`list`)
    
        * `day` (`str`)
        * `occurrence` (`float`)
    
      * `week_days` (`list`)
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.
    """
    retry: pulumi.Output[dict]
    """
    A `retry` block defining how to retry as described below.
    
      * `count` (`float`)
      * `interval` (`str`)
    """
    start_time: pulumi.Output[str]
    """
    The time the first instance of the job is to start running at.
    """
    state: pulumi.Output[str]
    """
    The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`
    """
    def __init__(__self__, resource_name, opts=None, action_storage_queue=None, action_web=None, error_action_storage_queue=None, error_action_web=None, job_collection_name=None, name=None, recurrence=None, resource_group_name=None, retry=None, start_time=None, state=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Scheduler Job.
        
        > **NOTE:** Support for Scheduler Job has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] action_storage_queue: A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.
        :param pulumi.Input[dict] action_web: A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.
        :param pulumi.Input[dict] error_action_storage_queue: A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.
        :param pulumi.Input[dict] error_action_web: A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.
        :param pulumi.Input[str] job_collection_name: Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Scheduler Job. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] recurrence: A `recurrence` block defining a job occurrence schedule.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] retry: A `retry` block defining how to retry as described below.
        :param pulumi.Input[str] start_time: The time the first instance of the job is to start running at.
        :param pulumi.Input[str] state: The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`
        
        The **action_storage_queue** object supports the following:
        
          * `message` (`pulumi.Input[str]`)
          * `sasToken` (`pulumi.Input[str]`)
          * `storageAccountName` (`pulumi.Input[str]`)
          * `storageQueueName` (`pulumi.Input[str]`)
        
        The **action_web** object supports the following:
        
          * `authenticationActiveDirectory` (`pulumi.Input[dict]`)
        
            * `audience` (`pulumi.Input[str]`)
            * `client_id` (`pulumi.Input[str]`)
            * `secret` (`pulumi.Input[str]`)
            * `tenant_id` (`pulumi.Input[str]`)
        
          * `authenticationBasic` (`pulumi.Input[dict]`)
        
            * `password` (`pulumi.Input[str]`)
            * `username` (`pulumi.Input[str]`)
        
          * `authenticationCertificate` (`pulumi.Input[dict]`)
        
            * `expiration` (`pulumi.Input[str]`) - (Computed)  The certificate expiration date.
            * `password` (`pulumi.Input[str]`)
            * `pfx` (`pulumi.Input[str]`)
            * `subject_name` (`pulumi.Input[str]`) - (Computed) The certificate's certificate subject name.
            * `thumbprint` (`pulumi.Input[str]`) - (Computed) The certificate thumbprint.
        
          * `body` (`pulumi.Input[str]`)
          * `headers` (`pulumi.Input[dict]`)
          * `method` (`pulumi.Input[str]`)
          * `url` (`pulumi.Input[str]`)
        
        The **error_action_storage_queue** object supports the following:
        
          * `message` (`pulumi.Input[str]`)
          * `sasToken` (`pulumi.Input[str]`)
          * `storageAccountName` (`pulumi.Input[str]`)
          * `storageQueueName` (`pulumi.Input[str]`)
        
        The **error_action_web** object supports the following:
        
          * `authenticationActiveDirectory` (`pulumi.Input[dict]`)
        
            * `audience` (`pulumi.Input[str]`)
            * `client_id` (`pulumi.Input[str]`)
            * `secret` (`pulumi.Input[str]`)
            * `tenant_id` (`pulumi.Input[str]`)
        
          * `authenticationBasic` (`pulumi.Input[dict]`)
        
            * `password` (`pulumi.Input[str]`)
            * `username` (`pulumi.Input[str]`)
        
          * `authenticationCertificate` (`pulumi.Input[dict]`)
        
            * `expiration` (`pulumi.Input[str]`) - (Computed)  The certificate expiration date.
            * `password` (`pulumi.Input[str]`)
            * `pfx` (`pulumi.Input[str]`)
            * `subject_name` (`pulumi.Input[str]`) - (Computed) The certificate's certificate subject name.
            * `thumbprint` (`pulumi.Input[str]`) - (Computed) The certificate thumbprint.
        
          * `body` (`pulumi.Input[str]`)
          * `headers` (`pulumi.Input[dict]`)
          * `method` (`pulumi.Input[str]`)
          * `url` (`pulumi.Input[str]`)
        
        The **recurrence** object supports the following:
        
          * `count` (`pulumi.Input[float]`)
          * `end_time` (`pulumi.Input[str]`)
          * `frequency` (`pulumi.Input[str]`)
          * `hours` (`pulumi.Input[list]`)
          * `interval` (`pulumi.Input[float]`)
          * `minutes` (`pulumi.Input[list]`)
          * `month_days` (`pulumi.Input[list]`)
          * `monthly_occurrences` (`pulumi.Input[list]`)
        
            * `day` (`pulumi.Input[str]`)
            * `occurrence` (`pulumi.Input[float]`)
        
          * `week_days` (`pulumi.Input[list]`)
        
        The **retry** object supports the following:
        
          * `count` (`pulumi.Input[float]`)
          * `interval` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/scheduler_job.html.markdown.
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

            __props__['action_storage_queue'] = action_storage_queue
            __props__['action_web'] = action_web
            __props__['error_action_storage_queue'] = error_action_storage_queue
            __props__['error_action_web'] = error_action_web
            if job_collection_name is None:
                raise TypeError("Missing required property 'job_collection_name'")
            __props__['job_collection_name'] = job_collection_name
            __props__['name'] = name
            __props__['recurrence'] = recurrence
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['retry'] = retry
            __props__['start_time'] = start_time
            __props__['state'] = state
        super(Job, __self__).__init__(
            'azure:scheduler/job:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, action_storage_queue=None, action_web=None, error_action_storage_queue=None, error_action_web=None, job_collection_name=None, name=None, recurrence=None, resource_group_name=None, retry=None, start_time=None, state=None):
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] action_storage_queue: A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.
        :param pulumi.Input[dict] action_web: A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.
        :param pulumi.Input[dict] error_action_storage_queue: A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.
        :param pulumi.Input[dict] error_action_web: A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.
        :param pulumi.Input[str] job_collection_name: Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Scheduler Job. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] recurrence: A `recurrence` block defining a job occurrence schedule.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] retry: A `retry` block defining how to retry as described below.
        :param pulumi.Input[str] start_time: The time the first instance of the job is to start running at.
        :param pulumi.Input[str] state: The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`
        
        The **action_storage_queue** object supports the following:
        
          * `message` (`pulumi.Input[str]`)
          * `sasToken` (`pulumi.Input[str]`)
          * `storageAccountName` (`pulumi.Input[str]`)
          * `storageQueueName` (`pulumi.Input[str]`)
        
        The **action_web** object supports the following:
        
          * `authenticationActiveDirectory` (`pulumi.Input[dict]`)
        
            * `audience` (`pulumi.Input[str]`)
            * `client_id` (`pulumi.Input[str]`)
            * `secret` (`pulumi.Input[str]`)
            * `tenant_id` (`pulumi.Input[str]`)
        
          * `authenticationBasic` (`pulumi.Input[dict]`)
        
            * `password` (`pulumi.Input[str]`)
            * `username` (`pulumi.Input[str]`)
        
          * `authenticationCertificate` (`pulumi.Input[dict]`)
        
            * `expiration` (`pulumi.Input[str]`) - (Computed)  The certificate expiration date.
            * `password` (`pulumi.Input[str]`)
            * `pfx` (`pulumi.Input[str]`)
            * `subject_name` (`pulumi.Input[str]`) - (Computed) The certificate's certificate subject name.
            * `thumbprint` (`pulumi.Input[str]`) - (Computed) The certificate thumbprint.
        
          * `body` (`pulumi.Input[str]`)
          * `headers` (`pulumi.Input[dict]`)
          * `method` (`pulumi.Input[str]`)
          * `url` (`pulumi.Input[str]`)
        
        The **error_action_storage_queue** object supports the following:
        
          * `message` (`pulumi.Input[str]`)
          * `sasToken` (`pulumi.Input[str]`)
          * `storageAccountName` (`pulumi.Input[str]`)
          * `storageQueueName` (`pulumi.Input[str]`)
        
        The **error_action_web** object supports the following:
        
          * `authenticationActiveDirectory` (`pulumi.Input[dict]`)
        
            * `audience` (`pulumi.Input[str]`)
            * `client_id` (`pulumi.Input[str]`)
            * `secret` (`pulumi.Input[str]`)
            * `tenant_id` (`pulumi.Input[str]`)
        
          * `authenticationBasic` (`pulumi.Input[dict]`)
        
            * `password` (`pulumi.Input[str]`)
            * `username` (`pulumi.Input[str]`)
        
          * `authenticationCertificate` (`pulumi.Input[dict]`)
        
            * `expiration` (`pulumi.Input[str]`) - (Computed)  The certificate expiration date.
            * `password` (`pulumi.Input[str]`)
            * `pfx` (`pulumi.Input[str]`)
            * `subject_name` (`pulumi.Input[str]`) - (Computed) The certificate's certificate subject name.
            * `thumbprint` (`pulumi.Input[str]`) - (Computed) The certificate thumbprint.
        
          * `body` (`pulumi.Input[str]`)
          * `headers` (`pulumi.Input[dict]`)
          * `method` (`pulumi.Input[str]`)
          * `url` (`pulumi.Input[str]`)
        
        The **recurrence** object supports the following:
        
          * `count` (`pulumi.Input[float]`)
          * `end_time` (`pulumi.Input[str]`)
          * `frequency` (`pulumi.Input[str]`)
          * `hours` (`pulumi.Input[list]`)
          * `interval` (`pulumi.Input[float]`)
          * `minutes` (`pulumi.Input[list]`)
          * `month_days` (`pulumi.Input[list]`)
          * `monthly_occurrences` (`pulumi.Input[list]`)
        
            * `day` (`pulumi.Input[str]`)
            * `occurrence` (`pulumi.Input[float]`)
        
          * `week_days` (`pulumi.Input[list]`)
        
        The **retry** object supports the following:
        
          * `count` (`pulumi.Input[float]`)
          * `interval` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/scheduler_job.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["action_storage_queue"] = action_storage_queue
        __props__["action_web"] = action_web
        __props__["error_action_storage_queue"] = error_action_storage_queue
        __props__["error_action_web"] = error_action_web
        __props__["job_collection_name"] = job_collection_name
        __props__["name"] = name
        __props__["recurrence"] = recurrence
        __props__["resource_group_name"] = resource_group_name
        __props__["retry"] = retry
        __props__["start_time"] = start_time
        __props__["state"] = state
        return Job(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

