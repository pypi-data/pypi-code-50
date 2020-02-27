from setuptools import setup
from paga_connect_client import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pagaconnect',
      version='0.0.1',
      description='Paga Connect Library',
      # url='https://github.com/edwardpopoola/pypaystack',
      author=version.__author__,
      author_email='devcomm@paga.com',
      # license=version.__license__,
      # test_suite='nose.collector',
      # tests_require=['nose'],
      # install_requires=['requests'],
      py_modules=["pagaconnect"],
      packages=['paga_connect_client'],
      long_description=long_description,
      long_description_content_type="text/markdown",

      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
          "Operating System :: OS Independent",
      ],
      )
