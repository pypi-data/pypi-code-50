from setuptools import setup, find_packages

with open('history.md') as history_file:
    HISTORY = history_file.read()


with open('README.md') as readme_file:
    README = readme_file.read()


# python setup.py sdist
# twine upload dist/*

setup_args = dict(
    name='viso',
    version='11',
    description='Useful tools to work with Visualization in python ',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    include_package_data=True,
    packages=find_packages(include=['Viso',
    'Viso.DataFactory',
    'Viso.Layout'
    ]),
    author='Mohammad Saed Haj Ali',
    author_email='ite.s3ed@gmail.com',
    keywords=['hists', 'viso', 'vis']
    # url='https://github.com/ncthuc/elastictools',
    # download_url='https://pypi.org/project/viso/'
)

install_requires = [
    # 'elasticsearch>=6.0.0,<7.0.0',
    # 'jinja2'
    'numpy',
    'dash',
    'dash_core_components',
    'dash_html_components',
    'plotly',
    'pandas',
    'dash_bootstrap_components'

]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)