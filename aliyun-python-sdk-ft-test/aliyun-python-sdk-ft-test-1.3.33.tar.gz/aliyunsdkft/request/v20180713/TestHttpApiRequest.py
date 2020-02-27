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

class TestHttpApiRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ft', '2018-07-13', 'TestHttpApi')

	def get_IspSignatureSecretKey(self):
		return self.get_query_params().get('IspSignatureSecretKey')

	def set_IspSignatureSecretKey(self,IspSignatureSecretKey):
		self.add_query_param('IspSignatureSecretKey',IspSignatureSecretKey)

	def get_StringValue(self):
		return self.get_body_params().get('StringValue')

	def set_StringValue(self,StringValue):
		self.add_body_params('StringValue', StringValue)

	def get_OtherParam(self):
		return self.get_body_params().get('OtherParam')

	def set_OtherParam(self,OtherParam):
		self.add_body_params('OtherParam', OtherParam)

	def get_BooleanParam(self):
		return self.get_query_params().get('BooleanParam')

	def set_BooleanParam(self,BooleanParam):
		self.add_query_param('BooleanParam',BooleanParam)

	def get_DefaultValue(self):
		return self.get_body_params().get('DefaultValue')

	def set_DefaultValue(self,DefaultValue):
		self.add_body_params('DefaultValue', DefaultValue)

	def get_IspSignature(self):
		return self.get_query_params().get('IspSignature')

	def set_IspSignature(self,IspSignature):
		self.add_query_param('IspSignature',IspSignature)