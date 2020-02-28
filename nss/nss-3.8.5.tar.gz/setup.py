from __future__ import print_function
from setuptools import setup, find_packages
import sys

'''
setup(
     name="nanshansql",
     version="3.7.1",
     author="JingRui Zhu",
     author_email="870239526@qq.com",
     url='https://pypi.org/',
     description="Simple and fast database operation",
     long_description=open("README.rst").read(),
     license="MIT",
     #url="https://github.com/desion/tidy_page",
     packages=['nssql'],
     install_requires=[],
     classifiers=[
          "Topic :: Text Processing :: Indexing"
          ],
     )
mport setuptools

 

'''
 

setup(
    name="nss",
    version="3.8.5",
    author="Jingrui Zhu",
    author_email="870239526@qq.com",
    description="Simple and fast database operation",
    long_description=open("README.rst").read(),
    url="https://pypi.org/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
