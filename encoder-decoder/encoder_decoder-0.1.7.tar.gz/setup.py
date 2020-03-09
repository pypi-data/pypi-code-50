from setuptools import setup, find_packages

setup(name='encoder_decoder',
      version='0.1.7',
      description='Functions to encode and decode commonly used data formats to support transmission of data over the web.',
      url='https://github.com/UMass-Rescue/encoder_decoder',
      author='Jagath Jai Kumar, Prasanna Lakkur Subramanyam',
      author_email='prasanna.lakkur@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
            'numpy'
      ],
      zip_safe=False)