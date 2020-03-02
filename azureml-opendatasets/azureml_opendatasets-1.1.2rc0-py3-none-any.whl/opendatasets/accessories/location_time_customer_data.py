# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains functionality for wrapping customer data with location and time columns."""

from .customer_data import CustomerData
from .location_data import LatLongColumn, ZipCodeColumn, LocationCustomerData
from .time_data import TimeCustomerData

from multimethods import multimethod


class LocationTimeCustomerData (LocationCustomerData, TimeCustomerData):
    """Defines a class wrapper for customer data which contains location column and time column.

    .. code-block:: python

        LocationTimeCustomerData(data, _latlong_column, _time_column_name)
        LocationTimeCustomerData(data, _zipcode_column, _time_column_name)
    """

    @multimethod(object, LatLongColumn, str)
    def __init__(self, data, _latlong_column, _time_column_name):
        """
        Initialize the class using latlong_column class instance.

        :param data: An object representing customer data.
        :type data: azureml.opendatasets.accessories.customer_data.CustomerData
        :param _latlong_column: An instance of a latlong column.
        :type _latlong_column: azureml.opendatasets.accessories.location_data.LatLongColumn
        :param _time_column_name: A datetime column name.
        :type _time_column_name: str
        """
        self.time_column_name = _time_column_name
        (self.latitude_column_name, self.longitude_column_name) = [_latlong_column.lat_name, _latlong_column.long_name]
        CustomerData.__init__(self, data)
        self.extend_time_column(self.env)

    @multimethod(object, ZipCodeColumn, str)
    def __init__(self, data, _zipcode_column, _time_column_name):
        """
        Initialize the class using zipcode_column class instance.

        :param data: An object representing customer data.
        :type data: azureml.opendatasets.accessories.customer_data.CustomerData
        :param _latlong_column: An instance of a zipcode column.
        :type _latlong_column: azureml.opendatasets.accessories.location_data.ZipCodeColumn
        :param _time_column_name: A datetime column name.
        :type _time_column_name: str
        """
        self.time_column_name = _time_column_name
        CustomerData.__init__(self, data)
        self.extend_zip_column(self.env, _zipcode_column.name)
        self.extend_time_column(self.env)
