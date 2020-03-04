from setuptools import setup, find_packages

setup(
    name='trood-cli',
    version=0.1,
    packages=find_packages(),
    include_package_data=True,
    author='Trood Inc',
    url='',
    install_requires=[
        u'requests==2.22.0', 'click', 'pyfiglet', 'tabulate', 'keyring'
    ],
    entry_points='''
        [console_scripts]
        trood=trood.cli.trood:trood
    '''
)