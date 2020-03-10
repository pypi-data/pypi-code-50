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

class list_func(object):
	'''
	func:'最大值', '最小值', '元组转列表'
	     '第_项', '第_至_项'
	'''
	def 最大值(self, li):
		return max(li)

	def 最小值(self, li):
		return min(li)

	def 元组转列表(self, tmp):
		return list(tmp)

	def 第_项(self, num, li):
		return li[num + 1]

	def 第_至_项(self, n1, n2, li):
		return li[n1:n2]

