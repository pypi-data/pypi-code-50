# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.15.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1EventSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'component': 'str',
        'host': 'str'
    }

    attribute_map = {
        'component': 'component',
        'host': 'host'
    }

    def __init__(self, component=None, host=None, local_vars_configuration=None):  # noqa: E501
        """V1EventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._component = None
        self._host = None
        self.discriminator = None

        if component is not None:
            self.component = component
        if host is not None:
            self.host = host

    @property
    def component(self):
        """Gets the component of this V1EventSource.  # noqa: E501

        Component from which the event is generated.  # noqa: E501

        :return: The component of this V1EventSource.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this V1EventSource.

        Component from which the event is generated.  # noqa: E501

        :param component: The component of this V1EventSource.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def host(self):
        """Gets the host of this V1EventSource.  # noqa: E501

        Node name on which the event is generated.  # noqa: E501

        :return: The host of this V1EventSource.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this V1EventSource.

        Node name on which the event is generated.  # noqa: E501

        :param host: The host of this V1EventSource.  # noqa: E501
        :type: str
        """

        self._host = host

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1EventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1EventSource):
            return True

        return self.to_dict() != other.to_dict()
