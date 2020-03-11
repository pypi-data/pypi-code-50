


from .AbstractTargetDirectoryStrategy import AbstractTargetDirectoryStrategy




class TargetDirectoryStrategy_StaticDir(AbstractTargetDirectoryStrategy):

	def __init__(self, extraSubDirPath:str = None):
		if extraSubDirPath is not None:
			assert isinstance(extraSubDirPath, str)
			assert extraSubDirPath
			assert extraSubDirPath[0] != "/"
		self.__extraSubDirPath = extraSubDirPath
	#

	def selectEffectiveTargetDirectory(self, baseTargetDirPath:str):
		assert isinstance(baseTargetDirPath, str)

		if self.__extraSubDirPath is not None:
			baseTargetDirPath += "/" + self.__extraSubDirPath

		return baseTargetDirPath
	#

#

