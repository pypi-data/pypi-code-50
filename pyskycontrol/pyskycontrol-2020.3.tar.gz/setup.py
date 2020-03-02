from setuptools import setup, find_packages

setup(
    name='pyskycontrol',
    version='2020.3',
    description='A Python library to interface with Sky',
    long_description="A Python library to interface with the Sky",
    url='https://Ktech6@bitbucket.org/Ktech6/pyskycontrol.git',

    author='ktech6',
    author_email='ktech6@outlook.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        #        'Topic :: Software Development :: API',
        'License :: OSI Approved :: MIT License',
        #        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.5.*',
    keywords='Sky Library',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    #    packages=["pyhiveapi"],
    #    install_requires=[],

    install_requires=['requests', 'beautifulsoup4', 'lxml']
)
