from distutils.core import setup

import os


def version():
    setupDir = os.path.dirname(os.path.realpath(__file__))
    versionFile = open(os.path.join(setupDir, 'gtdb_validation_tk', 'VERSION'))
    return versionFile.readline().strip()

setup(
    name='gtdb_validation_tk',
    version=version(),
    author='Donovan Parks',
    author_email='donovan.parks@gmail.com',
    packages=['gtdb_validation_tk'],
    scripts=['bin/gtdb_validation_tk'],
    package_data={'gtdb_validation_tk' : ['VERSION']},
    url='http://pypi.python.org/pypi/genometreetk/',
    license='GPL3',
    description='A toolbox for validating the GTDB taxonomy.',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy >= 1.8.0",
        "biolib >= 0.1.0",
        "dendropy >= 4.0.0"],
)
