import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Orange_Vision",
    version="0.0.1",
    author="Danny Dasilva",
    author_email="dannydasilva.solutions@gmail.com",
    description="FRC Orange Vision",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Danny-Dasilva/Orange_Vision",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
