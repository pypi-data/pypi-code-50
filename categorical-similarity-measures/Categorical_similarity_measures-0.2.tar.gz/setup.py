from distutils.core import setup
setup(
  name = 'Categorical_similarity_measures',
  packages = ['Categorical_similarity_measures'],
  version = '0.2',
  license='MIT',
  description = 'Similarity Measures Utility Package',
  author = 'Ajay Mukund S',
  author_email = 'ajaymukund1998@gmail.com',
  url = 'https://github.com/AjayMukundS/Categorical_similarity_measures',
  download_url = 'https://github.com/AjayMukundS/Categorical_similarity_measures/archive/v_01.tar.gz',
  keywords = ['Similarity', 'Distance', 'Categorical data'],
  install_requires=[
          'pandas',
          'numpy',
          'category_encoders',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
