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


class PolicyV1beta1AllowedHostPath(object):
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
        'path_prefix': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'path_prefix': 'pathPrefix',
        'read_only': 'readOnly'
    }

    def __init__(self, path_prefix=None, read_only=None, local_vars_configuration=None):  # noqa: E501
        """PolicyV1beta1AllowedHostPath - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path_prefix = None
        self._read_only = None
        self.discriminator = None

        if path_prefix is not None:
            self.path_prefix = path_prefix
        if read_only is not None:
            self.read_only = read_only

    @property
    def path_prefix(self):
        """Gets the path_prefix of this PolicyV1beta1AllowedHostPath.  # noqa: E501

        pathPrefix is the path prefix that the host volume must match. It does not support `*`. Trailing slashes are trimmed when validating the path prefix with a host path.  Examples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food` or `/etc/foo`  # noqa: E501

        :return: The path_prefix of this PolicyV1beta1AllowedHostPath.  # noqa: E501
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        """Sets the path_prefix of this PolicyV1beta1AllowedHostPath.

        pathPrefix is the path prefix that the host volume must match. It does not support `*`. Trailing slashes are trimmed when validating the path prefix with a host path.  Examples: `/foo` would allow `/foo`, `/foo/` and `/foo/bar` `/foo` would not allow `/food` or `/etc/foo`  # noqa: E501

        :param path_prefix: The path_prefix of this PolicyV1beta1AllowedHostPath.  # noqa: E501
        :type: str
        """

        self._path_prefix = path_prefix

    @property
    def read_only(self):
        """Gets the read_only of this PolicyV1beta1AllowedHostPath.  # noqa: E501

        when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.  # noqa: E501

        :return: The read_only of this PolicyV1beta1AllowedHostPath.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this PolicyV1beta1AllowedHostPath.

        when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.  # noqa: E501

        :param read_only: The read_only of this PolicyV1beta1AllowedHostPath.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, PolicyV1beta1AllowedHostPath):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyV1beta1AllowedHostPath):
            return True

        return self.to_dict() != other.to_dict()
