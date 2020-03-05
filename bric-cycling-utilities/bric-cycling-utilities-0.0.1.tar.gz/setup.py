import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bric-cycling-utilities",
    version="0.0.1",
    author="Brian Carlsen",
    author_email="carlsen.bri@gmail.com",
    description="Utilities for cycling stability experiments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    install_requires=[
    ],
    package_data={
    }
)