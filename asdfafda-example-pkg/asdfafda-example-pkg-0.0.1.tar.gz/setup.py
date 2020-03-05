import setuptools
import os

with open(os.path.dirname(os.path.abspath(__file__)) + "/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="asdfafda-example-pkg",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
