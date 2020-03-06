#!/usr/bin/env python

# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# pylint:disable=missing-docstring

import re
import os
from io import open
from setuptools import find_packages, setup

# Change the PACKAGE_NAME only to change folder and different name
PACKAGE_NAME = "bing-commerce-ingestion"
PACKAGE_FOLDER_PATH = "microsoft/bing/commerce/ingestion"

# Version extraction inspired from 'requests'
with open(os.path.join(PACKAGE_FOLDER_PATH, 'version.py'), 'r') as fd:
    version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=version,
        description="Microsoft Bing for Commerce ingestion SDK for Python",
        long_description=readme,
        long_description_content_type="text/markdown",
        license="MIT License",
        author="Microsoft Corporation",
        author_email="opencommerce@microsoft.com",
        maintainer="Microsoft",
        maintainer_email="opencommerce@microsoft.com",
        url="https://github.com/Azure/azure-sdk-for-python",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
            "License :: OSI Approved :: MIT License",
        ],
        packages=find_packages(
            exclude=[
                "test"
            ]
        ),
        install_requires=parse_requirements("requirements.txt")
    )