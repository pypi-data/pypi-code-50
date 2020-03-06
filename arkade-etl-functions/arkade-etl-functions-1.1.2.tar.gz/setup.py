import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arkade-etl-functions",
    version="1.1.2",
    author="Tim Moon",
    author_email="timmoon.arkade@gmail.com",
    description="Common library package for etl-functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arkade-digital/etl-functions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
