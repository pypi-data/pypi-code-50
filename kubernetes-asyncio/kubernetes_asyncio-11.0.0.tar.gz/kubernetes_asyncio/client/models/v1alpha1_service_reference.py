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


class V1alpha1ServiceReference(object):
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
        'name': 'str',
        'namespace': 'str',
        'path': 'str',
        'port': 'int'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'path': 'path',
        'port': 'port'
    }

    def __init__(self, name=None, namespace=None, path=None, port=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ServiceReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._namespace = None
        self._path = None
        self._port = None
        self.discriminator = None

        self.name = name
        self.namespace = namespace
        if path is not None:
            self.path = path
        if port is not None:
            self.port = port

    @property
    def name(self):
        """Gets the name of this V1alpha1ServiceReference.  # noqa: E501

        `name` is the name of the service. Required  # noqa: E501

        :return: The name of this V1alpha1ServiceReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1ServiceReference.

        `name` is the name of the service. Required  # noqa: E501

        :param name: The name of this V1alpha1ServiceReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1ServiceReference.  # noqa: E501

        `namespace` is the namespace of the service. Required  # noqa: E501

        :return: The namespace of this V1alpha1ServiceReference.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1ServiceReference.

        `namespace` is the namespace of the service. Required  # noqa: E501

        :param namespace: The namespace of this V1alpha1ServiceReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def path(self):
        """Gets the path of this V1alpha1ServiceReference.  # noqa: E501

        `path` is an optional URL path which will be sent in any request to this service.  # noqa: E501

        :return: The path of this V1alpha1ServiceReference.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1alpha1ServiceReference.

        `path` is an optional URL path which will be sent in any request to this service.  # noqa: E501

        :param path: The path of this V1alpha1ServiceReference.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def port(self):
        """Gets the port of this V1alpha1ServiceReference.  # noqa: E501

        If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive).  # noqa: E501

        :return: The port of this V1alpha1ServiceReference.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this V1alpha1ServiceReference.

        If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive).  # noqa: E501

        :param port: The port of this V1alpha1ServiceReference.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if not isinstance(other, V1alpha1ServiceReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ServiceReference):
            return True

        return self.to_dict() != other.to_dict()
