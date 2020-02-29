from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="jactivecollab",
    version="0.1.1",
    author="Frederik Semmel",
    author_email="frederiksemmel@gmail.com",
    description="This package contains useful functions to extract data from Active Collab. It is designed for ETH juniors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    py_modules=["jactivecollab"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests >= 2.22.0",
        "numpy >= 1.18.0",
        "pandas >= 1.0",
        "mysql-connector-python >= 8.0",
    ],
)
