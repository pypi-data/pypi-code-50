
import os
import signal
import subprocess

import jk_pathpatternmatcher2
import jk_utils
import jk_typo3
from jk_typing import checkFunctionSignature

from .AbstractThaniyaTask import AbstractThaniyaTask
from .ThaniyaBackupContext import ThaniyaBackupContext
from .EnumTarPathMode import EnumTarPathMode
from .ThaniyaTar import ThaniyaTar
from .ThaniyaMySQL import ThaniyaMySQL




#
# This backup task addresses local Typo3 installations.
#
class ThaniyaTask_BackupTypo3(AbstractThaniyaTask):

	#
	# Configuration parameters:
	#
	# @param	str mediaWikiDirPath		(required) The absolute directory path where the Typo3 installation can be found.
	#										The final directory name in the path must be the same as the site name of the Wiki.
	#										Additionally there must be a cron script named "<sitename>cron.sh".
	# @param	str userName				(required) The name of the user account under which NGINX, PHP and the Wiki cron process are executed.
	#
	@checkFunctionSignature()
	def __init__(self,
		typo3DirPath:str,
		):

		self.__typo3Helper = jk_typo3.Typo3InstallationMgr(typo3DirPath)

		self.__ignoreDirPathPatterns = None
	#

	def __getMySQLDBParameters(self) -> dict:
		typo3Settings = self.__typo3Helper.getLocalSettings()
		dbSettings = typo3Settings["DB"]["Connections"]["Default"]
		assert dbSettings["driver"] == "mysqli"

		return dbSettings["host"], dbSettings["port"], dbSettings["dbname"], dbSettings["user"], dbSettings["password"]
	#

	@property
	def logMessageCalculateSpaceRequired(self) -> str:
		return "Calculating backup size of Typo3 installation: " + repr(self.__typo3Helper.getSiteName())
	#

	def calculateSpaceRequired(self, ctx:ThaniyaBackupContext) -> int:
		# process root directory

		nErrorsWikiRoot, nSizeTypo3Root = ThaniyaTar.tarCalculateSize(
			ctx,
			jk_pathpatternmatcher2.walk(
				self.__typo3Helper.typo3BaseDirPath,
				ignoreDirPathPatterns = self.__ignoreDirPathPatterns
			)
		)
		ctx.log.info("I/O expected for the local installation: " + jk_utils.formatBytes(nSizeTypo3Root))

		# process database directory

		dbHost, dbPort, dbName, dbUser, dbPwd = self.__getMySQLDBParameters()
		assert dbHost in [ "127.0.0.1", "localhost" ]
		assert dbPort == 3306

		nSizeDB = ThaniyaMySQL.mySQLDumpCalculateSize(
			ctx=ctx,
			dbName=dbName,
			dbUserName=dbUser,
			dbPassword=dbPwd,
			)

		ctx.log.info("I/O expected for the database: " + jk_utils.formatBytes(nSizeDB))

		return nSizeTypo3Root + nSizeDB
	#

	@property
	def logMessagePerformBackup(self) -> str:
		return "Performing backup of Typo3 installation: " + repr(self.__typo3Helper.getSiteName())
	#

	def performBackup(self, ctx:ThaniyaBackupContext):
		siteName = self.__typo3Helper.getSiteName()

		# process root directory

		ThaniyaTar.tar(
			ctx=ctx,
			outputTarFilePath=ctx.absPath(siteName + "-typo3.tar"),
			walker=jk_pathpatternmatcher2.walk(
				self.__typo3Helper.typo3BaseDirPath,
				ignoreDirPathPatterns = self.__ignoreDirPathPatterns
			),
			pathMode=EnumTarPathMode.RELATIVE_PATH_WITH_BASE_DIR,
		)

		# process database directory

		dbHost, dbPort, dbName, dbUser, dbPwd = self.__getMySQLDBParameters()
		assert dbHost in [ "127.0.0.1", "localhost" ]
		assert dbPort == 3306

		ThaniyaMySQL.mySQLDump(
			ctx=ctx,
			dbName=dbName,
			dbUserName=dbUser,
			dbPassword=dbPwd,
			outputDumpFilePath=ctx.absPath(siteName + "-typo3.sql"),
		)
	#

#









