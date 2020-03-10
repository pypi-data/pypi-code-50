import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nested-dictionaries",
    version="0.0.1",
    author="Robert Poirier",
    author_email="linuxaddikt@robsarea.com",
    description="Nested Dictionaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LiNuXaDDiKt/python_nested_dictionaries",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
