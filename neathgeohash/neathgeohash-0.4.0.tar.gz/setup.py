from setuptools import setup, find_packages
from codecs import open
from os import path

VERSION = '0.4.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='neathgeohash',
    version=VERSION,
    description='Python module for interacting with geohashes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mpdwulit/neathgeohash',
    download_url='https://github.com/mpdwulit/neathgeohash/tarball/' + VERSION,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='geohash gis eep95 conf95',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    author='Marek Dwulit',
    author_email='marek.dwulit@gmail.com',
    install_requires=[
        'pygeohash',
        'geopy',
        'numpy'
    ],
    python_requires='>=3.6'
)
