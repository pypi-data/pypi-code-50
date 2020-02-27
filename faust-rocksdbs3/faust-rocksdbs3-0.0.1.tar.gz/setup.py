from setuptools import find_packages, setup
import re

with open("README.md") as file:
    long_description = file.read()


def find_version():
    with open("faust_rocksdbs3/__init__.py") as file:
        version_file = file.read()
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
        )
        if version_match:
            return version_match.group(1)


setup(
    name="faust-rocksdbs3",
    version=find_version(),
    description="Faust RocksDB store extension that also backup / restores to an S3 bucket",
    long_description_content_type="text/markdown",
    author="Andrew Johnson",
    author_email="andrejohnson@expediagroup.com",
    packages=find_packages(),
    url="https://github.com/andrejohnson-expedia/faust-rocksdb-s3",
    package_data={"": ["*.*"]},
    include_package_data=True,
    install_requires=[
        "aiobotocore>=0.11.1",
        "faust>=1.7",
        "python-rocksdb"
    ],
    entry_points={
        'faust.stores': [
            'rocksdbs3 = faust_rocksdbs3.rocksdb_s3:Store'
        ]
    },
)


