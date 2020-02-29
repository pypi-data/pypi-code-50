import setuptools

setuptools.setup(
      name='py_random_words',
      version='0.4',
      url='https://github.com/andreasonny83/py_random_words',
      license='MIT',
      author='andreasonny83',
      author_email='andreasonny83@gmail.com',
      description='Generate random names',
      packages=setuptools.find_packages(),
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      python_requires='>=3.6',
)
