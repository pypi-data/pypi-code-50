import os
import re

from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(ROOT, 'finders', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='finders',
    description=
    'Finders - Find resources to determine if you want to keep them',
    long_description=open('README.md').read(),
    version=get_version(),
    license='MIT',
    install_requires=[
        'boto3',
    ],
    url='https://github.com/acaire/finders',
    packages=find_packages(exclude=['tests*']),
    author='Ash Caire',
    author_email='ash.caire@gmail.com',
    keywords=[
        'finders', 'keepers', 'resource', 'discovery', 'aws', 'cloudformation',
        'stacks'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)
