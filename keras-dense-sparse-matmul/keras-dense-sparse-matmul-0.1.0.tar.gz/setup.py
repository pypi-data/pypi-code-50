from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='keras-dense-sparse-matmul',
      version='0.1.0',
      description='Multiply row vector with sparse matrix in tensorflow',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/ulf1/keras-dense-sparse-matmul',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['keras_dense_sparse_matmul'],
      install_requires=[
          'setuptools>=40.0.0',
          'tensorflow>=2.1.*'],
      python_requires='>=3.6',
      zip_safe=False)
