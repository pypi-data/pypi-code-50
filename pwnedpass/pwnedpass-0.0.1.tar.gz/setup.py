#!/usr/bin/env python3

import setuptools
from pathlib import Path

HERE = Path(__file__).parent

with open(HERE / 'README.md') as f:
	long_description = f.read()

setuptools.setup(
	name='pwnedpass',
	py_modules=['pwnedpass'],
	author='io mintz',
	url='https://git.csdisaster.club/io/pwnedpass',
	version='0.0.1',
	description="Queries a local instance of Troy Hunt's Pwned Passwords database. (Port of https://github.com/tylerchr/pwnedpass)",
	long_description=long_description,
	long_description_content_type='text/markdown; variant=GFM',
	python_requires='>=3.6.0',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Intended Audience :: End Users/Desktop',
		'Topic :: Utilities',
		'Natural Language :: English',
		'Operating System :: OS Independent',
	],
	license='BlueOak-1.0.0',
	entry_points={
		'console_scripts': [
			'pwnedpass = pwnedpass:main',
		],
	},
)
