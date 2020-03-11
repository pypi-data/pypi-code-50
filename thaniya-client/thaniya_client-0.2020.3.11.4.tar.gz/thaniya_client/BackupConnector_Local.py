


import os

import jk_utils

from .AbstractBackupConnector import AbstractBackupConnector
from .ThaniyaIO import ThaniyaIO
from .ThaniyaBackupContext import ThaniyaBackupContext




class BackupConnector_Local(AbstractBackupConnector):

	def __init__(self):
		self.__targetDirPath = None
	#

	def initialize(self, ctx:ThaniyaBackupContext, targetDirPath:str, nExpectedNumberOfBytesToWrite:int, parameters:dict):
		self.__targetDirPath = targetDirPath
	#

	def deinitialize(self, ctx:ThaniyaBackupContext, bError:bool, statsContainer:dict):
		pass
	#

	@property
	def isReady(self) -> bool:
		return self.__targetDirPath
	#

	@property
	def targetDirPath(self) -> str:
		return self.__targetDirPath
	#

	def dump(self):
		print("BackupConnector_Local")
		#for key in [ "_sessionID",
		#	"mountPoint" ]:
		#	print("\t" + key, "=", getattr(self, key))
	#

#












