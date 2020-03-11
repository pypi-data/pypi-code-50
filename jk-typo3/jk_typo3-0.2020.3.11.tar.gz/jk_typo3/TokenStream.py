

class TokenStream(object):

	class _Mark(object):

		def __init__(self, parent, pos):
			self.__parent = parent
			self.__pos = pos
		#

		def resetToMark(self):
			self.__parent._pos = self.__pos
		#

	#

	def __init__(self, tokens:list):
		self._data = list(tokens)
		self._pos = 0
	#

	def __iter__(self):
		for v in self._data[self._pos:]:
			yield v
	#

	def __len__(self):
		return len(self._data) - self._pos
	#

	def __str__(self):
		ret = "TokenStream["
		bAddComma = False
		n = 3
		for item in self:
			if n == 0:
				ret += ", ..."
				break
			n -= 1
			if bAddComma:
				ret += ", "
			else:
				bAddComma = True
			ret += str(item)
		return ret + "]"
	#

	def dump(self, nMax:int = 30):
		print("TokenStream[")
		n = nMax + 1
		for item in self:
			if n == 0:
				print("\t...")
				break
			n -= 1
			print("\t" + str(item))
		print("]")
	#

	def __repr__(self):
		return self.__str__()
	#

	def next(self):
		if self._pos == len(self._data):
			return None
		ret = self._data[self._pos]
		self._pos += 1
		return ret
	#

	def peekOne(self):
		if self._pos == len(self._data):
			return None
		return self._data[self._pos]
	#

	def peekMany(self, n:int = -1):
		if self._pos == len(self._data):
			return []
		return self._data[self._pos:n]
	#

	def mark(self):
		return TokenStream._Mark(self, self._pos)
	#

	def tryEat(self, tokenType:str, tokenValue:str = None):
		assert tokenType

		if self._pos == len(self._data):
			return None

		t = self._data[self._pos]
		if t.type == tokenType:
			if tokenValue is None:
				self._pos += 1
				return t
			else:
				if t.value == tokenValue:
					self._pos += 1
					return t
				else:
					return None
		else:
			return None
	#

	def location(self) -> str:
		if self._pos == len(self._data):
			return "<eos>"
		else:
			t = self._data[self._pos]
			return str(t.lineNo) + ":" + str(t.colNo)
	#

	def hasMoreTokens(self) -> bool:
		return self._pos < len(self._data)
	#

	def isEOS(self) -> bool:
		return self._pos >= len(self._data)
	#

#





