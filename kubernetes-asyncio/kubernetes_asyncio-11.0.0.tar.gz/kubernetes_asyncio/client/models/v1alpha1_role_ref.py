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


class V1alpha1RoleRef(object):
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
        'api_group': 'str',
        'kind': 'str',
        'name': 'str'
    }

    attribute_map = {
        'api_group': 'apiGroup',
        'kind': 'kind',
        'name': 'name'
    }

    def __init__(self, api_group=None, kind=None, name=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1RoleRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_group = None
        self._kind = None
        self._name = None
        self.discriminator = None

        self.api_group = api_group
        self.kind = kind
        self.name = name

    @property
    def api_group(self):
        """Gets the api_group of this V1alpha1RoleRef.  # noqa: E501

        APIGroup is the group for the resource being referenced  # noqa: E501

        :return: The api_group of this V1alpha1RoleRef.  # noqa: E501
        :rtype: str
        """
        return self._api_group

    @api_group.setter
    def api_group(self, api_group):
        """Sets the api_group of this V1alpha1RoleRef.

        APIGroup is the group for the resource being referenced  # noqa: E501

        :param api_group: The api_group of this V1alpha1RoleRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_group is None:  # noqa: E501
            raise ValueError("Invalid value for `api_group`, must not be `None`")  # noqa: E501

        self._api_group = api_group

    @property
    def kind(self):
        """Gets the kind of this V1alpha1RoleRef.  # noqa: E501

        Kind is the type of resource being referenced  # noqa: E501

        :return: The kind of this V1alpha1RoleRef.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1alpha1RoleRef.

        Kind is the type of resource being referenced  # noqa: E501

        :param kind: The kind of this V1alpha1RoleRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this V1alpha1RoleRef.  # noqa: E501

        Name is the name of resource being referenced  # noqa: E501

        :return: The name of this V1alpha1RoleRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1RoleRef.

        Name is the name of resource being referenced  # noqa: E501

        :param name: The name of this V1alpha1RoleRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, V1alpha1RoleRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1RoleRef):
            return True

        return self.to_dict() != other.to_dict()
