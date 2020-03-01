# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "django",
]

setup(
    name="django-checkbox-normalize",
    version="0.1.0",
    description="It's bad design to put label after checkbox for BooleanField widget, so let's make it normal.",
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
    keywords=["django admin extentions", "django checkbox normalize"],
    install_requires=requires,
    packages=find_packages(".", exclude=["django_checkbox_normalize_example", "django_checkbox_normalize_example.migrations", "django_checkbox_normalize_demo"]),
    py_modules=["django_checkbox_normalize"],
    zip_safe=False,
    include_package_data=True,
)