"""
# aws-cdk-featureflags

![build](https://github.com/elegantdevelopment/aws-cdk-featureflags/workflows/build/badge.svg)
[![dependencies Status](https://david-dm.org/elegantdevelopment/aws-cdk-featureflags/status.svg)](https://david-dm.org/elegantdevelopment/aws-cdk-featureflags)
[![npm](https://img.shields.io/npm/dt/aws-cdk-featureflags)](https://www.npmjs.com/package/aws-cdk-featureflags)

[![npm version](https://badge.fury.io/js/aws-cdk-featureflags.svg)](https://badge.fury.io/js/aws-cdk-featureflags)
[![NuGet version](https://badge.fury.io/nu/ElegantDevelopment.AWSCDKDynamoDBSeeder.svg)](https://badge.fury.io/nu/ElegantDevelopment.AWSCDKFeatureFlags)
[![PyPI version](https://badge.fury.io/py/aws-cdk-featureflags.svg)](https://badge.fury.io/py/aws-cdk-featureflags)
[![Maven Central](https://img.shields.io/maven-central/v/io.github.elegantdevelopment/AWSCDKDynamoDBSeeder?color=brightgreen)](https://repo1.maven.org/maven2/io/github/elegantdevelopment/AWSCDKFeatureFlags/)

An [AWS CDK](https://aws.amazon.com/cdk) feature flag implementation

# :exclamation: WIP :exclamation:

This package is a **WORK IN PROGRESS**, please make sure you're not using this until we've reached at least v1.0.0.

## Why this package

For when you want feature flags.

## How do I use it

Install using your favourite package manager:

```sh
yarn add aws-cdk-featureflags
```

### Example TypeScript usage

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk_featureflags import FeatureFlags
feature_flags = FeatureFlags(self, "featureflags")
Function(self, "my-function",
    code=Code.from_asset("./my-function"),
    handler="index.handler",
    environment={
        "FEATURE_FLAGS_URL": feature_flags.url
    }
)
```

## Versioning

Currently pre-release. Check back when we've reached at least 1.0.0!
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_apigateway
import aws_cdk.aws_dynamodb
import aws_cdk.aws_lambda
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("aws-cdk-featureflags", "0.1.2", __name__, "aws-cdk-featureflags@0.1.2.jsii.tgz")


class FeatureFlags(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-featureflags.FeatureFlags"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str) -> None:
        """
        :param scope: -
        :param id: -

        stability
        :stability: experimental
        """
        jsii.create(FeatureFlags, self, [scope, id])

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "url")


__all__ = ["FeatureFlags", "__jsii_assembly__"]

publication.publish()
