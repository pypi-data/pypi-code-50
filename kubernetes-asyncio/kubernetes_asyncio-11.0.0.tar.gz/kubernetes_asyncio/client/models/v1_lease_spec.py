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


class V1LeaseSpec(object):
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
        'acquire_time': 'datetime',
        'holder_identity': 'str',
        'lease_duration_seconds': 'int',
        'lease_transitions': 'int',
        'renew_time': 'datetime'
    }

    attribute_map = {
        'acquire_time': 'acquireTime',
        'holder_identity': 'holderIdentity',
        'lease_duration_seconds': 'leaseDurationSeconds',
        'lease_transitions': 'leaseTransitions',
        'renew_time': 'renewTime'
    }

    def __init__(self, acquire_time=None, holder_identity=None, lease_duration_seconds=None, lease_transitions=None, renew_time=None, local_vars_configuration=None):  # noqa: E501
        """V1LeaseSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._acquire_time = None
        self._holder_identity = None
        self._lease_duration_seconds = None
        self._lease_transitions = None
        self._renew_time = None
        self.discriminator = None

        if acquire_time is not None:
            self.acquire_time = acquire_time
        if holder_identity is not None:
            self.holder_identity = holder_identity
        if lease_duration_seconds is not None:
            self.lease_duration_seconds = lease_duration_seconds
        if lease_transitions is not None:
            self.lease_transitions = lease_transitions
        if renew_time is not None:
            self.renew_time = renew_time

    @property
    def acquire_time(self):
        """Gets the acquire_time of this V1LeaseSpec.  # noqa: E501

        acquireTime is a time when the current lease was acquired.  # noqa: E501

        :return: The acquire_time of this V1LeaseSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._acquire_time

    @acquire_time.setter
    def acquire_time(self, acquire_time):
        """Sets the acquire_time of this V1LeaseSpec.

        acquireTime is a time when the current lease was acquired.  # noqa: E501

        :param acquire_time: The acquire_time of this V1LeaseSpec.  # noqa: E501
        :type: datetime
        """

        self._acquire_time = acquire_time

    @property
    def holder_identity(self):
        """Gets the holder_identity of this V1LeaseSpec.  # noqa: E501

        holderIdentity contains the identity of the holder of a current lease.  # noqa: E501

        :return: The holder_identity of this V1LeaseSpec.  # noqa: E501
        :rtype: str
        """
        return self._holder_identity

    @holder_identity.setter
    def holder_identity(self, holder_identity):
        """Sets the holder_identity of this V1LeaseSpec.

        holderIdentity contains the identity of the holder of a current lease.  # noqa: E501

        :param holder_identity: The holder_identity of this V1LeaseSpec.  # noqa: E501
        :type: str
        """

        self._holder_identity = holder_identity

    @property
    def lease_duration_seconds(self):
        """Gets the lease_duration_seconds of this V1LeaseSpec.  # noqa: E501

        leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed RenewTime.  # noqa: E501

        :return: The lease_duration_seconds of this V1LeaseSpec.  # noqa: E501
        :rtype: int
        """
        return self._lease_duration_seconds

    @lease_duration_seconds.setter
    def lease_duration_seconds(self, lease_duration_seconds):
        """Sets the lease_duration_seconds of this V1LeaseSpec.

        leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed RenewTime.  # noqa: E501

        :param lease_duration_seconds: The lease_duration_seconds of this V1LeaseSpec.  # noqa: E501
        :type: int
        """

        self._lease_duration_seconds = lease_duration_seconds

    @property
    def lease_transitions(self):
        """Gets the lease_transitions of this V1LeaseSpec.  # noqa: E501

        leaseTransitions is the number of transitions of a lease between holders.  # noqa: E501

        :return: The lease_transitions of this V1LeaseSpec.  # noqa: E501
        :rtype: int
        """
        return self._lease_transitions

    @lease_transitions.setter
    def lease_transitions(self, lease_transitions):
        """Sets the lease_transitions of this V1LeaseSpec.

        leaseTransitions is the number of transitions of a lease between holders.  # noqa: E501

        :param lease_transitions: The lease_transitions of this V1LeaseSpec.  # noqa: E501
        :type: int
        """

        self._lease_transitions = lease_transitions

    @property
    def renew_time(self):
        """Gets the renew_time of this V1LeaseSpec.  # noqa: E501

        renewTime is a time when the current holder of a lease has last updated the lease.  # noqa: E501

        :return: The renew_time of this V1LeaseSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._renew_time

    @renew_time.setter
    def renew_time(self, renew_time):
        """Sets the renew_time of this V1LeaseSpec.

        renewTime is a time when the current holder of a lease has last updated the lease.  # noqa: E501

        :param renew_time: The renew_time of this V1LeaseSpec.  # noqa: E501
        :type: datetime
        """

        self._renew_time = renew_time

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
        if not isinstance(other, V1LeaseSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1LeaseSpec):
            return True

        return self.to_dict() != other.to_dict()
