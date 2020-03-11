import os
import json
import sensiml.base.utility as utility


class Segmetner(object):
    """Base class for a segmenter object."""

    def __init__(self, connection, project):
        """Initialize a metadata object.

            Args:
                connection
                project
        """
        self._uuid = ""
        self._name = ""
        self._parameters = None
        self._preprocess = None
        self._custom = True
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
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        self._parameters = value

    @property
    def preprocess(self):
        return self._preprocess

    @preprocess.setter
    def preprocess(self, value):
        self._preprocess = value

    def insert(self):
        """Calls the REST API and inserts a metadata object onto the server using the local object's properties."""
        url = "project/{0}/segmenter/".format(
            self._project.uuid
        )
        label_info = {
            "name": self.name,
            "preprocess": self.preprocess,
            "parameters": self.parameters,
        }
        response = self._connection.request("post", url, label_info)
        response_data, err = utility.check_server_response(response)
        if err is False:
            self.uuid = response_data["id"]

    def update(self):
        """Calls the REST API and updates the object on the server."""
        url = "project/{0}/segmenter/{1}/".format(
            self._project.uuid, self.uuid
        )
        label_info = {
            "name": self.name,
            "preprocess": self.preprocess,
            "parameters": self.parameters,
        }
        response = self._connection.request("put", url, label_info)
        response_data, err = utility.check_server_response(response)

    def delete(self):
        """Calls the REST API and deletes the object from the server."""
        url = "project/{0}/segmenter/{1}/".format(
            self._project.uuid, self.uuid
        )
        response = self._connection.request("delete", url)
        response_data, err = utility.check_server_response(response)

    def refresh(self):
        """Calls the REST API and populates the local object's properties from the server."""
        url = "project/{0}/segmenter/{1}/".format(
            self._project.uuid, self.uuid
        )
        response = self._connection.request("get", url)
        response_data, err = utility.check_server_response(response)
        if err is False:
            self.initialize_from_dict(response_data)

    def initialize_from_dict(self, data):
        """Reads a json dictionary and populates a single metadata object.

            Args:
                dict (dict): contains the uuid, name, type
        """
        self.uuid = data["id"]
        self.name = data["name"]
        self.preprocess = data['preporcess']
        self.parameters = data['parameters']


class SegmenterSet(object):
    """Base class for a segmenter object."""

    def __init__(self, connection, project, initialize_set=True):
        self._connection = connection
        self._project = project
        self._set = None

        if initialize_set:
            self.refresh()

    @property
    def segmenters(self):
        if self._set is None:
            self._set = self.get_set()

        return self._set

    def refresh(self):
        self._set = self.get_set()


    def get_set(self):
        """Gets a list of all segmenters in the project.

        Returns:
            list (segmenters)
        """
        err = False
        url = "project/{0}/segmenter/".format(self._project.uuid)
        response = self._connection.request("get", url)
        try:
            response_data, err = utility.check_server_response(response)
        except ValueError:
            print(response)
        # Populate the retrieved featurefiles
        segmenters = []

        if err is False:
            try:
                for segmenter_params in response_data:
                    segmenters.append(segmenter_params)
            except:
                pass

        return segmenters
