#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "pandas==0.25.0",
    "click==7.0",
    "click-log==0.3.2",
    "cutadapt==2.4",
    "flake8==3.7.8",
]

setup_requirements = [
    "pandas==0.25.0",
    "click==7.0",
    "click-log==0.3.2",
    "cutadapt==2.4",
    "flake8==3.7.8",
]

test_requirements = [
    "pandas==0.25.0",
    "click==7.0",
    "click-log==0.3.2",
    "cutadapt==2.4",
    "flake8==3.7.8",
]

setup(
    author="Ronak Hasmukh Shah",
    author_email="rons.shah@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description="This package will help process, merge and link fastq in user specified directory from manifest file",
    entry_points={"console_scripts": ["process_fastq=process_fastq.cli:main"]},
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description="https://github.com/rhshah/process_fastq",
    include_package_data=True,
    keywords="process_fastq",
    name="process_fastq",
    packages=find_packages(include=["process_fastq","utilites"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/rhshah/process_fastq",
    version="2.1.1",
    zip_safe=False,
)
