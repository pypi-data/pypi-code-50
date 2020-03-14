"""
# CDK SSM Document

[![CDK docs](https://img.shields.io/badge/CDK-docs-orange)](https://awscdk.io/packages/cdk-ssm-document@0.1.0)
[![npm version](https://badge.fury.io/js/cdk-ssm-document.svg)](https://www.npmjs.com/package/cdk-ssm-document)
[![PyPI version](https://badge.fury.io/py/cdk-ssm-document.svg)](https://pypi.org/project/cdk-ssm-document/)
[![NuGet version](https://badge.fury.io/nu/CDK.SSM.Document.svg)](https://www.nuget.org/packages/CDK.SSM.Document/)
[![GitHub](https://img.shields.io/github/license/udondan/cdk-ssm-document)](https://github.com/udondan/cdk-ssm-document/blob/master/LICENSE)

[AWS CDK](https://aws.amazon.com/cdk/) L3 construct for managing SSM Documents.

Roadmap:

* Documentation
* Example
* Function / Parameter documentation
* Tests
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_cloudformation
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-ssm-document", "0.1.4", __name__, "cdk-ssm-document@0.1.4.jsii.tgz")


class Document(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-ssm-document.Document"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, content: typing.Union[str, "DocumentContent"], name: str, document_type: typing.Optional[str]=None, target_type: typing.Optional[str]=None, update_default_version: typing.Optional[bool]=None, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param content: 
        :param name: 
        :param document_type: 
        :param target_type: 
        :param update_default_version: 
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}

        stability
        :stability: experimental
        """
        props = DocumentProps(content=content, name=name, document_type=document_type, target_type=target_type, update_default_version=update_default_version, description=description, env=env, stack_name=stack_name, tags=tags)

        jsii.create(Document, self, [scope, id, props])


