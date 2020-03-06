from setuptools import setup

__author__ = 'Mahmoud Hashemi'
__version__ = '0.0.2'
__contact__ = 'mahmoud@hatnote.com'
__url__ = 'https://github.com/mahmoud/fjord'
__license__ = 'BSD'

with open('README.md') as read_me:
    long_description = read_me.read()

setup(name='fjord',
      version=__version__,
      description="The web framework you've been pining for.",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author=__author__,
      author_email=__contact__,
      url=__url__,
      # project_urls={'Documentation': 'https://fjord.readthedocs.io/en/latest/',},
      packages=['fjord'],
      install_requires=['clastic', 'lithoxyl', 'boltons>=19.3.0', 'face', 'SQLAlchemy'],
      # entry_points={'console_scripts': ['fj = fjord.cli:console_main']},
      include_package_data=True,
      zip_safe=False,
      license=__license__,
      platforms='any',
      classifiers=[
          'Topic :: Utilities',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy', ]
      )

"""
A brief checklist for release:

* tox
* git commit (if applicable)
* Bump setup.py version off of -dev
* git commit -a -m "bump version for x.y.z release"
* python setup.py sdist bdist_wheel upload
* bump docs/conf.py version
* git commit
* git tag -a vx.y.z -m "brief summary"
* write CHANGELOG
* git commit
* bump setup.py version onto n+1 dev
* git commit
* git push

"""
