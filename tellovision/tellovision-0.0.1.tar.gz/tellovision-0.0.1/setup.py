import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="tellovision",
	version="0.0.1",
	author="Jacob Bendele",
	author_email="Jacob.Bendele.ff@gmail.com",
	description="A package for RYZE Tello drone CV applications",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Jacob-Bendele/tellovision",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
)
