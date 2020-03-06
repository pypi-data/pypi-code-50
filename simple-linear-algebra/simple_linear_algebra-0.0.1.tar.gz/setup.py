import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_linear_algebra", 
    version="0.0.1",
    author="Roger Hu",
    author_email="handeasy@gmail.com",
    description="A small package to implement basic linear algebra operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caroger/linear_algebra",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
