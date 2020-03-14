#import setuptools
from setuptools import find_packages, setup

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setup(
    name="SmileLog", # Replace with your own username
    version="1.0.0",
    author="Sitthykun LY",
    author_email="ly.sitthykun@gmail.com",
    description="Log and Consoler assistant",
    long_description="SmileLog is smart tracking library",
    long_description_content_type="text/markdown",
    url="https://github.com/sitthykun/smilelog",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
