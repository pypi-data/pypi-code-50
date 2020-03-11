#!/usr/bin/env python3
# vim: set ft=python fileencoding=utf-8:

from setuptools import setup, find_packages


version = '1.0.2.dev4'

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
        name='pynfact',
        version=version,
        author='J. A. Corbal',
        author_email='jacorbal@gmail.com',
        url='https://github.com/jacorbal/pynfact/wiki',
        download_url='https://github.com/jacorbal/pynfact',
        project_urls={
            'Documentation': 'https://github.com/jacorbal/pynfact/wiki',
            'Funding': 'https://jacorbal.es/pynfact', 'Source':
            'https://github.com/jacorbal/pynfact', 'Tracker':
            'https://github.com/jacorbal/pynfact/issues'},
        description='Blog-oriented static web generator using Jinja2 templates.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        license='MIT',
        keywords=['blog', 'markdown', 'static', 'web', 'site', 'generator'],
        py_modules=find_packages(),
        packages=['pynfact'],
        entry_points={'console_scripts': ['pynfact = pynfact.__main__:main']},
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Site Management',
            'Topic :: Software Development :: Code Generators',
            'Topic :: Text Processing :: Markup :: HTML',
            'Topic :: Utilities',
        ],
        install_requires=[
            'feedgen >= 0.9.0',
            'jinja2 >= 2.7',
            'markdown >= 3.0.0',
            'pygments',
            'unidecode',
        ],
        python_requires='>=3.6',
        include_package_data=True,
)

