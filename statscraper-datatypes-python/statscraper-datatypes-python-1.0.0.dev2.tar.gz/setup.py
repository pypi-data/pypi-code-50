"""Python bindings for statscraper-datatypes."""
from setuptools import setup


def readme():
    """Import README for use as long_description."""
    with open("README.rst") as f:
        return f.read()


setup(
    name='statscraper-datatypes-python',
    version='1.0.0-dev2',

    description='Python bindings for statscraper-datatypes',
    long_description=readme(),
    url='https://gitlab.com/jplusplus/statscraper-datatypes-python',
    author='Leonard Wallentin, J++ Stockholm',
    author_email='stockholm@jplusplus.org',
    license='MIT',
    packages=["datatypes"],
    install_requires=[],
)
