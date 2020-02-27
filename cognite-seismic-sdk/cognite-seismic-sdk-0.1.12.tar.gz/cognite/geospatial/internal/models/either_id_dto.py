# coding: utf-8

"""
    Cognite API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: playground
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cognite.geospatial.internal.configuration import Configuration


class EitherIdDTO(object):
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
        'id': 'int',
        'external_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'externalId'
    }

    def __init__(self, id=None, external_id=None, local_vars_configuration=None):  # noqa: E501
        """EitherIdDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._external_id = None
        self.discriminator = None

        self.id = id
        self.external_id = external_id

    @property
    def id(self):
        """Gets the id of this EitherIdDTO.  # noqa: E501

        A JavaScript-friendly internal ID for the object.  # noqa: E501

        :return: The id of this EitherIdDTO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EitherIdDTO.

        A JavaScript-friendly internal ID for the object.  # noqa: E501

        :param id: The id of this EitherIdDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id > 9007199254740991):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `9007199254740991`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id < 1):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this EitherIdDTO.  # noqa: E501

        External Id provided by client. Should be unique within a given project/resource combination.  # noqa: E501

        :return: The external_id of this EitherIdDTO.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this EitherIdDTO.

        External Id provided by client. Should be unique within a given project/resource combination.  # noqa: E501

        :param external_id: The external_id of this EitherIdDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_id is None:  # noqa: E501
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) > 255):
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `255`")  # noqa: E501

        self._external_id = external_id

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
        if not isinstance(other, EitherIdDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EitherIdDTO):
            return True

        return self.to_dict() != other.to_dict()
