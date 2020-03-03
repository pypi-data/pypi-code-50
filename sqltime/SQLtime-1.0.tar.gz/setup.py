from setuptools import setup
setup(
  name = 'SQLtime',
  packages = ['SQLtime'],
  version = 'v1.0',
  license='MIT',
  description = 'Python lib to automate time based SQLi',   # Give a short description about your library
  author = 'Nishit',
  author_email = 'nishit@mailfence.com',
  url = 'https://github.com/nishitm/SQLtime',
  download_url = 'https://github.com/nishitm/SQLtime/archive/v1.0.tar.gz',
  keywords = ['Blind time based SQL injection', 'Pentesting', "AppSec"],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ],
)
