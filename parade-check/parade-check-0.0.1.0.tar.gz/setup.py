# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='parade-check',
    version="0.0.1.0",
    author='Pan Chen',
    author_email='chenpan9012@gmail.com',
    description='A check module of parade',
    url='https://github.com/qianmosolo/parade-check',
    install_requires=['parade'],
    packages=find_packages('src'),
    package_dir=({'parade': 'src/parade'}),
    zip_safe=False,
    python_requires='>=3.4',
    include_package_data=True,
    platforms=['any'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX'
    ],
    setup_requires=[
        "setuptools_scm>=1.5"
    ]
)
