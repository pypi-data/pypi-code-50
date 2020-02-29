#!/usr/bin/python\r\n
import setuptools
from setuptools import setup
import os
setup(name='summarizer4u',
version='0.3.1',
description='Get your text summarized',
url='https://github.com/Navan0',
author='Navaneeth KT',
author_email='nktclt@gmail.com',
long_description="""# summarizer4uGet your text summarized ! \n \n from summarizer4u import summary \n \n text = summary("your text go here") \n \n print(text) """,
long_description_content_type='text/markdown',
packages=setuptools.find_packages(),
install_requires=['spacy'],
zip_safe=False)

os.system("python -m spacy download en_core_web_sm")
