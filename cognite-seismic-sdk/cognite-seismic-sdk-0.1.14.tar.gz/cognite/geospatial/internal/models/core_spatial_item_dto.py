# coding: utf-8

"""
    Cognite API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: playground
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cognite.geospatial.internal.configuration import Configuration


class CoreSpatialItemDTO(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'external_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'description': 'str',
        'metadata': 'dict(str, str)',
        'asset_ids': 'list[int]',
        'source': 'str',
        'geometry': 'GeometrySpatialDTO',
        'crs': 'str'
    }

    attribute_map = {
        'name': 'name',
        'external_id': 'externalId',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'description': 'description',
        'metadata': 'metadata',
        'asset_ids': 'assetIds',
        'source': 'source',
        'geometry': 'geometry',
        'crs': 'crs'
    }

    def __init__(self, name=None, external_id=None, start_time=None, end_time=None, description=None, metadata=None, asset_ids=None, source=None, geometry=None, crs=None, local_vars_configuration=None):  # noqa: E501
        """CoreSpatialItemDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._external_id = None
        self._start_time = None
        self._end_time = None
        self._description = None
        self._metadata = None
        self._asset_ids = None
        self._source = None
        self._geometry = None
        self._crs = None
        self.discriminator = None

        self.name = name
        if external_id is not None:
            self.external_id = external_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata
        if asset_ids is not None:
            self.asset_ids = asset_ids
        if source is not None:
            self.source = source
        self.geometry = geometry
        self.crs = crs

    @property
    def name(self):
        """Gets the name of this CoreSpatialItemDTO.  # noqa: E501

        The name of the spatial item  # noqa: E501

        :return: The name of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CoreSpatialItemDTO.

        The name of the spatial item  # noqa: E501

        :param name: The name of this CoreSpatialItemDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def external_id(self):
        """Gets the external_id of this CoreSpatialItemDTO.  # noqa: E501

        External Id provided by client. Should be unique within a given project/resource combination.  # noqa: E501

        :return: The external_id of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CoreSpatialItemDTO.

        External Id provided by client. Should be unique within a given project/resource combination.  # noqa: E501

        :param external_id: The external_id of this CoreSpatialItemDTO.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) > 255):
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `255`")  # noqa: E501

        self._external_id = external_id

    @property
    def start_time(self):
        """Gets the start_time of this CoreSpatialItemDTO.  # noqa: E501

        The number of milliseconds since 00:00:00 Thursday, 1 January 1970, Coordinated Universal Time (UTC), minus leap seconds.  # noqa: E501

        :return: The start_time of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CoreSpatialItemDTO.

        The number of milliseconds since 00:00:00 Thursday, 1 January 1970, Coordinated Universal Time (UTC), minus leap seconds.  # noqa: E501

        :param start_time: The start_time of this CoreSpatialItemDTO.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                start_time is not None and start_time < 0):  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CoreSpatialItemDTO.  # noqa: E501

        The number of milliseconds since 00:00:00 Thursday, 1 January 1970, Coordinated Universal Time (UTC), minus leap seconds.  # noqa: E501

        :return: The end_time of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CoreSpatialItemDTO.

        The number of milliseconds since 00:00:00 Thursday, 1 January 1970, Coordinated Universal Time (UTC), minus leap seconds.  # noqa: E501

        :param end_time: The end_time of this CoreSpatialItemDTO.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                end_time is not None and end_time < 0):  # noqa: E501
            raise ValueError("Invalid value for `end_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._end_time = end_time

    @property
    def description(self):
        """Gets the description of this CoreSpatialItemDTO.  # noqa: E501

        Textual description of the spatial item.  # noqa: E501

        :return: The description of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CoreSpatialItemDTO.

        Textual description of the spatial item.  # noqa: E501

        :param description: The description of this CoreSpatialItemDTO.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 500):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `500`")  # noqa: E501

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this CoreSpatialItemDTO.  # noqa: E501

        Custom, application specific metadata. String key -> String value.  # noqa: E501

        :return: The metadata of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CoreSpatialItemDTO.

        Custom, application specific metadata. String key -> String value.  # noqa: E501

        :param metadata: The metadata of this CoreSpatialItemDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def asset_ids(self):
        """Gets the asset_ids of this CoreSpatialItemDTO.  # noqa: E501

        Asset IDs of related asset resource item that this spatial item relates to.  # noqa: E501

        :return: The asset_ids of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: list[int]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        """Sets the asset_ids of this CoreSpatialItemDTO.

        Asset IDs of related asset resource item that this spatial item relates to.  # noqa: E501

        :param asset_ids: The asset_ids of this CoreSpatialItemDTO.  # noqa: E501
        :type: list[int]
        """

        self._asset_ids = asset_ids

    @property
    def source(self):
        """Gets the source of this CoreSpatialItemDTO.  # noqa: E501

        The source of this spatial item  # noqa: E501

        :return: The source of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CoreSpatialItemDTO.

        The source of this spatial item  # noqa: E501

        :param source: The source of this CoreSpatialItemDTO.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                source is not None and len(source) > 128):
            raise ValueError("Invalid value for `source`, length must be less than or equal to `128`")  # noqa: E501

        self._source = source

    @property
    def geometry(self):
        """Gets the geometry of this CoreSpatialItemDTO.  # noqa: E501


        :return: The geometry of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: GeometrySpatialDTO
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this CoreSpatialItemDTO.


        :param geometry: The geometry of this CoreSpatialItemDTO.  # noqa: E501
        :type: GeometrySpatialDTO
        """
        if self.local_vars_configuration.client_side_validation and geometry is None:  # noqa: E501
            raise ValueError("Invalid value for `geometry`, must not be `None`")  # noqa: E501

        self._geometry = geometry

    @property
    def crs(self):
        """Gets the crs of this CoreSpatialItemDTO.  # noqa: E501

        CRS specified using epsg:<number>  # noqa: E501

        :return: The crs of this CoreSpatialItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._crs

    @crs.setter
    def crs(self, crs):
        """Sets the crs of this CoreSpatialItemDTO.

        CRS specified using epsg:<number>  # noqa: E501

        :param crs: The crs of this CoreSpatialItemDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and crs is None:  # noqa: E501
            raise ValueError("Invalid value for `crs`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                crs is not None and len(crs) > 128):
            raise ValueError("Invalid value for `crs`, length must be less than or equal to `128`")  # noqa: E501

        self._crs = crs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CoreSpatialItemDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoreSpatialItemDTO):
            return True

        return self.to_dict() != other.to_dict()
