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


class V1ScopedResourceSelectorRequirement(object):
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
        'operator': 'str',
        'scope_name': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'operator': 'operator',
        'scope_name': 'scopeName',
        'values': 'values'
    }

    def __init__(self, operator=None, scope_name=None, values=None, local_vars_configuration=None):  # noqa: E501
        """V1ScopedResourceSelectorRequirement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._operator = None
        self._scope_name = None
        self._values = None
        self.discriminator = None

        self.operator = operator
        self.scope_name = scope_name
        if values is not None:
            self.values = values

    @property
    def operator(self):
        """Gets the operator of this V1ScopedResourceSelectorRequirement.  # noqa: E501

        Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.  # noqa: E501

        :return: The operator of this V1ScopedResourceSelectorRequirement.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this V1ScopedResourceSelectorRequirement.

        Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.  # noqa: E501

        :param operator: The operator of this V1ScopedResourceSelectorRequirement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def scope_name(self):
        """Gets the scope_name of this V1ScopedResourceSelectorRequirement.  # noqa: E501

        The name of the scope that the selector applies to.  # noqa: E501

        :return: The scope_name of this V1ScopedResourceSelectorRequirement.  # noqa: E501
        :rtype: str
        """
        return self._scope_name

    @scope_name.setter
    def scope_name(self, scope_name):
        """Sets the scope_name of this V1ScopedResourceSelectorRequirement.

        The name of the scope that the selector applies to.  # noqa: E501

        :param scope_name: The scope_name of this V1ScopedResourceSelectorRequirement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scope_name is None:  # noqa: E501
            raise ValueError("Invalid value for `scope_name`, must not be `None`")  # noqa: E501

        self._scope_name = scope_name

    @property
    def values(self):
        """Gets the values of this V1ScopedResourceSelectorRequirement.  # noqa: E501

        An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.  # noqa: E501

        :return: The values of this V1ScopedResourceSelectorRequirement.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this V1ScopedResourceSelectorRequirement.

        An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.  # noqa: E501

        :param values: The values of this V1ScopedResourceSelectorRequirement.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if not isinstance(other, V1ScopedResourceSelectorRequirement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ScopedResourceSelectorRequirement):
            return True

        return self.to_dict() != other.to_dict()
