import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hiegeo",
    version="0.1.0",
    author="Alessandro Comunian",
    author_email="alessandro.comunian@unimi.it",
    description="Modelling stratigraphic alluvial architectures, constrained by stratigraphic hierarchy and relative chronology",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://bitbucket.org/alecomunian/hiegeo",
    packages=setuptools.find_packages(where="hiegeo"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy>=1.18.1",
        "matplotlib",
        "anytree",
        "pandas"],
    package_dir = {"": "hiegeo"},
)
