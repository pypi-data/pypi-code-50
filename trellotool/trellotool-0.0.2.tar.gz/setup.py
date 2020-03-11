import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='trellotool',
    version='0.0.2',
    licence='GNU General Public License v3',
    author='Michael Davies',
    author_email='michael@the-davies.net',
    description='A CLI for trello',
    install_requires=[
        "prettytable",
        "py-trello",
    ],
    download_url='https://github.com/mrda/trellotool/archive/0.0.1.tar.gz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mrda/trellotool',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
        'trellotool = trellotool.trellotool:main'
        ],
    },
)

