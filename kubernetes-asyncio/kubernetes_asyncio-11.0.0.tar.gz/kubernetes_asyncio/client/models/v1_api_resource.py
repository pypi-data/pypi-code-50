# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.15.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1APIResource(object):
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
        'categories': 'list[str]',
        'group': 'str',
        'kind': 'str',
        'name': 'str',
        'namespaced': 'bool',
        'short_names': 'list[str]',
        'singular_name': 'str',
        'storage_version_hash': 'str',
        'verbs': 'list[str]',
        'version': 'str'
    }

    attribute_map = {
        'categories': 'categories',
        'group': 'group',
        'kind': 'kind',
        'name': 'name',
        'namespaced': 'namespaced',
        'short_names': 'shortNames',
        'singular_name': 'singularName',
        'storage_version_hash': 'storageVersionHash',
        'verbs': 'verbs',
        'version': 'version'
    }

    def __init__(self, categories=None, group=None, kind=None, name=None, namespaced=None, short_names=None, singular_name=None, storage_version_hash=None, verbs=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1APIResource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._categories = None
        self._group = None
        self._kind = None
        self._name = None
        self._namespaced = None
        self._short_names = None
        self._singular_name = None
        self._storage_version_hash = None
        self._verbs = None
        self._version = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        if group is not None:
            self.group = group
        self.kind = kind
        self.name = name
        self.namespaced = namespaced
        if short_names is not None:
            self.short_names = short_names
        self.singular_name = singular_name
        if storage_version_hash is not None:
            self.storage_version_hash = storage_version_hash
        self.verbs = verbs
        if version is not None:
            self.version = version

    @property
    def categories(self):
        """Gets the categories of this V1APIResource.  # noqa: E501

        categories is a list of the grouped resources this resource belongs to (e.g. 'all')  # noqa: E501

        :return: The categories of this V1APIResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this V1APIResource.

        categories is a list of the grouped resources this resource belongs to (e.g. 'all')  # noqa: E501

        :param categories: The categories of this V1APIResource.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def group(self):
        """Gets the group of this V1APIResource.  # noqa: E501

        group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\".  # noqa: E501

        :return: The group of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1APIResource.

        group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\".  # noqa: E501

        :param group: The group of this V1APIResource.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def kind(self):
        """Gets the kind of this V1APIResource.  # noqa: E501

        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')  # noqa: E501

        :return: The kind of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1APIResource.

        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')  # noqa: E501

        :param kind: The kind of this V1APIResource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this V1APIResource.  # noqa: E501

        name is the plural name of the resource.  # noqa: E501

        :return: The name of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1APIResource.

        name is the plural name of the resource.  # noqa: E501

        :param name: The name of this V1APIResource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespaced(self):
        """Gets the namespaced of this V1APIResource.  # noqa: E501

        namespaced indicates if a resource is namespaced or not.  # noqa: E501

        :return: The namespaced of this V1APIResource.  # noqa: E501
        :rtype: bool
        """
        return self._namespaced

    @namespaced.setter
    def namespaced(self, namespaced):
        """Sets the namespaced of this V1APIResource.

        namespaced indicates if a resource is namespaced or not.  # noqa: E501

        :param namespaced: The namespaced of this V1APIResource.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and namespaced is None:  # noqa: E501
            raise ValueError("Invalid value for `namespaced`, must not be `None`")  # noqa: E501

        self._namespaced = namespaced

    @property
    def short_names(self):
        """Gets the short_names of this V1APIResource.  # noqa: E501

        shortNames is a list of suggested short names of the resource.  # noqa: E501

        :return: The short_names of this V1APIResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._short_names

    @short_names.setter
    def short_names(self, short_names):
        """Sets the short_names of this V1APIResource.

        shortNames is a list of suggested short names of the resource.  # noqa: E501

        :param short_names: The short_names of this V1APIResource.  # noqa: E501
        :type: list[str]
        """

        self._short_names = short_names

    @property
    def singular_name(self):
        """Gets the singular_name of this V1APIResource.  # noqa: E501

        singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.  # noqa: E501

        :return: The singular_name of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._singular_name

    @singular_name.setter
    def singular_name(self, singular_name):
        """Sets the singular_name of this V1APIResource.

        singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.  # noqa: E501

        :param singular_name: The singular_name of this V1APIResource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and singular_name is None:  # noqa: E501
            raise ValueError("Invalid value for `singular_name`, must not be `None`")  # noqa: E501

        self._singular_name = singular_name

    @property
    def storage_version_hash(self):
        """Gets the storage_version_hash of this V1APIResource.  # noqa: E501

        The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates.  # noqa: E501

        :return: The storage_version_hash of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._storage_version_hash

    @storage_version_hash.setter
    def storage_version_hash(self, storage_version_hash):
        """Sets the storage_version_hash of this V1APIResource.

        The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates.  # noqa: E501

        :param storage_version_hash: The storage_version_hash of this V1APIResource.  # noqa: E501
        :type: str
        """

        self._storage_version_hash = storage_version_hash

    @property
    def verbs(self):
        """Gets the verbs of this V1APIResource.  # noqa: E501

        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)  # noqa: E501

        :return: The verbs of this V1APIResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """Sets the verbs of this V1APIResource.

        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)  # noqa: E501

        :param verbs: The verbs of this V1APIResource.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and verbs is None:  # noqa: E501
            raise ValueError("Invalid value for `verbs`, must not be `None`")  # noqa: E501

        self._verbs = verbs

    @property
    def version(self):
        """Gets the version of this V1APIResource.  # noqa: E501

        version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)\".  # noqa: E501

        :return: The version of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1APIResource.

        version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)\".  # noqa: E501

        :param version: The version of this V1APIResource.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, V1APIResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1APIResource):
            return True

        return self.to_dict() != other.to_dict()
