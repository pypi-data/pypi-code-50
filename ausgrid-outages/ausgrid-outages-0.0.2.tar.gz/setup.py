#!/usr/bin/env python3
"""Web Redirect setup script."""
from datetime import datetime as dt

from setuptools import find_packages, setup

PROJECT_NAME = "Ausgrid Outage Data"
PROJECT_VERSION = "0.0.2"
PROJECT_PACKAGE_NAME = "ausgrid-outages"
PROJECT_LICENSE = "Apache License 2.0"
PROJECT_AUTHOR = "Troy Kelly"
PROJECT_COPYRIGHT = " 2020-{}, {}".format(dt.now().year, PROJECT_AUTHOR)
PROJECT_URL = "https://github.com/troykelly/python-ausgrid-outages"
PROJECT_EMAIL = "troy@troykelly.com"

REQUIRED_PYTHON_VER = (3, 7, 0)

PROJECT_GITHUB_USERNAME = "troykelly"
PROJECT_GITHUB_REPOSITORY = "python-ausgrid-outages"

PYPI_URL = "https://pypi.python.org/pypi/{}".format(PROJECT_PACKAGE_NAME)
GITHUB_PATH = "{}/{}".format(PROJECT_GITHUB_USERNAME, PROJECT_GITHUB_REPOSITORY)
GITHUB_URL = "https://github.com/{}".format(GITHUB_PATH)

DOWNLOAD_URL = "{}/archive/{}.zip".format(GITHUB_URL, PROJECT_VERSION)
PROJECT_URLS = {
    "Bug Reports": "{}/issues".format(GITHUB_URL),
}

PACKAGES = find_packages(exclude=["tests", "tests.*"])

REQUIRES = [
    "requests==2.23.0",
    "pip>=8.0.3",
]

MIN_PY_VERSION = ".".join(map(str, REQUIRED_PYTHON_VER))

setup(
    name=PROJECT_PACKAGE_NAME,
    version=PROJECT_VERSION,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires=">={}".format(MIN_PY_VERSION),
    test_suite="tests",
    entry_points={"console_scripts": ["redirector = redirect.__main__:main"]},
)
