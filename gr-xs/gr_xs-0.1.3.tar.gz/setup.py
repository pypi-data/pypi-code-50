from setuptools import setup, find_packages

setup(
    name='gr_xs',
    version='0.1.3',
    author='T. Yuan',
    author_email='tyuan@icecube.wisc.edu',
    description='Implementation of arxiv:1407.4415 for nu-e W-Boson resonance',
    long_description=open('README.md').read(),
    url='https://github.com/tianluyuan/gr_xs.git',
    packages=find_packages('./'),
    install_requires=['numpy',
                      'scipy'],
)
