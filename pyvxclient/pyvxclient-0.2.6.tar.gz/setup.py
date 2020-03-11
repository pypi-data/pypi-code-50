#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import os

from setuptools import setup, find_packages


requirements = [
    'bravado>=10.2.2',
    'Click>=7.0',
    'python-dateutil>=2.7.3',
    'PyYAML>=3.13',
    'requests==2.21.0',
    'swagger-spec-validator>=2.4.1',
    'urllib3==1.21.1'
]

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='pyvxclient',
    version='0.2.6',
    description='vxapi client',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='VX FIBER',
    author_email='info@vx.se',
    license='Copyright VNEXT AB',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requirements,
    tests_require=[
                      'tox',
                      'virtualenv',
                      'requests-mock'
                  ] + requirements,
    url='http://www.vx.se',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
