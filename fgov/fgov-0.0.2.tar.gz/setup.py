from distutils.core import setup

setup(
  name = 'fgov',
  packages = ['fgov'],
  version = '0.0.2',
  license='MIT',
  description = 'fgov is a cryptography library supporting several ciphers.',
  author = 'vsp',
  author_email = 'veryseriousprogrammer@gmail.com',
  url = 'https://github.com/vsp0/fgov',
  download_url = 'https://github.com/vsp0/fgov/archive/v_01.tar.gz',
  keywords = ['cryptography', 'math', 'ciphers'],
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)