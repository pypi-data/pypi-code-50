import os
from setuptools import setup, find_packages
# setuptools allows "python setup.py develop"

REQFILE = "requirements.txt"

exec(open(os.path.join("colorAlphabet", "__version__.py")).read())

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(REQFILE) as fp:
    requirements = fp.read()

setup(name='colorAlphabet',
    version=__version__,
    install_requires=requirements,
    author='Roberto Vidmar',
    author_email="rvidmar@inogs.it",
    description=('Use Paul Green-Armytage color alphabet to color text output'
            ' to a terminal'),
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://bitbucket.org/bvidmar/colorAlphabet',
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ),
    )
