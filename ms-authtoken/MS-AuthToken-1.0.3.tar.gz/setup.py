from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
  name = 'MS-AuthToken',         # How you named your package folder (MyLib)
  packages = ['MS-AuthToken'],   # Chose the same as "name"
  version = '1.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Use this library to generate authentication token for microsoft services like MS Graph api, Sharepoint rest api etc.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Taimoor Alam',   # Type in your name
  author_email = 'taimoor.6@hotmail.com',    # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/smartguy666/MS-AuthToken/archive/1.0.3.tar.gz',    # I explain this later on
  keywords = ['Microsoft', 'OAuth', 'MS', 'MS OAuth', 'Auth Token', 'Sharepoint rest api', 'Graph api', 'MS Graph api', 'Auth Token generator'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'pypandoc',
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