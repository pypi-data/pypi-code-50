import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='icsv',
	version='0.1.6',
	scripts=['icsv/csv'],
	license='MIT',
	keywords=['csv'],
	author='Samuel Mtembo',
	author_email='samuel@samuelworks.org',
	description='A simple script to make operating csv files easier',
	long_description=long_description,
	url='https://www.samuelworks.org',
	download_url='https://github.com/qodzero/icsv/archive/v1.0.6.tar.gz',
	packages=setuptools.find_packages(),
	install_requires=[],
	classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
	)
