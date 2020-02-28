import setuptools
from setuptools import setup
import os
try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

setup(name='summarizer4u',
version='0.1',
description='Get your text summarized',
url='https://github.com/Navan0',
author='Navaneeth KT',
author_email='nktclt@gmail.com',
license='MIT',
packages=setuptools.find_packages(),
install_requires=load_requirements("requirements.txt"),
zip_safe=False)

os.system("python -m spacy download en_core_web_sm")
