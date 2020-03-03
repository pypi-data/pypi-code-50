from setuptools import setup

setup(name='CTRegisterMicroserviceFlask',
      version='0.5.1',
      description='Library to interact with the Control-Tower api-gateway (register, do requests to other microservices, etc)',
      author='Vizzuality',
      author_email='info@vizzuality.com',
      license='MIT',
      packages=['CTRegisterMicroserviceFlask'],
      install_requires=[
        'flask',
        'requests'
      ],
      extras_require={
        'dev': [
            'pytest==5.2.2',
            'pytest-cov==2.8.1',
            'pytest-mock==1.11.1',
            'codecov==2.0.15',
            'requests_mock==1.7.0',
        ]
      },
      zip_safe=False)
