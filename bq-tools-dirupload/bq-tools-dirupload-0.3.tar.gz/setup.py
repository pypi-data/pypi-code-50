from setuptools import setup

setup(name='bq-tools-dirupload',
      version='0.3',
      description='Upload files to bisque/ViQi in parallel',
      long_description = open('README.rst').read(),
      author='ViQi Inc',
      author_email='support@viqi.org',
      url='https://www.viqi.org',
      license='BSD',
      packages=['bq', 'bq.tools'],
      install_requires = [
          'bisque-api',
          'future',
	  'configparser',
      ],
      zip_safe=False,
      entry_points = {
          'console_scripts' : [ 'bq-dirupload=bq.tools.uploaddirp:main' ]
      },
      classifiers = (
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          "License :: Other/Proprietary License",
          "Operating System :: OS Independent",
      ),
)
