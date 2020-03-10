#
#  setup.py
#  bxtorch
#
#  Created by Oliver Borchert on May 23, 2019.
#  Copyright (c) 2019 Oliver Borchert. All rights reserved.
#

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='BxTorch',
    version='0.7.2',

    author='Oliver Borchert',
    author_email='borchero@icloud.com',

    description='Large-Scale Machine and Deep Learning in PyTorch.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    url='https://github.com/borchero/bxtorch',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3.7',
    install_requires=[
        'torch>=1.3.1,<1.4.0',
        'numpy>=1.17.0,<2.0.0',
        'scipy>=1.3.2,<2.0.0',
        'numba>=0.47.0,<0.48.0',
        'scikit-learn>=0.22.1,<0.23.0'
    ],

    license='License :: OSI Approved :: MIT License',
    zip_safe=False
)
