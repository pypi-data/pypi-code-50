#!/usr/bin/env python
import io
from os.path import dirname, join

from setuptools import find_packages, setup

VERSION = (0, 0, 1)
__versionstr__ = '.'.join(map(str, VERSION))


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='mailinator-python-client',
    version=__versionstr__,
    description='Python Client for the Mailinator Email System https://www.mailinator.com',
    long_description=read('README.rst'),
    author='Adela Kacso-Vidrean (KVA)',
    author_email='adella.neacsu@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=read('requirements.txt'),
    license='GNU GENERAL PUBLIC LICENSE',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
