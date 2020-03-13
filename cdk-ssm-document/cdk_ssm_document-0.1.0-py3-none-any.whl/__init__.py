"""
# CDK SSM Documents

AWS CDK L3 construct for managing SSM Documents.

Documentation pending...
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
import aws_cdk.aws_kms
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-ssm-document", "0.1.0", __name__, "cdk-ssm-document@0.1.0.jsii.tgz")


class Document(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-ssm-document.Document"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, content: typing.Any, name: str, document_type: typing.Optional[str]=None, target_type: typing.Optional[str]=None, update_default_version: typing.Optional[bool]=None, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None) -> None:
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


@jsii.data_type(jsii_type="cdk-ssm-document.DocumentProps", jsii_struct_bases=[aws_cdk.core.StackProps], name_mapping={'description': 'description', 'env': 'env', 'stack_name': 'stackName', 'tags': 'tags', 'content': 'content', 'name': 'name', 'document_type': 'documentType', 'target_type': 'targetType', 'update_default_version': 'updateDefaultVersion'})
class DocumentProps(aws_cdk.core.StackProps):
    def __init__(self, *, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, content: typing.Any, name: str, document_type: typing.Optional[str]=None, target_type: typing.Optional[str]=None, update_default_version: typing.Optional[bool]=None):
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
    def content(self) -> typing.Any:
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


__all__ = ["Document", "DocumentProps", "__jsii_assembly__"]

publication.publish()
