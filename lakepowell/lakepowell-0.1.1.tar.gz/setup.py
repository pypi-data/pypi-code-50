import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "lakepowell",
    version="0.1.1",
    author="lakepowellapi",
    author_email="lakepowellapi@gmail.com",
    description="lake powell Python package",
    long_description="This package is an api for data collected at lake powell",
    long_description_content_type='text/markdown',
    url="https://github.com/hboekweg/fishdata.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
