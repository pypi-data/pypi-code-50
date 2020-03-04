# -*- coding: utf-8 -*-
"""
package/install module package ekca-service
"""

import sys
import os
from setuptools import setup

PYPI_NAME = 'ekca-plugin-ldap3'

BASEDIR = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, os.path.join(BASEDIR, 'ekca_service', 'plugins', 'password', 'ldap3'))
import __about__

setup(
    name=PYPI_NAME,
    license=__about__.__license__,
    version=__about__.__version__,
    description='EKCA service password plugin using ldap3 module',
    author=__about__.__author__,
    author_email=__about__.__mail__,
    maintainer=__about__.__author__,
    maintainer_email=__about__.__mail__,
    url='https://ekca.stroeder.com',
    download_url='https://pypi.python.org/pypi/'+PYPI_NAME,
    keywords=['PKI', 'SSH', 'SSH-CA', 'Certificate'],
    packages=['ekca_service.plugins.password.ldap3'],
    package_dir={'': '.'},
    test_suite='tests',
    python_requires='>=3.4.*',
    include_package_data=True,
    data_files=[],
    install_requires=[
        'setuptools',
        'ekca-service>={version}'.format(version=__about__.__version__),
        'ldap3>=2.4',
    ],
    zip_safe=False,
    entry_points={
        'ekca_service.plugins.password': [
            'ldap3 = ekca_service.plugins.password.ldap3:LDAPPasswordChecker',
        ],
    },
)
