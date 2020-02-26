from collections import Generator
from pytz import timezone
import requests
import os
from urllib.parse import urljoin

API_KEY = os.environ.get('ZUBIE_API_KEY', None)
CLIENT_ID = os.environ.get('ZUBIE_CLIENT_ID', None)
TZ = timezone('America/New_York')


class RestAdapter:
    """Adapter for communicating with Zubie API"""

    def __init__(self, api_key=API_KEY, client_id=CLIENT_ID):
        self.base_url = 'https://api.zubiecar.com/api/v2/zinc/'
        self._api_key = api_key
        self._client_id = client_id
        self._headers = {'Zubie-Api-Key': api_key}
        self._params = {'client_id': client_id}

    def _get(self, resource: str, **kwargs) -> dict:
        """Base get method used for all api calls"""
        params = self._params.copy()  # Sets default parameters
        params.update(kwargs)  # Adds provided keyword arguments to the call
        url = urljoin(self.base_url, resource)
        return requests.get(url=url, headers=self._headers, params=params).json()

    def _get_pages(self, *args, **kwargs):
        """Get function for getting pagination data"""
        cursor = kwargs.get('cursor')  # Cursor should be set to none initially
        while cursor is not False:
            result = self._get(*args, **kwargs)
            cursor = result.get('cursor', False)
            yield result

    def get_devices(self, q=None) -> dict:
        """Lists all active and pending devices (vehicle connected hardware) in account."""
        resource = 'devices'
        return self._get(resource, q=q)

    def get_device(self, key: str) -> dict:
        """Get single device by key"""
        resource = f'device/{{key}}'
        return self._get(resource, key=key)

    def get_groups(self, group_keys=None, show_inactive=False) -> dict:
        """Lists groups available in the account, based on the group permissions of the user.
        Groups are a way to provide hierarchical structure to account vehicles and restrict user permissions."""
        resource = 'groups'
        return self._get(resource, group_keys=group_keys, show_inactive=show_inactive)

    def get_vehicles(self, q=None, tag_keys=None, group_keys=None, cursor=None, size=None, expand=None) -> Generator:
        """Lists Vehicles in account. Restricted based on API user's group permissions. :param q: Search vehicles by
        nickname or full VIN. :type q: str :param tag_keys: Restrict results to include only vehicles with these tag
        keys. Multiple tag values may be provided, treated as an OR in filter. :type tag_keys: str :param group_keys:
        Restrict results to include only vehicles that are members of these groups (or their descendants). :type
        group_keys: str :param cursor: The cursor string used for pagination, signifying the object ID where to start
        the results. :type cursor: str :param size: The number of results to return per call. Default 50 if not
        provided. :type size: str :param expand: Default: [] Items Enum:"tags" "groups" "devices" "last_trip"
        Optional list of expanded properties to include in results :type expand: str
        """
        resource = 'vehicles'
        return self._get_pages(resource, q=q, tag_keys=tag_keys, group_keys=group_keys, cursor=cursor, size=size,
                               expand=expand)

    def get_vehicle(self, vehicle_key: str) -> dict:
        """Retrieve a single vehicle by vehicle key"""
        resource = f'vehicle/{{vehicle_key}}'
        return self._get(resource, vehicle_key=vehicle_key)

    def get_nearby_vehicles(self, lat: str, long: str, cursor=None, size=None) -> Generator:
        """Get list of nearby vehicles, using a given GPS point. Restricted based on API user's group permissions.
        :param lat: Latitude of the point.
        :param long: Longitude of the point.
        :param: cursor: The cursor string used for pagination, signifying the object ID where to start the results.
        :type cursor: str
        :param size: The number of results to return per call. Default 5 if not provided
        :type size: str
        """
        resource = 'vehicles/nearby'
        return self._get_pages(resource, lat=lat, long=long, cursor=cursor, size=size)

    def get_trips(self, user_key=None, vehicle_key=None, started_after=None, started_before=None, tag_keys=None,
                  cursor=None, size=None, expand=None) -> Generator:
        """Get a list of trips for the account. A trip is the logical grouping of all points that are recorded from
        the time the vehicle’s engine is started to the time the engine is turned off. :param user_key: Filter
        results to visits to a single driver. Optional. :type user_key: str :param vehicle_key: Filter results to a
        single vehicle. Optional. :type vehicle_key: str :param started_after: Filter results to only include trips
        that started on or after this timestamp. ISO8601 format (if no offset provided, assumed UTC). Optional. :type
        started_after: str :param started_before: Filter results to only include trips that started on or before this
        timestamp. ISO8601 format (if no offset provided, assumed UTC). Optional. :type started_before: str :param
        tag_keys: Restrict results to include only vehicles with these tag keys. Multiple tag values may be provided.
        Takes precedence over tags query param if both provided. :type tag_keys: str :param cursor: The cursor string
        used for pagination, signifying the object ID where to start the results. :type cursor: str :param size: The
        number of results to return per call. Default 10 if not provided. :type size: str :param expand: Default: [
        "user","vehicle","tags"] Items Enum:"user" "vehicle" "tags" Optional list of expanded properties to include
        in results :type expand: str
        """
        resource = 'trips'
        return self._get_pages(resource, user_key=user_key, vehicle_ke=vehicle_key, started_after=started_after,
                               started_before=started_before, tag_keys=tag_keys, cursor=cursor, size=size,
                               expand=expand)

    def get_trip(self, trip_key: str) -> dict:
        """Get the details for a single trip."""
        resource = f'trip/{{trip_key}}'
        return self._get(resource, trip_key=trip_key)

    def get_trip_points(self, trip_key: str, cursor=None, size=None) -> Generator:
        """Get the detailed GPS points and event details for a given trip.
        :param trip_key: Key for individual trip.
        :param cursor: The cursor string used for pagination, signifying the object ID where to start the results.
        :type cursor: str
        :param size: The number of results to return per call. Default 200 if not provided
        :type size: str
        """
        resource = f'trip/{{trip_key}}/points'
        return self._get_pages(resource, trip_key=trip_key, cursor=cursor, size=size)

    def get_visits(self, driver_key=None, vehicle_key=None, place_key=None, entry_after=None, entry_before=None,
                   cursor=None, size=None) -> Generator:
        """Get a a list of visits to all places for a given driver, vehicle or place. A visit begins at the trip
        point a car enters a geofence, and ends at the point they exit. :param driver_key: Filter results to visits
        to a single driver. Optional. :type driver_key: str :param vehicle_key: Filter results to a single vehicle.
        Optional. :type vehicle_key: str :param place_key: Filter results to a single place. Optional. :type
        place_key: str :param entry_after: Filter results to only include visits that started after this timestamp.
        Optional. :type entry_after: str :param entry_before: Filter results to only include visits that started
        before this timestamp. Optional. :type entry_before: str :param cursor: The cursor string used for
        pagination, signifying the object ID where to start the results. :type cursor: str :param size: The number of
        results to return per call. Default 10 if not provided. :type size: str
        """
        return self._get_pages(driver_key=driver_key, vehicle_key=vehicle_key, place_key=place_key,
                               entry_after=entry_after, entry_before=entry_before, cursor=cursor, size=size)


if __name__ == '__main__':
    RA = RestAdapter()
    devices = RA.get_devices()
    groups = RA.get_groups()
    vehicles = RA.get_vehicles()
    trips = RA.get_trips()