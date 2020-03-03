from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["biopython>=1.76", "numpy>=1.17.5", "pandas>=0.23"]

setup(
    name="gRNAsearch",
    version="0.0.1",
    author="Runyu Hong",
    author_email="Runyu.Hong@nyu.edu",
    description="Search for guide RNA sites in PCR tags",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rhong3/gRNAsearch",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
)
