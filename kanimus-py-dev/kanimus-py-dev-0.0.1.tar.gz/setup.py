import setuptools, os

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name=os.environ['PKG_NAME'],
    version='0.0.1',
    author='Bob Gold',
    author_email='kanimus.developers@gmail.com',
    description='Python common library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/spacecloud.kanimus/backend/kanimus-py',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
