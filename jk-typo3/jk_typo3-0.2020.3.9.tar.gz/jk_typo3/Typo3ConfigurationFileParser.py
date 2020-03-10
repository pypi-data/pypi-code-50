


import re
import os
import sys





from jk_utils import TypedValue
from jk_utils.tokenizer import Token, Stack
import jk_php_tokenizer

from .TokenStream import TokenStream






class Typo3ConfigurationFileParser(object):



	__TOKENIZER = jk_php_tokenizer.PHPTokenizer()



	def parseText(self, rawText:str) -> dict:
		tokenStream = TokenStream(Typo3ConfigurationFileParser.__TOKENIZER.tokenize(rawText))

		ret = self._tryRead_S(tokenStream)
		if ret is None:
			tokenStream.dump()
			raise Exception("Syntax error at: " + tokenStream.location() + ". Expected: PHP intro signature")

		assert isinstance(ret, dict)

		if tokenStream.hasMoreTokens():
			tokenStream.dump()
			raise Exception("Syntax error at: " + tokenStream.location() + ". Excessive tokens!")

		return ret
	#



	def parseFile(self, filePath:str):
		with open(filePath, "r") as f:
			return self.parseText(f.read())
	#



	#
	# S	->		phpintro	"return"	ASSOCARRAY		semicolon
	#
	def _tryRead_S(self, ts:TokenStream):
		t = ts.tryEat("phpintro")
		if t is None:
			return None

		t = ts.tryEat("word", "return")
		if t is None:
			ts.dump()
			raise Exception("Syntax error at: " + ts.location() + ". Expected: 'return'")

		bSuccess, ret = self._tryRead_ASSOCARRAY(ts)
		if not bSuccess:
			ts.dump()
			raise Exception("Syntax error at: " + ts.location() + ". Expected: associative array")

		t = ts.tryEat("semicolon")
		if t is None:
			ts.dump()
			raise Exception("Syntax error at: " + ts.location() + ". Expected: ';'")

		return ret
	#



	#
	# EMTPYARRAY	->		"["		"]"
	#
	def _tryRead_EMTPYARRAY(self, ts:TokenStream):
		m = ts.mark()

		# check start condition: "["

		t = ts.tryEat("lparen2")
		if t is None:
			return False, None

		# check termination condition: "["

		t = ts.tryEat("rparen2")
		if t is None:
			m.resetToMark()
			return False, None

		return True, []
	#



	#
	# ASSOCARRAY	->		"["		ASSOCARRAY_COMPONENT+		"]"
	#
	def _tryRead_ASSOCARRAY(self, ts:TokenStream):
		m = ts.mark()

		# check start condition: "["

		t = ts.tryEat("lparen2")
		if t is None:
			return False, None

		ret = {}

		bExpectTermination = False
		while True:
			# check EOS

			if ts.isEOS():
				ts.dump()
				raise Exception("Unexpected EOS!")

			# check termination condition: "]"

			t = ts.tryEat("rparen2")
			if t is None:
				if bExpectTermination:
					raise Exception("Syntax error at: " + ts.location() + ". Expected: ']'")
			else:
				return True, ret

			# read array item

			bSuccess, key, value = self._tryRead_ASSOCARRAY_ELEMENT(ts)
			if bSuccess:
				ret[key] = value
			else:
				if len(ret) == 0:
					m.resetToMark()
					return False, None
				else:
					raise Exception("Syntax error at: " + ts.location() + ". Expected: associative array element, ',' or ']'")

			# read comma

			t = ts.tryEat("op", ",")
			if t is None:
				bExpectTermination = True
	#



	#
	# STDARRAY	->		"["		STDARRAY_COMPONENT+		"]"
	#
	def _tryRead_STDARRAY(self, ts:TokenStream):
		m = ts.mark()

		# check start condition: "["

		t = ts.tryEat("lparen2")
		if t is None:
			return False, None

		ret = []

		bExpectTermination = False
		while True:
			# check EOS

			if ts.isEOS():
				ts.dump()
				raise Exception("Unexpected EOS!")

			# check termination condition: "]"

			t = ts.tryEat("rparen2")
			if t is None:
				if bExpectTermination:
					raise Exception("Syntax error at: " + ts.location() + ". Expected: ']'")
			else:
				return True, ret

			# read array item

			bSuccess, value = self._tryRead_VALUE(ts)
			if bSuccess:
				ret.append(value)
			else:
				if len(ret) == 0:
					m.resetToMark()
					return False, None
				else:
					raise Exception("Syntax error at: " + ts.location() + ". Expected: standard array element, ',' or ']'")

			# read comma

			t = ts.tryEat("op", ",")
			if t is None:
				bExpectTermination = True
	#



	#
	# ASSOCARRAY_ELEMENT	->		str1	"=>"		VALUE
	#
	def _tryRead_ASSOCARRAY_ELEMENT(self, ts:TokenStream):
		m = ts.mark()

		t = ts.tryEat("str1")
		if t is None:
			return False, None, None
		key = t.value

		t = ts.tryEat("op", "=>")
		if t is None:
			m.resetToMark()
			return False, None, None

		b, ret = self._tryRead_VALUE(ts)
		if not b:
			ts.dump()
			raise Exception("Syntax error at: " + ts.location() + ". Expected: some value")

		return True, key, ret
	#



	#
	# VALUE			->		int
	#				|		str1
	#				|		str2
	#				|		bool
	#				|		null
	#				|		ASSOCARRAY
	#				|		STDARRAY
	#
	def _tryRead_VALUE(self, ts:TokenStream):
		t = ts.tryEat("str1")
		if t is not None:
			return True, t.value

		t = ts.tryEat("str2")
		if t is not None:
			return True, t.value

		t = ts.tryEat("int")
		if t is not None:
			return True, int(t.value)

		t = ts.tryEat("bool")
		if t is not None:
			return True, t.value == "true"

		t = ts.tryEat("null")
		if t is not None:
			return True, None

		bSuccess, ret = self._tryRead_EMTPYARRAY(ts)
		if bSuccess:
			return True, ret

		bSuccess, ret = self._tryRead_ASSOCARRAY(ts)
		if bSuccess:
			return True, ret

		bSuccess = self._tryRead_STDARRAY(ts)
		if bSuccess:
			return True, ret

		return False, None
	#

#


















