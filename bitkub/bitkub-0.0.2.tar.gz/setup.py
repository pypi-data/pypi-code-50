import pypandoc

from setuptools import setup
# from codecs import open
# from os import path


# here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='bitkub',
    version='0.0.2',
    description='A Python library for Bitkub API',
    long_description=long_description,
    url='https://github.com/sang-sakarin/bitkub',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    scripts=[],
    keywords='bitkub bitkub-python bitkub-python-sdk',
    packages=['bitkub'],
    install_requires=['requests'],
)
