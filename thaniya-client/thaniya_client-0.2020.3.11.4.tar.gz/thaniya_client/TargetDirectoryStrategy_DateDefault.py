


import os
import socket
import datetime

import jk_utils

from .AbstractTargetDirectoryStrategy import AbstractTargetDirectoryStrategy




class TargetDirectoryStrategy_DateDefault(AbstractTargetDirectoryStrategy):

	def __init__(self, extraSubDirPath:str = None):
		if extraSubDirPath is not None:
			assert isinstance(extraSubDirPath, str)
			assert extraSubDirPath
			assert extraSubDirPath[0] != "/"
		self.__extraSubDirPath = extraSubDirPath
	#

	def selectEffectiveTargetDirectory(self, baseTargetDirPath:str):
		assert isinstance(baseTargetDirPath, str)

		if self.__extraSubDirPath is not None:
			baseTargetDirPath += "/" + self.__extraSubDirPath

		hostname = socket.gethostname()
		assert isinstance(hostname, str)
		now = datetime.datetime.now()
		p = os.path.join(baseTargetDirPath, hostname, "{:04d}".format(now.year), "{:04d}-{:02d}-{:02d}".format(now.year, now.month, now.day))
		return p
	#

#

