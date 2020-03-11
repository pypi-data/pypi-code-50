


import sys
import time
import os
import subprocess
import string
import random

import jk_utils
import jk_mounting

from .AbstractBackupConnector import AbstractBackupConnector
from .ThaniyaIO import ThaniyaIO
from .ThaniyaBackupContext import ThaniyaBackupContext
from .utils.temp import writeTempFile




class BackupConnector_CIFSMount(AbstractBackupConnector):

	SMB_CLIENT_PATH = "/usr/bin/smbclient"
	MOUNT_PATH = "/bin/mount"
	SUDO_PATH = "/usr/bin/sudo"
	UMOUNT_PATH = "/bin/umount"

	def __init__(self):
		self.__targetDirPath = None
		self.__bIsMounted = False
	#

	def initialize(self, ctx:ThaniyaBackupContext, targetDirPath:str, nExpectedNumberOfBytesToWrite:int, parameters:dict):
		self.__targetDirPath = targetDirPath

		self._cifs_hostAddress = parameters.get("cifs_hostAddress")
		self._cifs_login = parameters.get("cifs_login")
		self._cifs_password = parameters.get("cifs_password")
		#self._cifs_port = parameters.get("cifs_port", 445)
		self._cifs_version = parameters.get("cifs_version")
		self._cifs_shareName = parameters.get("cifs_shareName")

		self._mountCIFS(
			self.__targetDirPath,
			self._cifs_hostAddress,
			#self._cifs_port,
			self._cifs_shareName,
			self._cifs_login,
			self._cifs_password,
			self._cifs_version)
		self.__bIsMounted = True
	#

	def deinitialize(self, ctx:ThaniyaBackupContext, bError:bool, statsContainer:dict):
		if self.__bIsMounted:
			# let's do 5 unmount attempts.
			for i in range(0, 4):
				time.sleep(1)
				try:
					self._umount(self.__targetDirPath)
					return
				except Exception as ee:
					pass
			time.sleep(1)
			self._umount(self.__targetDirPath)
	#

	@property
	def isReady(self) -> bool:
		return self.__bIsMounted
	#

	@property
	def targetDirPath(self) -> str:
		return self.__targetDirPath
	#

	def dump(self):
		print("BackupConnector_CIFSMount")
		#for key in [ "_sessionID",
		#	"mountPoint" ]:
		#	print("\t" + key, "=", getattr(self, key))
	#

	def _mountCIFS(self,
		localDirPath:str,
		cifsHostAddress:str,
		#cifsPort:int,
		cifsShareName:str,
		cifsLogin:str,
		cifsPassword:str,
		cifsVersion:str) -> bool:

		assert isinstance(localDirPath, str)
		assert os.path.isdir(localDirPath)
		localDirPath = os.path.abspath(localDirPath)

		mounter = jk_mounting.Mounter()
		mip = mounter.getMountInfoByMountPoint(localDirPath)
		if mip is not None:
			raise Exception("Directory " + repr(localDirPath) + " already used by mount!")

		credentialFilePath = writeTempFile("rw-------",
			"username=" + cifsLogin + "\npassword=" + cifsPassword + "\n"
			)

		try:

			options = [
				"user=",
				cifsLogin,
				",credentials=",
				credentialFilePath,
				",rw",
			]
			if cifsVersion:
				options.append(",vers=")
				options.append(cifsVersion)

			cmd = [
				BackupConnector_CIFSMount.MOUNT_PATH,
				"-t", "cifs",
				"-o", "".join(options),
				"//" + cifsHostAddress + "/" + cifsShareName,
				localDirPath,
			]
			# print(" ".join(cmd))

			p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			p.stdin.write((cifsPassword + "\n").encode("utf-8"))
			(stdout, stderr) = p.communicate(timeout=3)
			if p.returncode != 0:
				returnCode1 = p.returncode
				stdOutData1 = stdout.decode("utf-8")
				stdErrData1 = stderr.decode("utf-8")
				print("Mount attempt 1:")
				print("\tcmd =", cmd)
				print("\treturnCode =", returnCode1)
				print("\tstdOutData =", repr(stdOutData1))
				print("\tstdErrData =", repr(stdErrData1))
				raise Exception("Failed to mount device!")
				return False
			else:
				return True

		finally:
			try:
				os.unlink(credentialFilePath)
			except:
				pass
	#

	def _umount(self, localDirPath:str, throwExceptionOnError:bool = True) -> bool:
		assert isinstance(localDirPath, str)
		assert isinstance(throwExceptionOnError, bool)

		cmd = [
			BackupConnector_CIFSMount.UMOUNT_PATH,
			localDirPath,
		]
		p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		(stdout, stderr) = p.communicate(timeout=10)
		if p.returncode != 0:
			returnCode = p.returncode
			stdOutData = stdout.decode("utf-8")
			stdErrData = stderr.decode("utf-8")
			print("Unmount attempt:")
			print("\treturnCode =", returnCode)
			print("\tstdOutData =", repr(stdOutData))
			print("\tstdErrData =", repr(stdErrData))
			if throwExceptionOnError:
				raise Exception("Failed to umount device!")
			return False
		else:
			return True
	#

#












