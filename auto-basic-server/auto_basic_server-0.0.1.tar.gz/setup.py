#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 11:22
# @Author  : Liang Yanpeng
# @File    : setup.py


from setuptools import find_packages, setup

setup(
    name="auto_basic_server",
    version="0.0.1",
    author="Liang Yanpeng",
    author_email="liangyanpeng@qianxin.com",
    description="basic server functions",
    long_description="Functions that are appropriate for each project",
    # package_dir={'': 'mypack'},
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[])

