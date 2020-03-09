from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setup(
	name="epdnorway",
	version="0.3",
	description="Extract and organize datapoints from Epd Norway DataSet",
    long_description=long_description,
    long_description_content_type="text/markdown",
	url="https://bitbucket.com/knakk/epdnorway",
	author="Knakk AS",
	author_email="benjamin@knakk.no",
	license="MIT",
    packages=["epdnorway"],
	install_requires=["xmltodict"],
    python_requires='>=3.7',
	zip_safe=False
)
