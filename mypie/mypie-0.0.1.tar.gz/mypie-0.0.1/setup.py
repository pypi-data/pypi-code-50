import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypie",
    version="0.0.1",
    author="Manmohan Mishra",
    author_email="manmohan.techie@gmail.com",
    description="A small self help package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://radiantinfonet.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)