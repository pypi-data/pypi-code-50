from setuptools import setup, find_packages


setup(
    name='resourcify',
    version='0.2.6',
    license='MIT License',
    platforms='Linux',
    package_dir={'': 'lib'},
    packages=find_packages('lib'),

    install_requires=['requests', 'python-forge'],

    package_data={
        '': ['*.rst'],
    },

    author='Yang Youseok',
    author_email='ileixe@gmail.com',
    description='Resource library to make ReST client easy',
    long_description=open('README.rst').read(),
    keywords='http rest client',
    url='http://github.com/Xeite/resourcify',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ]
)
