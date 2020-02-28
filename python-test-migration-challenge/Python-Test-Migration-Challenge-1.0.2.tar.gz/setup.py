from setuptools import setup
import setuptools

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Python-Test-Migration-Challenge",
    version="1.0.2",
    description="A Python package to do cloud migration Coding challenge",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/alhadbhadekar/python-test-migrate-challenge",
    author="Alhad Bhadekar",
    author_email="alhad.bhadekar@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["dill"],
)
