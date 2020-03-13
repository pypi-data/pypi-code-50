import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='NathanJamesToolbox',
    version='0.1',
    scripts=['NathanJamesToolbox'],
    author="Paulo Fajardo",
    author_email="paulo.fajardo@nathanjames.com",
    description="Package for NJ scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pfajardo-nj/NathanJamesToolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
