# vim: expandtab tabstop=4 shiftwidth=4

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='pylint-beergarden',
    version='0.1.1',
    author='Bill Allen',
    author_email='photo.allen@gmail.com',
    description='A pylint plugin for the Beergarden framework.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='pylint beergarden'.split(),
    url='https://github.com/gershwinlabs/pylint-beergarden',
    packages=['pylint_beergarden'],
    package_data={},
    install_requires=['pylint',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ]
)
