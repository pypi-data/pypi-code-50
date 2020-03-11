




import os
import re






class PathPatternMatcher(object):

	def __init__(self, orgPattern:str, bAbsolute:bool, sRegex:str):
		self.__orgPattern = orgPattern
		self.__bAbsolute = bAbsolute
		self.__sRegex = sRegex
		self.__r = re.compile(sRegex)
	#

	@property
	def regexPattern(self) -> str:
		return self.__sRegex
	#

	def match(self, fullPath:str, relPath:str) -> bool:
		if self.__bAbsolute:
			s = fullPath
		else:
			s = relPath
		ret = self.__r.match(s) is not None
		# print("-- check:", repr(self.__orgPattern), repr(self.__sRegex), repr(s), repr(fullPath), repr(relPath), "=>", ("true" if ret else "false"))
		return ret
	#

	def __str__(self):
		return "<PathPatternMatcher(" + repr(self.__orgPattern) + ")>"
	#

	def __repr__(self):
		return "<PathPatternMatcher(" + repr(self.__orgPattern) + ")>"
	#

#










