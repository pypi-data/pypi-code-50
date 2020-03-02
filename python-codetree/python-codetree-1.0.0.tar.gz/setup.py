from __future__ import division, print_function
from setuptools import setup, find_packages

tests_require = [
    "coverage>=4.4",
    'futures>=3.1.1;python_version<="2.7"',
    'mock>=2.0;python_version<="2.7"',
    "nose>=1.3.7",
    "pip>=9.0",
    "requests>=2.18",
    "setuptools>=36.0.1",
    "six>=1.10",
    "flake8"
]

setup(
    name="python-codetree",
    version="1.0.0",
    description="A code tree builder",
    url="https://launchpad.net/codetree",
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers"],
    entry_points={
        "console_scripts": ['codetree = codetree.cli:main']},
    include_package_data=False,
    install_requires=[
        'futures;python_version<="2.7"',
        'requests',
        'six'
    ],
    extras_require={
        "tests": tests_require,
    },
    tests_require=tests_require,
)
