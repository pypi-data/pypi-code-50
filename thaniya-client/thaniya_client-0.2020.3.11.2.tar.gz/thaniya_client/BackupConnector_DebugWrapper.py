


from .ThaniyaBackupContext import ThaniyaBackupContext
from .AbstractBackupConnector import AbstractBackupConnector




class BackupConnector_DebugWrapper(AbstractBackupConnector):

	def __init__(self, backupClient:AbstractBackupConnector):
		self.__backupClient = backupClient
	#

	def initialize(self, ctx:ThaniyaBackupContext, targetDirPath:str, nExpectedNumberOfBytesToWrite:int, parameters:dict):
		print("> initialize: begin")
		self.__backupClient.initialize(ctx, targetDirPath, nExpectedNumberOfBytesToWrite, parameters)
		print("> initialize: end")
	#

	def deinitialize(self, ctx:ThaniyaBackupContext, bError:bool, statsContainer:dict):
		print("> deinitialize: begin")
		self.__backupClient.deinitialize(ctx, bError, statsContainer)
		print("> initialize: end")
	#

	@property
	def isReady(self) -> bool:
		print("> isReady: begin")
		return self.__backupClient.isReady
		print("> isReady: end")
	#

	@property
	def targetDirPath(self) -> str:
		print("> targetDirPath: begin")
		return self.__backupClient.targetDirPath
		print("> targetDirPath: end")
	#

	def onBackupCompleted(self, bError:bool):
		print("> onBackupCompleted: begin")
		self.__backupClient.onBackupCompleted(bError)
		print("> onBackupCompleted: end")
	#

	def dump(self):
		print("> dump: begin")
		self.__backupClient.dump()
		print("> dump: end")
	#

#













