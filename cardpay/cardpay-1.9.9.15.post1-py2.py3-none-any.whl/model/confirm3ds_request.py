# coding: utf-8

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on [OAuth 2.0](https://oauth.net/2/) standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cardpay.model.request import Request  # noqa: F401,E501


class Confirm3dsRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"request": "Request", "pa_res": "str"}

    attribute_map = {"request": "request", "pa_res": "PaRes"}

    def __init__(self, request=None, pa_res=None):  # noqa: E501
        """Confirm3dsRequest - a model defined in Swagger"""  # noqa: E501

        self._request = None
        self._pa_res = None
        self.discriminator = None

        self.request = request
        self.pa_res = pa_res

    @property
    def request(self):
        """Gets the request of this Confirm3dsRequest.  # noqa: E501

        Request  # noqa: E501

        :return: The request of this Confirm3dsRequest.  # noqa: E501
        :rtype: Request
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this Confirm3dsRequest.

        Request  # noqa: E501

        :param request: The request of this Confirm3dsRequest.  # noqa: E501
        :type: Request
        """
        if request is None:
            raise ValueError(
                "Invalid value for `request`, must not be `None`"
            )  # noqa: E501

        self._request = request

    @property
    def pa_res(self):
        """Gets the pa_res of this Confirm3dsRequest.  # noqa: E501

        Bank authentication result *(for BANKCARD payment method only)*  # noqa: E501

        :return: The pa_res of this Confirm3dsRequest.  # noqa: E501
        :rtype: str
        """
        return self._pa_res

    @pa_res.setter
    def pa_res(self, pa_res):
        """Sets the pa_res of this Confirm3dsRequest.

        Bank authentication result *(for BANKCARD payment method only)*  # noqa: E501

        :param pa_res: The pa_res of this Confirm3dsRequest.  # noqa: E501
        :type: str
        """
        if pa_res is None:
            raise ValueError(
                "Invalid value for `pa_res`, must not be `None`"
            )  # noqa: E501

        self._pa_res = pa_res

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                if value is not None:
                    result[attr] = value
        if issubclass(Confirm3dsRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Confirm3dsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
