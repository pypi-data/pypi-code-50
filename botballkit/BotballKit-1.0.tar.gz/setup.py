import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='BotballKit',
    version='1.0',
    author='Luke',
    author_email='lukepc@protonmail.com',
    description='An object-oriented wrapper for the KIPR library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/devluke/botballkit',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.7',
)
