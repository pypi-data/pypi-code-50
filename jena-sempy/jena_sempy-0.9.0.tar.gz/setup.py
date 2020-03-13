from setuptools import setup

setup(
    name='jena_sempy',
    version='0.9.0',
    description='Manipulates semantic information and offers planning capabilities.',
    author='Alexandre Angleraud',
    author_email='alexandre.angleraud@tuni.fi',
    download_url='https://github.com/Zorrander/jena_sempy/archive/v0.9.0.tar.gz',
    license='New BSD License',
    test_suite="tests",
    install_requires=[
     'requests',
     'rdflib',
     'networkx',
     #'matplotlib',
     'secrets',
     'matplotlib<=2-2-4'
    ],
    packages=[
     'jena_com',
     'jena_reasoning',
     'jena_models'
    ]
)
