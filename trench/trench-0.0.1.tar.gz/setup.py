#!/usr/bin/env python
import setuptools
from trench import version

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="trench",
    version=version,
    author="Kirill Pavlov",
    author_email="k@p99.io",
    description="Deep learning library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slothai/pytrench",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
