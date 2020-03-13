# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @Date:   2020-03-08 14:34:45
# @E-mail: maoyongfan@163.com
# @Last Modified by:   yongfanmao
# @Last Modified time: 2020-03-13 11:38:50

__version__ = "1.0"

from robot.api import logger
from requests import sessions
from HelloBikeLibrary.data_conversion import soa_loads
import json

class Request(object):

	def request_client(self,url="https://fox-backend.hellobike.cn/gct/soarequest", method='post', **kwargs):
		"""
			支持rpc请求与soap请求
			支持加密http请求,请传参数 encode=True
			返回内容为:
				状态码,请求返回内容

			例:
			|$(content) |request client | http://10.111.30.72:8099/api/accountbalance
		"""
		logger.info(url)
		logger.info(kwargs['data'])
		with sessions.Session() as session:
			# 需加密http请求
			if "encode" in kwargs and kwargs['encode']:
				# 加密
				body = dict(header={}, body=kwargs['data'])
				rep = session.request(url="https://fox-backend.hellobike.cn/fox/encode", method='post', json=body)
				header = rep.json()['data']["header"]
				body = rep.json()['data']["encode"]
				print (body)
				# 发送加密请求
				rep = session.request(url=url, method=method, json=body, headers=header)
				body = dict(header=dict(Chaos="true"), response=rep.text)
				# 解密返回
				rep = session.request(url="https://fox-backend.hellobike.cn/fox/decode", method='post', json=body)
				return rep
			# soa序列化和反序列化
			elif 'data' in kwargs and 'iface' in kwargs['data']:
				data_struct = kwargs.pop('data')
				if 'request' in data_struct:
					for key, values in data_struct['request'].items():
						if isinstance(values, (list, dict)):
							values = json.dumps(values)
							data_struct['request'][key] = values
					data_struct['request'] = json.dumps(data_struct['request'])
				rep = session.request(url=url, method=method, json=data_struct)
				return rep.status_code,soa_loads(rep.text)
			# 非加密http请求
			else:
				# print ('haha',url,data)
				if 'headers' in kwargs:
					rep = session.request(url=url, method=method, json=kwargs['data'],headers=headers)
				else:
					rep = session.request(url=url, method=method, json=kwargs['data'])
				
				return rep.status_code,soa_loads(rep.text)


if __name__ == '__main__':
	# data = {
	# "authorization": True,
	# "env": "fat",
	# "iface": "com.hellobike.geo.ifaces.GeoServiceIface",
	# "method": "nearBikesNumber",
	# "service": "AppAlphapayFacadeService",
	# "addr": "10.111.10.60:61500",
	# "request": {"arg0": {
	# 	"currentLat": 31.122925,
	# 	"currentLng": 121.364965,
	# 	"radiusNum": 15000,
	# 	"cityCode": "021"
	# 	}}
	# }

	data = {
	"env": "fat",
	"iface": "com.hellobike.ride.api.iface.RideIface",
	"method": "startRide",
	"addr": "10.111.14.20:50010",
	"request": {"arg0": {
		"startLat": 31.1249201,
		"orderGuid": 15838439485081200101051,
		"bikeNo": "2500500899",
		"startChannel":4,
		"startTime":1583843948913,
		"userGuid":"c8f71e7c8bc049a8988cec062408a570",
		"posType": 0,
		"startLng": 121.3602946
		}}
	}


	# data = {
	# 	"env":"fat",
	# 	"mobilePhone":"12010002000",
	# 	"balance":"10"
	# }
	# data = {
	# "action": "user.ride.create",
	# "version": "5.35.0",
	# "systemCode": "61",
	# "adCode": "",
	# "token": "477cbf33108d488e9a8573f7efba1ee1",
	# "areaEdgeDistance": 6489.923941076401,
	# "bikeNo": "5120000393",
	# "cityCode": "021",
	# "connectBluetooth": False,
	# "deviceHash": "95b04a3725d102d9019b6ffcf45d86917486297a79fc4870f021592a596d583f",
	# "deviceId": "860714040783362",
	# "deviceUserAgent": "Mozilla/5.0 (Linux; Android 9; Redmi K20 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36",
	# "force": 1,
	# "lat": "31.1249201",
	# "lng": "121.3602946",
	# "mode": 0,
	# "model": 0,
	# "rideLicenseforce": 1,
	# "signalType": 5
	# }
	headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
	request = Request()
	#"http://10.111.30.72:8099/api/accountbalance"
	url="https://fat-bike.hellobike.com/api"
	print(request.request_client(data=data))
