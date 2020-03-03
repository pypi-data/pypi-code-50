import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk-featureflags",
    "version": "0.1.2",
    "description": "An AWS CDK feature flag implementation",
    "license": "Apache-2.0",
    "url": "https://github.com/elegantdevelopment/aws-cdk-featureflags#readme",
    "long_description_content_type": "text/markdown",
    "author": "Justin Taylor<jtaylor@elegantdevelopment.co.uk>",
    "project_urls": {
        "Source": "https://github.com/elegantdevelopment/aws-cdk-featureflags.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "ElegantDevelopment.AWSCDKFeatureFlags",
        "ElegantDevelopment.AWSCDKFeatureFlags._jsii"
    ],
    "package_data": {
        "ElegantDevelopment.AWSCDKFeatureFlags._jsii": [
            "aws-cdk-featureflags@0.1.2.jsii.tgz"
        ],
        "ElegantDevelopment.AWSCDKFeatureFlags": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.22.0",
        "publication>=0.0.3",
        "aws-cdk.aws-apigateway>=1.27.0, <2.0.0",
        "aws-cdk.aws-dynamodb>=1.27.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.27.0, <2.0.0",
        "aws-cdk.core>=1.27.0, <2.0.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
