#!/user/bin/env python
from distutils.core import setup
import setuptools

setup(
    name="pierwszy_pakiet_pajtona",
    version="0.3",
    packages=setuptools.find_packages(),
    description="First PythonPackage",
    author="Unknown",
    author_email="unknown@gmail.com",
    install_requires = ['requests'],

)