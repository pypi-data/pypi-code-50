from setuptools import setup, find_packages

setup(
    name='pyrebase5',
    version='5.0.1',
    url='https://github.com/davidvartanian/Pyrebase',
    description='A simple python wrapper for the Firebase API',
    author='James Childs-Maidment',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
    ],
    keywords='Firebase',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests',
        'gcloud',
        'oauth2client',
        'requests_toolbelt>=0.7',
        'python_jwt>=3.2',
        'pycryptodome>=3.4'
    ]
)
