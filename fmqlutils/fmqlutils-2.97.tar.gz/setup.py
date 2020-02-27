from setuptools import setup

setup(name='fmqlutils',
      description = 'FMQL Utilities',
      long_description = """A Python framework and set of executables for caching datasets from FileMan systems using FMQL. Includes support for data analysis and modeling""",
      version='2.97',
      install_requires = [
          'rpcutils>=2.0'
          #'pytz>=2019.1'
      ],
      classifiers = ["Development Status :: 4 - Beta", "Programming Language :: Python :: 2.7"],
      url='http://github.com/Caregraf/fmqlutils',
      license='Apache License, Version 2.0',
      keywords='VistA,FileMan,CHCS,FMQL',
      package_dir = {'fmqlutils': ''},
      packages = ['fmqlutils', 'fmqlutils.cacher', 'fmqlutils.typer', 'fmqlutils.reporter'],
      entry_points = {
          'console_scripts': ['fmqlcacher=fmqlutils.cacher.cacher:main', 'fmqlv2er=fmqlutils.cacher.v2er:main', 'fmqlcachehealth=fmqlutils.reporter.cacheHealthReporter:main', 'fmqltyper=fmqlutils.typer.reduceReportTypes:main']
      }
)
