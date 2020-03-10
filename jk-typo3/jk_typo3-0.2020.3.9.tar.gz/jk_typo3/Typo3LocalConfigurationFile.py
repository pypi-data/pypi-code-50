

import os
import codecs
import re
import shutil


import jk_console

from .Typo3ConfigurationFileParser import Typo3ConfigurationFileParser






#
# This class represents the "LocalConfiguration.php" file in a Typo3 installation.
#
# During loading the file data is parsed. Internally a line is stored in an array. Each array entry is a 3-tuple containing the following data:
# 0) An identifier specifying the type of the line: "-", "varappend", "var", "vari" and "varii"
# 1) The raw text of the line
# 2) An instance of <c>MediaWikiLocalSettingsValue</c> representing the parsed version of the line or <c>None</c> otherwise
#
class Typo3LocalConfigurationFile(object):



	# ================================================================================================================================
	# ==== Constructor Methods



	#
	# Constructor method.
	#
	def __init__(self):
		self.__data = None
		self.__filePath = None
	#



	# ================================================================================================================================
	# ==== Properties



	@property
	def isLoaded(self):
		return self.__data != None
	#



	@property
	def data(self) -> dict:
		return self.__data
	#



	# ================================================================================================================================
	# ==== Methods



	"""
	#
	# For debugging purposes only: Write the internal state of this object to STDOUT.
	#
	def dump(self, onlyLineNumbers:list = None):
		if onlyLineNumbers is not None:
			assert isinstance(onlyLineNumbers, (set, tuple, list))
			onlyLineNumbers = set(onlyLineNumbers)

		print("Typo3LocalConfigurationFile")
		print("\t__bChanged: " + str(self.__changedFlag))
		print("\t__filePath: " + str(self.__filePath))

		if self.__data != None:
			table = jk_console.SimpleTable()

			if onlyLineNumbers:
				bFirst = True
				bLastWasPoints = False
				for (b, data) in self.__data:
					if data.lineNo in onlyLineNumbers:
						if bFirst:
							bFirst = False
							if data.lineNo > 1:
								table.addRow("...", "...", "...")
						table.addRow(str(b), Typo3LocalConfigurationFile.__getType(data), str(data))
						bLastWasPoints = False
					else:
						if not bLastWasPoints:
							table.addRow("...", "...", "...")
							bLastWasPoints = True
						bFirst = False
			else:
				for (b, data) in self.__data:
					table.addRow(str(b), Typo3LocalConfigurationFile.__getType(data), str(data))
			print("\t__lines:")
			table.print(prefix="\t\t")
	#
	"""



	#
	# Load a LocalConfiguration.php file.
	#
	# @param	str dirPath			The MediaWiki installation directory path.
	# @param	str filePath		The file path of the MediaWiki "LocalConfiguration.php" file.
	# @param	str rawText			The raw file content of a "LocalConfiguration.php" file.
	#
	def load(self, dirPath = None, filePath = None, rawText:str = None) -> dict:
		if rawText is not None:
			assert isinstance(rawText, str)
			filePath = None
		elif filePath is not None:
			assert isinstance(filePath, str)
			with codecs.open(filePath, "r", "utf-8") as f:
				rawText = f.read()
		elif dirPath is not None:
			assert isinstance(dirPath, str)
			filePath = os.path.join(dirPath, "public/typo3conf/LocalConfiguration.php")
			with codecs.open(filePath, "r", "utf-8") as f:
				rawText = f.read()
		else:
			raise Exception("At least one of the following arguments must be specified: 'dirPath', 'filePath' or 'rawText'!")

		self.__data = Typo3ConfigurationFileParser().parseText(rawText)
		assert isinstance(self.__data, dict)

		self.__filePath = filePath

		return self.__data
	#



	# ================================================================================================================================
	# ==== Static Methods



	@staticmethod
	def __getType(something):
		tName = something.__class__.__name__
		return tName
	#



#













