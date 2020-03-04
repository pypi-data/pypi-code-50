import setuptools


def read_content(file: str) -> str:
    with open(file, 'r') as f:
        return f.read().strip()


setuptools.setup(
    name='gramat',
    version=read_content('version.txt'),
    author='Sergio Pedraza',
    author_email='sergio.uriel.ph@gmail.com',
    description='Gramat language implementation',
    long_description=read_content('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/gramat-lang/python-gramat',
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    license='MIT',
    install_requires=read_content('requirements-main.txt'),
    # See: https://pypi.org/classifiers/
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
