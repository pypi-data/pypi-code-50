from distutils.core import setup
import os.path


setup(
  name = 'Snoopfluke',         # How you named your package folder (MyLib)
  packages = ['Snoopfluke'],   # Chose the same as "name"
  version = '0.0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Show MY NAME',   # Give a short description about your library
  long_description='plese read in: https://github.com/Snoop-Fluke',
  author = 'Loong Wissawakorn',                   # Type in your name
  author_email = 'flukelaksee@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Snoop-Fluke',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Snoop-Fluke/FW_Matrix_LoRA/releases/tag/0.0.1',    # I explain this later on
  keywords = ['Snoopfluke', 'fluke', 'Thanasak', 'Yaemburi'],   # Keywords that define your package best
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
