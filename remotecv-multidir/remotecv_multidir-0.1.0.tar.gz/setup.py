# coding: utf-8

from setuptools import setup, find_packages



def readme():
    with open('README.md') as f:
        return f.read()


__version__ = None
exec(open('remotecv_multidir/_version.py').read())


setup(
    name='remotecv_multidir',
    version=__version__,
    description="RemoteCV image loader from multiple local directories",
    keywords='imaging face detection feature opencv multidir thumbor storage loader',
    author='Benn Eichhorn',
    author_email='beichhor@gmail.com',
    url='https://github.com/benneic/remotecv_multidir',
    license='MIT',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: MacOS',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.6',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                 'Topic :: Multimedia :: Graphics :: Presentation'],
    zip_safe=False,
    include_package_data=True,
    
    packages=find_packages(),
    install_requires=[
        'derpconf'
    ],
    extras_require={
    },
    long_description=readme(),
)