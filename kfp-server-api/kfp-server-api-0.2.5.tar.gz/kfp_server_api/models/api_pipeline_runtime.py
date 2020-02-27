# coding: utf-8

"""
    KF Pipelines API

    Generated python client for the KF Pipelines server API  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiPipelineRuntime(object):
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
        'pipeline_manifest': 'str',
        'workflow_manifest': 'str'
    }

    attribute_map = {
        'pipeline_manifest': 'pipeline_manifest',
        'workflow_manifest': 'workflow_manifest'
    }

    def __init__(self, pipeline_manifest=None, workflow_manifest=None):  # noqa: E501
        """ApiPipelineRuntime - a model defined in Swagger"""  # noqa: E501

        self._pipeline_manifest = None
        self._workflow_manifest = None
        self.discriminator = None

        if pipeline_manifest is not None:
            self.pipeline_manifest = pipeline_manifest
        if workflow_manifest is not None:
            self.workflow_manifest = workflow_manifest

    @property
    def pipeline_manifest(self):
        """Gets the pipeline_manifest of this ApiPipelineRuntime.  # noqa: E501

        Output. The runtime JSON manifest of the pipeline, including the status of pipeline steps and fields need for UI visualization etc.  # noqa: E501

        :return: The pipeline_manifest of this ApiPipelineRuntime.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_manifest

    @pipeline_manifest.setter
    def pipeline_manifest(self, pipeline_manifest):
        """Sets the pipeline_manifest of this ApiPipelineRuntime.

        Output. The runtime JSON manifest of the pipeline, including the status of pipeline steps and fields need for UI visualization etc.  # noqa: E501

        :param pipeline_manifest: The pipeline_manifest of this ApiPipelineRuntime.  # noqa: E501
        :type: str
        """

        self._pipeline_manifest = pipeline_manifest

    @property
    def workflow_manifest(self):
        """Gets the workflow_manifest of this ApiPipelineRuntime.  # noqa: E501

        Output. The runtime JSON manifest of the argo workflow. This is deprecated after pipeline_runtime_manifest is in use.  # noqa: E501

        :return: The workflow_manifest of this ApiPipelineRuntime.  # noqa: E501
        :rtype: str
        """
        return self._workflow_manifest

    @workflow_manifest.setter
    def workflow_manifest(self, workflow_manifest):
        """Sets the workflow_manifest of this ApiPipelineRuntime.

        Output. The runtime JSON manifest of the argo workflow. This is deprecated after pipeline_runtime_manifest is in use.  # noqa: E501

        :param workflow_manifest: The workflow_manifest of this ApiPipelineRuntime.  # noqa: E501
        :type: str
        """

        self._workflow_manifest = workflow_manifest

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
        if issubclass(ApiPipelineRuntime, dict):
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
        if not isinstance(other, ApiPipelineRuntime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
