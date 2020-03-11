




import os
import re






class PathPatternMatcherCollection(list):

	def match(self, fullPath:str, relPath:str) -> bool:
		for m in self:
			r = m.match(fullPath, relPath)
			if r:
				return True
		return False
	#

#










