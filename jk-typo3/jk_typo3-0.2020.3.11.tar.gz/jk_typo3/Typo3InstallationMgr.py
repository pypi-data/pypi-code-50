

import os
import signal
import subprocess
import typing
import json

import jk_utils
from jk_typing import *
import jk_version



from .Typo3LocalConfigurationFile import Typo3LocalConfigurationFile




#
# This class helps dealing with Typo3 installations running on a system.
#
class Typo3InstallationMgr(object):

	#
	# Configuration parameters:
	#
	# @param	str typo3DirPath			(required) The absolute directory path where the Typo3 installation can be found.
	#										The final directory name in the path must be the same as the site name of the Wiki.
	#										Additionally there must be a cron script named "<sitename>cron.sh".
	# @param	str userName				(required) The name of the user account under which NGINX, PHP and the Wiki cron process are executed.
	#
	@checkFunctionSignature()
	def __init__(self,
		typo3DirPath:str,
		):

		# check Typo3 installation directory and load settings

		assert isinstance(typo3DirPath, str)
		assert typo3DirPath
		assert os.path.isdir(typo3DirPath)
		assert os.path.isabs(typo3DirPath)

		assert os.path.isdir(os.path.join(typo3DirPath, "public"))
		assert os.path.isdir(os.path.join(typo3DirPath, "var"))
		assert os.path.isfile(os.path.join(typo3DirPath, "public", "typo3conf", "LocalConfiguration.php"))

		self.__composerFilePath = os.path.join(typo3DirPath, "composer.json")
		assert os.path.isfile(self.__composerFilePath)

		self.__typo3DirPath = typo3DirPath

		self.__typo3LocalSettingsFile = None
	#

	#
	# The parent directory of the media wiki installation
	#
	@property
	def typo3BaseDirPath(self) -> str:
		return self.__typo3DirPath
	#

	def getVersion(self) -> jk_version.Version:
		with open(self.__composerFilePath, "r") as f:
			jComposer = json.load(f)
		sVersion = jComposer["require"]["typo3/cms-core"]
		assert sVersion[0] == "~"
		return jk_version.Version(sVersion[1:])
	#

	def getSiteName(self) -> str:
		s = self.getLocalSettings()
		return s["SYS"]["sitename"]
	#

	def getLocalSettings(self) -> dict:
		if self.__typo3LocalSettingsFile is None:
			self.__typo3LocalSettingsFile = Typo3LocalConfigurationFile()
			self.__typo3LocalSettingsFile.load(dirPath = self.__typo3DirPath)

		return self.__typo3LocalSettingsFile.data
	#

#




