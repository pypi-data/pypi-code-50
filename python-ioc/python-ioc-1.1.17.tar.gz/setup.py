#!/usr/bin/env python3
#!/usr/bin/env python3
#
# Copyright (C) 2019-2020 Cochise Ruhulessin
#
# This file is part of python-ioc.
#
# python-ioc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# python-ioc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-ioc.  If not, see <https://www.gnu.org/licenses/>.
from setuptools import setup


version = str.strip(open('ioc/VERSION').read())
requirements = str.split(open('requirements.txt').read(), '\n')


setup(
    name='python-ioc',
    version=version,
    description='Python Inversion of Control Framework',
    author='Cochise Ruhulessin',
    author_email='cochiseruhulessin@gmail.com',
    url='https://www.wizardsofindustry.net',
    project_name='Inversion of Control',
    install_requires=requirements,
    packages=[
        'ioc',
        'ioc.schema',
    ]
)
