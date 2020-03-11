

from .PathPatternMatcher import PathPatternMatcher
from .PathPatternMatcherCollection import PathPatternMatcherCollection





_REGEX_REPLACEMENT_MAP = {
	"^": "\\^",
	"?": "?",
	"$": "\\$",
	".": "\\.",
	"+": "\\+",
	"|": "\\|",
	"(": "\\(",
	")": "\\)",
	"[": "\\[",
	"]": "\\]",
	"{": "\\{",
	"}": "\\}",
	"\\": "\\\\",
	"*": "[^/]*"
}


#
# Compile a path pattern.
#
# @return	PathPatternMatcher			The regex based pattern matcher
#
def compilePattern(sPattern:str, raiseExceptionOnError:bool = True) -> PathPatternMatcher:
	if not sPattern:
		if raiseExceptionOnError:
			raise Exception("No data!")
		else:
			return None

	assert isinstance(sPattern, str)

	sOrgPattern = sPattern
	bAbsolute = sPattern.startswith("/")
	if bAbsolute:
		sPattern = sPattern[1:]

	components = []
	sPatternParts = sPattern.split("/")

	for sPatternPart in sPatternParts:
		components2 = []
		if sPatternPart == "**":
			components2.append(".*")
		else:
			i = 0
			while i < len(sPatternPart):
				p = sPatternPart[i]
				pNext = sPatternPart[i + 1] if i < len(sPatternPart) - 1 else None
				if (p == "*") and (pNext == "*"):
					# detected: "....***...."
					if raiseExceptionOnError:
						raise Exception("Failed to compile pattern: " + repr(sOrgPattern))
					else:
						return None
				repl = _REGEX_REPLACEMENT_MAP.get(p)
				if repl is not None:
					components2.append(repl)
				else:
					components2.append(p)
				i += 1
		if not components2:
			# detected: "....//...."
			if raiseExceptionOnError:
				raise Exception("Failed to compile pattern: " + repr(sOrgPattern))
			else:
				return None
		components.append("".join(components2))

	ret = "/".join(components) + "$"
	if bAbsolute:
		return PathPatternMatcher(sOrgPattern, bAbsolute, "^/" + ret)
	return PathPatternMatcher(sOrgPattern, bAbsolute, "^" + ret)
#





def compileAllPatterns(patterns) -> PathPatternMatcherCollection:
	assert isinstance(patterns, (tuple, list))

	c = PathPatternMatcherCollection()
	for p in patterns:
		r = compilePattern(p)
		c.append(r)
	if not c:
		return None
	return c
#





