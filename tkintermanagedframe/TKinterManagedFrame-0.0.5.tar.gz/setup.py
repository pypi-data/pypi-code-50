import setuptools
from distutils.core import setup
setup(
	name='TKinterManagedFrame',
	packages=['TKinterManagedFrame'],
	version='0.0.5',
	license='GNU GPL',
	description='Adds a Tkinter Frame class that offers simple update functionality',
	author='Christopher "Arkevorkhat" Trent',
	url='',
	install_requires=['tkinter','wheel'],
	classifiers=[
			  'Development Status :: 3 - Alpha', 
			  'Intended Audience :: Developers',
			  'Topic :: Software Development :: Libraries :: Tcl Extensions',
			  'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
			  'Natural Language :: English',
			  ])
