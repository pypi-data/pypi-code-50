from setuptools import setup, find_packages

filename = 'graph-report/version.py'
exec(compile(open(filename, 'rb').read(), filename, 'exec'))

setup(name='graphreport',
      version=__version__,
      description='Custom metrics based report for robot framework',
      long_description='Dashboard view of robotframework results created by parsing output.xml using robot.result api',
      classifiers=[
          'Framework :: Robot Framework',
          'Programming Language :: Python',
          'Topic :: Software Development :: Testing',
      ],
      keywords='robotframework report for graph',
      author='user',
      author_email='mdeepam69@gmail.com',
      url='https://github.com/usr123321/graphreports',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'robotframework',
          'beautifulsoup4',
          'gevent'
      ],
      entry_points={
          'console_scripts': [
              'graphreport=robotframework_metrics.runner:main',
          ]
      },
      )
