class base(object):
	'''
	func:'打印'
	'''
	def 打印(self, a):
		print(a)

class data_type(object):		
	'''
	func:'二进制', '八进制', '十六进制', '十进制',
	     '整型', '浮点型', '绝对值', '字符串'
	'''
	def 二进制(self, a):
		return bin(a)

	def 八进制(self, a):
		return oct(a)

	def 十六进制(self, a):
		return hex(a)

	def 十进制(self, num, type_ = 2):
		if type_ >= 2 and type_ <= 36:
			return int(num, type_)
		else:
			print('最大36， 最小2， 或0')

	def 整型(self, a):
		return int(a)

	def 浮点型(self, a):
		return float(a)

	def 绝对值(self, a):
		return abs(a)

	def 字符串(self, a):
		return str(a)
