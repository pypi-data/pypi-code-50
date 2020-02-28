#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="armistice",
    version="0.0.0",
    description="Hardware private key storage for next-generation cryptography",
    long_description="Hardware private key storage for next-generation cryptography (e.g. BLS) initially targeting USB armory Mk II devices from F-Secure",
    author="Tony Arcieri",
    author_email="tony@iqlusion.io",
    url="https://github.com/iqlusioninc/armistice/blob/develop/README.md",
    packages=["armistice"],
    package_dir={"armistice": "armistice"},
    include_package_data=True,
    install_requires=[],
    license="Apache Software License",
    keywords=["encryption", "signing"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
    ],
    test_suite="tests",
    tests_require=[]
)
