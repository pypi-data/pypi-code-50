import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jbs-utils",
    version="0.0.1",
    author="Technion Data and Knowledge Lab (TD&K)",
    author_email="omishali@cs.technion.ac.il",
    description="Utilities for working with the JBS data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TechnionTDK/jbs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)