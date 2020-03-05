# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='meshjp',
    version='0.1.0Dev',
    description='Mesh GIS for Japan',
    author='Kota Mori',
    author_email='kmori05@gmail.com',
    #url='',
    #download_url='',

    packages=find_packages(),
    install_requires=['numpy', 'shapely'],
    test_require=['pytest'],
    package_data={},
    entry_points={},
    
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
