from setuptools import setup

setup(
    name = 'dsbox',
    packages = ['dsbox'],
    version = 'v0.2-alpha',  # Ideally should be same as your GitHub release tag varsion
    description = '',
    author = 'Kedar Dabhadkar',
    author_email = 'kdabhadk@gmail.com',
    url = 'https://github.com/dkedar7/dsbox',
    download_url = 'https://github.com/dkedar7/dsbox/archive/v0.2-alpha.tar.gz',
    keywords = ['Data Science', 'Machine Learning'],
    classifiers = [],
    install_requires = ['scipy',
     'numpy', 
     'math', 
     'pandas', 
     'matplotlib', 
     'seaborn', 
     'pandas_profiler']
)