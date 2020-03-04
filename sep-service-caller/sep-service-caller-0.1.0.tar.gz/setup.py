from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='sep-service-caller',
      author='Matt Daily',
      author_email='mdaily@lco.global',
      url='https://github.com/LCOGT/sep-service-caller',
      description='Command line tool to call LCO source extraction service',
      long_description=long_description,
      long_description_content_type='text/markdown',
      version='0.1.0',
      packages=find_packages(),
      install_requires=['requests==2.22.0', 'lcogt-logging==0.3.2'],
      entry_points={'console_scripts': ['sep-service=sep_service_caller.main:main']})
