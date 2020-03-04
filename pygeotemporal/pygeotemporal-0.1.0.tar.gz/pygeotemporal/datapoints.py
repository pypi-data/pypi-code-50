"""
    Geostreams Datapoints API
"""

from builtins import str
from builtins import object
import logging

from dateutil.parser import parse

from pygeotemporal.client import GeostreamsClient


class DatapointsApi(object):
    """
        API to manage the REST CRUD endpoints for datapoints.
    """
    def __init__(self, client=None, host=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = GeostreamsClient(host=host, username=username, password=password)

    def datapoint_post(self, datapoint):
        """
        Add a datapoint.

        :return: If successful or not.
        :rtype: `requests.Response`
        """
        logging.debug("Adding datapoint")
        try:
            return self.client.post("/datapoints", datapoint)
        except Exception as e:
            logging.error("Error adding datapoint %s: %s", datapoint, e.message)

    def datapoints_count_by_sensor_get(self, sensor_id):
        """
        Get the list of all available sensors.

        :return: Full list of sensors.
        :rtype: `requests.Response`
        """
        logging.debug("Counting datapoints by sensor")
        try:
            return self.client.get("/datapoints?sensor_id=%s&onlyCount=true" % sensor_id)
        except Exception as e:
            logging.error("Error counting datapoints by sensor %s: %s", sensor_id, e.message)

    def datapoint_latest_get(self, sensor_id, stream_id, since=None):
        """
        Get latest datapoint for a given stream by retrieving datapoint since a recent date and then grabbing
        the latest one.

        TODO: this should be an API endpoint
        """
        latest_datapoint = None
        # logging.info("Getting datapoints for stream %s since %s " % stream_id, since)
        if since is None:
            url = "/datapoints?stream_id=%s" % stream_id
        else:
            url = "/datapoints?stream_id=%s&since=%s" % (stream_id, since)
        try:
            datapoints = self.client.get_json(url)
            if isinstance(datapoints, list) and len(datapoints) > 0:
                latest_datapoint = datapoints[-1]
                start_date = parse(latest_datapoint['start_time']).strftime('%Y-%m-%d-%H-%M')
                logging.info("Fetched datapoints for " + str(sensor_id) + " starting on " + start_date)
            else:
                logging.debug("No datapoints exist for " + str(sensor_id))
        except Exception as e:
            logging.error("Error getting datapoints for stream %s since %s: %s", stream_id, since, e.message)

        return latest_datapoint

    def datapoint_create_json(self, start_time, end_time, longitude, latitude, sensor_id, stream_id, sensor_name,
                              properties=None, owner=None, source=None, procedures=None, elevation=0):
        datapoint = {
            'start_time': start_time,
            'end_time': end_time,
            'type': 'Feature',
            'geometry': {
                'type': "Point",
                'coordinates': [
                    longitude,
                    latitude,
                    elevation
                ]
            },
            'stream_id': str(stream_id),
            'sensor_id': str(sensor_id),
            'sensor_name': str(sensor_name)
        }

        if properties is not None:
            datapoint['properties'] = properties
            datapoint['properties']['site'] = sensor_name
            if owner is not None:
                datapoint['properties']["owner"] = owner
            if source is not None:
                datapoint['properties']['source'] = source
            if procedures is not None:
                datapoint['properties']['procedures'] = procedures

        return datapoint

    def datapoint_create_bulk(self, datapoints):
        logging.debug("Adding Datapoints in Bulk")
        try:
            return self.client.post("/datapoints/bulk", datapoints)
        except Exception as e:
            logging.error("Error adding bulk datapoint: %s", e.message)


