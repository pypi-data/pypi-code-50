"""Ansible Roster
"""

import sys

__version__ = "0.1.9"

# Used by Makefile to get the version
if sys.argv[1] == "version":
    print(__version__)
    sys.exit(0)

if sys.argv[1] == "prerelease":
    import semver
    from sh import sed

    suffix = sys.argv[2]
    v = semver.parse_version_info(__version__)
    v = str(v.replace(prerelease=suffix, build=None))
    sed(["-E", "-i", rf's/^(__version__\s+=)\s+".*\w*"$/\1 "{v}"/', __file__])
    sys.exit(0)

from setuptools import setup, find_packages

__author__ = "Julien Lecomte"
__contact__ = "julien@lecomte.at"
__copyright__ = "2019-2020, Julien Lecomte"
__url__ = "https://gitlab.com/jlecomte/projects/roster"
__license__ = "MIT"

# Used setup.py, but not sphinx-build
if sys.argv[0] == "setup.py":
    with open("requirements.txt", encoding="utf-8") as f:
        requirements = f.read().splitlines()
    with open("README.md", encoding="utf-8") as f:
        readme = f.read()

    setup(
        name="ansible-roster",
        description="Ansible simplified yaml inventory",
        version=__version__,
        license=__license__,
        author=__author__,
        author_email=__contact__,
        url=__url__,
        long_description=readme,
        long_description_content_type="text/markdown",
        python_requires=">=3.6",
        packages=find_packages(exclude=["docs*", "tests*"]),
        install_requires=requirements,
        include_package_data=True,
        classifiers=[
            # See: https://pypi.python.org/pypi?:action=list_classifiers
            "Topic :: System :: Installation/Setup",
            "Topic :: System :: Software Distribution",
            "Topic :: System :: Systems Administration",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: MIT License",
            # List of python versions and their support status:
            # https://en.wikipedia.org/wiki/CPython#Version_history
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    )
