import codecs
import os
import sys

from setuptools import find_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


long_description = read('README.md')

packages = find_packages(where='create_models')

setup(
    name='canaa-model-furlan',
    version=get_version(os.path.join('create_models', 'main.py')),
    description="Canaa Base model creator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    url='https://pip.pypa.io/',
    keywords='canaa hbsis',
    project_urls={
        "Documentation": "https://pip.pypa.io",
        "Source": "https://github.com/guionardo/canaa-base-model-creator",
    },
    author='Guionardo Furlan',
    author_email='guionardo@gmail.com',
    packages=find_packages(
        where=".",
        exclude=["tests"],
    ),
    entry_points={
        "console_scripts": [
            "canaa-model=create_models.main:main"
        ]
    },
    install_requires=[],
    zip_safe=False,
    python_requires='>=3.6.*'
)
