import setuptools
from os import path


#
# Preparation
#
here = path.dirname (path.realpath (__file__))



#
# Packaging Instructions -- Quick DER -- arpa2.quickder
#
extension = setuptools.Extension (name='_quickder',
                      sources=[
                          path.join(here, 'python', 'src', '_quickder.c'),
                          path.join(here, 'lib', 'der_header.c'),
                          path.join(here, 'lib', 'der_unpack.c'),
                          path.join(here, 'lib', 'der_pack.c')],
                      include_dirs=[path.join(here, 'include')],
                      )

readme = open (path.join (here, 'PYTHON.MD')).read ()
setuptools.setup (

	# What?
	name = 'arpa2.quickder',
	version = '1.4.0',
	url = 'https://gitlab.com/arpa2/quick-der',
	description = 'Quick DER -- Abstract Base Classes for generated ASN.1 handlers',
	long_description = readme,
	long_description_content_type = 'text/markdown',

	# Who?
	author = 'Rick van Rein (for the ARPA2 Quick DER project)',
	author_email = 'rick@openfortress.nl',

	# Where?
	ext_modules = [ extension ],
	namespace_packages = [ 'arpa2', ],
	packages = [
		'arpa2',
		'arpa2.quickder',
	],
	package_dir = {
		'arpa2'          : path.join (here, 'python'),
		'arpa2.quickder' : path.join (here, 'python', 'quickder'),
	},
	package_data = {
		'arpa2.quickder' : [ path.join (here, 'PYTHON.MD'),
		],
	},

	# Requirements
	install_requires = [ 'asn1ate>=0.6.0', 'colored', 'six' ],
	extras_require = {
		'TOOLS' : [ 'arpa2.quickder_tools' ],
	},

)




#
# Packaging Instructions -- Quick DER -- arpa2.quickder_tools
#
readme = open (path.join (here, 'TOOLS.MD')).read ()
setuptools.setup (

	# What?
	name = 'arpa2.quickder_tools',
	version = '1.4.0',
	url = 'https://gitlab.com/arpa2/quick-der',
	description = 'Quick DER -- Tools to work with ASN.1 specifications',
	long_description = readme,
	long_description_content_type = 'text/markdown',

	# Who?
	author = 'Rick van Rein (for the ARPA2 Quick DER project)',
	author_email = 'rick@openfortress.nl',

	# Where?
	namespace_packages = [ 'arpa2', ],
	packages = [
		'arpa2',
		'arpa2.quickder_tools',
		'arpa2.quickder_tools.generators',
	],
	package_dir = {
		'arpa2'                           : path.join (here, 'python'),
		'arpa2.quickder_tools'            : path.join (here, 'python', 'tools'),
		'arpa2.quickder_tools.generators' : path.join (here, 'python', 'tools', 'generators'),
	},
	package_data = {
		'arpa2.quickder_tools' : [ path.join (here, 'TOOLS.MD'),
		                           path.join (here, 'img', 'derdump-screenshot.png'),
		],
	},
	entry_points = {
		'console_scripts' : [
			'asn2quickder=arpa2.quickder_tools.asn2quickder:main',
			'asn1literate=arpa2.quickder_tools.asn1literate:main',
			'derdump=arpa2.quickder_tools.derdump:main',
		],
	},

	# Requirements
	install_requires = [ 'asn1ate>=0.6.0', 'colored', 'six' ],
	extras_require = {
		'RUNTIME' : [ 'arpa2.quickder' ],
	},

)


