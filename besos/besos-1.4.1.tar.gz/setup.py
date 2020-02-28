import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="besos",
    version="1.4.1",
    description="A library for Building and Energy Simulation, Optimization and Surrogate-modelling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude="pytests"),
    include_package_data=True,
    author="Ralph Evins",
    author_email="revins@uvic.ca",
    url="https://gitlab.com/energyincities/besos",
    license="GPL",
    maintainer="Paul Kovacs",
    maintainer_email="pkovacs@uvic.ca",
    install_requires=[
        "dataclasses",
        "eppy",
        "pyDOE2",
        "numpy",
        "pandas",
        "platypus-opt",
        "rbfopt",
        "matplotlib",
        "ipywidgets",
        "jupytext",
        "pathos",
        "sklearn",
        "pyKriging",
        "pyehub",
        "dask[complete]",
        "geomeppy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)
