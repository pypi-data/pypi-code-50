#! /usr/bin/env python
# encoding: utf-8

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
# To use a consistent encoding
from codecs import open
from os import path
import sys

# ???????
# import ssl
# try:
#     ssl._create_default_https_context = ssl._create_unverified_context
# except Exception:
#     pass

here = path.abspath(path.dirname(__file__))

# ???????
# class PyTest(TestCommand):
#     user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]
#
#     def initialize_options(self):
#         TestCommand.initialize_options(self)
#         self.pytest_args = []
#
#     def finalize_options(self):
#         TestCommand.finalize_options(self)
#         self.test_args = []
#         self.test_suite = True
#
#     def run_tests(self):
#         import pytest
#         errno = pytest.main(self.pytest_args)
#         sys.exit(errno)

# ?????
# cmdclass = {}
# cmdclass['test'] = PyTest

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(
    name='zly-resource-module',                                    #项目名
    version='1.0.1',                                        #版本
    keywords='dingding, ding, dtalk, dingtalk, SDK',        #关键字
    description='DingTalk SDK for Python',                  #简短描述
    long_description=long_description,                      #详细描述
    # url='https://github.com/007gzs/dingtalk-sdk',         #网址
    # author='007gzs',
    # author_email='007gzs@sina.com',
    license='MIT',                                           #许可证
    classifiers=[                                            #分类器
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    # packages=[
    #     'aishow_model_app',
    #     'aishow_model_app.apis',
    #     'aishow_model_app.models',
    #     'aishow_model_app.storage',
    #     'aishow_model_app.model',
    #     'aishow_model_app.templates',
    #     'aishow_model_app.docs',
    #     'aishow_model_app.tests',
    # ],
    py_modules=["config","manage"],
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True,
    python_requires='>=3.6',
    # tests_require=[
    #     'pytest',
    #     'redis',
    #     'pymemcache',
    # ],
    # cmdclass=cmdclass,
    # extras_require={
    #     'cryptography': ['cryptography'],
    #     'pycrypto': ['pycrypto'],
    # },
)
