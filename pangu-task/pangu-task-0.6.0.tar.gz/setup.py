#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: camellibby
# Mail: camelxinliang@sina.com
# Created Time: 2019-11-22
#############################################


from setuptools import setup, find_packages

setup(
    name="pangu-task",
    version="0.6.0",
    keywords=("pip", "python", "pangu", "job",  "task"),
    description="Asynchronously run function with callback",
    long_description="Asynchronously run function with callback",
    license="MIT Licence",

    url="https://github.com/camellibby/pangu-task",
    author="camellibby",
    author_email="camelxinliang@sina.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)
