from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='consolidate_requirements',
    version='0.0.3',
    description='Package to consolidate multiple requirements files into one',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Daniel Hawes',
    author_email='hawesdb@gmail.com',
    keywords=['Python 3', 'Requirements'],
    url='https://github.com/hawesdb/consolidate-requirements',
    download_url='https://pypi.org/project/consolidate-requirements/'
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)