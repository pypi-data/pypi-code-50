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


class Segment(object):
    """Base class for a label object."""

    def __init__(self, connection, project, capture, segmenter=None, label=None, label_value=None):
        """Initialize a metadata object.

            Args:
                connection
                project
                capture
        """
        self._uuid = ""
        self._sample_start = 0
        self._sample_end = 0
        self._connection = connection
        self._project = project
        self._capture = capture
        self._segmenter = segmenter
        self._label = label
        self._label_value = label_value

    @property
    def uuid(self):
        """Auto generated unique identifier for the metadata object"""
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value



    @property
    def sample_start(self):
        """The index of the first sample of the label"""
        return self._sample_start

    @sample_start.setter
    def sample_start(self, value):
        self._sample_start = value

    @property
    def sample_end(self):
        """The index of the last sample of the label"""
        return self._sample_end

    @sample_end.setter
    def sample_end(self, value):
        self._sample_end = value

    @property
    def segmenter(self):
        """The index of the last sample of the label"""
        return self._segmenter

    @segmenter.setter
    def segmenter(self, value):
        self._segmenter = value

    @property
    def label(self):
        if isinstance(self._label, str):
            return self._label
        else:
            return self._label.uuid

    @label.setter
    def label(self, value):
        self._label = value

    @property
    def label_value(self):
        if isinstance(self._label_value, str):
            return self._label_value
        else:
            return self._label_value.uuid

    @label_value.setter
    def label_value(self, value):
        self._label_value = value

    def insert(self):
        """Calls the REST API and inserts a metadata object onto the server using the local object's properties."""
        self._capture.await_ready()
        url = "project/{0}/capture/{1}/label-relationship/".format(
            self._project.uuid, self._capture.uuid
        )
        label_info = {
            "capture_sample_sequence_start": self.sample_start,
            "capture_sample_sequence_end": self.sample_end,
            "label": self.label,
            "label_value": self.label_value,
            "segmenter": self.segmenter,
        }
        response = self._connection.request("post", url, label_info)
        response_data, err = utility.check_server_response(response)
        if err is False:
            self.uuid = response_data["uuid"]

    def update(self):
        """Calls the REST API and updates the object on the server."""
        self._capture.await_ready()
        url = "project/{0}/capture/{1}/label-relationship/{2}/".format(
            self._project.uuid, self._capture.uuid, self.uuid
        )
        label_info = {
            "capture_sample_sequence_start": self.sample_start,
            "capture_sample_sequence_end": self.sample_end,
            "label": self.label,
            "label_value": self.label_value,
            "segmenter": self.segmenter,
        }
        response = self._connection.request("put", url, label_info)
        response_data, err = utility.check_server_response(response)

    def delete(self):
        """Calls the REST API and deletes the object from the server."""
        url = "project/{0}/capture/{1}/label-relationship/{2}/".format(
            self._project.uuid, self._capture.uuid, self.uuid
        )
        response = self._connection.request("delete", url)
        response_data, err = utility.check_server_response(response)

    def refresh(self):
        """Calls the REST API and populates the local object's properties from the server."""
        url = "project/{0}/capture/{1}/label-relationship/{2}/".format(
            self._project.uuid, self._capture.uuid, self.uuid
        )
        response = self._connection.request("get", url)
        response_data, err = utility.check_server_response(response)
        if err is False:
            self.initialize_from_dict(response_data)

    def initialize_from_dict(self, data):
        """Reads a json dictionary and populates a single metadata object.

            Args:
                data (dict): contains the uuid, type, value, capture_sample_sequence_start, and
                capture_sample_sequence_end properties
        """
        self.uuid = data["uuid"]
        self.sample_start = data["capture_sample_sequence_start"]
        self.sample_end = data["capture_sample_sequence_end"]
        self.segmenter = data.get("segmenter", None)
        self.label = data['label']
        self.label_value = data['label_value']
        

class SegmentSet:
    """Base class for a collection of segments"""

    def __init__(self, connection, project, capture, initialize_set=True):
        self._connection = connection
        self._project = project
        self._capture = capture
        self._set = None

        if initialize_set:
            self.refresh()
        

    @property
    def segments(self):
        if self._set is None:
            self._set = self.get_set()

        return self._set

    def refresh(self):
        self._set = self.get_set()

    def _new_obj_from_dict(self, data):
        """Creates a new label from data in the dictionary.

            Args:
                dict (dict): contains label properties uuid, name, type, value, capture_sample_sequence_start, and
                capture_sample_sequence_end

            Returns:
                label object

        """
        segment = Segment(self._connection, self._project, self._capture)
        segment.initialize_from_dict(data)
        return segment

    def get_set(self):
        """Gets all of the capture's label objects in a list.

            Returns:
                list[label]
        """
        # Query the server and get the json
        url = "project/{0}/capture/{1}/label-relationship/".format(
            self._project.uuid, self._capture.uuid
        )
        response = self._connection.request("get", url)
        response_data, err = utility.check_server_response(response)
        if err:
            print(err)
            return None

        # Populate each label from the server
        segmentset = []

        for obj in response_data:
            segmentset.append(self._new_obj_from_dict(obj))

        return segmentset
