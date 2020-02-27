# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetSpotMarketRequestResult:
    """
    A collection of values returned by getSpotMarketRequest.
    """
    def __init__(__self__, device_ids=None, request_id=None, id=None):
        if device_ids and not isinstance(device_ids, list):
            raise TypeError("Expected argument 'device_ids' to be a list")
        __self__.device_ids = device_ids
        """
        List of IDs of devices spawned by the referenced Spot Market Request
        """
        if request_id and not isinstance(request_id, str):
            raise TypeError("Expected argument 'request_id' to be a str")
        __self__.request_id = request_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetSpotMarketRequestResult(GetSpotMarketRequestResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSpotMarketRequestResult(
            device_ids=self.device_ids,
            request_id=self.request_id,
            id=self.id)

def get_spot_market_request(request_id=None,opts=None):
    """
    Provides a Packet spot_market_request datasource. The datasource will contain list of device IDs created by referenced Spot Market Request.
    
    :param str request_id: The id of the Spot Market Request

    > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/spot_market_request.html.markdown.
    """
    __args__ = dict()

    __args__['requestId'] = request_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('packet:index/getSpotMarketRequest:getSpotMarketRequest', __args__, opts=opts).value

    return AwaitableGetSpotMarketRequestResult(
        device_ids=__ret__.get('deviceIds'),
        request_id=__ret__.get('requestId'),
        id=__ret__.get('id'))
