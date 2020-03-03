"""
Setup script for IaC
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
version = "0.0.1-1"

setup(
    name='iac',
    version=version,
    description="Infrastructure as Code",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dsikes/iac',
    author='Dan Sikes',
    author_email='dansikes7@gmail.com',
    keywords='iac, infrastructure, code',
    packages=find_packages(),
    install_requires=['requests'],

    project_urls={
        'Source': 'https://github.com/dsikes/iac',
    },
)