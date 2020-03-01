import setuptools

setuptools.setup(
	name="JSONFileOBJDB", # Replace with your own username
	version="0.0.8",
	author="win.stitch.23",
	author_email="win.stitch.23@gmail.com",
	description="JSON File OBJ DB",
	url="https://github.com/0187773933/JSONFileOBJDB",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)

install_requires = [
	'json',
	'pathlib'
]