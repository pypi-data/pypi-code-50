# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_variety",
    version="0.1.0",
    author="maida",
    author_email="624486877@qq.com",
    description="Use variety by python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LZC6244/py_variety",
    packages=setuptools.find_packages(),
    install_requires=[
        'pymongo'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
