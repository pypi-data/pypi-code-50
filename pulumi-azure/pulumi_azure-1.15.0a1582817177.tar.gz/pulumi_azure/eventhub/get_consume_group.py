# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetConsumeGroupResult:
    """
    A collection of values returned by getConsumeGroup.
    """
    def __init__(__self__, eventhub_name=None, location=None, name=None, namespace_name=None, resource_group_name=None, user_metadata=None, id=None):
        if eventhub_name and not isinstance(eventhub_name, str):
            raise TypeError("Expected argument 'eventhub_name' to be a str")
        __self__.eventhub_name = eventhub_name
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if namespace_name and not isinstance(namespace_name, str):
            raise TypeError("Expected argument 'namespace_name' to be a str")
        __self__.namespace_name = namespace_name
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if user_metadata and not isinstance(user_metadata, str):
            raise TypeError("Expected argument 'user_metadata' to be a str")
        __self__.user_metadata = user_metadata
        """
        Specifies the user metadata.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetConsumeGroupResult(GetConsumeGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConsumeGroupResult(
            eventhub_name=self.eventhub_name,
            location=self.location,
            name=self.name,
            namespace_name=self.namespace_name,
            resource_group_name=self.resource_group_name,
            user_metadata=self.user_metadata,
            id=self.id)

def get_consume_group(eventhub_name=None,name=None,namespace_name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Event Hubs Consumer Group within an Event Hub.
    
    :param str eventhub_name: Specifies the name of the EventHub.
    :param str name: Specifies the name of the EventHub Consumer Group resource.
    :param str namespace_name: Specifies the name of the grandparent EventHub Namespace.
    :param str resource_group_name: The name of the resource group in which the EventHub Consumer Group's grandparent Namespace exists.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/eventhub_consumer_group.html.markdown.
    """
    __args__ = dict()

    __args__['eventhubName'] = eventhub_name
    __args__['name'] = name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:eventhub/getConsumeGroup:getConsumeGroup', __args__, opts=opts).value

    return AwaitableGetConsumeGroupResult(
        eventhub_name=__ret__.get('eventhubName'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        namespace_name=__ret__.get('namespaceName'),
        resource_group_name=__ret__.get('resourceGroupName'),
        user_metadata=__ret__.get('userMetadata'),
        id=__ret__.get('id'))
