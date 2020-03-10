import setuptools
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="tf_cloud_cli",
    version="0.0.2",
    author="njeirath",
    description="A CLI to the Terraform Cloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/njeirath/tf_cloud_cli",
    packages=find_packages(),
    py_modules=["cli"],
    install_requires=["click==7.1.1", "requests==2.23.0"],
    entry_points={"console_scripts": ["tf_cloud_cli = cli:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