@jsii.data_type(jsii_type="cdk-ssm-document.DocumentContent", jsii_struct_bases=[], name_mapping={'main_steps': 'mainSteps', 'schema_version': 'schemaVersion', 'description': 'description', 'parameters': 'parameters'})
class DocumentContent():
    def __init__(self, *, main_steps: typing.List["DocumentMainSteps"], schema_version: str, description: typing.Optional[str]=None, parameters: typing.Optional[typing.Mapping[str,"DocumentParameter"]]=None):
        """
        :param main_steps: 
        :param schema_version: 
        :param description: 
        :param parameters: 

        stability
        :stability: experimental
        """
        self._values = {
            'main_steps': main_steps,
            'schema_version': schema_version,
        }
        if description is not None: self._values["description"] = description
        if parameters is not None: self._values["parameters"] = parameters

    @builtins.property
    def main_steps(self) -> typing.List["DocumentMainSteps"]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('main_steps')

    @builtins.property
    def schema_version(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('schema_version')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('description')

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[str,"DocumentParameter"]]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('parameters')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DocumentContent(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-ssm-document.DocumentMainSteps", jsii_struct_bases=[], name_mapping={'action': 'action', 'inputs': 'inputs', 'name': 'name', 'precondition': 'precondition'})
class DocumentMainSteps():
    def __init__(self, *, action: str, inputs: typing.Mapping[str,typing.Any], name: str, precondition: typing.Optional[typing.Mapping[str,typing.Any]]=None):
        """
        :param action: 
        :param inputs: 
        :param name: 
        :param precondition: 

        stability
        :stability: experimental
        """
        self._values = {
            'action': action,
            'inputs': inputs,
            'name': name,
        }
        if precondition is not None: self._values["precondition"] = precondition

    @builtins.property
    def action(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('action')

    @builtins.property
    def inputs(self) -> typing.Mapping[str,typing.Any]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('inputs')

    @builtins.property
    def name(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def precondition(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('precondition')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DocumentMainSteps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-ssm-document.DocumentParameter", jsii_struct_bases=[], name_mapping={'description': 'description', 'type': 'type', 'allowed_pattern': 'allowedPattern', 'allowed_values': 'allowedValues', 'default': 'default', 'display_type': 'displayType', 'max_chars': 'maxChars', 'max_items': 'maxItems', 'min_chars': 'minChars', 'min_items': 'minItems'})
class DocumentParameter():
    def __init__(self, *, description: str, type: str, allowed_pattern: typing.Optional[str]=None, allowed_values: typing.Optional[typing.List[str]]=None, default: typing.Any=None, display_type: typing.Optional[str]=None, max_chars: typing.Optional[jsii.Number]=None, max_items: typing.Optional[jsii.Number]=None, min_chars: typing.Optional[jsii.Number]=None, min_items: typing.Optional[jsii.Number]=None):
        """
        :param description: 
        :param type: 
        :param allowed_pattern: 
        :param allowed_values: 
        :param default: 
        :param display_type: 
        :param max_chars: 
        :param max_items: 
        :param min_chars: 
        :param min_items: 

        stability
        :stability: experimental
        """
        self._values = {
            'description': description,
            'type': type,
        }
        if allowed_pattern is not None: self._values["allowed_pattern"] = allowed_pattern
        if allowed_values is not None: self._values["allowed_values"] = allowed_values
        if default is not None: self._values["default"] = default
        if display_type is not None: self._values["display_type"] = display_type
        if max_chars is not None: self._values["max_chars"] = max_chars
        if max_items is not None: self._values["max_items"] = max_items
        if min_chars is not None: self._values["min_chars"] = min_chars
        if min_items is not None: self._values["min_items"] = min_items

    @builtins.property
    def description(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('description')

    @builtins.property
    def type(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('type')

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('allowed_pattern')

    @builtins.property
    def allowed_values(self) -> typing.Optional[typing.List[str]]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('allowed_values')

    @builtins.property
    def default(self) -> typing.Any:
        """
        stability
        :stability: experimental
        """
        return self._values.get('default')

    @builtins.property
    def display_type(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('display_type')

    @builtins.property
    def max_chars(self) -> typing.Optional[jsii.Number]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('max_chars')

    @builtins.property
    def max_items(self) -> typing.Optional[jsii.Number]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('max_items')

    @builtins.property
    def min_chars(self) -> typing.Optional[jsii.Number]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('min_chars')

    @builtins.property
    def min_items(self) -> typing.Optional[jsii.Number]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('min_items')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DocumentParameter(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-ssm-document.DocumentProps", jsii_struct_bases=[aws_cdk.core.StackProps], name_mapping={'description': 'description', 'env': 'env', 'stack_name': 'stackName', 'tags': 'tags', 'content': 'content', 'name': 'name', 'document_type': 'documentType', 'target_type': 'targetType', 'update_default_version': 'updateDefaultVersion'})
class DocumentProps(aws_cdk.core.StackProps):
    def __init__(self, *, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, content: typing.Union[str, "DocumentContent"], name: str, document_type: typing.Optional[str]=None, target_type: typing.Optional[str]=None, update_default_version: typing.Optional[bool]=None):
        """
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param content: 
        :param name: 
        :param document_type: 
        :param target_type: 
        :param update_default_version: 

        stability
        :stability: experimental
        """
        if isinstance(env, dict): env = aws_cdk.core.Environment(**env)
        self._values = {
            'content': content,
            'name': name,
        }
        if description is not None: self._values["description"] = description
        if env is not None: self._values["env"] = env
        if stack_name is not None: self._values["stack_name"] = stack_name
        if tags is not None: self._values["tags"] = tags
        if document_type is not None: self._values["document_type"] = document_type
        if target_type is not None: self._values["target_type"] = target_type
        if update_default_version is not None: self._values["update_default_version"] = update_default_version

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """A description of the stack.

        default
        :default: - No description.
        """
        return self._values.get('description')

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.core.Environment]:
        """The AWS environment (account/region) where this stack will be deployed.

        default
        :default:

        - The ``default-account`` and ``default-region`` context parameters will be
          used. If they are undefined, it will not be possible to deploy the stack.
        """
        return self._values.get('env')

    @builtins.property
    def stack_name(self) -> typing.Optional[str]:
        """Name to deploy the stack with.

        default
        :default: - Derived from construct path.
        """
        return self._values.get('stack_name')

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Stack tags that will be applied to all the taggable resources and the stack itself.

        default
        :default: {}
        """
        return self._values.get('tags')

    @builtins.property
    def content(self) -> typing.Union[str, "DocumentContent"]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('content')

    @builtins.property
    def name(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def document_type(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('document_type')

    @builtins.property
    def target_type(self) -> typing.Optional[str]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('target_type')

    @builtins.property
    def update_default_version(self) -> typing.Optional[bool]:
        """
        stability
        :stability: experimental
        """
        return self._values.get('update_default_version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DocumentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["Document", "DocumentContent", "DocumentMainSteps", "DocumentParameter", "DocumentProps", "__jsii_assembly__"]

publication.publish()
