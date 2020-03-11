

import time
import datetime
import typing

import jk_utils
import jk_logging
from jk_typing import checkFunctionSignature


from .ThaniyaBackupContext import ThaniyaBackupContext




"""
def thaniya_context(description):
	def thaniya_context2(func):
		def wrapped(*wargs, **kwargs):
			print(func)
			print(func.__annotations__)
			kwargs["c"] = "cc"
			return 'I got a wrapped up {} for you'.format(str(func(*wargs, **kwargs)))
		return wrapped
	return thaniya_context2
#
"""




"""
class MeasureDuration(object):

	def __init__(self, taskName:str, log:jk_logging.AbstractLogger):
		self.__taskName = taskName
		self.__log = log

		self.__t0 = None
	#

	def __enter__(self):
		self.__t0 = time.time()
		d0 = datetime.datetime.fromtimestamp(self.__t0)
		self.__log.info("Starting " + self.__taskName + " at: " + str(d0) + " (" + str(int(self.__t0)) + ")")
	#

	def __exit__(self, etype, ee, traceback):
		t1 = time.time()
		d1 = datetime.datetime.fromtimestamp(t1)
		self.__log.info("Terminating " + self.__taskName + " at: " + str(d1) + " (" + str(int(t1)) + ")")

		fDurationSeconds = t1 - self.__t0
		self.__log.info("Time spent on " + self.__taskName + ": " + jk_utils.formatTime(fDurationSeconds))
	#

#
"""




class ProcessingFallThroughError(Exception):

	pass

#




class ProcessingContext(object):

	#
	# @param	str name						The text to write to the log on descend.
	# @param	str targetDirPath				The destination directory to write files to. This argument is <c>None</c> if a specific
	#											section of activities (wrapped by this context) should not perform any writing.
	# @param	jk_logging.AbstractLogger log	The logger to use for writing log messages.
	# @param	bool bMeasureDuration			If <c>True</c> after completing this context time measurement information is written to the log.
	#
	@checkFunctionSignature()
	def __init__(self, text:str, targetDirPath:typing.Union[str,None], log:jk_logging.AbstractLogger, bMeasureDuration:bool = True,
		statsContainer:dict = None, statsDurationKey:str = None):

		self.__text = text
		self.__targetDirPath = targetDirPath
		self.__log = log
		self.__bMeasureDuration = bMeasureDuration
		self.__statsContainer = statsContainer
		self.__statsDurationKey = statsDurationKey

		self.__t0 = None
		self.__t1 = None
		self.__nestedLog = None
	#

	@property
	def log(self):
		return self.__nestedLog
	#

	@property
	def duration(self) -> float:
		if self.__t0 is None:
			return -1
		else:
			if self.__t1 is None:
				return time.time() - self.__t0
			else:
				return self.__t1 - self.__t0
	#

	def __enter__(self):
		self.__nestedLog = self.__log.descend(self.__text)

		self.__t0 = time.time()
		# d0 = datetime.datetime.fromtimestamp(self.__t0)
		# self.__nestedLog.info("Starting this activity at: " + str(d0) + " (" + str(int(self.__t0)) + ")")

		return ThaniyaBackupContext(self.__targetDirPath, self.__nestedLog, self)
	#

	def __exit__(self, etype, ee, traceback):
		self.__t1 = time.time()
		#d1 = datetime.datetime.fromtimestamp(t1)
		fDurationSeconds = self.__t1 - self.__t0

		# NOTE: we skip fall through errors as they already have been logged

		#if ee and (ee is not jk_logging.AbstractLogger._EINSTANCE):
		if ee and not isinstance(ee, ProcessingFallThroughError) and not ee.__class__.__name__.endswith("_ExceptionInChildContextException"):
			self.__nestedLog.error(ee)

		if self.__bMeasureDuration:
			if ee:
				#self.__nestedLog.error("Terminating with error at: " + str(d1) + " (" + str(int(t1)) + ")")
				#self.__nestedLog.error("Time spent: " + jk_utils.formatTime(fDurationSeconds))
				self.__nestedLog.notice("Terminating with error after time spent: " + jk_utils.formatTime(fDurationSeconds))
			else:
				#self.__nestedLog.success("Terminating without error at: " + str(d1) + " (" + str(int(t1)) + ")")
				#self.__nestedLog.success("Time spent: " + jk_utils.formatTime(fDurationSeconds))
				self.__nestedLog.notice("Terminating with success after time spent: " + jk_utils.formatTime(fDurationSeconds))

		if self.__bMeasureDuration:
			if not ee:
				if (self.__statsContainer is not None) and self.__statsDurationKey:
					self.__statsContainer[self.__statsDurationKey] = fDurationSeconds

		if ee and not isinstance(ee, ProcessingFallThroughError) and not ee.__class__.__name__.endswith("_ExceptionInChildContextException"):
			raise ProcessingFallThroughError()
	#

#








