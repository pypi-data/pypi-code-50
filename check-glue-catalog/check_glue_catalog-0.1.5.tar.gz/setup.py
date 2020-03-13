import io
from os import path
from setuptools import setup, find_packages

MYDIR = path.abspath(path.dirname(__file__))

cmdclass = {}
ext_modules = []

setup(
    name='check_glue_catalog',  
    version='0.1.5',
    author="Marcelo Santino",
    author_email="eu@marcelosantino.com.br",
    description="Check for details in Glue Catalog and tell if its outdated",
    url='https://github.com/msantino/check-glue-catalog',
    long_description=io.open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=["boto3"],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )