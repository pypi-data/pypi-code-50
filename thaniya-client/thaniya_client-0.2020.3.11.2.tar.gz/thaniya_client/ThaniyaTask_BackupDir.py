


import os

import jk_pathpatternmatcher2
import jk_utils
from jk_typing import checkFunctionSignature

from .AbstractThaniyaTask import AbstractThaniyaTask
from .ThaniyaBackupContext import ThaniyaBackupContext

from .EnumTarPathMode import EnumTarPathMode
from .ThaniyaTar import ThaniyaTar





class ThaniyaTask_BackupDir(AbstractThaniyaTask):

	@checkFunctionSignature()
	def __init__(self, sourceDirPath:str):
		assert sourceDirPath
		if not os.path.isdir(sourceDirPath):
			raise Exception("No such directory: " + sourceDirPath)
		if not os.path.isabs(sourceDirPath):
			raise Exception("Not an absolute path: " + sourceDirPath)

		self.__sourceDirPath = sourceDirPath

		self.__targetFileName = sourceDirPath.replace("/", "-") + ".tar"
		if self.__targetFileName.startswith("-"):
			self.__targetFileName = self.__targetFileName[1:]
	#

	@property
	def logMessageCalculateSpaceRequired(self) -> str:
		return "Calculating backup size of directory: " + repr(self.__sourceDirPath)
	#

	@checkFunctionSignature()
	def calculateSpaceRequired(self, ctx:ThaniyaBackupContext) -> int:
		nErrors, nSize = ThaniyaTar.tarCalculateSize(
			ctx=ctx,
			walker=jk_pathpatternmatcher2.walk(self.__sourceDirPath)
			)

		ctx.log.info("I/O expected: " + jk_utils.formatBytes(nSize))

		return nSize
	#

	@property
	def logMessagePerformBackup(self) -> str:
		return "Performing backup of directory: " + repr(self.__sourceDirPath)
	#

	@checkFunctionSignature()
	def performBackup(self, ctx:ThaniyaBackupContext):
		ThaniyaTar.tar(
			ctx=ctx,
			outputTarFilePath=ctx.absPath(self.__targetFileName),
			walker=jk_pathpatternmatcher2.walk(self.__sourceDirPath),
			pathMode = EnumTarPathMode.RELATIVE_PATH_WITH_BASE_DIR
			)

		ctx.log.info("Backup performed.")
	#

#














