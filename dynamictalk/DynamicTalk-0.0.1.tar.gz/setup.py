import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DynamicTalk",
    version="0.0.1",
    author="Will Watkinson",
    author_email="wjwats4295@gmail.com",
    description="Explore Netsuite's WSDL and convert Python Dictionaries into Netsuite XML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/wjwatkinson/dynamictalk",
    packages=["dynamictalk"],
    install_requires=['netsuite',
                      'zeep',
                      'xmltodict'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
