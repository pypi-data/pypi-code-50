'''
rm -rf build/
rm -rf dist/
python3 setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

user: __token__
pwd: pypi-AgEIcHlwaS5vcmcCJDA0NGM2OTA1LTYxNGQtNGYyNC04N2E5LTY3NTIwYjZiNzUwYgACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgQML8aZmY247uVBhnFyO2cZZE6VAxwnrol64i0zHNjjY
'''

from setuptools import setup, find_packages

requires = [
    'APScheduler==3.6.3',
    'boto3==1.11.0',
    'botocore==1.14.0',
    'certifi==2019.11.28',
    'chardet==3.0.4',
    'Click==7.0',
    'configparser==4.0.2',
    'docopt==0.6.2',
    'docutils==0.15.2',
    'ecdsa==0.15',
    'Flask==1.1.1',
    'Flask-Cors==3.0.8',
    'gitdb2==2.0.6',
    'GitPython==3.0.5',
    'gunicorn==20.0.4',
    'idna==2.8',
    'itsdangerous==1.1.0',
    'Jinja2==2.10.3',
    'jmespath==0.9.4',
    'jose==1.0.0',
    'MarkupSafe==1.1.1',
    'minio==5.0.7',
    'pyasn1==0.4.8',
    'pyfcm==1.4.7',
    'pykwalify==1.7.0',
    'PyMySQL==0.9.3',
    'pyodbc==4.0.28',
    'python-dateutil==2.8.1',
    'python-jose==3.1.0',
    'pytz==2019.3',
    'PyYAML==5.3',
    'requests==2.22.0',
    'rsa==4.0',
    's3transfer==0.3.0',
    'six==1.13.0',
    'smmap2==2.0.5',
    'tzlocal==2.0.0',
    'urllib3==1.25.7',
    'Werkzeug==0.16.0'
]

setup(name='cautil',
      version='2.1',
      description='The UTILITY for Cloud Agnostic',
      url='http://github.com/whirldata/cautil',
      author='Whirldata',
      author_email='info@whirldatascience.com.com',
      license='MIT',
      install_requires=requires,
      packages=find_packages(),
      zip_safe=False)
