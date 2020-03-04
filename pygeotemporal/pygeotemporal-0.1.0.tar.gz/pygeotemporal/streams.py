"""
    Geostreams Streams API
"""

from builtins import range
from builtins import object
import logging
import json
from pygeotemporal.client import GeostreamsClient


class StreamsApi(object):
    """
        API to manage the REST CRUD endpoints for Streams.
    """
    def __init__(self, client=None, host=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = GeostreamsClient(host=host, username=username, password=password)

    def streams_get(self):
        """
        Get the list of all available streams.

        :return: Full list of streams.
        :rtype: `requests.Response`
        """
        logging.debug("Getting all streams")
        try:
            return self.client.get("/streams")
        except Exception as e:
            logging.error("Error retrieving stream list: %s", e.message)

    def streams_get_by_id(self, id):
        logging.debug("Getting stream with id %s" % id)
        try:
            return self.client.get("/streams/%s" % id)
        except Exception as e:
            logging.error("Error retrieving stream with id %s: %s" % id, e.message )

    def stream_get_by_name_json(self, stream_name):
        """
        Get a specific stream by id.

        :return: stream object as JSON.
        :rtype: `requests.Response`
        """
        logging.debug("Getting stream %s" % stream_name)
        stream = self.client.get("/streams?stream_name=" + stream_name).json()
        if 'status' in stream and stream['status'] == "No data found" or not stream["streams"]:
            return None
        else:
            return stream

    def stream_post(self, stream):
        """
        Create stream.

        :return: stream json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding stream")

        try:
            return self.client.post("/streams", stream)
        except Exception as e:
            logging.error("Error retrieving streams: %s", e.message)

    def stream_post_json(self, stream):
        """
        Create stream.

        :return: stream json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding or getting stream")

        stream_from_geostreams = self.stream_get_by_name_json(stream['name'])

        if stream_from_geostreams is None:
            logging.info("Creating stream with name: " + stream['name'])
            result = self.client.post("/streams", stream)
            if result.status_code != 200:
                logging.info("Error posting stream")
            stream_from_geostreams = self.stream_get_by_name_json(stream['name'])

        logging.info("Found stream %s", stream['name'])
        return stream_from_geostreams["streams"][0]

    def stream_delete(self, stream_id):
        """
        Delete a specific stream by id.

        :return: If successfull or not.
        :rtype: `requests.Response`
        """
        logging.debug("Deleting stream %s" % stream_id)
        try:
            return self.client.delete("/streams/%s" % stream_id)
        except Exception as e:
            logging.error("Error deleting stream %s: %s", stream_id, e.message)

    def stream_create_json_from_sensor(self, sensor):
        """
        Create stream from sensor. Note: It does not post the stream to the API

        :param: sensor
        :return: stream Json object
        """

        stream = {
            "sensor_id": sensor['id'],
            "name": sensor['name'],
            "type": sensor['geoType'],
            "geometry": sensor['geometry'],
            "properties": sensor['properties']
        }

        return stream

    def stream_delete_range(self, start, end, keyword):
        """
        Deletes streams in a range of indexes [start, end] where the name includes keyword.

        """

        for i in range(start, end + 1):
            stream = self.streams_get_by_id(i)
            json_stream = json.loads(stream.content)
            if 'name' in json_stream:

                if keyword.lower() in json_stream['name'].encode("ascii").lower():
                    self.stream_delete(i)
                    logging.info("Stream Deleted, %s", i)
                else:
                    logging.info("Sensor not deleted %s, no keyword match, stream name: %s", i, json_stream["name"])

            else:
                logging.info("No name keyword in stream, stream doesn't exist. Stream Id: %s", i)
        return
