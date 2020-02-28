#!/usr/bin/env python
# coding:utf-8

from setuptools import setup, find_packages

setup(
    name="highfre",
    version="1.0.0",
    keywords=("pip", "highfre"),
    description="An highfre demo",
    long_description="An high fre BTC project demo",
    license="MIT Licence",
    url="https://github.com/confiself/highfre",
    author="confiself",
    author_email="1120396510@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests"]
)
