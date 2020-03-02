#coding=utf-8

from distutils.core import setup

setup(
	name='pythonMathDemo', 	#对外模块的名字
	version='1.0', 			#版本号
	description='这是第一个对外发布的模块，用于测试，包含数学运算法则', #描述
	author='TravisFan', 	 	#作者
	author_email='travisfan01@sina.com', #邮箱
	py_modules=['pythonMathDemo.additionDemo','pythonMathDemo.subtractionDemo',
				'pythonMathDemo.divisionDemo','pythonMathDemo.exponentDemo',
				'pythonMathDemo.modulesDemo','pythonMathDemo.multiplicationDemo',
				'pythonMathDemo.floorDivisionDemo']  # 要发布的模块
)
