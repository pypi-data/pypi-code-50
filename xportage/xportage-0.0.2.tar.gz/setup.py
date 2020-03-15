import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="xportage",
    version="0.0.2",
    description="Makes reading data easy.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mrdrozdov/xportage",
    author="Andrew Drozdov",
    author_email="andrew@mrdrozdov.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["xportage"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "xportage=xportage.__main__:main",
        ]
    },
)