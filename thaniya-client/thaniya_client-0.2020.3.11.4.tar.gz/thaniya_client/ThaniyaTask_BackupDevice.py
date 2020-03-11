


import os
import typing

import jk_pathpatternmatcher2
import jk_utils
from jk_typing import checkFunctionSignature
import jk_mounting

from .AbstractThaniyaTask import AbstractThaniyaTask
from .ThaniyaBackupContext import ThaniyaBackupContext

from .EnumTarPathMode import EnumTarPathMode
from .ThaniyaTar import ThaniyaTar
from .ThaniyaIO import ThaniyaIO






class ThaniyaTask_BackupDevice(AbstractThaniyaTask):

	@checkFunctionSignature()
	def __init__(self, devicePath:str, targetFileName:typing.Union[str,None] = None, ensureNotMounted:bool = False):
		assert devicePath
		assert os.path.exists(devicePath)
		assert os.path.isabs(devicePath)
		assert devicePath.startswith("/dev/")

		assert isinstance(ensureNotMounted, bool)
		self.__ensureNotMounted = ensureNotMounted

		if targetFileName is not None:
			assert targetFileName

		self.__devicePath = devicePath

		if targetFileName:
			self.__targetFileName = targetFileName
		else:
			self.__targetFileName = devicePath.replace("/", "-")
			if self.__targetFileName.startswith("-"):
				self.__targetFileName = self.__targetFileName[1:]
			self.__targetFileName = "device--" + self.__targetFileName + ".rawdev"
	#

	@property
	def logMessageCalculateSpaceRequired(self) -> str:
		return "Determining backup size of device: " + repr(self.__devicePath)
	#

	def calculateSpaceRequired(self, ctx:ThaniyaBackupContext) -> int:
		nSize = ThaniyaIO.getSizeOfDevice(ctx, self.__devicePath)
		ctx.log.info("I/O expected: " + jk_utils.formatBytes(nSize))
		return nSize
	#

	@property
	def logMessagePerformBackup(self) -> str:
		return "Performing backup of device: " + repr(self.__devicePath)
	#

	def performBackup(self, ctx:ThaniyaBackupContext):
		if self.__ensureNotMounted:
			mi = jk_mounting.Mounter().getMountInfoByFilePath(self.__devicePath)
			if mi is not None:
				raise Exception("The device is still mounted: " + repr(self.__devicePath))

		ThaniyaIO.copyDevice(
			ctx=ctx,
			sourceDevicePath=self.__devicePath,
			targetFileOrDirectoryPath=ctx.absPath(self.__targetFileName),
			)

		ctx.log.info("Backup performed.")
	#

#














