from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='parenclitic',
      version='0.1.7',
      description='Parenclitic approach with kernels inside',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/mike-live/parenclitic',
      author='Mikhail Krivonosov',
      author_email='mike_live@mail.ru',
      license='MIT',
      packages=['parenclitic'],
      install_requires=[
          'numpy',
          'python-igraph',
          'pandas',
          'sklearn',
          'scipy'
      ],
      classifiers=[ # https://pypi.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      zip_safe=False
)