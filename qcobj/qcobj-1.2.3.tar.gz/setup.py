#
# R. Vidmar, 20180906
# R. Vidmar, 20200302
#

from setuptools import setup, find_packages
import subprocess
import os

PACKAGE = "qcobj"
REQFILE = "requirements.txt"

exec(open(os.path.join(PACKAGE, "__version__.py")).read())

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(REQFILE) as fp:
    requirements = fp.read()

setup(name=PACKAGE,
        version=__version__,
        install_requires=requirements,
        author='Roberto Vidmar',
        author_email='rvidmar@inogs.it',
        description='A quantity aware configObject',
        license='MIT',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://bitbucket.org/bvidmar/qcobj',
        packages=find_packages(),
        scripts=['bin/cfggui.py', ],
        classifiers=(
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.6",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ),
        )
