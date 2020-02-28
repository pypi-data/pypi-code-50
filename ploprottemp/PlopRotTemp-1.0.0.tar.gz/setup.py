import pele_platform
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
from distutils.extension import Extension
import PlopRotTemp

here = path.abspath(path.dirname(__file__))
ext_modules = []
cmdclass = {}
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
     long_description = f.read()

setup(
    name="PlopRotTemp",
    version=PlopRotTemp.__version__,
    description='Extract forcefield parameters of a small molecule using OPLS2005',
    long_description=long_description,
    url="https://github.com/NostrumBioDiscovery/PlopRotTemp",
    author='Daniel Soler',
    author_email='daniel.soler@nostrumbiodiscovery.com',
    packages=find_packages(exclude=['docs', 'tests']),
    package_data={},
    include_package_data=True,
    install_requires=[],    
    cmdclass=cmdclass,
    ext_modules=ext_modules  # accepts a glob pattern
)
