#!/usr/bin/env python3

from pathlib import Path
from types import SimpleNamespace

from setuptools import find_packages, setup

v = {}
exec(next(Path(".").glob("*/__version__.py")).read_text(), None, v)
v = SimpleNamespace(**v)


setup(
    name="dle",
    author=v.__author__,
    author_email=v.__author_email__,
    description=v.__description__,
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license=v.__license__,
    url=v.__url__,
    version=v.__version__,
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={"console_scripts": ["dle = dle.__main__:main"]},
    install_requires=Path("requirements.txt").read_text().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
)
