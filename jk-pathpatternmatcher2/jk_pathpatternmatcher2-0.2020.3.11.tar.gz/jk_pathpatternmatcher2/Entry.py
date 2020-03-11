
import typing
import os
import collections
import stat
import pwd
import grp





#
# @field	str fullPath		The absolute file path to the entry
# @field	str baseDirPath		The absolute directory path the search is based on
# @field	str relPath			The relative path to the entry (based on <c>baseDirPath</c>)
# @field	str dirPath			The directory the entry resides in
# @field	str name			The name the entry
# @field	str type			"d" for directory, "f" for file, "l" for symbolic link
#
class Entry(object):

	def __init__(self,
			fullPath:str, baseDirPath:str, relPath:str, dirPath:str, name:str, type:str, mtime:float, uid:int, gid:int, size:int, linkText:str,
			exception:Exception):
		self.exception = exception
		self.fullPath = fullPath
		self.baseDirPath = baseDirPath
		self.relPath = relPath
		self.dirPath = dirPath
		self.name = name
		self.type = type
		self.mtime = mtime
		self.uid = uid
		self.gid = gid
		self.size = size
		self.linkText = linkText
	#

	@property
	def isError(self):
		return self.exception is not None
	#

	@property
	def group(self):
		x = grp.getgrgid(self.gid)
		if x:
			return x.gr_name
		else:
			return None
	#

	@property
	def user(self):
		x = pwd.getpwuid(self.uid)
		if x:
			return x.pw_name
		else:
			return None
	#

	def __repr__(self):
		return "<Entry(" + repr(self.fullPath) + ")>"
	#

	def __str__(self):
		return "<Entry(" + repr(self.fullPath) + ")>"
	#

#



#Entry = collections.namedtuple("Entry", [ "fullPath", "baseDirPath", "relPath", "dirPath", "name", "type", "mtime", "uid", "gid", "size", "linkText" ])





