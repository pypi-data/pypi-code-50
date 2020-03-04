# coding: utf-8

"""
    Geostreams Cache API
"""

from builtins import str
from builtins import object
import logging
from datetime import datetime

from dateutil import parser
from dateutil.relativedelta import relativedelta

from pygeotemporal.client import GeostreamsClient


class CacheApi(object):
    """
        This class provides functionality related to the Cache. Currently it is able to invalidate and prime the cache.
    """
    def __init__(self, client=None, host=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = GeostreamsClient(host=host, username=username, password=password)

    def invalidate_cache(self, sensor_id):
        """Invalidate sensor cache"""
        logging.debug("Invalidating cache for sensor %s" % sensor_id)
        try:
            return self.client.get("/cache/invalidate?sensor_id=%s" % sensor_id)
        except Exception as e:
            logging.error("Error invalidating cache for sensor %s" % sensor_id, e.message)

    def bin(self, sensor_id):
        """Bin sensor's datapoints"""
        logging.debug("Binning %s" % sensor_id)
        try:
            return self.client.post("/cache?sensor_id=%s" % sensor_id, content=None)
        except Exception as e:
            logging.error("Error binning sensor %s" % sensor_id, e.message)

    def prime_cache(self, sensor_id):
        """Prime the cache of a specific sensor."""
        logging.info(" Caching datapoints for sensor with id: " + str(sensor_id))

        try:
            sensor = self.client.get("/sensors/%s" % str(sensor_id)).json()
        except Exception as e:
            logging.error("Error getting sensor %s" % sensor_id, e.message)

        # Calculate time in days between start and end date of sensor info
        delta_days = (datetime.strptime(sensor['max_end_time'], "%Y-%m-%dT%H:%M:%SZ") -
                      datetime.strptime(sensor['min_start_time'], "%Y-%m-%dT%H:%M:%SZ")).days

        # Calculate time in years between start and end date of sensor info
        delta_years = relativedelta(parser.parse(sensor['max_end_time']), parser.parse(sensor['min_start_time'])).years

        if delta_years > 100:
            time_bin = 'decade'
        elif delta_years > 50:
            time_bin = 'lustrum'
        elif delta_years > 25:
            time_bin = 'year'
        elif delta_years > 10:
            time_bin = 'season'
        elif delta_years > 1:
            time_bin = 'month'
        else:
            if delta_days > 14:
                time_bin = 'day'
            elif delta_days > 3:
                time_bin = 'hour'
            else:
                time_bin = 'minute'

        try:
            return self.client.get("/datapoints/bin/" + str(time_bin) + "/1?sensor_id=" + str(sensor_id))
        except Exception as e:
            logging.error("Error priming cache for sensor %s" % sensor_id, e.message)
