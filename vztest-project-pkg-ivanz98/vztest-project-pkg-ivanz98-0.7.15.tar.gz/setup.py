from __future__ import print_function

from setuptools import setup
import sys

import unittest

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('pony.orm.tests', pattern='test_*.py')
    return test_suite

name = "vztest-project-pkg-ivanz98"
version = "0.7.15"
description = "test project"
long_description = "desc"

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries',
    'Topic :: Database'
]

author = "Alexander Kozlovsky, Alexey Malashkevich"
author_email = "team@ponyorm.com"
url = "https://ponyorm.com"
licence = "Apache License Version 2.0"

packages = [
    "pony",
    "pony.flask",
    "pony.flask.example",
    "pony.orm",
    "pony.orm.dbproviders",
    "pony.orm.examples",
    "pony.orm.integration",
    "pony.orm.tests",
    "pony.thirdparty",
    "pony.thirdparty.compiler",
    "pony.utils"
]

package_data = {
    'pony.flask.example': ['templates/*.html'],
    'pony.orm.tests': ['queries.txt']
}

#download_url = "http://pypi.python.org/pypi/pony/"

if __name__ == "__main__":
    pv = sys.version_info[:2]
    if pv not in ((2, 7), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)):
        s = "Sorry, but %s %s requires Python of one of the following versions: 2.7, 3.3-3.8." \
            " You have version %s"
        print(s % (name, version, sys.version.split(' ', 1)[0]))
        sys.exit(1)

    setup(
        name=name,
        version=version,
        description=description,
        long_description=long_description,
        classifiers=classifiers,
        author=author,
        author_email=author_email,
        url=url,
        license=licence,
        packages=packages,
        package_data=package_data,
        #download_url=download_url,
        test_suite='setup.test_suite'
    )
