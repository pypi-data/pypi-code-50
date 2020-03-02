#coding=utf-8

from distutils.core import setup

setup(
	name='pythonMathAlgorithm', 	#对外模块的名字
	version='1.1', 					#版本号
	description='数学算法包', 		#描述
	author='TravisFan', 	 		#作者
	author_email='travisfan01@sina.com', #邮箱
	py_modules=['pythonMathAlgorithm.additionAlgorithm','pythonMathAlgorithm.subtractionAlgorithm',
				'pythonMathAlgorithm.divisionAlgorithm','pythonMathAlgorithm.exponentAlgorithm',
				'pythonMathAlgorithm.modulesAlgorithm','pythonMathAlgorithm.multiplicationAlgorithm',
				'pythonMathAlgorithm.floorDivisionAlgorithm']  # 要发布的模块
)