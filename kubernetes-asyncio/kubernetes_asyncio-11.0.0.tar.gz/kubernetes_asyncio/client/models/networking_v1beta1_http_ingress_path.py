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


class NetworkingV1beta1HTTPIngressPath(object):
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
        'backend': 'NetworkingV1beta1IngressBackend',
        'path': 'str'
    }

    attribute_map = {
        'backend': 'backend',
        'path': 'path'
    }

    def __init__(self, backend=None, path=None, local_vars_configuration=None):  # noqa: E501
        """NetworkingV1beta1HTTPIngressPath - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._backend = None
        self._path = None
        self.discriminator = None

        self.backend = backend
        if path is not None:
            self.path = path

    @property
    def backend(self):
        """Gets the backend of this NetworkingV1beta1HTTPIngressPath.  # noqa: E501


        :return: The backend of this NetworkingV1beta1HTTPIngressPath.  # noqa: E501
        :rtype: NetworkingV1beta1IngressBackend
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this NetworkingV1beta1HTTPIngressPath.


        :param backend: The backend of this NetworkingV1beta1HTTPIngressPath.  # noqa: E501
        :type: NetworkingV1beta1IngressBackend
        """
        if self.local_vars_configuration.client_side_validation and backend is None:  # noqa: E501
            raise ValueError("Invalid value for `backend`, must not be `None`")  # noqa: E501

        self._backend = backend

    @property
    def path(self):
        """Gets the path of this NetworkingV1beta1HTTPIngressPath.  # noqa: E501

        Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \"path\" part of a URL as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a catch all sending traffic to the backend.  # noqa: E501

        :return: The path of this NetworkingV1beta1HTTPIngressPath.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NetworkingV1beta1HTTPIngressPath.

        Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \"path\" part of a URL as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a catch all sending traffic to the backend.  # noqa: E501

        :param path: The path of this NetworkingV1beta1HTTPIngressPath.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if not isinstance(other, NetworkingV1beta1HTTPIngressPath):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkingV1beta1HTTPIngressPath):
            return True

        return self.to_dict() != other.to_dict()
