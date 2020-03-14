"""
# CDK SSM Document

[![CDK docs](https://img.shields.io/badge/CDK-docs-orange)](https://awscdk.io/packages/cdk-ssm-document@1.0.0)
[![npm version](https://badge.fury.io/js/cdk-ssm-document.svg)](https://www.npmjs.com/package/cdk-ssm-document)
[![PyPI version](https://badge.fury.io/py/cdk-ssm-document.svg)](https://pypi.org/project/cdk-ssm-document/)
[![NuGet version](https://badge.fury.io/nu/CDK.SSM.Document.svg)](https://www.nuget.org/packages/CDK.SSM.Document/)
[![GitHub](https://img.shields.io/github/license/udondan/cdk-ssm-document)](https://github.com/udondan/cdk-ssm-document/blob/master/LICENSE)

[AWS CDK](https://aws.amazon.com/cdk/) L3 construct for managing SSM Documents.

CloudFormation's support for SSM Documents [currently is lacking updating functionality](https://github.com/aws-cloudformation/aws-cloudformation-coverage-roadmap/issues/339). Instead of updating a document, CFN will replace it. The old document is destroyed and a new one is saved with a different name. This is problematic because:

* When names potentially changes, you cannot directly reference a document
* Old versions are permanently lost

This construct provides document support in a way it should have been implemented in the first place:

* Changes on documents will cerate new versions
* Versions cannot be deleted

## Usage

### Creating a document from a YAML or JSON file

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
from cdk_ssm_document import Document
import fs as fs
import path as path

class TestStack(cdk.Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags)

        file = path.join(__dirname, "../documents/hello-world-yaml.yml")
        Document(self, "SSM-Document-HelloWorld",
            name="HelloWorld",
            content=fs.read_file_sync(file).to_string()
        )
```

### Creating a document via inline definition

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
from cdk_ssm_document import Document
import fs as fs
import path as path

class TestStack(cdk.Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags)

        Document(self, "SSM-Document-HelloWorld",
            name="HelloWorld",
            content={
                "schema_version": "2.2",
                "description": "Echo Hello World!",
                "parameters": {
                    "text": {
                        "default": "Hello World!",
                        "description": "Text to echo",
                        "type": "String"
                    }
                },
                "main_steps": [{
                    "name": "echo",
                    "action": "aws:runShellScript",
                    "inputs": {
                        "run_command": ["echo \"{{text}}\""
                        ]
                    },
                    "precondition": {
                        "StringEquals": ["platformType", "Linux"
                        ]
                    }
                }
                ]
            }
        )
```

### Deploy all YAML/JSON files from a directory

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
from cdk_ssm_document import Document
import fs as fs
import path as path

class TestStack(cdk.Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags)

        dir = path.join(__dirname, "../documents")
        files = fs.readdir_sync(dir)for (const i in files) {
                    const name = files[i];
                    const shortName = name.split('.').slice(0, -1).join('.'); // removes file extension
                    const file = `${dir}/${name}`;

                    new Document(this, `SSM-Document-${shortName}`, {
                        name: shortName,
                        content: fs.readFileSync(file).toString(),
                    });
                }
```

## Using the Lambda as a custom resource in CloudFormation - without CDK

If you're still not convinced to use the [AWS CDK](https://aws.amazon.com/cdk/), you can still use the Lambda as a [custom resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) in your CFN template. Here is how:

1. **Create a zip fie for the Lambda:**

   To create a zip from the Lambda source run:

   ```bash
   lambda/build
   ```

   This will generate the file `lambda/code.zip`.
2. **Upload the Lambda function:**

   Upload this  zip file to an S3 bucket via cli, Console or however you like.

   Example via cli:

   ```bash
   aws s3 cp lambda/code.zip s3://example-bucket/code.zip
   ```
3. **Deploy a CloudFormation stack utilizing the zip as a custom resource provider:**

   Example CloudFormation template:

   ```yaml
   ---
   AWSTemplateFormatVersion: "2010-09-09"
   Resources:
     SSMDocExecutionRole:
       Type: AWS::IAM::Role
       Properties:
         RoleName: CFN-Resource-Custom-SSM-Document
         AssumeRolePolicyDocument:
           Version: "2012-10-17"
           Statement:
             - Effect: Allow
               Principal:
                 Service: lambda.amazonaws.com
               Action: sts:AssumeRole
         ManagedPolicyArns:
           - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
           - Ref: SSMDocExecutionPolicy

     SSMDocExecutionPolicy:
       Type: AWS::IAM::ManagedPolicy
       Properties:
         ManagedPolicyName: CFN-Resource-Custom-SSM-Document
         PolicyDocument:
           Version: "2012-10-17"
           Statement:
             - Effect: Allow
               Action:
                 - ssm:ListDocuments
                 - ssm:ListTagsForResource
               Resource: "*"
             - Effect: Allow
               Action:
                 - ssm:CreateDocument
                 - ssm:AddTagsToResource
               Resource: "*"
               Condition:
                 StringEquals:
                   aws:RequestTag/CreatedBy: CFN::Resource::Custom::SSM-Document
             - Effect: Allow
               Action:
                 - ssm:DeleteDocument
                 - ssm:DescribeDocument
                 - ssm:GetDocument
                 - ssm:ListDocumentVersions
                 - ssm:ModifyDocumentPermission
                 - ssm:UpdateDocument
                 - ssm:UpdateDocumentDefaultVersion
                 - ssm:AddTagsToResource
                 - ssm:RemoveTagsFromResource
               Resource: "*"
               Condition:
                 StringEquals:
                   aws:ResourceTag/CreatedBy: CFN::Resource::Custom::SSM-Document

     SSMDocFunction:
       Type: AWS::Lambda::Function
       Properties:
         FunctionName: CFN-Resource-Custom-SSM-Document-Manager
         Code:
           S3Bucket: example-bucket
           S3Key: code.zip
         Handler: index.handler
         Runtime: nodejs10.x
         Timeout: 3
         Role: !GetAtt SSMDocExecutionRole.Arn

     MyDocument:
       Type: Custom::SSM-Document
       Properties:
         Name: MyDocument
         ServiceToken: !GetAtt SSMDocFunction.Arn
         StackName: !Ref AWS::StackName
         UpdateDefaultVersion: true # default: true
         Content:
           schemaVersion: "2.2"
           description: Echo Hello World!
           parameters:
             text:
               type: String
               description: Text to echo
               default: Hello World!
           mainSteps:
             - name: echo
               action: aws:runShellScript
               inputs:
                 runCommand:
                   - echo "{{text}}"
               precondition:
                 StringEquals:
                   - platformType
                   - Linux
         DocumentType: Command # default: Command
         TargetType: / # default: /
         Tags:
           CreatedBy: CFN::Resource::Custom::SSM-Document # required, see above policy conditions
   ```

## Roadmap

* Automated Tests
* Tagging support in a more standardized way
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

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-ssm-document", "1.0.0", __name__, "cdk-ssm-document@1.0.0.jsii.tgz")


class Document(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-ssm-document.Document"):
    """An SSM document."""
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, content: typing.Union[str, "DocumentContent"], name: str, document_type: typing.Optional[str]=None, target_type: typing.Optional[str]=None, update_default_version: typing.Optional[bool]=None, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """Defines a new SSM document.

        :param scope: -
        :param id: -
        :param content: Content of the SSM document. Can be passed as string or as object
        :param name: Name of the document. The name must be between 3 and 128 characters. Valid characters are a-z, A-Z, 0-9, and _, -, and . only
        :param document_type: Document type based on the service that you want to use. Default: Command
        :param target_type: Types of resources the document can run on. For example, ``/AWS::EC2::Instance`` or ``/`` for all resource types. Default: /
        :param update_default_version: Defined if the default version should be updated to the latest version on document updates. Default: true
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        """
        props = DocumentProps(content=content, name=name, document_type=document_type, target_type=target_type, update_default_version=update_default_version, description=description, env=env, stack_name=stack_name, tags=tags)

        jsii.create(Document, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """Name of the document."""
        return jsii.get(self, "name")


@jsii.data_type(jsii_type="cdk-ssm-document.DocumentContent", jsii_struct_bases=[], name_mapping={'main_steps': 'mainSteps', 'schema_version': 'schemaVersion', 'description': 'description', 'parameters': 'parameters'})
class DocumentContent():
    def __init__(self, *, main_steps: typing.List["DocumentMainStep"], schema_version: str, description: typing.Optional[str]=None, parameters: typing.Optional[typing.Mapping[str,"DocumentParameter"]]=None):
        """The content of the SSM document.

        The syntax of your document is defined by the schema version used to create it.

        This module only supports schema version 2.2

        For details see https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-doc-syntax.html

        :param main_steps: An object that can include multiple steps (plugins). Steps include one or more actions, an optional precondition, a unique name of the action, and inputs (parameters) for those actions. For more information about documents, including information about creating documents and the differences between schema versions, see https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-plugins.html
        :param schema_version: The schema version to use, e.g. 2.2.
        :param description: Information you provide to describe the purpose of the document.
        :param parameters: The parameters the document accepts.
        """
        self._values = {
            'main_steps': main_steps,
            'schema_version': schema_version,
        }
        if description is not None: self._values["description"] = description
        if parameters is not None: self._values["parameters"] = parameters

    @builtins.property
    def main_steps(self) -> typing.List["DocumentMainStep"]:
        """An object that can include multiple steps (plugins).

        Steps include one or more actions, an optional precondition, a unique name of the action, and inputs (parameters) for those actions.

        For more information about documents, including information about creating documents and the differences between schema versions, see https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-plugins.html
        """
        return self._values.get('main_steps')

    @builtins.property
    def schema_version(self) -> str:
        """The schema version to use, e.g. 2.2."""
        return self._values.get('schema_version')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """Information you provide to describe the purpose of the document."""
        return self._values.get('description')

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[str,"DocumentParameter"]]:
        """The parameters the document accepts."""
        return self._values.get('parameters')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DocumentContent(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-ssm-document.DocumentMainStep", jsii_struct_bases=[], name_mapping={})
class DocumentMainStep():
    def __init__(self):
        """Steps include one or more actions, an optional precondition, a unique name of the action, and inputs (parameters) for those actions.

        For more information about documents, including information about creating documents and the differences between schema versions, see https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-plugins.html
        """
        self._values = {
        }

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DocumentMainStep(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-ssm-document.DocumentParameter", jsii_struct_bases=[], name_mapping={'description': 'description', 'type': 'type', 'allowed_pattern': 'allowedPattern', 'allowed_values': 'allowedValues', 'default': 'default', 'display_type': 'displayType', 'max_chars': 'maxChars', 'max_items': 'maxItems', 'min_chars': 'minChars', 'min_items': 'minItems'})
class DocumentParameter():
    def __init__(self, *, description: str, type: str, allowed_pattern: typing.Optional[str]=None, allowed_values: typing.Optional[typing.List[str]]=None, default: typing.Any=None, display_type: typing.Optional[str]=None, max_chars: typing.Optional[jsii.Number]=None, max_items: typing.Optional[jsii.Number]=None, min_chars: typing.Optional[jsii.Number]=None, min_items: typing.Optional[jsii.Number]=None):
        """An SSM document parameter.

        :param description: A description of the parameter.
        :param type: Allowed values include the following: String, StringList, Boolean, Integer, MapList, and StringMap. To view examples of each type, see https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-plugins.html#top-level-properties-type
        :param allowed_pattern: The regular expression the parameter must match.
        :param allowed_values: Allowed values for the parameter.
        :param default: The default value of the parameter or a reference to a parameter in Parameter Store.
        :param display_type: Used to display either a textfield or a textarea in the AWS console. textfield is a single-line text box. textarea is a multi-line text area
        :param max_chars: The maximum number of parameter characters allowed.
        :param max_items: The maximum number of items allowed.
        :param min_chars: The minimum number of parameter characters allowed.
        :param min_items: The minimum number of items allowed.
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
        """A description of the parameter."""
        return self._values.get('description')

    @builtins.property
    def type(self) -> str:
        """Allowed values include the following: String, StringList, Boolean, Integer, MapList, and StringMap.

        To view examples of each type, see https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-plugins.html#top-level-properties-type
        """
        return self._values.get('type')

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[str]:
        """The regular expression the parameter must match."""
        return self._values.get('allowed_pattern')

    @builtins.property
    def allowed_values(self) -> typing.Optional[typing.List[str]]:
        """Allowed values for the parameter."""
        return self._values.get('allowed_values')

    @builtins.property
    def default(self) -> typing.Any:
        """The default value of the parameter or a reference to a parameter in Parameter Store."""
        return self._values.get('default')

    @builtins.property
    def display_type(self) -> typing.Optional[str]:
        """Used to display either a textfield or a textarea in the AWS console.

        textfield is a single-line text box. textarea is a multi-line text area
        """
        return self._values.get('display_type')

    @builtins.property
    def max_chars(self) -> typing.Optional[jsii.Number]:
        """The maximum number of parameter characters allowed."""
        return self._values.get('max_chars')

    @builtins.property
    def max_items(self) -> typing.Optional[jsii.Number]:
        """The maximum number of items allowed."""
        return self._values.get('max_items')

    @builtins.property
    def min_chars(self) -> typing.Optional[jsii.Number]:
        """The minimum number of parameter characters allowed."""
        return self._values.get('min_chars')

    @builtins.property
    def min_items(self) -> typing.Optional[jsii.Number]:
        """The minimum number of items allowed."""
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
        """Definition of the SSM document.

        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param content: Content of the SSM document. Can be passed as string or as object
        :param name: Name of the document. The name must be between 3 and 128 characters. Valid characters are a-z, A-Z, 0-9, and _, -, and . only
        :param document_type: Document type based on the service that you want to use. Default: Command
        :param target_type: Types of resources the document can run on. For example, ``/AWS::EC2::Instance`` or ``/`` for all resource types. Default: /
        :param update_default_version: Defined if the default version should be updated to the latest version on document updates. Default: true
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
        """Content of the SSM document.

        Can be passed as string or as object
        """
        return self._values.get('content')

    @builtins.property
    def name(self) -> str:
        """Name of the document.

        The name must be between 3 and 128 characters. Valid characters are a-z, A-Z, 0-9, and _, -, and . only
        """
        return self._values.get('name')

    @builtins.property
    def document_type(self) -> typing.Optional[str]:
        """Document type based on the service that you want to use.

        default
        :default: Command
        """
        return self._values.get('document_type')

    @builtins.property
    def target_type(self) -> typing.Optional[str]:
        """Types of resources the document can run on.

        For example, ``/AWS::EC2::Instance`` or ``/`` for all resource types.

        default
        :default: /
        """
        return self._values.get('target_type')

    @builtins.property
    def update_default_version(self) -> typing.Optional[bool]:
        """Defined if the default version should be updated to the latest version on document updates.

        default
        :default: true
        """
        return self._values.get('update_default_version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DocumentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["Document", "DocumentContent", "DocumentMainStep", "DocumentParameter", "DocumentProps", "__jsii_assembly__"]

publication.publish()
