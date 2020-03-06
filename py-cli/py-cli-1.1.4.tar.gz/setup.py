# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

import re
from os import path


def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(path.join(project, '__init__.py')).read())

    return result.group(1)


with open('README.md', encoding='utf-8') as readme_file:
    _long_description = readme_file.read()

setup(
    author='handy',
    author_email='cvdnn@foxmail.com',
    url='https://pypi.org/project/py-cli/',

    license='Apache v2.0',
    description='gitrunner cli script',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    keywords=["gitlab_runner_cli", "android_cli"],

    name='py-cli',
    version=get_property('__version__', 'xcli'),

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['androguard', 'oss2', 'requests'],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
            'pycli = xcli.deploy:invoke',
        ],
    },

    # 此项需要，否则卸载时报windows error
    zip_safe=False
)
