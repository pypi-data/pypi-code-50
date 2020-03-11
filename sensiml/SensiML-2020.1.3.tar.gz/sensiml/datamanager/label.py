import json
from numpy import float64, int64
import sensiml.base.utility as utility
import logging
import time


logger = logging.getLogger(__name__)


class LabelType(object):
    Int = "integer"
    Float = "float"
    String = "string"


class Label(object):
    """Base class for a label object."""

    def __init__(self, connection, project):
        """Initialize a metadata object.

            Args:
                connection
                project
        """
        self._uuid = ""
        self._name = ""
        self._value_type = "string"
        self._metadata = False
        self._is_dropdown = None
        self._last_modified = ""
        self._created_at = ""
        self._connection = connection
        self._project = project

    @property
    def uuid(self):
        """Auto generated unique identifier for the metadata object"""
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value

    @property
    def name(self):
        """The name property of the metadata object"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def value_type(self):
        """The data type of the metadata object"""
        return self._value_type

    @value_type.setter
    def value_type(self, value):
        self._value_type = value

    def insert(self):
        """Calls the REST API and inserts a metadata object onto the server using the local object's properties."""
        url = "project/{0}/label/".format(
            self._project.uuid
        )
        label_info = {
            "name": self.name,
            "type": self.value_type,
            "is_dropdown": self.is_dropdown,
            "metadata": self.metadata
        }
        response = self._connection.request("post", url, label_info)
        response_data, err = utility.check_server_response(response)
        if err is False:
            self.uuid = response_data["uuid"]

    def update(self):
        """Calls the REST API and updates the object on the server."""
        url = "project/{0}/label/{1}/".format(
            self._project.uuid, self.uuid
        )
        label_info = {
            "name": self.name,
            "type": self.value_type,
            "value": self.value,
            "is_dropdown": self.is_dropdown
        }
        response = self._connection.request("put", url, label_info)
        response_data, err = utility.check_server_response(response)

    def delete(self):
        """Calls the REST API and deletes the object from the server."""
        url = "project/{0}/label/{1}/".format(
            self._project.uuid, self.uuid
        )
        response = self._connection.request("delete", url)
        response_data, err = utility.check_server_response(response)

    def refresh(self):
        """Calls the REST API and populates the local object's properties from the server."""
        url = "project/{0}/label/{1}/".format(
            self._project.uuid, self.uuid
        )
        response = self._connection.request("get", url)
        response_data, err = utility.check_server_response(response)
        if err is False:
            self.initialize_from_dict(response_data)

    def initialize_from_dict(self, data):
        """Reads a json dictionary and populates a single metadata object.

            Args:
                data (dict): contains the uuid, name, type
        """
        self.uuid = data["uuid"]
        self.name = data["name"]
        if data["type"] == LabelType.Int:
            self.value_type = int(data["type"])
        elif data["type"] == LabelType.Float:
            self.value_type = float(data["type"])
        else:
            self.value_type = data["type"]


class LabelSet(object):

    def __init__(self, connection, project, initialize_set=True):
        """Initialize a metadata object.

            Args:
                connection
                project
        """
        self._connection = connection
        self._project = project
        self._set = None

        if initialize_set:
            self.refresh()

    @property
    def labels(self):
        if self._set is None:
            self._set = self.get_set()

        return self._set

    def refresh(self):
        self._set = self.get_set()


    def get_set(self):
        """Calls the REST API and inserts a metadata object onto the server using the local object's properties."""
        url = "project/{0}/label/".format(
            self._project.uuid
        )

        response = self._connection.request("get", url)
        response_data, err = utility.check_server_response(response)
        if err:
            raise Exception(err)

        # Populate each label from the server
        labels = []
        for obj in response_data:
            labels.append(self._new_obj_from_dict(obj))

        return labels

    def _new_obj_from_dict(self, data):
        """Creates a new label from data in the dictionary.

            Args:
                data (dict): contains label properties uuid, name, type

            Returns:
                label object

        """
        obj = Label(self._connection, self._project)
        obj.initialize_from_dict(data)
        return obj
