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

from pprint import pprint

from libcloud.dns.types import Provider
from libcloud.dns.providers import get_driver

Zerigo = get_driver(Provider.CLOUDFLARE)

driver = Zerigo('tomaz@tomaz.me', 'bae540b356fbf88ddb364875c9bb3ef4ab303')

zones = driver.list_zones()
pprint(zones)

records = zones[0].list_records()
pprint(records)

print(zones[0].export_to_bind_format())
