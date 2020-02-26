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


class V1VolumeProjection(object):
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
        'config_map': 'V1ConfigMapProjection',
        'downward_api': 'V1DownwardAPIProjection',
        'secret': 'V1SecretProjection',
        'service_account_token': 'V1ServiceAccountTokenProjection'
    }

    attribute_map = {
        'config_map': 'configMap',
        'downward_api': 'downwardAPI',
        'secret': 'secret',
        'service_account_token': 'serviceAccountToken'
    }

    def __init__(self, config_map=None, downward_api=None, secret=None, service_account_token=None, local_vars_configuration=None):  # noqa: E501
        """V1VolumeProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config_map = None
        self._downward_api = None
        self._secret = None
        self._service_account_token = None
        self.discriminator = None

        if config_map is not None:
            self.config_map = config_map
        if downward_api is not None:
            self.downward_api = downward_api
        if secret is not None:
            self.secret = secret
        if service_account_token is not None:
            self.service_account_token = service_account_token

    @property
    def config_map(self):
        """Gets the config_map of this V1VolumeProjection.  # noqa: E501


        :return: The config_map of this V1VolumeProjection.  # noqa: E501
        :rtype: V1ConfigMapProjection
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """Sets the config_map of this V1VolumeProjection.


        :param config_map: The config_map of this V1VolumeProjection.  # noqa: E501
        :type: V1ConfigMapProjection
        """

        self._config_map = config_map

    @property
    def downward_api(self):
        """Gets the downward_api of this V1VolumeProjection.  # noqa: E501


        :return: The downward_api of this V1VolumeProjection.  # noqa: E501
        :rtype: V1DownwardAPIProjection
        """
        return self._downward_api

    @downward_api.setter
    def downward_api(self, downward_api):
        """Sets the downward_api of this V1VolumeProjection.


        :param downward_api: The downward_api of this V1VolumeProjection.  # noqa: E501
        :type: V1DownwardAPIProjection
        """

        self._downward_api = downward_api

    @property
    def secret(self):
        """Gets the secret of this V1VolumeProjection.  # noqa: E501


        :return: The secret of this V1VolumeProjection.  # noqa: E501
        :rtype: V1SecretProjection
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this V1VolumeProjection.


        :param secret: The secret of this V1VolumeProjection.  # noqa: E501
        :type: V1SecretProjection
        """

        self._secret = secret

    @property
    def service_account_token(self):
        """Gets the service_account_token of this V1VolumeProjection.  # noqa: E501


        :return: The service_account_token of this V1VolumeProjection.  # noqa: E501
        :rtype: V1ServiceAccountTokenProjection
        """
        return self._service_account_token

    @service_account_token.setter
    def service_account_token(self, service_account_token):
        """Sets the service_account_token of this V1VolumeProjection.


        :param service_account_token: The service_account_token of this V1VolumeProjection.  # noqa: E501
        :type: V1ServiceAccountTokenProjection
        """

        self._service_account_token = service_account_token

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
        if not isinstance(other, V1VolumeProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VolumeProjection):
            return True

        return self.to_dict() != other.to_dict()
