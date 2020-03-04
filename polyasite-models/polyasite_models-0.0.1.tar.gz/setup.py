import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="polyasite_models",
    version="0.0.1",
    author="Christina J. Herrmann",
    author_email="christina.herrmann@unibas.ch",
    description="Models for PolyASite web service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires='>=2.7',
    install_requires=[
        "mongoengine >=0.18.2",
    ],
)
