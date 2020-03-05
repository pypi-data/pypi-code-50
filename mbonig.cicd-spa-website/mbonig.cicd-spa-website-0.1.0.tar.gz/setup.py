import json
import setuptools

kwargs = json.loads("""
{
    "name": "mbonig.cicd-spa-website",
    "version": "0.1.0",
    "description": "A CDK construct which pulls code from a source repository, builds it, then deploys to an S3 bucket (with CloudFront if a certificate is required)",
    "license": "MIT",
    "url": "https://github.com/mbonig/cicd-spa-website",
    "long_description_content_type": "text/markdown",
    "author": "Matthew Bonig<matthew.bonig@gmail.com>",
    "project_urls": {
        "Source": "https://github.com/mbonig/cicd-spa-website"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "mbonig.cicd-spa-website",
        "mbonig.cicd-spa-website._jsii"
    ],
    "package_data": {
        "mbonig.cicd-spa-website._jsii": [
            "cicd_spa_website@0.1.0.jsii.tgz"
        ],
        "mbonig.cicd-spa-website": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=1.0.0",
        "publication>=0.0.3",
        "aws-cdk.aws-certificatemanager>=1.27.0, <2.0.0",
        "aws-cdk.aws-cloudfront>=1.27.0, <2.0.0",
        "aws-cdk.aws-codebuild>=1.27.0, <2.0.0",
        "aws-cdk.aws-codepipeline>=1.27.0, <2.0.0",
        "aws-cdk.aws-codepipeline-actions>=1.27.0, <2.0.0",
        "aws-cdk.aws-iam>=1.27.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.27.0, <2.0.0",
        "aws-cdk.aws-route53>=1.27.0, <2.0.0",
        "aws-cdk.aws-route53-targets>=1.27.0, <2.0.0",
        "aws-cdk.aws-s3>=1.27.0, <2.0.0",
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
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
