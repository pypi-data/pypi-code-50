import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "mxmul_pkg_wht",
    version = "0.1.0",
    author = "Haitao Wu",
    author_email = "wht_93@163.com",
    description = "An example for teaching how to publish a Python package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)