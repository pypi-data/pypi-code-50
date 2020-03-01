from setuptools import setup, find_packages

setup(
    name="klik-bencode",
    version="0.1",
    url="https://github.com/malhotraguy/klik_interview",
    license="MIT",
    author="Rahul Malhotra",
    author_email="electronicsgrad@gmail.com",
    description="To decode the Bencode string to Python native datatypes",
    packages=find_packages(exclude=["tests"]),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    python_requires=">=3.6",
)
