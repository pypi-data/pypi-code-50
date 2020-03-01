from setuptools import setup, find_packages

from jsonnote import __version__

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='jsonnote',
    author='vipervit',
    author_email='vitolg1@gmail.com',
    license='Apache',
    description='A simple utility for working with JSON files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Utilities"
    ]
)
