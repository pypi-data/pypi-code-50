from distutils.core import setup
import os.path


setup(
  name = 'yatimaCom',         # How you named your package folder (MyLib)
  packages = ['yatimaCom'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Show My Name Jaaa',   # Give a short description about your library
  author = 'Yatima Chooruang',                   # Type in your name
  author_email = 'ch.yatima05@gmail.com',      # Type in your E-Mail
  download_url = 'https://github.com/Myname/archive/0.0.1.zip',    # I explain this later on
  keywords = ['Yatima'],   # Keywords that define your package best
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
