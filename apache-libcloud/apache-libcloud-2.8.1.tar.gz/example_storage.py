# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from io import BytesIO
from pprint import pprint
import sys

from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver


Driver = get_driver(Provider.GOOGLE_STORAGE)
driver = Driver('libcloud-test@api-project-767966281678.iam.gserviceaccount.com',
              '/home/kami/Downloads/api-project-767966281678-b44d02952d31.json',
              project='api-project-767966281678')

Driver = get_driver(Provider.AZURE_BLOBS)
driver = Driver('libclouddevblobs',
                'CWNVu69mq/9HUX7+hLNEWPulX4/45KLYN306CpW0BBccV4Ot6JyPxXsHRxK+wGENCYMf97NqPYUEA0nUtnDnqg==')


Driver = get_driver(Provider.CLOUDFILES)
driver = Driver('kamislo',
                'ad514c7eb8a55dfefecc6a1a1770aa47',
                region='ord')


#driver = Driver('GOOGC7RCLUYGL3IUBRNW', 'kjZ0t1VCFIz2zOCJXEv532mG4mlTZIg2NWd4Mrat')

containers = driver.list_containers()
container = containers[0]
container_objects = driver.list_container_objects(containers[0])

iterator = BytesIO(b'0123456789')


obj = driver.upload_object_via_stream(iterator=BytesIO(b'0123456789'), container=container, object_name='test1.xlsm')
#                                      extra={'content_type': 'application/vnd.ms-excel.sheet.macroenabled.12'})

print(driver.download_object_range(obj=obj, destination_path='1.obj', start_bytes=5, end_bytes=None, overwrite_existing=True))
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=0, end_bytes=1)))
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=0, end_bytes=2)))
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=0, end_bytes=3)))
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=5, end_bytes=8)))
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=5)))

print('====')
sys.exit(1)

driver = get_driver(Provider.LOCAL)('.')

containers = driver.list_containers()
container = containers[0]
obj = driver.upload_object_via_stream(iterator=iterator, container=container, object_name='test1.xlsm')
print(driver.download_object_range(obj=obj, destination_path='3.obj', start_bytes=0, end_bytes=6, overwrite_existing=True))
sys.exit(1)
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=0, end_bytes=1)))
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=0, end_bytes=2)))
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=5, end_bytes=8)))
print(next(driver.download_object_range_as_stream(obj=obj, start_bytes=5)))

