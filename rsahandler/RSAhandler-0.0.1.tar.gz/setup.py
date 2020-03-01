from setuptools import setup, find_packages

setup(name='RSAhandler', 
      version='0.0.1', 
      author='2runo',
      author_email='2runo04@gmail.com',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires=['crypto', 'pycrypto'],
      zip_safe=False,
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
)