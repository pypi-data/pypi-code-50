

import os

import jk_logging





class ThaniyaBackupContext(object):

	def __init__(self, targetDirPath:str, log:jk_logging.AbstractLogger, processingContext):
		self.__targetDirPath = targetDirPath
		self.__log = log
		self.__processingContext = processingContext
	#

	@property
	def duration(self) -> float:
		return self.__processingContext.duration
	#

	@property
	def log(self) -> jk_logging.AbstractLogger:
		return self.__log
	#

	@property
	def targetDirPath(self) -> str:
		return self.__targetDirPath
	#

	def descend(self, text:str):
		return ThaniyaBackupContext(self.__targetDirPath, self.__log.descend(text), self.__processingContext)
	#

	def absPath(self, fileName:str) -> str:
		if os.path.isabs(fileName):
			assert fileName.startswith(self.__targetDirPath)
			return fileName
		else:
			return os.path.join(self.__targetDirPath, fileName)
	#

#




