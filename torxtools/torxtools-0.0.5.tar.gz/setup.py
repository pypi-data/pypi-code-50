"""Torxtools

"""
#
# https://pypi.org/project/torxtools/
#
import sys

__version__ = "0.0.5"

# Used by Makefile to get the version
if sys.argv[1] == "version":
    print(__version__)
    sys.exit(0)

from setuptools import setup, find_packages

__author__ = "Julien Lecomte"
__contact__ = "julien@lecomte.at"
__copyright__ = "2020, Julien Lecomte"
__url__ = "https://gitlab.com/jlecomte/projects/torxtools"
__license__ = "MIT"

# Used setup.py, but not sphinx-build
if sys.argv[0] == "setup.py":
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()

    setup(
        name="torxtools",
        description="Less generic functionalities than Phillips and Pozidriv tools.",
        version=__version__,
        license=__license__,
        author=__author__,
        author_email=__contact__,
        url=__url__,
        long_description=__doc__,
        long_description_content_type="text/plain",
        python_requires=">=3.5",
        packages=find_packages(exclude=["docs*", "tests*"]),
        install_requires=requirements,
        include_package_data=True,
        classifiers=[
            # See: https://pypi.python.org/pypi?:action=list_classifiers
            "Topic :: Utilities",
            "Topic :: Software Development :: Libraries",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            # List of python versions and their support status:
            # https://en.wikipedia.org/wiki/CPython#Version_history
            "Development Status :: 2 - Pre-Alpha",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    )
