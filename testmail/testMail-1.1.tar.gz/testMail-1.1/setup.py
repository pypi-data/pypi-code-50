import setuptools

with open('README.md', 'r') as readme:
	long_description = readme.read()

setuptools.setup(
	name="testMail",
	version="1.1",
	license="MIT",
	author="FKgk",
	author_email="rhkd865@gmail.com",
	description="testing mail using smtp",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/FKgk/testMail',
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
	]
)