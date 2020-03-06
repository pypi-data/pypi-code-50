


import setuptools
from os import path

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="allcountry", # Replace with your own username
    version="0.1",
    author="Serhat YILDIRIM",
    author_email="serhatylidrm0@gmail.com",
    description="all city in world",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SerhatYildrm/World",
    packages=".",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={'package': ['data/data.json"']},
    include_package_data=True
)