# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class TestErrorCodeForGateWayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ft', '2018-07-13', 'TestErrorCodeForGateWay')

	def get_HttpStatusCode(self):
		return self.get_query_params().get('HttpStatusCode')

	def set_HttpStatusCode(self,HttpStatusCode):
		self.add_query_param('HttpStatusCode',HttpStatusCode)

	def get_Code(self):
		return self.get_query_params().get('Code')

	def set_Code(self,Code):
		self.add_query_param('Code',Code)

	def get_Success(self):
		return self.get_query_params().get('Success')

	def set_Success(self,Success):
		self.add_query_param('Success',Success)

	def get_Message(self):
		return self.get_query_params().get('Message')

	def set_Message(self,Message):
		self.add_query_param('Message',Message)