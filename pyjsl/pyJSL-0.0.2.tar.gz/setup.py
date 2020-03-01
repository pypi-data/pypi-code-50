from setuptools import setup, find_packages

setup(name='pyJSL', 
      version='0.0.2', 
      url='https://github.com/2runo/JSL-py',
      author='2runo',
      author_email='2runo04@gmail.com',
      description='It makes your WebSocket communications secure.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires=['crypto', 'pycrypto', 'simple_websocket_server', 'pyopenssl', 'RSAhandler'],
      zip_safe=False,
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
)