import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GusPI",
    version="0.0.12",
    author="Randy Geszvain",
    author_email="ygeszvain@gmail.com",
    description="A Statistical Support package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ygeszvain/GusPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
