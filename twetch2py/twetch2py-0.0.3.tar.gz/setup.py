from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name = 'twetch2py',         
  packages = ['twetch2py'],   
  version = '0.0.3', 
  license='MIT', 
  description = 'A class-based implementation of the Twetch SDK for Python',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Cyphergato, LLC',
  author_email = 'cyphergato@protonmail.com',
  url = 'https://gitlab.com/cyphergato/twetch2py',
  download_url = 'https://gitlab.com/cyphergato/twetch2py/-/archive/master/twetch2py-master.tar.gz',
  keywords = ['bitcoin', 'twetch', 'sdk'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)