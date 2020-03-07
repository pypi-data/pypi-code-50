from distutils.core import setup
import os.path

setup(
  name = 'alif',         # How you named your package folder (MyLib)
  packages = ['alif'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'virus Corona',   # Give a short description about your library
  long_description='hello uncleengineer',
  author = 'alifprabda',                   # Type in your name
  author_email = 'alif@gmail.com',      # Type in your E-Mail
  url = 'https://www.facebook.com/alif.make',   # Provide either the link to your github or to your website
  download_url = 'https://drive.google.com/file/d/1gXF6Iem1UA25gxV5tNenLGeF7awgBd3J/view?usp=sharing',    # I explain this later on
  keywords = ['a', 'alif', 'l', 'UncleEngineer'],   # Keywords that define your package best
  install_requires=[
          'uncleengineer',
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
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
