# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 11.1.0-rc.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class MasterSubjectCodeIdInput(object):

    swagger_types = {
        'first_name': 'str',
        'last_name': 'str',
        'date_of_birth': 'str',
        'patient_id': 'str',
        'use_patient_id': 'bool'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'date_of_birth': 'date_of_birth',
        'patient_id': 'patient_id',
        'use_patient_id': 'use_patient_id'
    }

    rattribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'date_of_birth': 'date_of_birth',
        'patient_id': 'patient_id',
        'use_patient_id': 'use_patient_id'
    }

    def __init__(self, first_name=None, last_name=None, date_of_birth=None, patient_id=None, use_patient_id=None):  # noqa: E501
        """MasterSubjectCodeIdInput - a model defined in Swagger"""
        super(MasterSubjectCodeIdInput, self).__init__()

        self._first_name = None
        self._last_name = None
        self._date_of_birth = None
        self._patient_id = None
        self._use_patient_id = None
        self.discriminator = None
        self.alt_discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        self.patient_id = patient_id
        self.use_patient_id = use_patient_id

    @property
    def first_name(self):
        """Gets the first_name of this MasterSubjectCodeIdInput.

        First name

        :return: The first_name of this MasterSubjectCodeIdInput.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MasterSubjectCodeIdInput.

        First name

        :param first_name: The first_name of this MasterSubjectCodeIdInput.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MasterSubjectCodeIdInput.

        Last name

        :return: The last_name of this MasterSubjectCodeIdInput.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MasterSubjectCodeIdInput.

        Last name

        :param last_name: The last_name of this MasterSubjectCodeIdInput.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this MasterSubjectCodeIdInput.

        Date of birth in YYYY-MM-DD format

        :return: The date_of_birth of this MasterSubjectCodeIdInput.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this MasterSubjectCodeIdInput.

        Date of birth in YYYY-MM-DD format

        :param date_of_birth: The date_of_birth of this MasterSubjectCodeIdInput.  # noqa: E501
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def patient_id(self):
        """Gets the patient_id of this MasterSubjectCodeIdInput.

        Patient id

        :return: The patient_id of this MasterSubjectCodeIdInput.
        :rtype: str
        """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        """Sets the patient_id of this MasterSubjectCodeIdInput.

        Patient id

        :param patient_id: The patient_id of this MasterSubjectCodeIdInput.  # noqa: E501
        :type: str
        """

        self._patient_id = patient_id

    @property
    def use_patient_id(self):
        """Gets the use_patient_id of this MasterSubjectCodeIdInput.

        Use patient ID for identification or first name, last name, DOB

        :return: The use_patient_id of this MasterSubjectCodeIdInput.
        :rtype: bool
        """
        return self._use_patient_id

    @use_patient_id.setter
    def use_patient_id(self, use_patient_id):
        """Sets the use_patient_id of this MasterSubjectCodeIdInput.

        Use patient ID for identification or first name, last name, DOB

        :param use_patient_id: The use_patient_id of this MasterSubjectCodeIdInput.  # noqa: E501
        :type: bool
        """

        self._use_patient_id = use_patient_id


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, MasterSubjectCodeIdInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
