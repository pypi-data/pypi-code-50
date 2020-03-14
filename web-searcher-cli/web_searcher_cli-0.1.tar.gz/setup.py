import os
from setuptools import setup

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='web_searcher_cli',
    version='0.1',
    packages=['search'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='consosle web search from google or yandex',
    # long_description=README,
    url='https://github.com/gmanru/web_searcher_cli',
    author='Gmvn',
    author_email='mrgman11@yandex.ru',
    keywords=['json', 'google', 'yandex', 'bs4'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'searcher = search.main:main',
        ]
    },
)
