from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name="pmdatapipelineslight",
	version="0.0.3",
	author="Jørgen Frøland",
	author_email="jorgen.froland@polarismedia.no",
	description="Lightweight version of data pipeline library for Polaris Media",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)