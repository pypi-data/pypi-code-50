import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyipx800",
    version="0.0.2",
    author="slashx57",
    author_email="boiselet@free.fr",
    description="Package to control IPX800v4 from GCEElectronics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slashx57/pyipx800",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
