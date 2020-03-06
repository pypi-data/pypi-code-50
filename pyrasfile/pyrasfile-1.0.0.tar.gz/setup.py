import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="pyrasfile",
    version="1.0.0",
    author="Daniel Philippus",
    author_email="dphilippus@protonmail.com",
    description="A collection of HEC-RAS file writers and parsers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/larflows/pyrasfile",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)

