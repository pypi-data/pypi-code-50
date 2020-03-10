from distutils.core import setup
import os.path


setup(
  name = 'robotframework-dictkeyallpaths',         # How you named your package folder (MyLib)
  packages = ['DictAllPaths'],   # Chose the same as "name"
  version = '0.1.8',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This is a function for robotframework that gets the keys of all values ​​in the dictionary.',   # Give a short description about your library
  long_description= 'Find more details at URL:https://github.com/yoochar/readme-robotframework-dictallpaths.git',
  author = 'Yoochar',                   # Type in your name
  author_email = 'yoochar@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/yoochar/readme-robotframework-dictallpaths.git',   # Provide either the link to your github or to your website
#  download_url = '',    # I explain this later on
  keywords = ['robot', 'robotframework', 'dictionary', 'path','key','jsonpath','dictpath','getallpath','getallkey','automation','api'],   # Keywords that define your package best

  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
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
