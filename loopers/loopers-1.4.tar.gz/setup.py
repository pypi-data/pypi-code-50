import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loopers",
    version="1.4",
    author="Akere Mukhtar Abiodun",
    author_email="akeremukhtar10@gmail.com",
    description="An email scrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sirrobot01/loopers",
    packages=['loopers'],
    install_requires=['requests', 'bs4']
)
