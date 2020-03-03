#!/usr/bin/python\r\n
import setuptools
from setuptools import setup
setup(name='summarizer4u',
version='0.3.2',
description='Get your text summarized',
url='https://github.com/Navan0',
author='Navaneeth KT',
author_email='nktclt@gmail.com',
long_description=""" Get your text summarized ! \n \n from summarizer4u import summary \n \n text = summary("your text go here") \n \n print(text) """,
long_description_content_type='text/markdown',
packages=setuptools.find_packages(),
classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
],
scripts=["con.py"],
install_requires=['spacy'],
zip_safe=False)
