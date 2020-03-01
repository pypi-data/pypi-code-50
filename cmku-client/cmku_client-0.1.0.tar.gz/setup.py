#!/usr/bin/env python3
from os.path import dirname, abspath, join
from setuptools import setup, find_packages

here = dirname(abspath(__file__))
requirements = open(join(here, "requirements.txt"))


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cmku_client", # Replace with your own username
    version="0.1.0",
    author="westwardharbor0",
    author_email="westwardharbor0@gmail.com",
    description="Client to access CMKU data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/westwardharbor0/cmku-client",
    packages=find_packages(),
    setup_requires=requirements.readlines(),
    install_requires=requirements.readlines(),
    py_modules=["cmku_client"],
)