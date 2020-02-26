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


class V1alpha1ClusterRole(object):
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
        'aggregation_rule': 'V1alpha1AggregationRule',
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'rules': 'list[V1alpha1PolicyRule]'
    }

    attribute_map = {
        'aggregation_rule': 'aggregationRule',
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'rules': 'rules'
    }

    def __init__(self, aggregation_rule=None, api_version=None, kind=None, metadata=None, rules=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ClusterRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aggregation_rule = None
        self._api_version = None
        self._kind = None
        self._metadata = None
        self._rules = None
        self.discriminator = None

        if aggregation_rule is not None:
            self.aggregation_rule = aggregation_rule
        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if rules is not None:
            self.rules = rules

    @property
    def aggregation_rule(self):
        """Gets the aggregation_rule of this V1alpha1ClusterRole.  # noqa: E501


        :return: The aggregation_rule of this V1alpha1ClusterRole.  # noqa: E501
        :rtype: V1alpha1AggregationRule
        """
        return self._aggregation_rule

    @aggregation_rule.setter
    def aggregation_rule(self, aggregation_rule):
        """Sets the aggregation_rule of this V1alpha1ClusterRole.


        :param aggregation_rule: The aggregation_rule of this V1alpha1ClusterRole.  # noqa: E501
        :type: V1alpha1AggregationRule
        """

        self._aggregation_rule = aggregation_rule

    @property
    def api_version(self):
        """Gets the api_version of this V1alpha1ClusterRole.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1alpha1ClusterRole.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1alpha1ClusterRole.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1alpha1ClusterRole.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this V1alpha1ClusterRole.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1alpha1ClusterRole.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1alpha1ClusterRole.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1alpha1ClusterRole.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1ClusterRole.  # noqa: E501


        :return: The metadata of this V1alpha1ClusterRole.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1ClusterRole.


        :param metadata: The metadata of this V1alpha1ClusterRole.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def rules(self):
        """Gets the rules of this V1alpha1ClusterRole.  # noqa: E501

        Rules holds all the PolicyRules for this ClusterRole  # noqa: E501

        :return: The rules of this V1alpha1ClusterRole.  # noqa: E501
        :rtype: list[V1alpha1PolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this V1alpha1ClusterRole.

        Rules holds all the PolicyRules for this ClusterRole  # noqa: E501

        :param rules: The rules of this V1alpha1ClusterRole.  # noqa: E501
        :type: list[V1alpha1PolicyRule]
        """

        self._rules = rules

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
        if not isinstance(other, V1alpha1ClusterRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ClusterRole):
            return True

        return self.to_dict() != other.to_dict()
