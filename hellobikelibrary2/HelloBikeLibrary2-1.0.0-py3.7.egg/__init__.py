# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @Date:   2020-03-08 13:24:25
# @E-mail: maoyongfan@163.com
# @Last Modified by:   yongfanmao
# @Last Modified time: 2020-03-13 16:56:34

from HelloBikeLibrary2.request import Request
from HelloBikeLibrary2.version import VERSION
from HelloBikeLibrary2.common import Common

__version__ = VERSION

class HelloBikeLibrary(Request,Common):
	"""
		HelloBikeLibrary 1.0
	"""
	ROBOT_LIBRARY_SCOPE = "GLOBAL"

if __name__ == '__main__':
	pass