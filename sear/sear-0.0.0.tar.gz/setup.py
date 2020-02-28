#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="sear",
    version="0.0.0",
    description="Signed/encrypted archive: a tar-like archive format",
    long_description="Signed/Encrypted ARchive: always-encrypted tar-like archive tool with optional signature support",
    author="Tony Arcieri",
    author_email="tony@iqlusion.io",
    url="https://github.com/iqlusioninc/sear/blob/develop/README.md",
    packages=["sear"],
    package_dir={"sear": "sear"},
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
