# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['sqlalchemy_imageattach_boto3']
install_requires = \
['SQLAlchemy-ImageAttach>=1.1.0,<1.2.0', 'boto3>=1.11,<2.0']

setup_kwargs = {
    'name': 'sqlalchemy-imageattach-boto3',
    'version': '0.1.0',
    'description': 'SQLAlchemy-ImageAttach AWS S3 Store with boto3',
    'long_description': '# SQLAlchemy-ImageAttach-boto3\n\nSQLAlchemy-ImageAttach AWS S3 Store with boto3\n',
    'author': 'Spoqa Creators',
    'author_email': 'dev@spoqa.com',
    'maintainer': 'rusty',
    'maintainer_email': 'rusty@spoqa.com',
    'url': 'https://github.com/spoqa/sqlalchemy-imageattach-boto3',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
}


setup(**setup_kwargs)
