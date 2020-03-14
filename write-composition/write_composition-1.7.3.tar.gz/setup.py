from setuptools import setup

with open('README.md', encoding = 'UTF-8') as fh:
	long_description = fh.read()

setup(name = 'write_composition',
version = '1.7.3',
data_files = [('Lib\\site-packages\\wc_data',
	         ['wc_data/data.json',
	         'wc_data/data_mingyan.json',
	         'wc_data/bullshit_place.json',
	         'wc_data/bullshit_achievement.json',
	         'wc_data/bullshit_school.json',
	         'wc_data/bullshit_job.json'])],
description = '手把手教你如何写出一篇完美的废话文章.',
author='pythonnlgs',
long_description = long_description,
long_description_content_type = 'text/markdown',
py_modules = ['write_composition']
)