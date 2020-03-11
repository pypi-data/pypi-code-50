import json
from numpy import float64, int64
import sensiml.base.utility as utility
import logging
import time


logger = logging.getLogger(__name__)


class LabelValue(object):
    Int = "integer"
    Float = "float"
    String = "string"


class LabelValue(object):
    """Base class for a label object."""

    def __init__(self, connection, project, label):
        """Initialize a metadata object.

            Args:
                connection
                project
                label
        """
        self._uuid = ""
        self._value = ""
        self._last_modified = ""
        self._created_at = ""
        self._connection = connection
        self._project = project
        self._label = label

    @property
    def uuid(self):
        """Auto generated unique identifier for the  label value object"""
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value

    @property
    def value(self):
        """The data type of the label value object"""
        return self._value

    @value.setter
    def value(self, value):
        """The data type of the label value object"""
        self._value = value

    @property
    def created_at(self):
        """The creatd time of the label value object"""
        return self._created_at

    def insert(self):
        """Calls the REST API and inserts a metadata object onto the server using the local object's properties."""
        url = "project/{0}/label/{1}/labelvalue/".format(
            self._project.uuid,
            self._label.uuid
        )
        data = {
            "value": self.value,
        }
        response = self._connection.request("post", url, data)
        response_data, err = utility.check_server_response(response)
        if err is False:
            self.uuid = response_data["uuid"]

    def update(self):
        """Calls the REST API and updates the object on the server."""
        url = "project/{0}/label/{1}/labelvalue/{2}".format(
            self._project.uuid,
            self._label.uuid,
            self.uuid
        )

        data = {
            "value": self.value,
        }

        response = self._connection.request("put", url, data)
        response_data, err = utility.check_server_response(response)

    def delete(self):
        """Calls the REST API and deletes the object from the server."""
        url = "project/{0}/label/{1}/labelvalue/{2}".format(
            self._project.uuid,
            self._label.uuid,
            self.uuid
        )
        response = self._connection.request("delete", url)
        response_data, err = utility.check_server_response(response)

    def refresh(self):
        """Calls the REST API and populates the local object's properties from the server."""
        url = "project/{0}/label/{1}/labelvalue/{2}".format(
            self._project.uuid,
            self._label.uuid,
            self.uuid
        )
        response = self._connection.request("get", url)
        response_data, err = utility.check_server_response(response)
        if err is False:
            self.initialize_from_dict(response_data)

    def initialize_from_dict(self, data):
        """Reads a json dictionary and populates a single metadata object.

            Args:
                dict (dict): contains the uuid, value
        """
        self.uuid = data["uuid"]
        self.value = data["value"]


class LabelValueSet(object):

    def __init__(self, connection, project, label, initialize_set=True):
        """Initialize a metadata object.

            Args:
                connection
                project
        """
        self._connection = connection
        self._project = project
        self._label = label
        self._set = None

        if initialize_set:
            self.refresh()

    @property
    def label_values(self):
        if self._set is None:
            self._set = self.get_set()

        return self._set

    def refresh(self):
        self._set = self.get_set()

    def get_set(self):
        """Calls the REST API and inserts a metadata object onto the server using the local object's properties."""
        url = "project/{0}/label/{1}/labelvalue/".format(
            self._project.uuid,
            self._label.uuid
        )

        response = self._connection.request("get", url)
        response_data, err = utility.check_server_response(response)
        if err:
            print(err)
            return None

        # Populate each label from the server
        labelvalues = []
        for obj in response_data:
            labelvalues.append(self._new_obj_from_dict(obj))

        return labelvalues

    def _new_obj_from_dict(self, data):
        """Creates a new label from data in the dictionary.

            Args:
                data (dict): contains label_value properties value, uuid

            Returns:
                label object

        """
        labelvalue = LabelValue(self._connection, self._project, self._label)
        labelvalue.initialize_from_dict(data)
        return labelvalue

    def __str__(self):
        s = ""
        if self._set:
            label = self._set[0]._label
            s = "LABEL\n"
            s += "\tname: " + str(label.name) + ' uuid: ' + \
                str(label.uuid) + "\n"
            s += "LABEL VALUES\n"
            for lbv in self._set:
                s += "\tvalue: " + str(lbv.value) + \
                    " uuid:" + str(lbv.uuid) + "\n"

        return s
