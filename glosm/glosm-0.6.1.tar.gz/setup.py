from setuptools import setup
import pathlib
import re

PACKAGE_NAME = "glosm"


def version():
    """Extract version from __init__.py"""
    here = pathlib.Path(__file__).parent.resolve()
    with open(str(here / PACKAGE_NAME / "__init__.py"), "r") as fd:
        for line in fd:
            if re.match("^__version__ = ", line):
                version_string = re.search(r"[0-9]+\.[0-9]+\.[0-9]+", line).group(0).strip()
                return version_string


setup(
    name=PACKAGE_NAME,
    version=version(),
    description="glorified secrets manager",
    author="tutti",
    author_email="data@tutti.ch",
    license="Proprietary",
    packages=[PACKAGE_NAME],
    zip_safe=False,
    entry_points={"console_scripts": ["glosm=glosm.cli:execute"]},
)
