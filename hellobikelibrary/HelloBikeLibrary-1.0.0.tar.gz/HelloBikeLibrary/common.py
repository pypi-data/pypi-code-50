# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @Date:   2020-03-10 14:52:05
# @E-mail: maoyongfan@163.com
# @Last Modified by:   yongfanmao
# @Last Modified time: 2020-03-13 11:38:35

from robot.api import logger
from HelloBikeLibrary.request import Request
import json

__version__ = "1.0"

class Common(object):

	def sendCodeV3(self,mobilePhone):
		url = "https://fat-api.hellobike.com/api"
		data = {
			"mobile" : mobilePhone,
			"source" : 0,
			"riskControlData" : {
			"userAgent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
			"deviceLon" : "121.363833",
			"roam" : "460",
			"systemCode" : "61",
			"deviceLat" : "31.122775"
			},
			"action" : "user.account.sendCodeV3"
		}
		rep = Request().request_client(url=url,data=data)

	def login_auth_app(self,mobilePhone):
		"""
			app登陆认证
			返回token,guid
		"""
		self.sendCodeV3(mobilePhone)
		app_url = "https://fat-api.hellobike.com/auth"
		data = {
		"clientId" : "01L01610000038690879",
		"version" : "5.34.0",
		"riskControlData" : {
			"userAgent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
			"deviceLon" : "121.363761",
			"roam" : "460",
			"systemCode" : "61",
			"deviceLat" : "31.122788"
		},
		"mobile" : mobilePhone,
		"longitude" : "121.363800",
		"latitude" : "31.122782",
		"cityCode" : "021",
		"code" : "1234",
		"action" : "user.account.login",
		"city" : "上海市",
		"systemCode" : "61",
		"adCode" : "310112"
		}
		rep = Request().request_client(url=app_url,data=data)
		if rep[0] == 200:
			content = rep[1]
			if content.get('data').get('token'):
				logger.info(content.get('data'))
				return content.get('data').get('token'),content.get('data').get('guid')
		else:
			raise Exception("App登陆失败")

if __name__ == '__main__':
	com = Common()
	print(com.login_auth_app("12010002000"))

