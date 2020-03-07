#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    author="Sylvain Bellemare",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python client for drand.",
    long_description=readme,
    license="MIT license",
    include_package_data=True,
    keywords="drand",
    name="drand",
    packages=find_packages(include=["drand", "drand.*"]),
    test_suite="tests",
    version="0.1.0.dev",
    zip_safe=False,
)
