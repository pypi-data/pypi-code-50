# -*- coding: utf-8 -*-
# from setuptools import setup, find_packages
import setuptools


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()



setuptools.setup(
    name='astroimages_fits',
    packages = ['astroimages_fits'],
    version='0.2.2',
    description='FITS files related routines and classes',
    # long_description=readme,
    # long_description_content_type="text/markdown",
    author='Rodrigo de Souza',
    author_email='rsouza01@gmail.com',
    url='https://github.com/AstroImages/astroimages-fits',
    download_url = 'https://github.com/AstroImages/astroimages-fits/archive/v_0.2.2.tar.gz',
    license=license,
    install_requires=[
        'astropy',
        'numpy'
    ],    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
