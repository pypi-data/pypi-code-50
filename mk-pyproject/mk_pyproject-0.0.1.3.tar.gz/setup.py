
#!/usr/bin/env python3
#vim:fileencoding=utf-8

import setuptools

from setuptools import setup
from codecs import open
import os

setup(
    name='mk_pyproject',
    version='0.0.1.1',
    description=(
        'create Python Project Template'
    ),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='chengxinyao',
    author_email='chengxinyao1991@163.com',
    license='MIT',
    url='https://github.com/chengcxy/mk_pyproject',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='python project structures',
    platforms='any',
    package_data={'templates': ['*']},
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    project_urls={  # Optional
        'Source': 'https://github.com/chengcxy/mk_pyproject',
    },
    include_package_data=True,
    extras_require={
    },
    data_files=[('', ['README.md'])],
    entry_points={
        'console_scripts': [
            'mk_pyproject=mk_pyproject.__main__:main',
        ],
    },
)
