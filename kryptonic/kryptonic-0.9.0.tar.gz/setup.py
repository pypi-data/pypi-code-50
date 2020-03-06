"""
This should be run with `python setup.py sdist bdist_wheel`
"""

import setuptools

version = '0.9.0' # This version will need to be updated with every new merge


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    # name: The name of the package. This should be the same name as the directory it is in
    # this name will be used by other applications via `import name` or `from name import ...`
    name='kryptonic',

    version=version,

    # author: You! Add your name.
    author='Nick Palenchar',
    # author_email: use your untapt email
    author_email='nick@untapt.com',

    # description: a short description of the package. It should not exceed the length of this comment you're reading.
    description='Easy UI testng in the spirit of python\'s own unittest module',
    # update the README.md file for the long_description
    long_description='',

    # url: can leave blank
    url='https://github.com/untapt/kryptonic',

    # As you `pip install` dependencies, be sure to add them to this list.
    # This should be the minimal requirements
    # See https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=[
        'pymongo',
        'selenium==3.141.0',
        'xmlrunner==1.7.7'],

    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Software Development :: Testing",
    ],
)
