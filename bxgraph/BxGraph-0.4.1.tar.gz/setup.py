#
#  setup.py
#  bxgraph
#
#  Created by Oliver Borchert on June 20, 2019.
#  Copyright (c) 2019 Oliver Borchert. All rights reserved.
#

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='BxGraph',
    version='0.4.1',

    author='Oliver Borchert',
    author_email='borchero@icloud.com',

    description='Graph Management in Python.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    url='https://gitlab.lrz.de/borchero/bxgraph',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.18.1,<2.0.0',
        'scipy>=1.4.1,<2.0.0',
        'numba>=0.47.0,<0.48.0'
    ],

    license='License :: OSI Approved :: MIT License',
    zip_safe=False
)
