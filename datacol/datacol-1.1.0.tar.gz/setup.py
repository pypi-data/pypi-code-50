from setuptools import setup

# The directory containing this file


# The text of the README file
desc = open('DESC.md')
desc = desc.read()

# This call to setup() does all the work
setup(
    name="datacol",
    version="1.1.0",
    packages=['datacol'],
    description="Localized, file-based database module.",
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/EKHolmes/DataCol/",
    author="Erik Holmes",
    author_email="zv.eevee6718@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
