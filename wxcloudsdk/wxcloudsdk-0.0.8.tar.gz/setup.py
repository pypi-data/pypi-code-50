from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wxcloudsdk', 
    version='0.0.8', 
    keywords='wechat miniprogram http sdk api', 
    description='Wechat miniprogram http api tools', 
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License', 
    url='',
    author='typingcat', 
    author_email='liuchunyao0321@gmail.com',
    packages=find_packages(), 
    include_package_data=True,
    platforms='any', 
    install_requires=["requests"],
    python_requires='>=3.6'
)