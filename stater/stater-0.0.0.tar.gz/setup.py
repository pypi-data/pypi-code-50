import setuptools
import stater

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stater",
    version=stater.version,
    author="mithem",
    author_email="miguel.themann@gmail.com",
    description=stater.__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mithem/PyServer",
    packages=["stater"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
