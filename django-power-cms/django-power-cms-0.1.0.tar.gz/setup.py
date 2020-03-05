# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "pillow==6.2.2",
    "django==2.2.10",
    "fastutils>=0.9.0",

    "django-modeladmin-reorder>=0.3.1",
    "django-ckeditor-5>=0.0.5",
    "django-mptt>=0.11.0",

    "django-static-jquery3>=3.3.1.1",
    "django-static-bootstrap>=3.3.7.1",
    "django-static-fontawesome>=5.12.1.1",
    "django-static-ionicons>=2.0.1.2",
    "django-fullname-localization>=0.1.0",
    "django-msms-admin>=0.1.1",
]

setup(
    name="django-power-cms",
    version="0.1.0",
    description="A power content management system based on django admin framework.",
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
    keywords=["django admin extentions", "django power cms"],
    install_requires=requires,
    packages=find_packages(".", exclude=["django_power_cms_example", "django_power_cms_example.migrations", "django_power_cms_demo"]),
    py_modules=["django_power_cms"],
    zip_safe=False,
    include_package_data=True,
)