from setuptools import setup, find_packages

# References for setup tools:
#  https://setuptools.readthedocs.io/en/latest/
# Building and Distributing Packages with Setuptools: https://setuptools.readthedocs.io/en/latest/setuptools.html


setup(name='pydiagrams',
      version='0.7.2',
      description='Generate software diagrams using Python syntax',
      #url='http://github.com/storborg/funniest',
      author='Matthew Billington',
      author_email='mbillington@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires = ['colour', 'pillow', 'plantuml'],
      # entry points defines the command line version
      entry_points = {},
      zip_safe=False,
      include_package_data=True
      )
