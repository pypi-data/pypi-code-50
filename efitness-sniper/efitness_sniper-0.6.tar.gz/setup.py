from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="efitness_sniper",
    version="0.6",
    install_requires=[
        'requests==2.23.0',
        'coloredlogs==14.0',
        'ruamel.yaml==0.16.10',
        'beautifulsoup4==4.8.2'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["efitness_sniper"],
    license="MIT",
    author="Marek Wajdzik",
    author_email="marek@wajdzik.eu",
    description="eFitness.com.pl Booking sniper",
    entry_points={"console_scripts": ["efitness=efitness_sniper.app:main"],},
    keywords = ['efitness', 'sniper', 'booking', 'bookings'],
    download_url= "https://github.com/consi/efitness-sniper/archive/0.6.tar.gz",
    classifiers=[
        'Development Status :: 4 - Beta', 
        'Intended Audience :: End Users/Desktop', 
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.7',
  ],
)
