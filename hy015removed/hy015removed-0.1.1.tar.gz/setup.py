# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name='hy015removed',
    version='0.1.1',
    description='hy015removed : compat functions removed in hy-lang ver0.15 for hy 0.18 ',
    url='https://github.com/niitsuma/hy015removed/',
    author='Hirotaka Niitsuma',
    author_email='hirotaka.niitsuma@gmail.com',
    license="GNU Affero General Public License",
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='hy',
    install_requires=[], #'hy>=0.15' was removed becase gentoo linux hy package bug
    packages=['hy015removed'],
    package_data={'hy015removed': ['*.hy',],},
    test_suite='nose.collector',
    tests_require=['nose'],
    platforms='any',
)
