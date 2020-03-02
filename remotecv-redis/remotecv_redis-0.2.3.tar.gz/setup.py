# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='remotecv_redis',
    version='0.2.3',
    description="Redis image loader for remotecv",
    long_description="""
Redis image loader for remotecv which is an OpenCV worker for facial and feature recognition
The loader for Redis is compatible with the tc_redis.storage plugins for Thumbor.
""",
    keywords='imaging face detection feature opencv redis thumbor storage loader',
    author='Benn Eichhorn',
    author_email='beichhor@gmail.com',
    url='https://github.com/benneic/remotecv_redis',
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
        'redis>=2.10.0,<3.0.0'
    ],
    extras_require={
    },
)