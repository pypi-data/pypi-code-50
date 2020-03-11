# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

with open(os.path.join(here, "requirements.txt"), "r", encoding="utf-8") as fobj:
    requires = fobj.readlines()
requires = [x.strip() for x in requires if x.strip()]

setup(
    name="unzip-aes",
    version="0.1.0",
    description="Unzip AES encrypted zip file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zencore",
    author_email="dobetter@zencore.cn",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["command line utils", "unzip-aes"],
    install_requires=requires,
    packages=find_packages("."),
    py_modules=["unzip_aes"],
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "unzip-aes = unzip_aes:unzip",
        ]
    },
)