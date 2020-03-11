#!/usr/bin/env python
from pathlib import Path
from setuptools import setup, find_packages

version_file = Path(__file__).parent.joinpath("pygnn", "VERSION.txt")
version = version_file.read_text(encoding="UTF-8").strip()

with open("requirements.txt") as reqs_file:
    install_requires = reqs_file.read().splitlines()

setup(
    name="pygnn",
    version=version,
    author="Andrew chang",
    author_email="aychang995@gmail.com",
    packages=find_packages(),
    keywords=[
        "Graph Neural Network",
        "Machine Learning",
        "ML",
        "Geometric",
        "GNN",
        "torch",
        "pytorch",
        "Deep Learning",
    ],
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=True,
)
