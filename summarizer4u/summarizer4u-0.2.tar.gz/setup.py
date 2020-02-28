import setuptools
from setuptools import setup
import os
setup(name='summarizer4u',
version='0.2',
description='Get your text summarized',
url='https://github.com/Navan0',
author='Navaneeth KT',
author_email='nktclt@gmail.com',
license='MIT',
packages=setuptools.find_packages(),
install_requires=['spacy'],
zip_safe=False)

os.system("python -m spacy download en_core_web_sm")
