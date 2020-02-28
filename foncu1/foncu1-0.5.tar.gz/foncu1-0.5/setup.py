from setuptools import setup
setup(
  name = 'foncu1',         # How you named your package folder (MyLib)
  packages = ['/home/foncu/Desktop/foncu1'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Global Library Testing by Foncu',   # Give a short description about your library
  author = 'firat oncu',                   # Type in your name
  author_email = 'f.firatoncu@hepsiburada.com',      # Type in your E-Mail
  url = 'https://github.com/firatoncu',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/firatoncu/foncu1/archive/v0.5.tar.gz',    # I explain this later on
  keywords = ['GLOBAL', 'LIBRARY', 'FIRAT', 'ONCU'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
  ],
)