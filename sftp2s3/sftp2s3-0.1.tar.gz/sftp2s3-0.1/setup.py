import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sftp2s3",
    version="0.1",
    author="Devendra singh",
    author_email="singh.devendra58@gmail.com",
    description="Objective of the library is to provide easy to use programmable interface for migrating data from sftp to s3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/singh-devendra58/sftp2s3",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
    ],
)
