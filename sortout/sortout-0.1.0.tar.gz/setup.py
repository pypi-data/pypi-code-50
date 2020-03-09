from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readMe:
    longDesc = readMe.read()

setup(
  name = 'sortout',
  packages = find_packages(),
  version = '0.1.0',
  license='AGPL 3.0',
  description = 'An integrative library that contains tools for using various types of sorting algorithms to work together.',
  long_description = longDesc,
  long_description_content_type='text/markdown',
  include_package_data=True,
  author = 'Yogesh Aggarwal',
  author_email = 'developeryogeshgit@gmail.com',
  url = 'https://github.com/yogesh-aggarwal/sortout',
  download_url = 'https://github.com/yogesh-aggarwal/sortout/blob/master/dist/sortout-0.1.0.tar.gz',
  keywords = ['SORTING', 'MULTIPLE SORTS', 'ALGORITHMS'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
