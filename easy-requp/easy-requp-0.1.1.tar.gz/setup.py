"""Easy ReqUp setup file."""

import codecs
import glob
import os.path
import shutil

import setuptools


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


for d in ["build", "dist"] + glob.glob("*.egg-info"):
    if os.path.isdir(d):
        print(f"deleting directory {d}")
        shutil.rmtree(d)


setuptools.setup(
    name="easy-requp",
    version=get_version("easy_requp.py"),
    description="Easily manage Python packages based on requirements file specifications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lucatrv/easy-requp",
    author="Luca Trevisani",
    author_email="lucatrv@hotmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    keywords="package manager pip requirements",
    packages=setuptools.find_packages(),
    py_modules=["easy_requp"],
    install_requires=["pip>=10.0.0", "setuptools>=26.1.0"],
    python_requires=">=3.8",
)
