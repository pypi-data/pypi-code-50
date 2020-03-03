import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prsample", 
    version="0.0.2",
    author="Andrew Stanford-Jason",
    author_email="andrewstanfordjason@gmail.com",
    description="A pseudo-random data sampler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewstanfordjason/prsample",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)