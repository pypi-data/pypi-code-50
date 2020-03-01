from setuptools import setup, find_packages

from setuptools.extension import Extension

#read more on : 
#http://python-packaging.readthedocs.io/en/latest/minimal.html
#for projects not from pypi: dependency_links = ['url']
#


setup(name='st_git_hooks',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
      ],
      version='0.0.1')
