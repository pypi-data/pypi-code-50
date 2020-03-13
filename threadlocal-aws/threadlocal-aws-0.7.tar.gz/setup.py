# Copyright 2019 Pasi Niemi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
from setuptools import setup

setup(name='threadlocal-aws',
      version='0.7',
      description='Library to access threadlocal aws clients and resources',
      url='http://github.com/NitorCreations/threadlocal-aws',
      download_url='https://github.com/NitorCreations/threadlocal-aws/tarball/0.7',
      author='Pasi Niemi',
      author_email='pasi.niemi@nitor.com',
      license='Apache 2.0',
      packages=['threadlocal_aws'],
      include_package_data=True,
      install_requires=[
          'boto3',
          'urllib3'
      ] + (['wmi'] if sys.platform.startswith('win') else []),
      zip_safe=True)
