import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cdasws",
    version="0.1.4",
    description="NASA's Coordinated Data Analysis System Web Service Client Library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://cdaweb.sci.gsfc.nasa.gov/WebServices/REST",
    author="Bernie Harris",
    author_email="gsfc-spdf-support@lists.nasa.gov",
    license="NOSA",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["python-dateutil", "requests", "spacepy"],
    entry_points={
        "console_scripts": [
            "cdasws=cdasws.__main__:example",
        ]
    },
)
