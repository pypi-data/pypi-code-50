# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

from setuptools import setup, find_packages
from version import VERSION

v = open(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'sqlalchemy_qubole', '__init__.py'))
version = '.'.join([str(v) for v in VERSION if v is not None])
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(name='sqlalchemy_qubole',
      version=version,
      description="Qubole Presto/Hive for SQLAlchemy",
      license='Apache License, Version 2.0',
      url='https://docs.qubole.com/en/latest/connectivity-options/partner-integration/sqlalchemy/sqlalchemy-index.html',
      author='Qubole',
      author_email='support@qubole.com',
      long_description=open(readme).read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Database :: Front-Ends',
      ],
      install_requires=[
          'SQLAlchemy', 'future', 'pyhive==0.6.1', 'python-dateutil', 'JPype1==0.6.3', 'JayDeBeApi==1.1.1'
      ],
      extras_require={
          "jdbc": ["JPype1==0.6.3", "JayDeBeApi==1.1.1"]
      },
      keywords='SQLAlchemy Qubole',
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          'sqlalchemy.dialects': [
              'qubole = sqlalchemy_qubole.prestodialect:QubolePrestoDialect',
              'qubole.presto = sqlalchemy_qubole.prestodialect:QubolePrestoDialect',
              'qubole.hive = sqlalchemy_qubole.hivedialect:QuboleHiveDialect',
          ]
      }
    )
