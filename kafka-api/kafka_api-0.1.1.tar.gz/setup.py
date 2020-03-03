from setuptools import setup, find_packages

setup(name='kafka_api',
      version='0.1.1',
      description='High level API for Apache Kafka (over kafka-python lib)',
      packages=find_packages(),

      install_requires=["kafka-python>=2.0.1"],


      author_email='epolyak@yandex.ru',
      author='Evgeniy Polyak',
      zip_safe=False)
