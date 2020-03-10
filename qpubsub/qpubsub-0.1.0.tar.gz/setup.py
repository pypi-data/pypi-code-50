import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def python_version_bump_from_shell_file():
    with open(os.path.join(here, "VERSION"), encoding="utf-8") as f:
        __version__ = f.read().strip()
        # you can't trust the module to reach out of qpubsub at runtime
        # so write it to a python file at build time
        # I haven't seen this before, but it is the best way to handle exposing version
        # in a way that works with python's module bs, but is accessible to other languages
        # like bash or groovy for CI/CD stuff
        with open(os.path.join(here, "qpubsub", "version.py"), "w+", encoding="utf-8") as v:
            v.write("# Don't change this file, ../VERSION is the source of truth\n")
            v.write(f'__version__ = "{__version__}"')
    return __version__


setup(
    name="qpubsub",
    packages=find_packages(),
    author="Qordoba",
    author_email="sam.havens@qordoba.com",
    url="https://github.com/Qordobacode/library.qpubsub",
    version=python_version_bump_from_shell_file(),
    license="unlicensed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6.4",
    install_requires=[
        'google-cloud-pubsub==1.3.1',
        'singleton-decorator==1.0.0',
        'toolz==0.10.0',
        'qai==2.6.1',
    ],
)
