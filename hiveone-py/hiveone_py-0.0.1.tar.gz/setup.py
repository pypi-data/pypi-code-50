import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="hiveone_py",
    version="0.0.1",
    author="Danny Aziz",
    author_email="danny@hive.one",
    description="Python SDK for Hive.one API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests'],
    url="https://github.com/hive-one/hive-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)