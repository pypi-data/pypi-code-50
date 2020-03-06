from setuptools import setup, find_packages
from distutils.core import  Extension

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
   name='WUDESIM_Py',
   version='0.0.2',
   description='A model for simulating water quality in the dead-end branches of drinking water distribution networks',
   author='Ahmed Abokifa',
   author_email=' abokifa@uic.edu',
   packages=find_packages(),  #same as name
   license="MIT license",
   long_description=readme,
   data_files=[('WUDESIM_Py', ['WUDESIM_Py/epanet2.dll']),
               ('WUDESIM_Py', ['WUDESIM_Py/WUDESIM_LIB.dll']) ]
)
