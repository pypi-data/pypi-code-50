from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='cgx_notebooks',
      version='1.0.9',
      description='Repository to distribute CloudGenix Python Notebooks and easily install helper functions.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ebob9/cgx-notebooks',
      author='Aaron Edwards',
      author_email='cgx_notebooks@ebob9.com',
      license='MIT',
      install_requires=[
            'cloudgenix >= 5.2.1b1',
            'cloudgenix-idname>=2.0.1',
            'plotly>=4.5.2',
            'pandas>=1.0.1',
            'IPython',
            'ipywidgets',
            'numpy',
            'fuzzywuzzy',
            'python-levenshtein'
      ],
      packages=['cgx_notebooks'],
      python_requires='>=3.6.1',
      classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
      ]
      )
