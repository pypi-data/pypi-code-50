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


class V1beta1StorageClass(object):
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
        'allow_volume_expansion': 'bool',
        'allowed_topologies': 'list[V1TopologySelectorTerm]',
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'mount_options': 'list[str]',
        'parameters': 'dict(str, str)',
        'provisioner': 'str',
        'reclaim_policy': 'str',
        'volume_binding_mode': 'str'
    }

    attribute_map = {
        'allow_volume_expansion': 'allowVolumeExpansion',
        'allowed_topologies': 'allowedTopologies',
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'mount_options': 'mountOptions',
        'parameters': 'parameters',
        'provisioner': 'provisioner',
        'reclaim_policy': 'reclaimPolicy',
        'volume_binding_mode': 'volumeBindingMode'
    }

    def __init__(self, allow_volume_expansion=None, allowed_topologies=None, api_version=None, kind=None, metadata=None, mount_options=None, parameters=None, provisioner=None, reclaim_policy=None, volume_binding_mode=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1StorageClass - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allow_volume_expansion = None
        self._allowed_topologies = None
        self._api_version = None
        self._kind = None
        self._metadata = None
        self._mount_options = None
        self._parameters = None
        self._provisioner = None
        self._reclaim_policy = None
        self._volume_binding_mode = None
        self.discriminator = None

        if allow_volume_expansion is not None:
            self.allow_volume_expansion = allow_volume_expansion
        if allowed_topologies is not None:
            self.allowed_topologies = allowed_topologies
        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if mount_options is not None:
            self.mount_options = mount_options
        if parameters is not None:
            self.parameters = parameters
        self.provisioner = provisioner
        if reclaim_policy is not None:
            self.reclaim_policy = reclaim_policy
        if volume_binding_mode is not None:
            self.volume_binding_mode = volume_binding_mode

    @property
    def allow_volume_expansion(self):
        """Gets the allow_volume_expansion of this V1beta1StorageClass.  # noqa: E501

        AllowVolumeExpansion shows whether the storage class allow volume expand  # noqa: E501

        :return: The allow_volume_expansion of this V1beta1StorageClass.  # noqa: E501
        :rtype: bool
        """
        return self._allow_volume_expansion

    @allow_volume_expansion.setter
    def allow_volume_expansion(self, allow_volume_expansion):
        """Sets the allow_volume_expansion of this V1beta1StorageClass.

        AllowVolumeExpansion shows whether the storage class allow volume expand  # noqa: E501

        :param allow_volume_expansion: The allow_volume_expansion of this V1beta1StorageClass.  # noqa: E501
        :type: bool
        """

        self._allow_volume_expansion = allow_volume_expansion

    @property
    def allowed_topologies(self):
        """Gets the allowed_topologies of this V1beta1StorageClass.  # noqa: E501

        Restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature.  # noqa: E501

        :return: The allowed_topologies of this V1beta1StorageClass.  # noqa: E501
        :rtype: list[V1TopologySelectorTerm]
        """
        return self._allowed_topologies

    @allowed_topologies.setter
    def allowed_topologies(self, allowed_topologies):
        """Sets the allowed_topologies of this V1beta1StorageClass.

        Restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature.  # noqa: E501

        :param allowed_topologies: The allowed_topologies of this V1beta1StorageClass.  # noqa: E501
        :type: list[V1TopologySelectorTerm]
        """

        self._allowed_topologies = allowed_topologies

    @property
    def api_version(self):
        """Gets the api_version of this V1beta1StorageClass.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1beta1StorageClass.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1beta1StorageClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1beta1StorageClass.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this V1beta1StorageClass.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1beta1StorageClass.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1beta1StorageClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1beta1StorageClass.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1beta1StorageClass.  # noqa: E501


        :return: The metadata of this V1beta1StorageClass.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1beta1StorageClass.


        :param metadata: The metadata of this V1beta1StorageClass.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def mount_options(self):
        """Gets the mount_options of this V1beta1StorageClass.  # noqa: E501

        Dynamically provisioned PersistentVolumes of this storage class are created with these mountOptions, e.g. [\"ro\", \"soft\"]. Not validated - mount of the PVs will simply fail if one is invalid.  # noqa: E501

        :return: The mount_options of this V1beta1StorageClass.  # noqa: E501
        :rtype: list[str]
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """Sets the mount_options of this V1beta1StorageClass.

        Dynamically provisioned PersistentVolumes of this storage class are created with these mountOptions, e.g. [\"ro\", \"soft\"]. Not validated - mount of the PVs will simply fail if one is invalid.  # noqa: E501

        :param mount_options: The mount_options of this V1beta1StorageClass.  # noqa: E501
        :type: list[str]
        """

        self._mount_options = mount_options

    @property
    def parameters(self):
        """Gets the parameters of this V1beta1StorageClass.  # noqa: E501

        Parameters holds the parameters for the provisioner that should create volumes of this storage class.  # noqa: E501

        :return: The parameters of this V1beta1StorageClass.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this V1beta1StorageClass.

        Parameters holds the parameters for the provisioner that should create volumes of this storage class.  # noqa: E501

        :param parameters: The parameters of this V1beta1StorageClass.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def provisioner(self):
        """Gets the provisioner of this V1beta1StorageClass.  # noqa: E501

        Provisioner indicates the type of the provisioner.  # noqa: E501

        :return: The provisioner of this V1beta1StorageClass.  # noqa: E501
        :rtype: str
        """
        return self._provisioner

    @provisioner.setter
    def provisioner(self, provisioner):
        """Sets the provisioner of this V1beta1StorageClass.

        Provisioner indicates the type of the provisioner.  # noqa: E501

        :param provisioner: The provisioner of this V1beta1StorageClass.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and provisioner is None:  # noqa: E501
            raise ValueError("Invalid value for `provisioner`, must not be `None`")  # noqa: E501

        self._provisioner = provisioner

    @property
    def reclaim_policy(self):
        """Gets the reclaim_policy of this V1beta1StorageClass.  # noqa: E501

        Dynamically provisioned PersistentVolumes of this storage class are created with this reclaimPolicy. Defaults to Delete.  # noqa: E501

        :return: The reclaim_policy of this V1beta1StorageClass.  # noqa: E501
        :rtype: str
        """
        return self._reclaim_policy

    @reclaim_policy.setter
    def reclaim_policy(self, reclaim_policy):
        """Sets the reclaim_policy of this V1beta1StorageClass.

        Dynamically provisioned PersistentVolumes of this storage class are created with this reclaimPolicy. Defaults to Delete.  # noqa: E501

        :param reclaim_policy: The reclaim_policy of this V1beta1StorageClass.  # noqa: E501
        :type: str
        """

        self._reclaim_policy = reclaim_policy

    @property
    def volume_binding_mode(self):
        """Gets the volume_binding_mode of this V1beta1StorageClass.  # noqa: E501

        VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.  # noqa: E501

        :return: The volume_binding_mode of this V1beta1StorageClass.  # noqa: E501
        :rtype: str
        """
        return self._volume_binding_mode

    @volume_binding_mode.setter
    def volume_binding_mode(self, volume_binding_mode):
        """Sets the volume_binding_mode of this V1beta1StorageClass.

        VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.  # noqa: E501

        :param volume_binding_mode: The volume_binding_mode of this V1beta1StorageClass.  # noqa: E501
        :type: str
        """

        self._volume_binding_mode = volume_binding_mode

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
        if not isinstance(other, V1beta1StorageClass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1StorageClass):
            return True

        return self.to_dict() != other.to_dict()
