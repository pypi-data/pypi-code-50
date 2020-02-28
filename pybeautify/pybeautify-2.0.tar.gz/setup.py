from setuptools import setup,find_packages
with open("README.md",encoding='utf-8') as f:
	long_desc=f.read()
setup(
name='pybeautify',
version='2.0',
description='Beautify',
long_description=long_desc,
long_description_content_type="text/markdown",
url="https://github.com/CKVB/Beautifier",
author='Chaitanya Krishna VB',
author_email='python7460@gmail.com',
license='MIT LICENSE',
packages=find_packages(),
classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)