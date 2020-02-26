from setuptools import *

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="outlier-priyank",
    version="1.0",
    description="Outlier",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="priyank raheja",
    author_email="praheja_be17@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
