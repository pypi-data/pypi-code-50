import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = "bushi",
  version = "0.2.1",
  author = "Alfi Maulana",
  author_email = "alfi.maulana.f@gmail.com",
  description = "Linux command line interface package",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://gitlab.com/ichiro-its/bushi",
  packages = setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.6",
)