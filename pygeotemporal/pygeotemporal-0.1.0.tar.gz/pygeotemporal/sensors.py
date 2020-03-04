"""
    Geostreams Sensors API.
"""
from __future__ import division

from builtins import object
import logging
import time
from datetime import datetime

from pygeotemporal.client import GeostreamsClient


class SensorsApi(object):
    """
        API to manage the REST CRUD endpoints for sensors.
    """
    def __init__(self, client=None, host=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = GeostreamsClient(host=host, username=username, password=password)

    def sensors_get(self):
        """
        Get the list of all available sensors.

        :return: Full list of sensors.
        :rtype: `requests.Response`
        """
        logging.debug("Getting all sensors")
        try:
            return self.client.get("/sensors")
        except Exception as e:
            logging.error("Error retrieving sensor list: %s", e.message)

    def sensors_refresh_cache(self):
        """
        Get all available sensors one by one, return nothing

        :rtype: `requests.Response`
        """
        logging.debug("Getting all sensors by each id")
        try:
            sensor_list = self.client.get("/sensors")

            for sensor in sensor_list.json():
                logging.debug("refresh sensor %s", sensor['id'])
                self.client.get("/sensors/%s" % sensor['id'])
                binning_filter = self.get_aggregation_bin(sensor['min_start_time'], sensor['max_end_time'])
                if sensor['properties']['type']['id'] == 'epa': 
                    binning_filter = 'semi'

                self.client.get("/datapoints/bin/%s/1?sensor_id=%s" % (binning_filter, sensor['id']))
                time.sleep(100)     
            return True    
        except Exception as e:
            logging.error("Error caching sensor list: %s", e.message)

    def sensor_refresh_cache(self, sensor_id):
        """
        Get all available sensors one by one, return nothing

        :rtype: `requests.Response`
        """
        logging.debug("prime cache for sensor %s" % sensor_id)
        try:
            response = self.client.get("/sensors/%s" % sensor_id)
            sensor = response.json()
            if 'min_start_time' not in sensor: 
                return False
            logging.debug("refresh sensor %s", sensor_id)
            self.client.get("/sensors/%s" % sensor_id)
            binningfilter = self.get_aggregation_bin(sensor['min_start_time'], sensor['max_end_time'])
            if sensor['properties']['type']['id'] == 'epa': 
                binningfilter = 'semi'

            self.client.get("/datapoints/bin/%s/1?sensor_id=%s" % (binningfilter, sensor_id))
    
            return True    
        except Exception as e:
            logging.error("Error caching sensor: %s", e.message)

    def sensor_get(self, sensor_id):
        """
        Get a specific sensor by id.

        :return: Sensor object as JSON.
        :rtype: `requests.Response`
        """
        logging.debug("Getting sensor %s" % sensor_id)
        try:
            return self.client.get("/sensors/%s" % sensor_id)
        except Exception as e:
            logging.error("Error retrieving sensor %s: %s", sensor_id, e.message)

    def sensor_get_by_name(self, sensor_name):
        """
        Get a specific sensor by id.

        :return: Sensor object as JSON.
        :rtype: `requests.Response`
        """
        logging.debug("Getting sensor %s" % sensor_name)
        try:
            return self.client.get("/sensors?sensor_name=" + sensor_name)
        except Exception as e:
            logging.error("Error retrieving sensor %s: %s", sensor_name, e.message)
            return None

    def sensor_post(self, sensor):
        """
        Create sensor.

        :return: sensor json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding sensor")
        try:
            return self.client.post("/sensors", sensor)
        except Exception as e:
            logging.error("Error adding sensor %s: %s", sensor['name'], e.message)

    def sensor_post_json(self, sensor):
        """
        Create sensor.

        :return: sensor json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding or getting sensor")
        try:

            if 'id' in sensor:
                sensor_from_geostreams = self.sensor_get(sensor['id']).json()
            elif 'name' in sensor:
                sensor_from_geostreams = self.sensor_get_by_name(sensor['name']).json()

            if len(sensor_from_geostreams['sensors']) > 0:
                logging.info("Found sensor " + sensor['name'])
                return sensor_from_geostreams['sensors'][0]
            else:
                logging.info("Creating sensor with name: " + sensor['name'])
                sensor_id = (self.client.post("/sensors", sensor)).json()
                sensor_from_geostreams = self.sensor_get(sensor_id['id']).json()
                return sensor_from_geostreams['sensor']
        except Exception as e:
            logging.error("Error adding sensor %s: %s", sensor['name'], e.message)

    def sensor_delete(self, sensor_id):
        """
        Delete a specific sensor by id.

        :return: If successful or not.
        :rtype: `requests.Response`
        """
        logging.debug("Deleting sensor %s" % sensor_id)
        try:
            return self.client.delete("/sensors/%s" % sensor_id)
        except Exception as e:
            logging.error("Error retrieving sensor %s: %s", sensor_id, e.message)

    def sensor_create_json(self, name, longitude, latitude, elevation, popup_content, region, huc=None, network=None,
                           organization_id=None, title=None):
        """Create sensor definition in JSON"""
        sensor = {
            "name": name,
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    longitude,
                    latitude,
                    elevation
                ]
            },
            "properties": {
                "name": name,
                "popupContent": popup_content,
                "region": region
            }
        }

        if network or id or title:
            sensor['properties']['type'] = {}

        if huc:
            sensor["properties"]["huc"] = huc
        if network:
            sensor['properties']['type']['network'] = network
        if organization_id:
            sensor['properties']['type']['id'] = organization_id
        if title:
            sensor['properties']['type']['title'] = title
        return sensor

    def sensor_statistics_post(self, sensor_id):
        """
        Update sensor statistics.

        :return: Full list of sensors.
        :rtype: `requests.Response`
        """
        logging.debug("Updating sensor statistics")
        sensor = (self.sensor_get(sensor_id)).json()["sensor"]
        try:
            return self.client.put("/sensors/%s/update" % sensor_id, content=sensor)
        except Exception as e:
            logging.error("Error updating sensor statistics for sensor %s: %s", sensor_id, e.message)

    def get_aggregation_bin(self, start_time, end_time):
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
        end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')
        year = end_time.year - start_time.year

        if year > 100: 
            time_bin = 'decade'
        elif year > 50: 
            time_bin = 'lustrum'
        elif year > 25:
            time_bin = 'year'
        elif year > 10:
            time_bin = 'season'
        elif year > 1:
            time_bin = 'month'
        else:
            diff_time = end_time - start_time
            b_time = divmod(diff_time.days * 86400 + diff_time.seconds, 60)[0]  # minutes
            b_time = b_time / 1440
            if b_time > 14:
                time_bin = 'day'
            elif b_time > 3:
                time_bin = 'hour'
            else:
                time_bin = 'minute'
        return time_bin

    def update_sensor_metadata(self, sensor):
        """
        Update sensor metadata
        :param sensor: Sensor json
        :return: Http response
        """
        logging.debug("Updating sensor's metadata")
        sensor_id = sensor["id"]
        try:
            return self.client.put("/sensors/%s" % sensor_id, content=sensor)
        except Exception as e:
            logging.error("Error updating sensor metadata for sensor %s: %s", sensor_id, e.message)
