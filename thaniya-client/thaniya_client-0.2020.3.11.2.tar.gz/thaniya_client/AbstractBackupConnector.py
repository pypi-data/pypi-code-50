

import typing
import string
import random
import os

import jk_utils


from .ThaniyaBackupContext import ThaniyaBackupContext




#
# This class represents a channel to a backup repository. Typically this is a client for a backup server.
# The regular way how this class is used is following this work flow:
# * instantiate a subclass of this class and pass it on to the backup driver;
# * the backup driver invokes `initialize()`; this method should connect to a backup server and prepare everything for backup
# * the backup is performed by writing to the directory returned by `targetDirPath`;
# * the backup driver invokes `deinitialize()` in order to tear down the connection;
#
class AbstractBackupConnector(object):

	@property
	def needsToBeRoot(self) -> bool:
		return False
	#

	def initialize(self, ctx:ThaniyaBackupContext, targetDirPath:str, nExpectedNumberOfBytesToWrite:int, parameters:dict):
		raise NotImplementedError()
	#

	def deinitialize(self, ctx:ThaniyaBackupContext, bError:bool, statsContainer:dict):
		raise NotImplementedError()
	#

	@property
	def isReady(self) -> bool:
		raise NotImplementedError()
	#

	@property
	def targetDirPath(self) -> str:
		raise NotImplementedError()
	#

	def dump(self):
		raise NotImplementedError()
	#

#













