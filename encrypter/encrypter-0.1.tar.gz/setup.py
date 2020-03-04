from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
  name = 'encrypter',         # How you named your package folder (MyLib)
  packages = ["src"],
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Plain text encrypter designed to handle ASCII characters based on a randomly generated constant',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Tester86',                   # Type in your name
  author_email = 'tester86t@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Tester86/encrypter',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Tester86/passfactory/encrypter.py/v_01.tar.gz',    # I explain this later on
  keywords = ['ENCRYPT', 'ENCRYPTER', 'DECRYPT', 'DECRYPTER', 'CYPHER', 'CHARACTER', 'ASCII'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)