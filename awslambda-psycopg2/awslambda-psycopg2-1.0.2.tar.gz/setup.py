import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awslambda-psycopg2",
    version="1.0.2",
    author="Yuvaraja",
    author_email="yuvaraja.gna@gmail.com",
    description="A aws psycopg2 package from psycopg2.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jkehler/awslambda-psycopg2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
