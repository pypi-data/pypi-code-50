from setuptools import setup, find_packages

setup(
    name='libwsgi',
    version='0.12',
    url='https://github.com/mixkorshun/libwsgi',
    description='',
    keywords=['wsgi'],

    author='Vladislav Bakin',
    author_email='vladislav@bakin.me',
    maintainer='Vladislav Bakin',
    maintainer_email='vladislav@bakin.me',

    license='MIT',
    packages=find_packages(exclude=['tests.*', 'tests']),

    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
