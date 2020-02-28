""" markdgenerator setuptools-based setup

"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
package_name = 'markdgenerator'

# get details from __about__.py
about = {}
with open(path.join(here, package_name, "__about__.py")) as fp:
    exec(fp.read(), about)


def from_about(key):
    if key in about:
        return about[key]
    else:
        return " undefined"

# Get the long description from the README file
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    version=from_about("__version__"),
    name=package_name,
    description=from_about("__summary__"),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url=from_about("__uri__"),
    author=from_about("__author__"),
    author_email=from_about("__email__"),
    python_requires='>=3.6',
    install_requires=[
        "pandas>=0.24.0",
    ],
    extras_require={
        "test": ["pytest"],
        "doc": ["sphinx"],
        "all": ["pytest", "sphinx"]
    },
    packages=find_packages(exclude=["tests", "docs", "backends"]),
    include_package_data=True,
    keywords="markdown, rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Text Processing :: Markup"
    ],
    license="BSD"

)
