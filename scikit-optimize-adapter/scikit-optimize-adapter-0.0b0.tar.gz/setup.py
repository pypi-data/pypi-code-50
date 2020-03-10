from setuptools import setup, find_packages


import adapter

VERSION = adapter.__version__

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
	name="scikit-optimize-adapter", 
	version=VERSION,
	author="Jay Kim",
	description="Dask parallelized bayesian optimization toolbox",
	long_description=long_description,
	long_description_content_type="text/x-rst",
	url=None,
	license="DSB 3-clause",
	packages=find_packages(),
	install_requires=["scikit-optimize>=0.7.4", "dask", "distributed"]
	)
