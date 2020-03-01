#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = ["Click>=7.0"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest>=3"]

setup(
    author="Samuel Luen-English",
    author_email="sluenenglish@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description=' A Python library with utilities to help contruct "interception" input manipulation flows.',
    entry_points={"console_scripts": ["pykeymapper=pykeymapper.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="pykeymapper",
    name="pykeymapper",
    packages=find_packages(include=["pykeymapper", "pykeymapper.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://gitlab.com/sluenenglish/pykeymapper",
    version="0.1.3",
    zip_safe=False,
)
