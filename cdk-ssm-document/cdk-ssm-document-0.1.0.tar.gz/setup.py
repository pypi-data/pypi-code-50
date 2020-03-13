import json
import setuptools

kwargs = json.loads("""
{
    "name": "cdk-ssm-document",
    "version": "0.1.0",
    "description": "CDK Construct for managing SSM Documents",
    "license": "MIT",
    "url": "https://github.com/udondan/cdk-ssm-document",
    "long_description_content_type": "text/markdown",
    "author": "Daniel Schroeder",
    "project_urls": {
        "Source": "https://github.com/udondan/cdk-ssm-document.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_ssm_document",
        "cdk_ssm_document._jsii"
    ],
    "package_data": {
        "cdk_ssm_document._jsii": [
            "cdk-ssm-document@0.1.0.jsii.tgz"
        ],
        "cdk_ssm_document": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.22.0",
        "publication>=0.0.3",
        "aws-cdk.aws-cloudformation>=1.24.0, <2.0.0",
        "aws-cdk.aws-iam>=1.24.0, <2.0.0",
        "aws-cdk.aws-kms>=1.24.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.24.0, <2.0.0",
        "aws-cdk.aws-s3>=1.24.0, <2.0.0",
        "aws-cdk.core>=1.24.0, <2.0.0"
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
