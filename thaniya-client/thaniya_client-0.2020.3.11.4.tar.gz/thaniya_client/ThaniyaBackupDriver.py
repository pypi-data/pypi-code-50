

import os
import typing
import time
import datetime
import json
import sys
import shutil

import jk_utils
import jk_logging
#from jk_testing import Assert
import jk_json
from jk_typing import checkFunctionSignature

from .constants import *
from .TargetDirectoryStrategy_StaticDir import TargetDirectoryStrategy_StaticDir
from .AbstractBackupConnector import AbstractBackupConnector
from .ThaniyaBackupContext import ThaniyaBackupContext
from .AbstractThaniyaTask import AbstractThaniyaTask
from .ThaniyaIO import ThaniyaIO
from .ProcessingContext import ProcessingContext, ProcessingFallThroughError
from .AbstractTargetDirectoryStrategy import AbstractTargetDirectoryStrategy






class ThaniyaBackupDriver(object):

	# ================================================================================================================================
	# ==== Constructor/Destructor
	# ================================================================================================================================

	#
	# Constructor method.
	#
	# @param	AbstractBackupConnector backupConnector				An object that is used to connect to a backup repository/backup server later.
	# @param	dict backupConnectorParameters						A dictionary that holds various parameters required to connect to the backup repository/backup server.
	# @param	str mountDirPath									The local mount point to mount the remote directory at. 
	# @param	AbstractTargetDirectoryStrategy targetDirStrategy	A strategy that decides about which target directory to use exactly.
	#
	@checkFunctionSignature()
	def __init__(self,
		backupConnector:AbstractBackupConnector,
		backupConnectorParameters:dict,
		mountDirPath:str,
		targetDirStrategy:typing.Union[AbstractTargetDirectoryStrategy,None] = None,
		):

		# verify arguments

		if not os.path.isdir(mountDirPath):
			raise Exception("Not a directory: " + repr(mountDirPath))
		if not os.path.isabs(mountDirPath):
			raise Exception("Not an absolute path: " + repr(mountDirPath))
		if mountDirPath == "/":
			raise Exception("Unsuitable path: " + repr(mountDirPath))
		if targetDirStrategy is None:
			targetDirStrategy = TargetDirectoryStrategy_StaticDir()

		# accept arguments

		if mountDirPath.endswith("/"):
			mountDirPath = mountDirPath[:-1]
		self.__mountDirPath = mountDirPath
		self.__mountDirPath2 = mountDirPath + "/"
		self.__backupConnector = backupConnector
		self.__backupConnectorParameters = backupConnectorParameters
		self.__targetDirStrategy = targetDirStrategy

		if backupConnector.needsToBeRoot:
			if os.geteuid() != 0:
				raise Exception("Need to be root to use backup connector " + repr(backupConnector.__class__.__name__) + "!")
	#

	# ================================================================================================================================
	# ==== Helper Methods
	# ================================================================================================================================

	@checkFunctionSignature()
	def __getDirTreeSize(self, dirPath:str, log:jk_logging.AbstractLogger) -> int:
		assert dirPath
		assert os.path.isabs(dirPath)
		assert os.path.isdir(dirPath)

		nestedLog = log.descend("Calculating size of directory: " + repr(dirPath))

		try:
			n = jk_utils.fsutils.getFolderSize(dirPath)

		except Exception as ee:
			nestedLog.exception(ee)
			raise

		nestedLog.notice("Size of " + repr(dirPath) + ": " + jk_utils.formatBytes(n))

		return n
	#

	@checkFunctionSignature()
	def __getBufferLogger(self, log:jk_logging.MulticastLogger) -> jk_logging.BufferLogger:
		for logger in log.loggers:
			if isinstance(logger, jk_logging.BufferLogger):
				return logger

		raise Exception("No buffer logger found in list of loggers!")
	#

	@checkFunctionSignature()
	def __writeLogToFiles(
		self,
		bufferLogger:jk_logging.BufferLogger,
		textFilePath:str,
		jsonFilePath:str,
		fileMode:typing.Union[int,str,jk_utils.ChModValue,None] = None,
		):

		bAppendToExistingFile = False
		logMsgFormatter = None

		jsonLogData = bufferLogger.getDataAsPrettyJSON()

		with open(jsonFilePath, "w") as f:
			json.dump(jsonLogData, f, indent="\t")

		fileLogger = jk_logging.FileLogger.create(
			textFilePath,
			"none",
			bAppendToExistingFile,
			False,
			fileMode,
			logMsgFormatter,

		)
		bufferLogger.forwardTo(fileLogger)
	#

	@checkFunctionSignature()
	def __analyseLogMessages(self, log:jk_logging.MulticastLogger) -> jk_logging.DetectionLogger:
		for logger in log.loggers:
			if isinstance(logger, jk_logging.BufferLogger):
				detectionLogger = jk_logging.DetectionLogger.create(jk_logging.NullLogger.create())
				logger.forwardTo(detectionLogger)
				return detectionLogger

		raise Exception("No buffer logger in list of loggers!")
	#

	# ================================================================================================================================
	# ==== Public Methods
	# ================================================================================================================================

	#
	# Invoke this method to perform a backup.
	#
	@checkFunctionSignature()
	def performBackup(self,
		backupTasks:list,
		bSimulate:bool
		):

		for x in backupTasks:
			assert isinstance(x, AbstractThaniyaTask)
			#Assert.isInstance(x, AbstractThaniyaTask)

		mainLog = jk_logging.MulticastLogger.create(
			jk_logging.ConsoleLogger.create(logMsgFormatter=jk_logging.COLOR_LOG_MESSAGE_FORMATTER),
			jk_logging.BufferLogger.create()
		)

		bError = False
		try:

			statsContainer = {
				"tStart": time.time(),
				"tEnd": None,
				"success": None,
				"expectedBytesToWrite": None,
				"totalBytesWritten": None,
				"avgWritingSpeed": None,
				"simulate": bSimulate,
			}

			effectiveTargetDirPath = None

			with ProcessingContext("Performing backup simulation" if bSimulate else "Performing backup", None, mainLog) as ctxMain:

				# --------------------------------------------------------------------------------------------------------------------------------
				# >>>> estimate the number of bytes we will likely have to write for this backup

				with ProcessingContext(
					text="Calculating disk space required",
					targetDirPath=None,
					log=ctxMain.log,
					bMeasureDuration=True,
					statsContainer=statsContainer,
					statsDurationKey="d0_calcDiskSpace"
				) as ctx:

					nExpectedBytesToWrite = 0
					for job in backupTasks:
						assert isinstance(job, AbstractThaniyaTask)
						#Assert.isInstance(job, AbstractThaniyaTask)

						nestedCtx = ctx.descend(job.logMessageCalculateSpaceRequired)
						with nestedCtx.log as nestedLog:
							nExpectedBytesToWrite += job.calculateSpaceRequired(nestedCtx)

					ctx.log.info("Estimated total size of backup: " + jk_utils.formatBytes(nExpectedBytesToWrite))

					statsContainer["expectedBytesToWrite"] = nExpectedBytesToWrite

				# --------------------------------------------------------------------------------------------------------------------------------
				# >>>> now connect to the backup repository

				with ProcessingContext(
					text="Connecting to backup repository and preparing backup",
					targetDirPath=None,
					log=ctxMain.log,
					bMeasureDuration=True,
					statsContainer=statsContainer,
					statsDurationKey="d1_connectAndPrepare"
				) as ctx:
					# check if there is a suitable directory where we can mount the remote file system

					ThaniyaIO.checkThatDirExists(ctx, self.__mountDirPath)
					ThaniyaIO.ensureDirMode(ctx, self.__mountDirPath, jk_utils.ChModValue("rwx------"))

					# mount the remote file system

					self.__backupConnector.initialize(ctx, self.__mountDirPath, nExpectedBytesToWrite, self.__backupConnectorParameters)

					if not self.__backupConnector.isReady:
						raise Exception("Backup client unexpectedly not ready for writing!")

					# select the target directory where we will store the data. the variable "effectiveTargetDirPath"
					# will receive the directory selected by the target directory strategy. we will write data there.

					effectiveTargetDirPath = self.__targetDirStrategy.selectEffectiveTargetDirectory(self.__mountDirPath)
					ctx.log.info("Selected target directory: " + repr(effectiveTargetDirPath))
					
					# verify that we have the correct directory: the "effectiveTargetDirPath" must be lokated somewhere within
					# the mounted directory tree.

					if effectiveTargetDirPath.endswith("/"):
						effectiveTargetDirPath2 = effectiveTargetDirPath
					else:
						effectiveTargetDirPath2 = effectiveTargetDirPath + "/"
					assert effectiveTargetDirPath2[:len(self.__mountDirPath2)] == self.__mountDirPath2

					ctx.log.notice("Creating subdirectories if necessary ...")
					ThaniyaIO.ensureDirExists(ctx, effectiveTargetDirPath, jk_utils.ChModValue("rwx------"))

					# check that the target directory fits our requirements: it must be empty.

					bIsEmpty, contentEntries = ThaniyaIO.checkIfDirIsEmpty(ctx, effectiveTargetDirPath)
					if not bIsEmpty:
						print(contentEntries)
						if STATS_JSON_FILE_NAME in contentEntries:
							# target directory already seems to contain a backup 
							ctx.log.warn("Target directory already seems to contain a backup: " + effectiveTargetDirPath2)
							ctx.log.warn("Overwriting this backup.")
						else:
							raise Exception("Backup directory contains various non-backup files or directories!")

					# now we are ready. but before we begin doing something let's write the backup stats first.

					jk_json.saveToFilePretty(statsContainer, os.path.join(effectiveTargetDirPath, STATS_JSON_FILE_NAME))

					# ----

					ctx.log.notice("Done.")

				# --------------------------------------------------------------------------------------------------------------------------------
				# >>>> Writing the backup data

				if not bSimulate:
					with ProcessingContext(
						text="Writing the backup data",
						targetDirPath=effectiveTargetDirPath,
						log=ctxMain.log,
						bMeasureDuration=True,
						statsContainer=statsContainer,
						statsDurationKey="d2_backup"
					) as ctx:

						for job in backupTasks:
							assert isinstance(job, AbstractThaniyaTask)
							#Assert.isInstance(job, AbstractThaniyaTask)

							nestedCtx = ctx.descend(job.logMessagePerformBackup)
							with nestedCtx.log as nestedLog:
								job.performBackup(nestedCtx)

						nTotalBytesWritten = self.__getDirTreeSize(effectiveTargetDirPath, ctx.log)
						fDuration = ctx.duration
						if (nTotalBytesWritten > 0) and (fDuration > 0):
							fAvgWritingSpeed = nTotalBytesWritten/fDuration
							sAvgWritingSpeed = jk_utils.formatBytesPerSecond(fAvgWritingSpeed)
						else:
							fAvgWritingSpeed = None
							sAvgWritingSpeed = "n/a"

						ctx.log.info("Total bytes written: " + jk_utils.formatBytes(nTotalBytesWritten))
						ctx.log.info("Average writing speed: " + sAvgWritingSpeed)

						statsContainer["totalBytesWritten"] = nTotalBytesWritten
						statsContainer["avgWritingSpeed"] = fAvgWritingSpeed

		except ProcessingFallThroughError as ee:
			bError = True
		except Exception as ee:
			bError = True
			mainLog.error(ee)

		# --------------------------------------------------------------------------------------------------------------------------------
		# >>>> Finish

		try:
			# detecting errors

			detectionLogger = self.__analyseLogMessages(mainLog)
			if detectionLogger.hasError() or detectionLogger.hasStdErr() or detectionLogger.hasException():
				bError = True

			# writing final status log message

			if bError:
				mainLog.error("Backup terminated erroneously.")
			else:
				mainLog.success("Backup successfully completed.")

			if effectiveTargetDirPath is not None:
				# let's try to write the backup stats before termination.

				statsContainer["tEnd"] = time.time()
				statsContainer["success"] = not bError

				jk_json.saveToFilePretty(statsContainer, os.path.join(effectiveTargetDirPath, STATS_JSON_FILE_NAME))

				# let's try to write the backup log before termination.

				bufferLogger = self.__getBufferLogger(mainLog)
				self.__writeLogToFiles(
					bufferLogger,
					os.path.join(effectiveTargetDirPath, PLAINTEXT_LOG_FILE_NAME),
					os.path.join(effectiveTargetDirPath, JSON_LOG_FILE_NAME)
				)

		except ProcessingFallThroughError as ee:
			bError = True
		except Exception as ee:
			bError = True
			mainLog.error(ee)

		# terminate connection

		try:
			with ProcessingContext("Terminating connection", None, mainLog) as ctxMain:
				self.__backupConnector.deinitialize(ctx, bError, statsContainer)

		except ProcessingFallThroughError as ee:
			bError = True
		except Exception as ee:
			bError = True
			mainLog.error(ee)
	#

	#
	# Perform a test of the connector.
	#
	@checkFunctionSignature()
	def testConnector(self):

		mainLog = jk_logging.MulticastLogger.create(
			jk_logging.ConsoleLogger.create(logMsgFormatter=jk_logging.COLOR_LOG_MESSAGE_FORMATTER),
			jk_logging.BufferLogger.create()
		)

		N_EXPECTED_BYTES_TO_WRITE = 1000

		bError = False
		try:

			statsContainer = {
				"tStart": time.time(),
				"tEnd": None,
				"success": None,
				"expectedBytesToWrite": None,
				"totalBytesWritten": None,
				"avgWritingSpeed": None,
				"simulate": True,
			}

			effectiveTargetDirPath = None

			with ProcessingContext("Performing connector test", None, mainLog) as ctxMain:

				# --------------------------------------------------------------------------------------------------------------------------------
				# >>>> connect to the backup repository

				with ProcessingContext(
					text="Connecting to backup repository and preparing backup",
					targetDirPath=None,
					log=ctxMain.log,
					bMeasureDuration=True,
					statsContainer=statsContainer,
					statsDurationKey="d1_connectAndPrepare"
				) as ctx:
					# check if there is a suitable directory where we can mount the remote file system

					ThaniyaIO.checkThatDirExists(ctx, self.__mountDirPath)
					ThaniyaIO.ensureDirMode(ctx, self.__mountDirPath, jk_utils.ChModValue("rwx------"))

					# mount the remote file system

					self.__backupConnector.initialize(ctx, self.__mountDirPath, N_EXPECTED_BYTES_TO_WRITE, self.__backupConnectorParameters)

					if not self.__backupConnector.isReady:
						raise Exception("Backup client unexpectedly not ready for writing!")

					# select the target directory where we will store the data. the variable "effectiveTargetDirPath"
					# will receive the directory selected by the target directory strategy. we will write data there.

					effectiveTargetDirPath = self.__targetDirStrategy.selectEffectiveTargetDirectory(self.__mountDirPath)
					ctx.log.info("Selected target directory: " + repr(effectiveTargetDirPath))
					
					# verify that we have the correct directory: the "effectiveTargetDirPath" must be lokated somewhere within
					# the mounted directory tree.

					if effectiveTargetDirPath.endswith("/"):
						effectiveTargetDirPath2 = effectiveTargetDirPath
					else:
						effectiveTargetDirPath2 = effectiveTargetDirPath + "/"
					assert effectiveTargetDirPath2[:len(self.__mountDirPath2)] == self.__mountDirPath2

					ctx.log.notice("Creating subdirectories if necessary ...")
					ThaniyaIO.ensureDirExists(ctx, effectiveTargetDirPath, jk_utils.ChModValue("rwx------"))

					# check that the target directory fits our requirements: it must be empty.

					bIsEmpty, contentEntries = ThaniyaIO.checkIfDirIsEmpty(ctx, effectiveTargetDirPath)
					if not bIsEmpty:
						if STATS_JSON_FILE_NAME in contentEntries:
							# target directory already seems to contain a backup 
							ctx.log.info("Directory already seems to contain a backup: " + effectiveTargetDirPath2)
						else:
							raise Exception("Backup directory contains various non-backup files or directories!")

					# now we are ready. but before we begin doing something let's write the backup stats first.

					jk_json.saveToFilePretty(statsContainer, os.path.join(effectiveTargetDirPath, STATS_JSON_FILE_NAME))

					# ----

					ctx.log.notice("Done.")

				# --------------------------------------------------------------------------------------------------------------------------------

		except ProcessingFallThroughError as ee:
			bError = True
		except Exception as ee:
			bError = True
			if not ee.__class__.__name__.endswith("_ExceptionInChildContextException"):
				mainLog.error(ee)

		# --------------------------------------------------------------------------------------------------------------------------------
		# >>>> Finish

		try:
			# detecting errors

			detectionLogger = self.__analyseLogMessages(mainLog)
			if detectionLogger.hasError() or detectionLogger.hasStdErr() or detectionLogger.hasException():
				bError = True

			# writing final status log message

			if bError:
				mainLog.error("Backup terminated erroneously.")
			else:
				mainLog.success("Backup successfully completed.")

			if effectiveTargetDirPath is not None:
				# let's try to write the backup stats before termination.

				statsContainer["tEnd"] = time.time()
				statsContainer["success"] = not bError

				jk_json.saveToFilePretty(statsContainer, os.path.join(effectiveTargetDirPath, STATS_JSON_FILE_NAME))

				# write log

				bufferLogger = self.__getBufferLogger(mainLog)
				self.__writeLogToFiles(
					bufferLogger,
					os.path.join(effectiveTargetDirPath, PLAINTEXT_LOG_FILE_NAME),
					os.path.join(effectiveTargetDirPath, JSON_LOG_FILE_NAME)
				)

		except ProcessingFallThroughError as ee:
			bError = True
		except Exception as ee:
			bError = True
			mainLog.error(ee)

		# terminate connection

		try:
			with ProcessingContext("Terminating connection", None, mainLog) as ctxMain:
				self.__backupConnector.deinitialize(ctx, bError, statsContainer)

		except ProcessingFallThroughError as ee:
			bError = True
		except Exception as ee:
			bError = True
			mainLog.error(ee)
	#

#


















