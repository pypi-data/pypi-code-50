"""
    Name: setup.py
    Author: Charles Zhang <694556046@qq.com>
    Propose: Setup script for pygrading!
    Coding: UTF-8

    Change Log:
        **2020.03.04**
        Update to 0.2.6!

        **2020.03.04**
        Update to 0.2.5!

        **2020.03.03**
        Update to 0.2.4!

        **2020.02.09**
        Update to 0.2.1!

        **2020.02.04**
        Update to 0.2.0!

        **2020.02.01**
        Update to 0.1.2!

        **2020.01.29**
        Update to 0.1.0!

        **2020.01.26**
        Create this file!
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygrading",
    version="0.2.6",
    author="Charles Zhang",
    author_email="694556046@qq.com",
    description="A Python ToolBox for CourseGrading platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhenomingZ/PyGrading",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
