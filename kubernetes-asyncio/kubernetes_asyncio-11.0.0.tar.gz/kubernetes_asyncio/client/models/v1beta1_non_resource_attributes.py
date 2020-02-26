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


class V1beta1NonResourceAttributes(object):
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
        'path': 'str',
        'verb': 'str'
    }

    attribute_map = {
        'path': 'path',
        'verb': 'verb'
    }

    def __init__(self, path=None, verb=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1NonResourceAttributes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._verb = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if verb is not None:
            self.verb = verb

    @property
    def path(self):
        """Gets the path of this V1beta1NonResourceAttributes.  # noqa: E501

        Path is the URL path of the request  # noqa: E501

        :return: The path of this V1beta1NonResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1beta1NonResourceAttributes.

        Path is the URL path of the request  # noqa: E501

        :param path: The path of this V1beta1NonResourceAttributes.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def verb(self):
        """Gets the verb of this V1beta1NonResourceAttributes.  # noqa: E501

        Verb is the standard HTTP verb  # noqa: E501

        :return: The verb of this V1beta1NonResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this V1beta1NonResourceAttributes.

        Verb is the standard HTTP verb  # noqa: E501

        :param verb: The verb of this V1beta1NonResourceAttributes.  # noqa: E501
        :type: str
        """

        self._verb = verb

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
        if not isinstance(other, V1beta1NonResourceAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1NonResourceAttributes):
            return True

        return self.to_dict() != other.to_dict()
