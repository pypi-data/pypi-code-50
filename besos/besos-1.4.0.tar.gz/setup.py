import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="besos",
    version="1.4.0",
    description="A library for Building and Energy Simulation, Optimization and Surrogate-modelling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude="pytests"),
    include_package_data=True,
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
