import os
import os.path

from setuptools import setup, Extension
import versioneer

# Default description in markdown
LONG_DESCRIPTION = open('README.md').read()


PKG_NAME     = 'tessdb-stats'
AUTHOR       = 'Rafael Gonzalez'
AUTHOR_EMAIL = 'astrorafael@yahoo.es'
DESCRIPTION  = 'tessdb internal statistics database for the tessdb observations database',
LICENSE      = 'MIT'
KEYWORDS     = 'Astronomy Python RaspberryPi LightPollution'
URL          = 'http://github.com/stars4all/tessdb-comdline/'
PACKAGES     = ["tess_event"]
DEPENDENCIES = []

CLASSIFIERS  = [
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: SQL',
    'Topic :: Scientific/Engineering :: Astronomy',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
    'Development Status :: 4 - Beta',
]


SCRIPTS = [
    'files/usr/local/bin/tess_event'
]

if os.name == "posix":

  setup(name             = PKG_NAME,
        version          = versioneer.get_version(),
        cmdclass         = versioneer.get_cmdclass(),
        author           = AUTHOR,
        author_email     = AUTHOR_EMAIL,
        description      = DESCRIPTION,
        long_description_content_type = "text/markdown",
        long_description = LONG_DESCRIPTION,
        license          = LICENSE,
        keywords         = KEYWORDS,
        url              = URL,
        classifiers      = CLASSIFIERS,
        packages         = PACKAGES,
        install_requires = DEPENDENCIES,
        scripts          = SCRIPTS
        )
 
  

else:
  
  print("Not supported OS")
