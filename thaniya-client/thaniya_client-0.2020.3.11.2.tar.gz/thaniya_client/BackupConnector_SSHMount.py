


import time
import os
import subprocess

from jk_testing import Assert
import jk_utils
import jk_mounting

from .AbstractBackupConnector import AbstractBackupConnector
from .ThaniyaIO import ThaniyaIO
from .ThaniyaBackupContext import ThaniyaBackupContext




class BackupConnector_SSHMount(AbstractBackupConnector):

	SSHFS_PATH = "/usr/bin/sshfs"
	SUDO_PATH = "/usr/bin/sudo"
	UMOUNT_PATH = "/bin/umount"

	def __init__(self):
		self.__targetDirPath = None
		self.__bIsMounted = False
	#

	def initialize(self, ctx:ThaniyaBackupContext, targetDirPath:str, nExpectedNumberOfBytesToWrite:int, parameters:dict):
		self.__targetDirPath = targetDirPath

		self._ssh_hostAddress = parameters.get("ssh_hostAddress")
		self._ssh_login = parameters.get("ssh_login")
		self._ssh_password = parameters.get("ssh_password")
		self._ssh_port = parameters.get("ssh_port", 22)
		self._ssh_dirPath = parameters.get("ssh_dirPath")

		self._mountSSH(self.__targetDirPath, self._ssh_hostAddress, self._ssh_port, self._ssh_login, self._ssh_password, self._ssh_dirPath)
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
		print("BackupConnector_SSHMount")
		#for key in [ "_sessionID",
		#	"mountPoint" ]:
		#	print("\t" + key, "=", getattr(self, key))
	#

	def _mountSSH(self, localDirPath:str, sshHostAddress:str, sshPort:int, sshLogin:str, sshPassword:str, sshDirPath:str) -> bool:
		assert isinstance(localDirPath, str)
		assert os.path.isdir(localDirPath)
		localDirPath = os.path.abspath(localDirPath)

		mounter = jk_mounting.Mounter()
		mip = mounter.getMountInfoByMountPoint(localDirPath)
		if mip is not None:
			raise Exception("Directory " + repr(localDirPath) + " already used by mount!")

		cmd = [
			BackupConnector_SSHMount.SSHFS_PATH,
			"-p", str(sshPort), "-o", "password_stdin", "-o", "reconnect", sshLogin + "@" + sshHostAddress + ":" + sshDirPath, localDirPath
		]

		p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		p.stdin.write((sshPassword + "\n").encode("utf-8"))
		(stdout, stderr) = p.communicate(timeout=3)
		if p.returncode != 0:
			returnCode1 = p.returncode
			stdOutData1 = stdout.decode("utf-8")
			stdErrData1 = stderr.decode("utf-8")
			p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			p.stdin.write(("yes\n" + sshPassword + "\n").encode("utf-8"))
			(stdout, stderr) = p.communicate(timeout=3)
			if p.returncode != 0:
				returnCode2 = p.returncode
				stdOutData2 = stdout.decode("utf-8")
				stdErrData2 = stderr.decode("utf-8")
				print("Mount attempt 1:")
				print("\tcmd =", cmd)
				print("\treturnCode =", returnCode1)
				print("\tstdOutData =", repr(stdOutData1))
				print("\tstdErrData =", repr(stdErrData1))
				print("Mount attempt 2:")
				print("\treturnCode =", returnCode2)
				print("\tstdOutData =", repr(stdOutData2))
				print("\tstdErrData =", repr(stdErrData2))
				raise Exception("Failed to mount device!")
				return False
			else:
				return True
		else:
			return True
	#

	def _umount(self, localDirPath:str, throwExceptionOnError:bool = True) -> bool:
		assert isinstance(localDirPath, str)
		assert isinstance(throwExceptionOnError, bool)

		cmd = [
			BackupConnector_SSHMount.SUDO_PATH,
			BackupConnector_SSHMount.UMOUNT_PATH,
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












