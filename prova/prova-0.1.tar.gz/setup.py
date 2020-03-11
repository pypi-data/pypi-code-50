#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from distutils.core import setup
setup(
  name = 'prova',
  packages = ['prova'],
  version = '0.1',
  license='MIT',
  description = 'this is a trial',
  author = 'Carlo Parodi',
  author_email = 'carlo.parodi91@gmail.com',
  url = 'https://github.com/Carlo-Parodi/prova.git',
  download_url = 'https://github.com/Carlo-Parodi/prova.git',
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
  install_requires=[
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)



