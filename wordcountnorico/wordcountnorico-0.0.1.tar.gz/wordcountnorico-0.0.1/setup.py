import setuptools

with open('readme.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='wordcountnorico',
    version='0.0.1',
    author='Norico',
    description='Exercise package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>3.6'
)
