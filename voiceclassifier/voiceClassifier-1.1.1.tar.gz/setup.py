from setuptools import setup

with open("README.md", 'r') as f:
  long_description = f.read()


setup(
  name = 'voiceClassifier',
  packages = ['voiceClassifier'],
  version = '1.1.1',
  license='MIT',        # https://help.github.com/articles/licensing-a-repository
  description="A simple package for voice classifiaction",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Raman Shinde',
  author_email = 'raman.shinde15@gmail.com',
  url = 'https://github.com/Raman-Raje/voiceClassifier',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Raman-Raje/voiceClassifier/archive/v_01_1.tar.gz',
  
  install_requires=[
          'astroid',
          'audioread',
          'cffi',
          'decorator',
          'isort',
          'joblib',
          'lazy-object-proxy',
          'librosa',
          'llvmlite',
          'mccabe',
          'numba',
          'numpy',
          'pandas',
          'pytz',
          'resampy',
          'scikit-learn',
          'scipy',
          'six',
          'SoundFile',
          'typed-ast',
          'wrapt',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
