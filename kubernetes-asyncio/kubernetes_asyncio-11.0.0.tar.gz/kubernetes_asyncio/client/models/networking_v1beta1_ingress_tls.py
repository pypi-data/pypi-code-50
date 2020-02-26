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


class NetworkingV1beta1IngressTLS(object):
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
        'hosts': 'list[str]',
        'secret_name': 'str'
    }

    attribute_map = {
        'hosts': 'hosts',
        'secret_name': 'secretName'
    }

    def __init__(self, hosts=None, secret_name=None, local_vars_configuration=None):  # noqa: E501
        """NetworkingV1beta1IngressTLS - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hosts = None
        self._secret_name = None
        self.discriminator = None

        if hosts is not None:
            self.hosts = hosts
        if secret_name is not None:
            self.secret_name = secret_name

    @property
    def hosts(self):
        """Gets the hosts of this NetworkingV1beta1IngressTLS.  # noqa: E501

        Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.  # noqa: E501

        :return: The hosts of this NetworkingV1beta1IngressTLS.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this NetworkingV1beta1IngressTLS.

        Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.  # noqa: E501

        :param hosts: The hosts of this NetworkingV1beta1IngressTLS.  # noqa: E501
        :type: list[str]
        """

        self._hosts = hosts

    @property
    def secret_name(self):
        """Gets the secret_name of this NetworkingV1beta1IngressTLS.  # noqa: E501

        SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener conflicts with the \"Host\" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.  # noqa: E501

        :return: The secret_name of this NetworkingV1beta1IngressTLS.  # noqa: E501
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this NetworkingV1beta1IngressTLS.

        SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener conflicts with the \"Host\" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.  # noqa: E501

        :param secret_name: The secret_name of this NetworkingV1beta1IngressTLS.  # noqa: E501
        :type: str
        """

        self._secret_name = secret_name

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
        if not isinstance(other, NetworkingV1beta1IngressTLS):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkingV1beta1IngressTLS):
            return True

        return self.to_dict() != other.to_dict()
