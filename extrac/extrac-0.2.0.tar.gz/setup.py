#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="extrac",
    version="0.2.0",
    description="decompression files",
    long_description_markdown_filename="README.md",
    py_modules=["python_extrac/extrac"],
    license="MIT",
    url="https://github.com/belingud/python_extrac",
    author="belingud",
    auth_email="zyx@lte.ink",
    packages=find_packages(),
    plantforms="Linux",
    python_requires=">=3.5",
    install_requires=["Click"],
    scripts=["python_extrac/extrac.py"],
    entry_points={"console_scripts": ["x=extrac:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
