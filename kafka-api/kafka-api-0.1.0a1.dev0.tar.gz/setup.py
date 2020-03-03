from setuptools import setup, find_packages

setup(name='kafka-api',
      version='0.1.0a1dev',
      description='High level API for Apache Kafka (over kafka-python lib)',
      packages=find_packages(),

      install_requires=["kafka-python>=2.0.1"],


      author_email='epolyak@yandex.ru',
      author='Evgenii Polyak',
      zip_safe=False)
