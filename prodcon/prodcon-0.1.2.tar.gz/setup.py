import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prodcon",
    version="0.1.2",
    author="Johannes Pertl",
    author_email="johannes.pertl@edu.fh-joanneum.at",
    description="An easy to use implementation of the producer consumer pattern",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JohannesPertl/prodcon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)