from setuptools import setup, Distribution, find_packages

class BinaryDistribution(Distribution):
	def is_pure(self):
		return False

setup(	name='adrt', version='0.0',
		description='Approximate Discrete Radon Transform',
		url='https://github.com/dnry/adrt/',
		author='Donsub Rim, Yoon-gu Hwang',
		author_email='dr1653@nyu.edu, yz0624@gmail.com',
		license='BSD 3-clause "New" or "Revised License"',
		packages=find_packages(),
		install_requires=[
			'numpy',
			'scipy',
			'matplotlib'
		],
		distclass=BinaryDistribution,
		zip_safe=False)
