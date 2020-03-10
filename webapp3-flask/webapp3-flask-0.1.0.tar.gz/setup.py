import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webapp3-flask", 
    version="0.1.0",
    author="Brandon Wegner",
    author_email="brandon.wegner@reddingsoftware.com",
    description="This program allows people to convert their old webapp2 classes to make them work with Python 3 using Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ReddingSoftware/Webapp3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)