# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wintergreen',
 'wintergreen.crypto',
 'wintergreen.initialize',
 'wintergreen.persistence',
 'wintergreen.platforms',
 'wintergreen.provision']

package_data = \
{'': ['*'], 'wintergreen': ['assets/*', 'templates/*']}

install_requires = \
['AWSIoTPythonSDK>=1.4,<2.0',
 'boto3>=1.9,<2.0',
 'click>=7.0,<8.0',
 'cryptography>=2.6,<3.0']

entry_points = \
{'console_scripts': ['wintergreen = wintergreen.cli:cli']}

setup_kwargs = {
    'name': 'wintergreen',
    'version': '0.2.2',
    'description': 'A tool for dealing with AWS IoT certificates',
    'long_description': '# THIS REPOSITORY IS A WORK IN PROGRESS\n**IF YOU SEE THIS MESSAGE DO NOT UNDER ANY CIRCUMSTANCE DELETE INFRASTRUCTURE HOPING THAT WINTERGREEN CAN REBUILD IT**\nWe\'re working on it.\n\n\n## Purpose\n\nThe responsibility of Wintergreen is to create and manage client-side SSL certificates for authenticating IoT devices with cloud services.\n\nAutomate device registry in AWS IoT because it sucks. `wintergreen` is a command line utility that provides mechanisms to automate cumbersome tasks related to signing and registering AWS IoT Thing device certificates.\n\n\n### What it does\n\nProvide a quick way to develop with a security-first mindset regarding your IoT web infrastructure by allowing you to avoid the hassle of generating and certs and associating them with your infrastructure\n\n### What it doesn\'t do\n\nProvide a secure pattern for managing device certificates in a hardware production setting.  It does not give you a secure means for allowing a third party manufacturer to generate and/or load certificates onto hardware.\n\n## Requirements\nAs Wintergreen manipulates AWS resources, an AWS account is required.\n\nWintergreen leverages boto3 and acts on the users behalf to create and manipulate resources in AWS.\nThe user should have AWS credentials set in their environment. In order to check this, you might use the AWS CLI and run `aws sts get-caller-identity`. This is the user wintergreen will leverage.\n\n## Installing the CLI\n`pip install wintergreen`\n\n## Run\n\n## Initialize\nInitialization means\n- Creating a ThingType\n- Creating a RootCA cert/key pair\n- Registering that RootCA with AWS\n- Creating a Just-in-time Provisioning role\n\nExample:\n`poetry run wintergreen init -t my-cool-thing`\nCheck your `~/.wintergreen` directory to see a subdirectory for `my-cool-thing`\n\n```bash\n$  wintergreen init --help\nUsage: wintergreen init [OPTIONS]\n\nOptions:\n  -t, --thing-type TEXT       AWS IoT thing type  [required]\n  -p, --platform [aws|local]  Platform to upload root CA  [required]\n  -a, --algorithm [rsa|ec]    Encryption algorithms supported  [required]\n  -c, --country TEXT          Country code (2-letter) to use for provisioning\n                              certs i.e. US  [required]\n  -f, --fqdn TEXT             Domain of the organization to use in the CA e.g.\n                              verypossible.com\n  -o, --organization TEXT     Organization name i.e. Very\n  -s, --state TEXT            State or Province code (2-letter) to use for\n                              provisioning certs i.e. TN\n  -l, --locality TEXT         Locality to use for provisioning certs i.e.\n                              Chattanooga\n  -u, --unit TEXT             Organizational unit to use for provisioning\n                              certs i.e. Engineering\n  -d, --days INTEGER          Days until CA will expire  [default: 365]\n  -k, --key-size INTEGER      [default: 2048]\n  --help                      Show this message and exit.\n\nOutputs:\n{\n    "platform_response": {\n        "thingTypeName": "thing_type",\n        "thingTypeArn": "arn:aws:iot:us-east-1:...",\n        "thingTypeId": "...",\n        "jitpRoleArn": "arn:aws:iam::...",\n        "certificateArn": "arn:aws:iot:us-east-1:..."\n    },\n    "success": true,\n    "platform": "aws"\n}\n```\n\n## Provision a new device\n\nProvisioning a device means generating a certificate/key pair to be used for the device to authenticate with AWS IoT.\n\n```bash\n$ wintergreen provision --help\nUsage: wintergreen provision [OPTIONS]\n\nOptions:\n  -t, --thing-type TEXT    Same as the thing-type that was chosen in the\n                           `init` step.\n  -cn, --common_name TEXT  Defaults to a UUIDv4\n  -c, --country TEXT       [required]\n  -o, --organization TEXT\n  -s, --state TEXT\n  -l, --locality TEXT\n  -u, --unit TEXT\n  -d, --days INTEGER       Days until certificate will expire  [default: 365]\n  -k, --key-size INTEGER   [default: 2048]\n  -n, --number INTEGER     Number of certificates to provision  [default: 1]\n  -v, --verbosity          Verbosity, add v\'s for more.\n  --help                   Show this message and exit.\n\nOutputs (depends on verbosity):\ncommon_name1\ncommon_name2\nGenerated 2 certificate(s)\n```\n\nThese will be written as files scoped by date into your `.wintergreen` directory. If you use the `-n` argument, it will generate a unique uuid for each cert and put all of the certs generated in their own folder. You\'ll also see an output.csv which contains a table of all the certs generated on this run.\n\n## Verifying if your provisioned cert can connect\nAfter running the `provision` command the cert/key will be saved in a directory named after the thing-type and common name as `deviceCertPlusCACert.crt` and `deviceKey.key`\n\n\n```bash\n$ wintergreen verify --help\nUsage: wintergreen verify [OPTIONS]\n\nOptions:\n  -p, --platform [aws|local]  Platform to upload root CA  [required]\n  -t, --thing-type TEXT       AWS IoT thing type  [required]\n  -cn, --common_name TEXT     Path to private key  [required]\n  --help                      Show this message and exit.\n\nOutputs (depending on success):\nCertificate verified on the aws platform! (exit code 0)\nUnable to verify certificate on the aws platform... (exit code 1)\n```\n\n\n## Get info about your wintergreen-provisioned devices\n\n```bash\n$ wintergreen info --help\nUsage: wintergreen info [OPTIONS]\n\nOptions:\n  -t, --thing-type TEXT    Thing type to receive info about\n  -cn, --common_name TEXT  Common name to receive info about\n  --help                   Show this message and exit.\n```\n\nCheck the thing types you have created:\n\n```bash\n$ wintergreen info\ntotal thing types: 3\nfoo\nbaz\nbar\n```\n\nCheck the things you have provisioned for a given thing type:\n\n```bash\n$ wintergreen info -t foo\nencryption algorithm: rsa\ntotal things: 3\na33bd27d-6511-4962-8aae-ad2b569b5904\n9742c666-e6c0-4410-8ff3-edfe2d1da37b\nd43c2e98-4559-45e3-bae5-271406936fbb\n```\n\nGet info about a specific thing you have provisioned:\n\n\n```bash\n$ wintergreen info -t foo -cn a33bd27d-6511-4962-8aae-ad2b569b5904\n{"date": "2019-12-11", "common_name": "a33bd27d-6511-4962-8aae-ad2b569b5904", "country": "US", "fqdn": "", "locality": "", "organization": "", "state": "", "unit": ""}\n```\n\n## The Full Workflow\n\n```bash\n$ wintergreen init -t example-thing\n{\n    "platform_response": {\n        "thingTypeName": "example-thing",\n        "thingTypeArn": "arn:aws:iot:us-east-1:...",\n        "thingTypeId": "...",\n        "jitpRoleArn": "arn:aws:iam::...",\n        "certificateArn": "arn:aws:iot:us-east-1:..."\n    },\n    "success": true,\n    "platform": "aws"\n}\n\n$ wintergreen provision -t example-thing -v\nsome-uuid-common-name\n\n$ wintergreen verify -t example-thing -cn some-uuid-common-name\nCertificate verified on the aws platform!\n\n$ wintergreen info\ntotal thing types: 1\nexample-thing\n```\n\n## Developing Wintergreen\n\nTo contribute to the project, please follow the [contributor instructions](CONTRIBUTING.md).\n',
    'author': 'Dan Lindeman',
    'author_email': 'lindemda@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/verypossible/wintergreen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
