# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 9:18
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : setup.py.py
# @Software: OA

# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='my_demofsdfsdfsdfsdfsdfsdjghj',
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)