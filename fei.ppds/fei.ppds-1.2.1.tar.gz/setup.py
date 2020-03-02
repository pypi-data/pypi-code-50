from setuptools import setup, find_packages


setup(name='fei.ppds',
      version='1.2.1',
      description="Customized synchronization classes",
      long_description=(open("README.rst").read()),
      long_description_content_type='text/x-rst',
      classifiers=[
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
      ],
      url='https://github.com/Programator2/ppds',
      license='Unlicense',
      namespace_packages=['fei'],
      packages=find_packages()
      )
