from distutils.core import setup
setup(
  name = 'simpletrail',         # How you named your package folder (MyLib)
  packages = ['simpletrail'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='Commercial',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'simple logging',   # Give a short description about your library
  author = 'Marco Fiorani',                   # Type in your name
  author_email = 'mfiorani88@gmail.com',      # Type in your E-Mail
  url = 'https://gitlab.com/mfiorani88/simpletrail',   # Provide either the link to your github or to your website
  download_url = 'https://gitlab.com/mfiorani88/simpletrail/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['logging', 'security', 'integrity'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'logging',
          'configparser',
          'Crypto',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 2.7',      #Specify which pyhton versions that you want to support
  ],
)
