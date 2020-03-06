import io
import sys
from os import path
from setuptools import setup, find_packages


DEPENDENCIES = ["fire", "requests", "redis"]
TEST_DEPENDENCIES = ["pylint", "pytest", "pytest-mock", "responses"]


def get_long_description():
    workspace = path.abspath(path.dirname(__file__))
    with io.open(path.join(workspace, "README.md"), encoding="utf-8") as readme:
        return readme.read()


setup(
    name="skt-scale",
    version="1.0.0",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    entry_points={"console_scripts": ["scalecli=scale.cli:cli"]},
    install_requires=DEPENDENCIES,
    test_require=TEST_DEPENDENCIES,
    extras_require={
        "test": TEST_DEPENDENCIES,
        ":python_version<'3'": ["enum34"],
    },
)
