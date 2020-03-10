#  logger-mixin setup.py (Last Modified 3/10/20, 10:36 AM)
#  Copyright (C) 2020 Daniel Sullivan (daniel.sullivan@state.mn.us
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os

from setuptools import setup

if os.environ.get('CI_COMMIT_TAG'):
    version = os.environ['CI_COMMIT_TAG']
else:
    version = os.environ['CI_JOB_ID']
setup(
    name='logger_mixin',
    version=version,
    packages=['logger_mixin'],
    url='https://gitlab.com/ds-mpca/logger-mixin',
    license='Lesser General Public License V3',
    author='Daniel Sullivan',
    author_email='daniel.sullivan@state.mn.us',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
    ]
)
