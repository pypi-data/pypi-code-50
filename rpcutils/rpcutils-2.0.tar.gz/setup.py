from setuptools import setup

setup(name='rpcutils',
      description = 'RPC Utilities',
      version='2.0',
      classifiers = ["Development Status :: 4 - Beta", "Programming Language :: Python :: 2.7"],
      url='http://github.com/Caregraf/rpcutils',
      license='Apache License, Version 2.0',
      keywords='VistA,CHCS,RPC',
      package_dir = {'rpcutils': ''},
      packages = ['rpcutils', 'rpcutils.rpcRunner'],
      entry_points = {
          'console_scripts': ['rpcrun=rpcutils.rpcRunner.RPCRunner:main']
      }
)
