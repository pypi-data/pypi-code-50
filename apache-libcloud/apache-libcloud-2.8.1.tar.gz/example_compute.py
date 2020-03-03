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

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

from libcloud.compute.drivers.ec2 import EC2NodeDriver
from libcloud.compute.drivers.rackspace import RackspaceNodeDriver

from typing import Type, cast

cls = get_driver(Provider.KUBEVIRT)

conn = cls(host='192.168.99.103',
           port=8443,
           secure=True,
           key_file='/home/kami/.minikube/client.key',
           cert_file='/home/kami/.minikube/client.crt',
           ca_cert='/home/kami/.minikube/ca.crt')
print(conn.list_nodes())

