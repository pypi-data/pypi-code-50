


import typing
import os
import collections
import stat


from .PathPatternMatcherCollection import PathPatternMatcherCollection
from .PathPatternMatcher import PathPatternMatcher
from .pm import compilePattern, compileAllPatterns
from .Entry import Entry





#
# Walks through all entries of a directory and returns them.
#
# @return	Entry[]		Returns an iterator over <c>Entry</c> objects. Each <c>Entry</c> object
#
def walk(*dirPaths,
		ignorePathPatterns = None,
		ignoreDirPathPatterns = None,
		ignoreFilePathPatterns = None,
		ignoreLinkPathPatterns = None,
		emitDirs:bool = True,
		emitFiles:bool = True,
		emitLinks:bool = True,
		emitBaseDirs:bool = True,
		recursive:bool = True,
		sort:bool = True,
		emitErrorEntries:bool = True
	) -> typing.Iterator[Entry]:

	ignorePathMatcher = None
	ignoreDirPathMatcher = None
	ignoreFilePathMatcher = None
	ignoreLinkPathMatcher = None

	if ignorePathPatterns:
		ignorePathMatcher = compileAllPatterns(ignorePathPatterns)
		ignoreFilePathMatcher = PathPatternMatcherCollection()
		ignoreFilePathMatcher.extend(ignorePathMatcher)
		ignoreDirPathMatcher = PathPatternMatcherCollection()
		ignoreDirPathMatcher.extend(ignorePathMatcher)
		ignoreLinkPathMatcher = PathPatternMatcherCollection()
		ignoreLinkPathMatcher.extend(ignorePathMatcher)

	if ignoreDirPathPatterns:
		r = compileAllPatterns(ignoreDirPathPatterns)
		if r is not None:
			if ignoreDirPathMatcher is None:
				ignoreDirPathMatcher = PathPatternMatcherCollection()
			ignoreDirPathMatcher.extend(r)

	if ignoreFilePathPatterns:
		r = compileAllPatterns(ignoreFilePathPatterns)
		if r is not None:
			if ignoreFilePathMatcher is None:
				ignoreFilePathMatcher = PathPatternMatcherCollection()
			ignoreFilePathMatcher.extend(r)

	if ignoreLinkPathPatterns:
		r = compileAllPatterns(ignoreLinkPathPatterns)
		if r is not None:
			if ignoreLinkPathMatcher is None:
				ignoreLinkPathMatcher = PathPatternMatcherCollection()
			ignoreLinkPathMatcher.extend(r)

	dirPaths2 = []
	for d in dirPaths:
		if isinstance(d, (list, tuple)):
			for d2 in d:
				assert isinstance(d2, str)
				# remove trailing slashes
				if d2.endswith("/") and (len(d2) > 1):
					d2 = d2[:-1]
				dirPaths2.append(d2)
		else:
			# remove trailing slashes
			if d.endswith("/") and (len(d) > 1):
				d = d[:-1]
			dirPaths2.append(d)

	for dirPath in dirPaths2:
		dirPath = os.path.abspath(dirPath)
		s = dirPath
		if not s.endswith(os.path.sep):
			s += os.path.sep
		removePathPrefixLen = len(s)
		dirsToGo = [ (dirPath, dirPath, removePathPrefixLen, emitBaseDirs) ]

		while dirsToGo:
			nextDirPath, baseDirPath, removePathPrefixLen, bEmitBaseDir = dirsToGo[0]
			del dirsToGo[0]

			if bEmitBaseDir:
				statResult = os.stat(baseDirPath)
				yield Entry(baseDirPath, baseDirPath, "", nextDirPath, "", "d",
					statResult.st_mtime,
					statResult.st_uid,
					statResult.st_gid,
					statResult.st_size,
					None,
					None)

			try:
				allEntries = os.listdir(nextDirPath)
			except Exception as ee:
				if emitErrorEntries:
					fullPath = os.path.join(nextDirPath, entry)
					relPath = fullPath[removePathPrefixLen:]
					yield Entry(fullPath, baseDirPath, relPath, None, None, "ed",
						None,
						None,
						None,
						None,
						None,
						ee)
				else:
					raise
				continue

			if sort:
				allEntries = sorted(allEntries)

			for entry in allEntries:
				fullPath = os.path.join(nextDirPath, entry)
				relPath = fullPath[removePathPrefixLen:]
				try:
					statResult = os.stat(fullPath, follow_symlinks=False)
					mode = statResult[stat.ST_MODE]
					if stat.S_ISDIR(mode):
						if ignoreDirPathMatcher and ignoreDirPathMatcher.match(fullPath, relPath):
							continue

						if emitDirs:
							yield Entry(fullPath, baseDirPath, relPath, nextDirPath, entry, "d",
								statResult.st_mtime,
								statResult.st_uid,
								statResult.st_gid,
								statResult.st_size,
								None,
								None)

						if recursive:
							dirsToGo.append((fullPath, baseDirPath, removePathPrefixLen, False))

					elif stat.S_ISLNK(mode):
						if ignoreLinkPathMatcher and ignoreLinkPathMatcher.match(fullPath, relPath):
							continue

						if emitFiles:
							try:
								yield Entry(fullPath, baseDirPath, relPath, nextDirPath, entry, "l",
									statResult.st_mtime,
									statResult.st_uid,
									statResult.st_gid,
									statResult.st_size,
									os.readlink(fullPath),
									None)
							except Exception as ee:
								if emitErrorEntries:
									yield Entry(fullPath, baseDirPath, relPath, nextDirPath, entry, "el",
										statResult.st_mtime,
										statResult.st_uid,
										statResult.st_gid,
										statResult.st_size,
										None,
										ee)
								else:
									raise

					elif stat.S_ISREG(mode):
						if ignoreFilePathMatcher and ignoreFilePathMatcher.match(fullPath, relPath):
							continue

						if emitFiles:
							yield Entry(fullPath, baseDirPath, relPath, nextDirPath, entry, "f",
								statResult.st_mtime,
								statResult.st_uid,
								statResult.st_gid,
								statResult.st_size,
								None,
								None)

				except FileNotFoundError as ee:
					# we end here if entry was a link but the link target does not exist
					pass
#




