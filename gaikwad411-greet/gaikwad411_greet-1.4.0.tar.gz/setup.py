"""Setup script for realpython-reader"""

import os.path
from setuptools import setup


# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))


# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()


# This call to setup() does all the work
setup(
    name="gaikwad411_greet",
    version="1.4.0",
    description="Greets the world in old stupid way",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gaikwad411/gaikwad411_greet",
    author="Sachin Gaikwad",
    author_email="gaikwad411@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["gaikwad411_greet"],
    include_package_data=True,
    install_requires=[

    ],
    entry_points={"console_scripts": ["gaikwad411_greet=gaikwad411_greet.__main__:main"]},
)
