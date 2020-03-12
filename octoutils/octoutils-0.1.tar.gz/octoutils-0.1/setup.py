from distutils.core import setup
setup(
  name='octoutils',
  version='0.1',
  license='MIT',
  description='Day-to-day scripts helpers.',
  author='Bruno Paes',
  author_email='brunopaes05@gmail.com',
  url='https://github.com/brunopaes/automatic-octo-utils',
  download_url='https://github.com/brunopaes/automatic-octo-utils/archive/v_01.tar.gz',
  keywords=['UTILS', 'HELPERS'],
  install_requires=[
      'validators',
      'beautifulsoup4',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
