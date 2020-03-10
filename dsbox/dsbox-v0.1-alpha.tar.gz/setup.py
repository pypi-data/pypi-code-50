from distutils.core import setup

setup(
    name = 'dsbox',
    packages = ['dsbox'],
    version = 'v0.1-alpha',  # Ideally should be same as your GitHub release tag varsion
    description = '',
    author = 'Kedar Dabhadkar',
    author_email = 'kdabhadk@gmail.com',
    url = 'https://github.com/dkedar7/dsbox',
    download_url = 'https://github.com/dkedar7/dsbox/archive/v0.1-alpha.tar.gz',
    keywords = ['Data Science', 'Machine Learning'],
    classifiers = [],
    requires_install = ['scipy',
     'numpy', 
     'math', 
     'pandas', 
     'matplotlib', 
     'seaborn', 
     'pandas_profiler']
)