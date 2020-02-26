# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.30
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.custom_property import CustomProperty  # noqa: F401,E501
from launchdarkly_api.models.feature_flag_config import FeatureFlagConfig  # noqa: F401,E501
from launchdarkly_api.models.links import Links  # noqa: F401,E501
from launchdarkly_api.models.member import Member  # noqa: F401,E501
from launchdarkly_api.models.variation import Variation  # noqa: F401,E501


class FeatureFlag(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key': 'str',
        'name': 'str',
        'description': 'str',
        'kind': 'str',
        'creation_date': 'float',
        'include_in_snippet': 'bool',
        'temporary': 'bool',
        'maintainer_id': 'str',
        'tags': 'list[str]',
        'variations': 'list[Variation]',
        'goal_ids': 'list[str]',
        'version': 'int',
        'custom_properties': 'dict(str, CustomProperty)',
        'links': 'Links',
        'maintainer': 'Member',
        'environments': 'dict(str, FeatureFlagConfig)',
        'archived_date': 'float',
        'archived': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'description': 'description',
        'kind': 'kind',
        'creation_date': 'creationDate',
        'include_in_snippet': 'includeInSnippet',
        'temporary': 'temporary',
        'maintainer_id': 'maintainerId',
        'tags': 'tags',
        'variations': 'variations',
        'goal_ids': 'goalIds',
        'version': '_version',
        'custom_properties': 'customProperties',
        'links': '_links',
        'maintainer': '_maintainer',
        'environments': 'environments',
        'archived_date': 'archivedDate',
        'archived': 'archived'
    }

    def __init__(self, key=None, name=None, description=None, kind=None, creation_date=None, include_in_snippet=None, temporary=None, maintainer_id=None, tags=None, variations=None, goal_ids=None, version=None, custom_properties=None, links=None, maintainer=None, environments=None, archived_date=None, archived=None):  # noqa: E501
        """FeatureFlag - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._name = None
        self._description = None
        self._kind = None
        self._creation_date = None
        self._include_in_snippet = None
        self._temporary = None
        self._maintainer_id = None
        self._tags = None
        self._variations = None
        self._goal_ids = None
        self._version = None
        self._custom_properties = None
        self._links = None
        self._maintainer = None
        self._environments = None
        self._archived_date = None
        self._archived = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if kind is not None:
            self.kind = kind
        if creation_date is not None:
            self.creation_date = creation_date
        if include_in_snippet is not None:
            self.include_in_snippet = include_in_snippet
        if temporary is not None:
            self.temporary = temporary
        if maintainer_id is not None:
            self.maintainer_id = maintainer_id
        if tags is not None:
            self.tags = tags
        if variations is not None:
            self.variations = variations
        if goal_ids is not None:
            self.goal_ids = goal_ids
        if version is not None:
            self.version = version
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if links is not None:
            self.links = links
        if maintainer is not None:
            self.maintainer = maintainer
        if environments is not None:
            self.environments = environments
        if archived_date is not None:
            self.archived_date = archived_date
        if archived is not None:
            self.archived = archived

    @property
    def key(self):
        """Gets the key of this FeatureFlag.  # noqa: E501


        :return: The key of this FeatureFlag.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FeatureFlag.


        :param key: The key of this FeatureFlag.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this FeatureFlag.  # noqa: E501

        Name of the feature flag.  # noqa: E501

        :return: The name of this FeatureFlag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureFlag.

        Name of the feature flag.  # noqa: E501

        :param name: The name of this FeatureFlag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FeatureFlag.  # noqa: E501

        Description of the feature flag.  # noqa: E501

        :return: The description of this FeatureFlag.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeatureFlag.

        Description of the feature flag.  # noqa: E501

        :param description: The description of this FeatureFlag.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def kind(self):
        """Gets the kind of this FeatureFlag.  # noqa: E501

        Whether the feature flag is a boolean flag or multivariate.  # noqa: E501

        :return: The kind of this FeatureFlag.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this FeatureFlag.

        Whether the feature flag is a boolean flag or multivariate.  # noqa: E501

        :param kind: The kind of this FeatureFlag.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def creation_date(self):
        """Gets the creation_date of this FeatureFlag.  # noqa: E501

        A unix epoch time in milliseconds specifying the creation time of this flag.  # noqa: E501

        :return: The creation_date of this FeatureFlag.  # noqa: E501
        :rtype: float
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this FeatureFlag.

        A unix epoch time in milliseconds specifying the creation time of this flag.  # noqa: E501

        :param creation_date: The creation_date of this FeatureFlag.  # noqa: E501
        :type: float
        """

        self._creation_date = creation_date

    @property
    def include_in_snippet(self):
        """Gets the include_in_snippet of this FeatureFlag.  # noqa: E501


        :return: The include_in_snippet of this FeatureFlag.  # noqa: E501
        :rtype: bool
        """
        return self._include_in_snippet

    @include_in_snippet.setter
    def include_in_snippet(self, include_in_snippet):
        """Sets the include_in_snippet of this FeatureFlag.


        :param include_in_snippet: The include_in_snippet of this FeatureFlag.  # noqa: E501
        :type: bool
        """

        self._include_in_snippet = include_in_snippet

    @property
    def temporary(self):
        """Gets the temporary of this FeatureFlag.  # noqa: E501

        Whether or not this flag is temporary.  # noqa: E501

        :return: The temporary of this FeatureFlag.  # noqa: E501
        :rtype: bool
        """
        return self._temporary

    @temporary.setter
    def temporary(self, temporary):
        """Sets the temporary of this FeatureFlag.

        Whether or not this flag is temporary.  # noqa: E501

        :param temporary: The temporary of this FeatureFlag.  # noqa: E501
        :type: bool
        """

        self._temporary = temporary

    @property
    def maintainer_id(self):
        """Gets the maintainer_id of this FeatureFlag.  # noqa: E501

        The ID of the member that should maintain this flag.  # noqa: E501

        :return: The maintainer_id of this FeatureFlag.  # noqa: E501
        :rtype: str
        """
        return self._maintainer_id

    @maintainer_id.setter
    def maintainer_id(self, maintainer_id):
        """Sets the maintainer_id of this FeatureFlag.

        The ID of the member that should maintain this flag.  # noqa: E501

        :param maintainer_id: The maintainer_id of this FeatureFlag.  # noqa: E501
        :type: str
        """

        self._maintainer_id = maintainer_id

    @property
    def tags(self):
        """Gets the tags of this FeatureFlag.  # noqa: E501

        An array of tags for this feature flag.  # noqa: E501

        :return: The tags of this FeatureFlag.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FeatureFlag.

        An array of tags for this feature flag.  # noqa: E501

        :param tags: The tags of this FeatureFlag.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def variations(self):
        """Gets the variations of this FeatureFlag.  # noqa: E501

        The variations for this feature flag.  # noqa: E501

        :return: The variations of this FeatureFlag.  # noqa: E501
        :rtype: list[Variation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """Sets the variations of this FeatureFlag.

        The variations for this feature flag.  # noqa: E501

        :param variations: The variations of this FeatureFlag.  # noqa: E501
        :type: list[Variation]
        """

        self._variations = variations

    @property
    def goal_ids(self):
        """Gets the goal_ids of this FeatureFlag.  # noqa: E501

        An array goals from all environments associated with this feature flag  # noqa: E501

        :return: The goal_ids of this FeatureFlag.  # noqa: E501
        :rtype: list[str]
        """
        return self._goal_ids

    @goal_ids.setter
    def goal_ids(self, goal_ids):
        """Sets the goal_ids of this FeatureFlag.

        An array goals from all environments associated with this feature flag  # noqa: E501

        :param goal_ids: The goal_ids of this FeatureFlag.  # noqa: E501
        :type: list[str]
        """

        self._goal_ids = goal_ids

    @property
    def version(self):
        """Gets the version of this FeatureFlag.  # noqa: E501


        :return: The version of this FeatureFlag.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FeatureFlag.


        :param version: The version of this FeatureFlag.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def custom_properties(self):
        """Gets the custom_properties of this FeatureFlag.  # noqa: E501

        A mapping of keys to CustomProperty entries.  # noqa: E501

        :return: The custom_properties of this FeatureFlag.  # noqa: E501
        :rtype: dict(str, CustomProperty)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this FeatureFlag.

        A mapping of keys to CustomProperty entries.  # noqa: E501

        :param custom_properties: The custom_properties of this FeatureFlag.  # noqa: E501
        :type: dict(str, CustomProperty)
        """

        self._custom_properties = custom_properties

    @property
    def links(self):
        """Gets the links of this FeatureFlag.  # noqa: E501


        :return: The links of this FeatureFlag.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FeatureFlag.


        :param links: The links of this FeatureFlag.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def maintainer(self):
        """Gets the maintainer of this FeatureFlag.  # noqa: E501


        :return: The maintainer of this FeatureFlag.  # noqa: E501
        :rtype: Member
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        """Sets the maintainer of this FeatureFlag.


        :param maintainer: The maintainer of this FeatureFlag.  # noqa: E501
        :type: Member
        """

        self._maintainer = maintainer

    @property
    def environments(self):
        """Gets the environments of this FeatureFlag.  # noqa: E501


        :return: The environments of this FeatureFlag.  # noqa: E501
        :rtype: dict(str, FeatureFlagConfig)
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this FeatureFlag.


        :param environments: The environments of this FeatureFlag.  # noqa: E501
        :type: dict(str, FeatureFlagConfig)
        """

        self._environments = environments

    @property
    def archived_date(self):
        """Gets the archived_date of this FeatureFlag.  # noqa: E501

        A unix epoch time in milliseconds specifying the archived time of this flag.  # noqa: E501

        :return: The archived_date of this FeatureFlag.  # noqa: E501
        :rtype: float
        """
        return self._archived_date

    @archived_date.setter
    def archived_date(self, archived_date):
        """Sets the archived_date of this FeatureFlag.

        A unix epoch time in milliseconds specifying the archived time of this flag.  # noqa: E501

        :param archived_date: The archived_date of this FeatureFlag.  # noqa: E501
        :type: float
        """

        self._archived_date = archived_date

    @property
    def archived(self):
        """Gets the archived of this FeatureFlag.  # noqa: E501

        Whether or not this flag is archived.  # noqa: E501

        :return: The archived of this FeatureFlag.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this FeatureFlag.

        Whether or not this flag is archived.  # noqa: E501

        :param archived: The archived of this FeatureFlag.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(FeatureFlag, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeatureFlag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
