from distutils.core import setup
setup(
  name = 'validframe', # How you named your package folder (MyLib)
  packages = ['validframe'], # Chose the same as "name"
  version = '0.1.1', # Start with a small number and increase it with every change you make
  license= 'MIT', # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'validium validators for pandas dataframes', # Give a short description about your library
  author = 'Jason Yung',
  author_email = 'json.yung@gmail.com',
  url = 'https://github.com/json2d/validframe', # Provide either the link to your github or to your website
  download_url = 'https://github.com/json2d/validframe/archive/v0.1.1.tar.gz',
  keywords = ['validation', 'dataframe', 'pandas', 'validium', 'rambda'], # Keywords that define your package best
  install_requires= ['validium', 'ramda'],
  classifiers=[
    'Development Status :: 3 - Alpha', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers', # Define your audience
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License', # Again, pick a license
    'Programming Language :: Python :: 3', # Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)