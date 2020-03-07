#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='user_tools',
    version='0.0.3',
    description=u'个人相关工具',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='SkypeKey',
    author_email='enablekey@outlook.com',
    url='https://github.com/Skypekey/user_tools',
    project_urls={
        'Documentation': 'https://github.com/Skypekey/user_tools/wiki',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/Skypekey/user_tools',
        'Tracker': 'https://github.com/Skypekey/user_tools/issues',
    },
    license='GNU GPLv3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    keywords='time file json',
    packages=find_packages(),
    # py_modules=[],
    install_requires=[],
    python_requires='>=3.8',
    # package_data={
    #     'sample': ['package_data.dat'],
    # },
    # data_files=[('my_data', ['data/data_file'])],
    # scripts=['scripts/xmlproc_parse', 'scripts/xmlproc_val']
    # entry_points={
    #     'console_scripts': [
    #     ]
    # },
)
