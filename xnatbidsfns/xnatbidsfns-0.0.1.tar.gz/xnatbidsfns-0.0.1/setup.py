import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='xnatbidsfns',
    version="0.0.1",
    author="Radiologcs/NRG",
    author_email="kate@radiologics.com",
    description="Utility functions for BIDS data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/radiologics/docker-images",
    packages=setuptools.find_packages()
)
