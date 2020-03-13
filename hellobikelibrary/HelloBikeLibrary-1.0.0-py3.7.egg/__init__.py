# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @Date:   2020-03-08 13:24:25
# @E-mail: maoyongfan@163.com
# @Last Modified by:   yongfanmao
# @Last Modified time: 2020-03-13 11:38:26

from HelloBikeLibrary.request import Request
from HelloBikeLibrary.version import VERSION
from HelloBikeLibrary.common import Common

__version__ = VERSION

class HelloBikeLibrary(Request,Common):
	"""
		HelloBikeLibrary 1.0
	"""
	ROBOT_LIBRARY_SCOPE = "GLOBAL"

if __name__ == '__main__':
	pass