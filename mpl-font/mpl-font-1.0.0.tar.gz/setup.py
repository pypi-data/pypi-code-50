from setuptools import setup, find_packages

setup(version='1.0.0',
      packages=find_packages(),
      include_package_data=True,
      package_data={
        'mpl_font': ['fonts/**/*.?t?'],
      },
      license='BSD',
      )
